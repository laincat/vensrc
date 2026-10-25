// Vensrc 独立维护版；阅读解析基于 venera-app/venera-configs 的 wnacg 1.0.6。
// 上游提交 a04e05591f7832f7166d6660546613c114d6738a；保留阅读功能。
class Wnacg extends ComicSource {
    name = "紳士漫畫"
    key = "wnacg"
    version = "1.3.1"
    minAppVersion = "1.3.4"
    url = "https://raw.githubusercontent.com/laincat/vensrc/main/sources/wnacg.js"

    _builtinDomains = ["www.wnacg.com", "www.wnacg.ru", "www.wn003.cfd", "www.wn004.cfd"]

    _validDomain(domain) {
        return typeof domain === "string" &&
            (this._builtinDomains.includes(domain) || /^www\.wn[0-9]{3,6}\.cfd$/.test(domain))
    }

    get baseUrl() {
        const domain = this.loadData("activeDomain") || this.loadSetting("domain") || "www.wnacg.com"
        if (!this._validDomain(domain)) {
            throw "请选择内置或发布页公布的绅士漫画域名"
        }
        return `https://${domain}`
    }

    _domains() {
        const cached = this.loadData("mirrorCache")?.domains
        return [...new Set([...this._builtinDomains,
            ...(Array.isArray(cached) ? cached.filter((domain) => this._validDomain(domain)).slice(0, 20) : [])])]
    }

    _parseDomains(body) {
        const doc = new HtmlDocument(body)
        const domains = []
        try {
            if (!/紳士漫畫地址發布頁/.test(doc.querySelector("title")?.text || "")) {
                throw "发布页标题不符，保留已有地址"
            }
            for (const row of doc.querySelectorAll("li")) {
                if (!/紳士漫畫最新地址/.test(row.text)) continue
                for (const link of row.querySelectorAll("a")) {
                    const match = String(link.attributes.href || "").match(/^https:\/\/([^/?#:@\s]+)\/?$/i)
                    const domain = match?.[1].toLowerCase()
                    if (this._validDomain(domain) && !domains.includes(domain)) domains.push(domain)
                }
            }
        } finally {
            doc.dispose()
        }
        if (!domains.length || domains.length > 20) throw "发布页没有可接受的漫画地址，保留已有地址"
        return domains
    }

    async _refreshDomains() {
        for (const page of ["https://wnacg01.link/", "https://wnacg02.link/"]) {
            try {
                const response = await Network.get(page, { "cache-time": "no" })
                if (response.status !== 200) continue
                const domains = this._parseDomains(response.body || "")
                await this.saveData("mirrorCache", { domains, checkedAt: Date.now() })
                return domains.length
            } catch (_) {
                // 发布页暂不可用时尝试备用发布页；不覆盖原有地址。
            }
        }
        throw "两个发布页均未能同步地址，继续使用已有地址；可稍后手动刷新"
    }

    async init() {
        const cache = this.loadData("mirrorCache")
        const checkedAt = cache?.checkedAt
        const age = Date.now() - checkedAt
        if (typeof checkedAt === "number" && age >= 0 && age < 86400000 &&
            Array.isArray(cache.domains) && cache.domains.length) return
        await this._refreshDomains()
    }

    async _chooseDomain() {
        const domains = this._domains()
        const current = this.baseUrl.slice("https://".length)
        const selected = await UI.showSelectDialog(
            "选择访问地址（发布页列出不代表当前网络可用）", domains, Math.max(0, domains.indexOf(current)))
        if (!Number.isInteger(selected) || selected < 0 || selected >= domains.length) return
        const domain = domains[selected]
        if (domain === current) return
        await this.deleteData("account")
        await this.saveData("activeDomain", domain)
        UI.showMessage(`已切换为 ${domain}，请重新登录；App 内网页登录仅使用 www.wnacg.com`)
    }

    get account() {
        const source = this
        return {
            loginWithWebview: {
                // 客户端在源注册前解析此地址，此时不能调用 loadSetting。
                url: "https://www.wnacg.com/users-login.html",
                checkStatus: (url, title) => {
                    const current = String(url || "").split(/[?#]/)[0].replace(/\/$/, "")
                    // 标题会因站点模板和语言变化；成功后再请求会员页核对正文。
                    return current === "https://www.wnacg.com/users-index.html" &&
                        !/您沒有權限|您没有权限|需要登錄|需要登录/.test(String(title || ""))
                },
                onLoginSuccess: async () => {
                    try {
                        await source._captureSession("https://www.wnacg.com", false)
                    } catch (error) {
                        await source.deleteData("account")
                        await Network.deleteCookies("https://www.wnacg.com")
                        UI.showMessage(`网页登录未通过会员页校验：${error}`)
                    }
                },
            },
            loginWithCookies: {
                fields: ["浏览器 Cookie（本人在对应域名登录并完成滑块后复制）"],
                validate: async (values) => {
                    if (!Array.isArray(values) || values.length !== 1 || typeof values[0] !== "string") {
                        throw "请填写浏览器请求中的 Cookie，勿填写账号密码或 Set-Cookie"
                    }
                    await source._installCookies(values[0])
                    return true
                },
            },
            logout: async () => {
                const domains = new Set([...source._domains(), source.baseUrl.slice("https://".length)])
                for (const domain of domains) await Network.deleteCookies(`https://${domain}`)
            },
        }
    }

    async _checkSession(base) {
        const response = await Network.get(`${base}/users-index.html`, {})
        const headers = response.headers || {}
        if (Object.entries(headers).some(([key, value]) =>
            key.toLowerCase() === "cf-mitigated" && String(value).toLowerCase() === "challenge") ||
            /cdn-cgi\/challenge-platform|cf-chl-/.test(response.body || "")) {
            throw "Cloudflare 仍要求验证；请在 App 内登录页完成验证，会话可能绑定网络或设备"
        }
        const logoutLinks = (response.body || "").matchAll(/<a\b[^>]*href\s*=\s*["']([^"']+)["']/gi)
        const loggedIn = response.status === 200 &&
            [...logoutLinks].some((match) => /^\/users-logout\.html(?:\?[^#]*)?$/.test(match[1]) ||
                (match[1].startsWith(base) &&
                    /^\/users-logout\.html(?:\?[^#]*)?$/.test(match[1].slice(base.length)))) &&
            !/您沒有權限|您没有权限|需要登錄|需要登录/.test(response.body || "")
        if (!loggedIn) {
            throw "会员会话未验证；请在 App 内登录页完成滑块，并确认域名一致、会话未过期"
        }
        return true
    }

    _cookieObjects(text, domain) {
        text = String(text || "").trim().replace(/^Cookie:\s*/i, "")
        if (!text || text.length > 16384 || /[\r\n]/.test(text)) {
            throw "Cookie 格式无效，请只复制一行 Cookie 请求头"
        }
        const names = new Set()
        return text.split(";").map((part) => {
            const match = part.trim().match(/^([!#$%&'*+\-.^_`|~0-9A-Za-z]+)=([^\x00-\x20\x7f;,]*)$/)
            if (!match || names.has(match[1]) || /^(path|domain|expires|max-age|samesite)$/i.test(match[1])) {
                throw "Cookie 格式无效，请复制 Cookie 请求头，勿复制 Set-Cookie"
            }
            names.add(match[1])
            return new Cookie({ name: match[1], value: match[2], domain })
        })
    }

    async _installCookies(text, base = this.baseUrl) {
        const domain = base.slice("https://".length)
        const cookies = this._cookieObjects(text, domain)
        const previous = await Network.getCookies(base)
        try {
            await Network.deleteCookies(base)
            await Network.setCookies(base, cookies)
            await this._checkSession(base)
            await this.saveData("account", "ok")
            return true
        } catch (error) {
            await Network.deleteCookies(base)
            await Network.setCookies(base, previous)
            throw error
        }
    }

    async _cookieHeader(base) {
        const host = base.slice("https://".length)
        const cookies = await Network.getCookies(base)
        const header = (Array.isArray(cookies) ? cookies : [])
            .filter((cookie) => cookie && /^[!#$%&'*+\-.^_`|~0-9A-Za-z]+$/.test(cookie.name || ""))
            .filter((cookie) => {
                const domain = String(cookie.domain || "").replace(/^\./, "")
                return !domain || host === domain || host.endsWith(`.${domain}`)
            })
            .map((cookie) => `${cookie.name}=${cookie.value ?? ""}`)
            .join("; ")
        if (!header || header.length > 16384) throw "当前域名没有可导出的有效 Cookie"
        return header
    }

    async _captureSession(base = this.baseUrl, copy = true) {
        await this._checkSession(base)
        const header = await this._cookieHeader(base)
        await this.saveData("account", "ok")
        const host = base.slice("https://".length)
        if (this.baseUrl !== base) await this.saveData("activeDomain", host)
        if (copy) await setClipboard(header)
        UI.showMessage(copy
            ? "会员会话已验证并自动登录；Cookie 已复制，请勿分享"
            : "会员会话已验证并自动登录")
        return header
    }

    async _copyCookies() {
        return this._captureSession(this.baseUrl, true)
    }

    async _importClipboard() {
        const text = await getClipboard()
        if (!text) throw "剪贴板中没有 Cookie，请先复制一行 Cookie 请求头"
        await this._installCookies(text)
        await setClipboard("")
        UI.showMessage("剪贴板 Cookie 已验证，已自动填入并登录")
    }

    parseComic(c) {
        let link = c.querySelector("div.pic_box > a").attributes["href"];
        let id = RegExp("(?<=-aid-)[0-9]+").exec(link)[0];
        let image =
            c.querySelector("div.pic_box > a > img").attributes["src"];
        image = `https:${image}`;
        let name = c.querySelector("div.info > div.title > a").text;
        let info = c.querySelector("div.info > div.info_col").text.trim();
        info = info.replaceAll('\n', '');
        info = info.replaceAll('\t', '');
        return new Comic({
            id: id,
            title: name,
            cover: image,
            description: info,
        })
    }

    explore = [
        {
            title: "紳士漫畫",

            type: "multiPartPage",

            load: async (page) => {
                let res = await Network.get(this.baseUrl, {})
                if (res.status !== 200) {
                    throw `Invalid Status Code ${res.status}`
                }
                let document = new HtmlDocument(res.body)
                let titleBlocks = document.querySelectorAll("div.title_sort");
                let comicBlocks = document.querySelectorAll("div.bodywrap");
                if (titleBlocks.length !== comicBlocks.length) {
                    throw "Invalid Page"
                }
                let result = []
                for (let i = 0; i < titleBlocks.length; i++) {
                    let title = titleBlocks[i].querySelector("div.title_h2").text.replaceAll(/\s+/g, '')
                    let link = titleBlocks[i].querySelector("div.r > a").attributes["href"]
                    let comics = []
                    let comicBlock = comicBlocks[i]
                    let comicElements = comicBlock.querySelectorAll("div.gallary_wrap > ul.cc > li")
                    for (let comicElement of comicElements) {
                        comics.push(this.parseComic(comicElement))
                    }
                    result.push({
                        title: title,
                        comics: comics,
                        viewMore: `category:${title}@${link}`
                    })
                }
                document.dispose()
                return result
            }
        }
    ]

    category = {
        title: "紳士漫畫",
        parts: [
            {
                name: "最新",

                type: "fixed",


                categories: ["最新"],

                itemType: "category",

                categoryParams: ["/albums.html"],

                groupParam: null,
            },
            {
                name: "同人誌",

                type: "fixed",


                categories: ["同人誌", "漢化", "日語", "English", "CG畫集", "3D漫畫", "寫真Cosplay"],

                itemType: "category",

                categoryParams: [
                    "/albums-index-cate-5.html",
                    "/albums-index-cate-1.html",
                    "/albums-index-cate-12.html",
                    "/albums-index-cate-16.html",
                    "/albums-index-cate-2.html",
                    "/albums-index-cate-22.html",
                    "/albums-index-cate-3.html",
                ],

                groupParam: null,
            },
            {
                name: "單行本",

                type: "fixed",


                categories: ["單行本", "漢化", "日語", "English",],

                itemType: "category",

                categoryParams: [
                    "/albums-index-cate-6.html",
                    "/albums-index-cate-9.html",
                    "/albums-index-cate-13.html",
                    "/albums-index-cate-17.html",
                ],

                groupParam: null,
            },
            {
                name: "雜誌短篇",

                type: "fixed",


                categories: ["雜誌短篇", "漢化", "日語", "English",],

                itemType: "category",

                categoryParams: [
                    "/albums-index-cate-7.html",
                    "/albums-index-cate-10.html",
                    "/albums-index-cate-14.html",
                    "/albums-index-cate-18.html",
                ],

                groupParam: null,
            },
            {
                name: "韓漫",

                type: "fixed",


                categories: ["韓漫", "漢化", "生肉",],

                itemType: "category",

                categoryParams: [
                    "/albums-index-cate-19.html",
                    "/albums-index-cate-20.html",
                    "/albums-index-cate-21.html",
                ],

                groupParam: null,
            },
        ],
        enableRankingPage: true,
    }

    categoryComics = {

        load: async (category, param, options, page) => {
            let url = this.baseUrl + param
            if (page !== 0) {
                if (!url.includes("-")) {
                    url = url.replaceAll(".html", "-.html");
                }
                url = url.replaceAll("index", "");
                let lr = url.split("albums-");
                lr[1] = `index-page-${page}${lr[1]}`;
                url = `${lr[0]}albums-${lr[1]}`;
            }

            let res = await Network.get(url, {})
            if (res.status !== 200) {
                throw `Invalid Status Code ${res.status}`
            }
            let document = new HtmlDocument(res.body)
            let comicElements = document.querySelectorAll("div.grid div.gallary_wrap > ul.cc > li")
            let comics = []
            for (let comicElement of comicElements) {
                comics.push(this.parseComic(comicElement))
            }
            let pagesLink = document.querySelectorAll("div.f_left.paginator > a");
            let pages = Number(pagesLink[pagesLink.length - 1].text)
            document.dispose()
            return {
                comics: comics,
                maxPage: pages,
            }
        },
        ranking: {
            options: [
                "day-Day",
                "week-Week",
                "month-Month",
            ],
            load: async (option, page) => {
                let url = `${this.baseUrl}/albums-favorite_ranking-type-${option}.html`
                if (page !== 0) {
                    url = `${this.baseUrl}/albums-favorite_ranking-page-${page}-type-${option}.html`
                }

                let res = await Network.get(url, {})
                if (res.status !== 200) {
                    throw `Invalid Status Code ${res.status}`
                }

                let document = new HtmlDocument(res.body)
                let comicElements = document.querySelectorAll("div.grid div.gallary_wrap > ul.cc > li")
                let comics = []
                for (let comicElement of comicElements) {
                    comics.push(this.parseComic(comicElement))
                }

                let pagesLink = document.querySelectorAll("div.f_left.paginator > a")
                let pages = 1
                if (pagesLink.length > 0) {
                    pages = Number(pagesLink[pagesLink.length - 1].text)
                }

                document.dispose()
                return {
                    comics: comics,
                    maxPage: pages,
                }
            }
        }
    }

    search = {

        load: async (keyword, options, page) => {
            let url = `${this.baseUrl}/search/?q=${encodeURIComponent(keyword)}&f=_all&s=create_time_DESC&syn=yes`
            if (page !== 0) {
                url += `&p=${page}`
            }
            let res = await Network.get(url, {})
            if (res.status !== 200) {
                throw `Invalid Status Code ${res.status}`
            }
            let document = new HtmlDocument(res.body)
            let comicElements = document.querySelectorAll("div.grid div.gallary_wrap > ul.cc > li")
            let comics = []
            for (let comicElement of comicElements) {
                comics.push(this.parseComic(comicElement))
            }
            let total = document.querySelectorAll("p.result > b")[0].text.replaceAll(',', '')
            const comicsPerPage = 24
            let pages = Math.ceil(Number(total) / comicsPerPage)
            document.dispose()
            return {
                comics: comics,
                maxPage: pages,
            }
        },
    }

    favorites = {
        multiFolder: true,
        isOldToNewSort: true,

        addOrDelFavorite: async (comicId, folderId, isAdding, favoriteId) => {
            if (!isAdding) {
                let res = await Network.get(`${this.baseUrl}/users-fav_del-id-${favoriteId}.html?ajax=true&_t=${randomDouble(0, 1)}`, {})
                if (res.status !== 200) {
                    throw 'Delete failed'
                }
            } else {
                let res = await Network.post(`${this.baseUrl}/users-save_fav-id-${comicId}.html`, {
                    'content-type': 'application/x-www-form-urlencoded'
                }, `favc_id=${folderId}`)
                if (res.status !== 200) {
                    throw 'Delete failed'
                }
            }
            return 'ok'
        },

        loadFolders: async (comicId) => {
            let res = await Network.get(`${this.baseUrl}/users-addfav-id-210814.html`, {})
            if (res.status !== 200) {
                throw 'Load failed'
            }
            let document = new HtmlDocument(res.body)
            let data = {}
            document.querySelectorAll("option").forEach((option => {
                if (option.attributes["value"] === "") return
                data[option.attributes["value"]] = option.text
            }))
            return {
                folders: data,
                favorited: []
            }
        },

        addFolder: async (name) => {
            let res = await Network.post(`${this.baseUrl}/users-favc_save-id.html`, {
                'content-type': 'application/x-www-form-urlencoded'
            }, `favc_name=${encodeURIComponent(name)}`)
            if (res.status !== 200) {
                throw 'Add failed'
            }
            return 'ok'
        },

        deleteFolder: async (folderId) => {
            let res = await Network.get(`${this.baseUrl}/users-favclass_del-id-${folderId}.html?ajax=true&_t=${randomDouble()}`, {})
            if (res.status !== 200) {
                throw 'Delete failed'
            }
            return 'ok'
        },

        loadComics: async (page, folder) => {
            let url = `${this.baseUrl}/users-users_fav-page-${page}-c-${folder}.html.html`
            let res = await Network.get(url, {})
            if (res.status !== 200) {
                throw `Invalid Status Code ${res.status}`
            }
            let document = new HtmlDocument(res.body)
            let comicBlocks = document.querySelectorAll("div.asTB")
            let comics = comicBlocks.map((comic) => {
                let cover = comic.querySelector("div.asTBcell.thumb > div > img").attributes["src"]
                cover = 'https:' + cover
                let time = comic.querySelector("div.box_cel.u_listcon > p.l_catg > span").text.replaceAll("創建時間：", "")
                let name = comic.querySelector("div.box_cel.u_listcon > p.l_title > a").text;
                let link = comic.querySelector("div.box_cel.u_listcon > p.l_title > a").attributes["href"];
                let id = RegExp("(?<=-aid-)[0-9]+").exec(link)[0];
                let delUrl = comic.querySelector("div.box_cel.u_listcon > p.alopt > a").attributes["onclick"];
                let favoriteId = RegExp("(?<=del-id-)[0-9]+").exec(delUrl)[0];
                return new Comic({
                    id: id,
                    title: name,
                    subtitle: time,
                    cover: cover,
                    favoriteId: favoriteId,
                })
            })
            let pages = 1
            let pagesLink = document.querySelectorAll("div.f_left.paginator > a")
            if (pagesLink.length > 0) {
                pages = Number(pagesLink[pagesLink.length - 1].text)
            }
            document.dispose()
            return {
                comics: comics,
                maxPage: pages,
            }
        }
    }

    comic = {

        loadInfo: async (id) => {
            let res = await Network.get(`${this.baseUrl}/photos-index-page-1-aid-${id}.html?order=asc&mode=list`, {})
            if (res.status !== 200) {
                throw `Invalid Status Code ${res.status}`
            }
            let document = new HtmlDocument(res.body)
            let title = document.querySelector("div.userwrap > h2").text
            let cover = document.querySelector("div.userwrap > div.asTB > div.asTBcell.uwthumb > img").attributes["src"]
            cover = 'https:' + cover
            cover = cover.substring(0, 6) + cover.substring(8)
            let labels = document.querySelectorAll("div.asTBcell.uwconn > label")
            let category = labels[0].text.split("：")[1]
            let isSeries = document.querySelector("#sr_pub") !== null
            let tagsDom = document.querySelectorAll("div.asTBcell.uwconn a.tagshow");
            let tags = new Map()
            tags.set(isSeries ? "章節" : "頁數", [labels[1].text.split("：")[1]])
            tags.set("分類", [category])
            if (tagsDom.length > 0) {
                tags.set("標籤", tagsDom.map((e) => e.text))
            }
            let description = document.querySelector("div.asTBcell.uwconn > p").text;
            let uploader = document.querySelector("div.asTBcell.uwuinfo > a > p").text;

            let chapters
            if (isSeries) {
                chapters = new Map()
                let page = 1
                let maxPage = 1
                try {
                    while (true) {
                        for (let chapter of document.querySelectorAll("a[data-chid]")) {
                            chapters.set(chapter.attributes["data-chid"], chapter.text.trim())
                        }
                        for (let link of document.querySelectorAll("div.f_left.paginator a[href]")) {
                            let match = link.attributes["href"].match(/-page-(\d+)-/)
                            if (match) maxPage = Math.max(maxPage, Number(match[1]))
                        }
                        if (page >= maxPage) break
                        page++
                        document.dispose()
                        document = null
                        let chapterRes = await Network.get(`${this.baseUrl}/photos-index-page-${page}-aid-${id}.html?order=asc&mode=list`, {})
                        if (chapterRes.status !== 200) {
                            throw `Invalid Status Code ${chapterRes.status}`
                        }
                        document = new HtmlDocument(chapterRes.body)
                    }
                } finally {
                    if (document) document.dispose()
                }
                if (chapters.size === 0) throw 'Invalid chapter directory'
            } else {
                document.dispose()
            }

            return new ComicDetails({
                id: id,
                title: title,
                cover: cover,
                chapters: chapters,
                tags: tags,
                description: description,
                uploader: uploader,
            })
        },

        loadThumbnails: async (id, next) => {
            next = next || '1'
            let res = await Network.get(`${this.baseUrl}/photos-index-page-${next}-aid-${id}.html`, {});
            if (res.status !== 200) {
                throw `Invalid Status Code ${res.status}`
            }
            let document = new HtmlDocument(res.body)
            if (document.querySelector("#sr_pub")) {
                document.dispose()
                return { thumbnails: [], next: null }
            }
            let thumbnails = document.querySelectorAll("div.pic_box.tb > a > img").map((e) => {
                return 'https:' + e.attributes["src"]
            })
            next = (Number(next) + 1).toString()
            let paginator = document.querySelector("div.f_left.paginator")
            let pagesLink = paginator ? paginator.children : []
            if (pagesLink.length === 0 || pagesLink[pagesLink.length - 1].classNames.includes("thispage")) {
                next = null
            }
            document.dispose()
            return {
                thumbnails: thumbnails,
                next: next
            }
        },

        loadEp: async (comicId, epId) => {
            let res = await Network.get(`${this.baseUrl}/photos-gallery-aid-${epId || comicId}.html`, {})
            if (res.status !== 200) {
                throw `Invalid Status Code ${res.status}`
            }
            const regex = RegExp(String.raw`//[^"]+/[^"]+\.[^"]+`, 'g');
            const matches = Array.from(res.body.matchAll(regex));
            return {
                images: matches.map((e) => 'https:' + e[0].substring(0, e[0].length - 1))
            }
        },

        onClickTag: (namespace, tag) => {
            return {
                action: 'search',
                keyword: tag,
            }
        },
    }

    settings = {
        domain: {
            title: "访问地址（切换后需重新登录）",
            type: "callback",
            buttonText: "选择地址",
            default: "www.wnacg.com",
            callback: () => this._chooseDomain(),
        },
        refreshDomains: {
            title: "备用地址（每天自动同步，失败保留原地址）",
            type: "callback",
            buttonText: "从发布页刷新",
            callback: async () => {
                const count = await this._refreshDomains()
                UI.showMessage(`已同步 ${count} 个发布页地址，请点击“选择地址”切换；不代表可用性验证通过`)
            },
        },
        copyCookies: {
            title: "获取并保存当前会员 Cookie",
            type: "callback",
            buttonText: "获取 Cookie",
            callback: () => this._copyCookies(),
        },
        importCookies: {
            title: "从剪贴板自动填入 Cookie（验证成功后登录）",
            type: "callback",
            buttonText: "自动填入",
            callback: () => this._importClipboard(),
        },
    }
}
