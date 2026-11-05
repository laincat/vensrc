/// 热辣漫画（2024manga）自建维护版
///
/// 为什么单独维护：官方源 venera-app/venera-configs 的 hot_manga.js 在
/// `comic.onClickTag` 里对「更新」「状态」两个命名空间直接 `throw "未支持此类Tag检索"`，
/// 用户在详情页点这两个标签就会看到报错弹窗。这里按接口自己实现一份，
/// 只声明能跳转的命名空间，其余命名空间不返回（Venera 约定：不返回=不跳转）。
class HotManga extends ComicSource {
    name = "热辣漫画"

    key = "hot_manga"

    version = "1.0.1"

    minAppVersion = "1.6.0"

    url = "https://github.com/laincat/vensrc/blob/main/sources/hot_manga.js"

    static defaultHost = "api.2024manga.com"

    /// 列表接口一页的条数，取接口文档默认值 30。
    static pageSize = 30

    /// 接口要求的客户端标识；缺了 platform/version 会返回空列表。
    static clientVersion = "2024.04.28"

    static themes = [
        ["冒險", "maoxian"], ["奇幻", "qihuan"], ["愛情", "aiqing"], ["校園", "xiaoyuan"],
        ["歡樂向", "huanlexiang"], ["輕小說", "qingxiaoshuo"], ["格鬥", "gedou"], ["職場", "zhichang"],
        ["治癒", "zhiyu"], ["搞笑", "gaoxiao"], ["穿越", "chuanyue"], ["後宮", "hougong"],
        ["異世界", "yishijie"], ["節操", "jiecao"], ["長條", "changtiao"], ["熱血", "rexue"],
    ]

    static orders = [["最近更新", "-datetime_updated"], ["人氣最高", "-popular"], ["最新上架", "-datetime_created"]]

    settings = {
        apiHost: {
            title: "接口域名",
            type: "input",
            default: HotManga.defaultHost,
            validator: "^(?!:\\/\\/)(?=.{1,253})([a-zA-Z0-9]([a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\\.)+[a-zA-Z]{2,}$",
        },
        imageQuality: {
            title: "圖片清晰度",
            type: "select",
            options: [
                { value: "h1500x", text: "高清（h1500x）" },
                { value: "h800x", text: "省流（h800x）" },
            ],
            default: "h1500x",
        },
    }

    get host() {
        return this.loadSetting("apiHost") || HotManga.defaultHost
    }

    get headers() {
        return {
            "Accept": "application/json",
            "webp": "1",
            "platform": "3",
            "version": HotManga.clientVersion,
            "X-Requested-With": "com.manga2020.app",
        }
    }

    /// 三层校验：HTTP 状态、JSON 结构、业务码。任何一层不对都直接报出可读原因，
    /// 避免把「接口变了」伪装成「列表为空」。
    async _get(path, params = {}) {
        const query = Object.entries(params)
            .filter(([, value]) => value !== undefined && value !== null && value !== "")
            .map(([name, value]) => `${encodeURIComponent(name)}=${encodeURIComponent(value)}`)
            .join("&")
        const url = `https://${this.host}${path}` + (query ? `?${query}` : "")
        const response = await Network.get(url, this.headers)
        if (response.status !== 200) throw `接口返回状态码 ${response.status}`
        let body
        try {
            body = JSON.parse(response.body)
        } catch (_) {
            throw "接口返回的不是 JSON，域名可能已被替换"
        }
        if (body.code !== 200) throw body.message || `接口错误码 ${body.code}`
        return body.results || {}
    }

    _comic(raw) {
        const authors = (raw.author || []).map((item) => item.name).filter(Boolean)
        return {
            id: raw.path_word,
            title: raw.name,
            cover: raw.cover,
            subTitle: authors.length ? authors.join(" / ") : undefined,
            description: (raw.theme || []).map((item) => item.name).filter(Boolean).join(" · ") || undefined,
        }
    }

    /// 列表统一回包：comics + 由总数换算的 maxPage。接口不给总数时返回 null，
    /// Venera 约定 null 表示「不限页数」。
    _list(results) {
        const comics = (results.list || []).filter((raw) => raw && raw.path_word && raw.name)
            .map((raw) => this._comic(raw))
        let maxPage = null
        const total = Number(results.total)
        if (Number.isFinite(total) && total >= 0) {
            maxPage = Math.max(1, Math.ceil(total / HotManga.pageSize))
        }
        return { comics, maxPage }
    }

    explore = [
        ...HotManga.orders.map(([title, ordering]) => ({
            title,
            type: "multiPageComicList",
            load: async (page) => this._list(await this._get("/api/v3/comics", {
                free_type: 1,
                limit: HotManga.pageSize,
                offset: (page - 1) * HotManga.pageSize,
                ordering,
            })),
        })),
        {
            title: "全彩",
            type: "multiPageComicList",
            load: async (page) => this._list(await this._get("/api/v3/comics", {
                free_type: 1,
                limit: HotManga.pageSize,
                offset: (page - 1) * HotManga.pageSize,
                ordering: "-datetime_updated",
                theme: "COLOR",
            })),
        },
    ]

    category = {
        title: "热辣漫画",
        parts: [
            {
                name: "按主題",
                type: "fixed",
                categories: HotManga.themes.map(([name]) => name),
                categoryParams: HotManga.themes.map(([, path]) => path),
                itemType: "category",
            },
            {
                name: "按排序",
                type: "fixed",
                categories: HotManga.orders.map(([name]) => name),
                categoryParams: HotManga.orders.map(([, ordering]) => ordering),
                itemType: "category",
            },
        ],
    }

    categoryComics = {
        load: async (category, param, options, page) => {
            const paging = {
                free_type: 1,
                limit: HotManga.pageSize,
                offset: (page - 1) * HotManga.pageSize,
            }
            // 排序分类的 param 是 ordering（以 - 开头），主题分类的 param 是主題 path_word。
            const theme = String(param || "").startsWith("-") ? "" : param
            const ordering = String(param || "").startsWith("-") ? param : "-datetime_updated"
            return this._list(await this._get("/api/v3/comics", { ...paging, ordering, theme }))
        },
    }

    search = {
        load: async (keyword, options, page) => {
            const text = String(keyword || "").trim()
            const paging = { limit: HotManga.pageSize, offset: (page - 1) * HotManga.pageSize }
            // 点作者标签时先把名字换成 path_word；接口的 author 参数只认 path_word。
            const authorPath = (this.loadData("authorPaths") || {})[text]
            if (authorPath) {
                const results = await this._get("/api/v3/comics", {
                    ...paging, ordering: "-datetime_updated", author: authorPath,
                })
                return this._list(results)
            }
            if (!text) return { comics: [], maxPage: 1 }
            return this._list(await this._get("/api/v3/search/comic", {
                ...paging, platform: 3, q: text, free_type: 1, _update: "true",
            }))
        },
    }

    comic = {
        loadInfo: async (id) => {
            const detail = await this._get(`/api/v3/comic2/${encodeURIComponent(id)}`, {
                in_mainland: "true", platform: 3,
            })
            const info = detail.comic
            if (!info) throw "详情接口没有返回漫画信息"
            const authors = (info.author || []).map((item) => item.name).filter(Boolean)
            if (authors.length) {
                const known = this.loadData("authorPaths") || {}
                for (const author of info.author || []) {
                    if (author.name && author.path_word) known[author.name] = author.path_word
                }
                this.saveData("authorPaths", known)
            }
            const chapters = {}
            for (const [groupKey, group] of Object.entries(detail.groups || {})) {
                const path = group.path_word || groupKey
                const name = group.name || groupKey
                chapters[name] = await this._chapters(id, path)
            }
            const status = info.status && info.status.display ? info.status.display : ""
            const region = info.region && info.region.display ? info.region.display : ""
            const updated = info.datetime_updated ? `更新於 ${info.datetime_updated}` : ""
            return {
                title: info.name,
                cover: info.cover,
                description: [String(info.brief || "").trim(), [status, region, updated].filter(Boolean).join(" · ")]
                    .filter(Boolean).join("\n\n"),
                tags: {
                    作者: authors,
                    標籤: (info.theme || []).map((item) => item.name).filter(Boolean),
                },
                chapters,
                subId: info.uuid,
            }
        },

        loadEp: async (comicId, epId) => {
            const detail = await this._get(
                `/api/v3/comic/${encodeURIComponent(comicId)}/chapter/${encodeURIComponent(epId)}`,
                { platform: 3, _update: "true" })
            const chapter = detail.chapter
            if (!chapter) throw "章节接口没有返回内容"
            const quality = this.loadSetting("imageQuality") || "h1500x"
            const images = (chapter.contents || [])
                .map((item) => String(item.url || ""))
                .filter(Boolean)
                // 接口按 h1500x / h800x 两种规格出图，换档时只替换这一段。
                .map((url) => url.replace(/h\d+x\.(webp|jpe?g|png)$/i, `${quality}.$1`))
            if (!images.length) throw "本章没有取到图片地址"
            return { images }
        },

        onClickTag: (namespace, tag) => {
            // 只对这里声明过的命名空间给跳转目标；其余一律不返回，Venera 会当作「不跳转」。
            if (namespace === "作者") return { action: "search", keyword: `${tag}` }
            if (namespace === "標籤" || namespace === "标签") return { action: "search", keyword: `${tag}` }
            return undefined
        },
    }

    async _chapters(comicId, groupPath) {
        const result = {}
        const limit = 100
        let offset = 0
        let total = Infinity
        while (offset < total) {
            const page = await this._get(
                `/api/v3/comic/${encodeURIComponent(comicId)}/group/${encodeURIComponent(groupPath)}/chapters`,
                { limit, offset })
            const list = page.list || []
            for (const item of list) {
                if (item && item.uuid) result[item.uuid] = String(item.name || item.uuid)
            }
            total = Number(page.total)
            if (!Number.isFinite(total)) total = list.length ? offset + list.length : 0
            if (!list.length) break
            offset += limit
        }
        return result
    }
}
