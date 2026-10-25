// Vensrc 独立维护版；阅读解析基于 venera-app/venera-configs 的 wnacg 1.0.6。
// 上游提交 a04e05591f7832f7166d6660546613c114d6738a；保留阅读功能。
class Wnacg extends ComicSource {
    name = "紳士漫畫"
    key = "wnacg"
    version = "1.2.1"
    minAppVersion = "1.3.4"
    url = "https://raw.githubusercontent.com/laincat/vensrc/main/sources/wnacg.js"

    get baseUrl() {
        const domain = this.loadSetting("domain") || "www.wnacg.com"
        if (!["www.wnacg.com", "www.wnacg.ru"].includes(domain)) {
            throw "请选择已核对的绅士漫画域名"
        }
        return `https://${domain}`
    }

    get account() {
        const source = this
        return {
            loginWithWebview: {
                // 客户端在源注册前解析此地址，此时不能调用 loadSetting。
                url: "https://www.wnacg.com/users-login.html",
                checkStatus: (url, title) => {
                    const base = source.baseUrl
                    const memberUrl = `${base}/users-index.html`
                    const current = String(url || "").split(/[?#]/)[0].replace(/\/$/, "")
                    const pageTitle = String(title || "").trim()
                    // 登录页也可能直接打开会员 URL；标题必须出现会员中心字样。
                    return current === memberUrl &&
                        /(?:用戶|用户|會員|会员|個人|个人|我的).*(?:中心|主頁|主页)/.test(pageTitle) &&
                        !/登[錄录]|登录|您沒有權限|您没有权限|權限不足|权限不足/.test(pageTitle)
                },
            },
            loginWithCookies: {
                fields: ["浏览器 Cookie（本人在对应域名登录并完成滑块后复制）"],
                validate: async (values) => {
                    if (!Array.isArray(values) || values.length !== 1 || typeof values[0] !== "string") {
                        throw "请填写浏览器请求中的 Cookie，勿填写账号密码或 Set-Cookie"
                    }
                    const text = values[0].trim().replace(/^Cookie:\s*/i, "")
                    if (!text || text.length > 16384 || /[\r\n]/.test(text)) {
                        throw "Cookie 格式无效，请只复制一行 Cookie 请求头"
                    }
                    const base = source.baseUrl
                    const domain = base.slice("https://".length)
                    const names = new Set()
                    const cookies = text.split(";").map((part) => {
                        const match = part.trim().match(/^([!#$%&'*+\-.^_`|~0-9A-Za-z]+)=([^\x00-\x20\x7f;,]*)$/)
                        if (!match || names.has(match[1]) || /^(path|domain|expires|max-age|samesite)$/i.test(match[1])) {
                            throw "Cookie 格式无效，请复制 Cookie 请求头，勿复制 Set-Cookie"
                        }
                        names.add(match[1])
                        return new Cookie({ name: match[1], value: match[2], domain })
                    })
                    const previous = await Network.getCookies(base)
                    try {
                        await Network.deleteCookies(base)
                        await Network.setCookies(base, cookies)
                        if (!await source._checkSession(base)) {
                            throw "会员会话未验证；请确认登录域名一致、Cookie 未过期，并在正常浏览器完成滑块"
                        }
                        return true
                    } catch (error) {
                        await Network.deleteCookies(base)
                        await Network.setCookies(base, previous)
                        throw error
                    }
                },
            },
            logout: async () => {
                await Network.deleteCookies("https://www.wnacg.com")
                await Network.deleteCookies("https://www.wnacg.ru")
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
        const loggedIn = response.status === 200 &&
            /<a\b[^>]*href\s*=\s*["'](?:https:\/\/www\.wnacg\.(?:com|ru))?\/users-logout\.html(?:\?[^"']*)?["']/i.test(response.body || "") &&
            !/您沒有權限|您没有权限|需要登錄|需要登录/.test(response.body || "")
        if (!loggedIn || this.baseUrl !== base) {
            throw "会员会话未验证；请在 App 内登录页完成滑块，并确认域名一致、会话未过期"
        }
        return true
    }

    async _copyCookies() {
        const base = this.baseUrl
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
        await this._checkSession(base)
        await setClipboard(header)
        UI.showMessage("已复制当前会员 Cookie；不要分享给他人")
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
            title: "访问域名（App 内网页登录请选 www.wnacg.com）",
            type: "select",
            options: [
                { value: "www.wnacg.com", text: "www.wnacg.com" },
                { value: "www.wnacg.ru", text: "www.wnacg.ru" },
            ],
            default: "www.wnacg.com",
        },
        copyCookies: {
            title: "获取 Cookie（仅复制到剪贴板）",
            type: "callback",
            buttonText: "获取 Cookie",
            callback: () => this._copyCookies(),
        },
    }
}
