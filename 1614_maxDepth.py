class Solution:
    def maxDepth(self, s: str) -> int:
        return max(accumulate(1 if x == '(' else -1 if x == ')' else 0 for x in s))
#         l, ans = 0, 0
#         i = 0
#         while i < len(s):
#             if s[i] == '(':
#                 l += 1
#                 ans = max(ans, l)
#             elif s[i] == ')':
#                 l -= 1
#             i += 1
        
#         return ans"use strict"

/**
 * 投票页面
 */

utils.get_vue({
  el: ".vue",
  data: page_data ? page_data : {},
  mounted: function mounted() {
    if (utils.is_pc() && self === top && !this.is_login) {
      utils.go_page(this.api.example_link)
      return
    }

    this.init_swiper() // 轮播图

    this.init_wx_js_sdk() // 微信jssdk

    this.init_count_down() // 倒计时

    this.init_pjax() // pjax

    this.init_marquee() // 顶部跑马灯

    this.init_audio() // 背景音乐

    this.init_bg_img() // 背景图片

    this.init_float_img() // 页面漂浮物
  },
  created: function created() {
    this.init()
  },
  computed: {
    pageCount: function pageCount() {
      return Math.ceil(this.vote_items.page_total / this.vote_items.size)
    },
    pages: function pages() {
      var vthis = this
      return utils
        .unique(
          [
            1,
            this.pageCount,
            this.vote_items.page,
            this.vote_items.page - 1,
            this.vote_items.page - 2,
            this.vote_items.page + 1,
            this.vote_items.page + 2,
          ]
            .filter(function (n) {
              return n >= 1 && n <= vthis.pageCount
            })
            .sort(function (a, b) {
              return a - b
            })
        )
        .reduce(function (prev, current, index, array) {
          prev.push(current)
          array[index + 1] !== undefined &&
            array[index + 1] - array[index] > 1 &&
            prev.push("...")
          return prev
        }, [])
    },
  },
  methods: {
    init: function init() {
      var vthis = this

      // 插屏
      vthis.init_screen()

      // 已经选中的选手
      vthis.check_vote_item_ids = utils.get_stor("check_vote_item_ids", [])

      // 搜索选手关键词
      vthis.vote_items.keyword = utils.get_stor("search_keyword", "")
      utils.set_stor("search_keyword", "")

      // 报名上传图片缓存
      vthis.sign_uploads = utils.get_stor("sign_uploads", [])

      switch (vthis.current_page) {
        case "index":
          vthis
            .get_vote_item_types()
            .then(function (data) {
              // 加载选手
              return vthis.get_vote_items()
            })
            .then(function (data) {
              // 滚动到底事件
              if (vthis.vote.param.page_vote_item_load_type == 1) {
                vthis.init_scroll()
              }
              if (vthis.vote.param.display_index_show_type == 1) {
                vthis.sleep(950).then(function () {
                  vthis.$redrawVueMasonry()
                })
              }
            })
          break

        case "rank":
          // 加载分类
          vthis
            .get_vote_item_types()
            .then(function (data) {
              // 加载选手
              return vthis.get_vote_items()
            })
            .then(function (data) {
              // 滚动到底事件
              if (vthis.vote.param.page_vote_item_load_type == 1) {
                vthis.init_scroll()
              }
            })
          break

        case "detail":
          // 选手页获取当前选手

          vthis
            .get_vote_item()
            .then(function (data) {
              // 初始化选手页轮播图
              if (vthis.vote.param.display_detail_img_swp === 1) {
                vthis.vote_item.imgs = vthis.regArr(vthis.vote_item.content)
                vthis.vote_item.content = vthis.replaceContent(
                  vthis.vote_item.content
                )
                setTimeout(function () {
                  new Swiper(".swiper-container2", {
                    pagination: {
                      el: ".swiper-pagination2",
                    },
                    autoplay: vthis.vote.param.page_banner_auto
                      ? {
                          delay: vthis.vote.param.page_banner_second * 1000,
                        }
                      : false,
                    effect: vthis.vote.param.page_banner_effect,
                    loop: true,
                    autoHeight: true,
                  })
                  $(".noswp-box img").hide() // 隐藏其余图片
                }, 300)
              }
              // 获取评论
              return vthis.get_vote_item_comments()
            })
            .then(function (data) {
              // 安全期间，选手加载完再重新初始化一遍wxjssdk

              vthis.init_wx_js_sdk() // 微信jssdk

              // vthis.generateVideo(vthis.vote_item.cover_bom, "playpoint")
            })
          break

        case "sign":
          // 加载分类
          vthis.get_vote_item_types().then(function () {
            // 加载已报名选手
            vthis.get_sign_vote_items()
          })
          break

        case "rule":
          // 说明页
          break
      }
    },

    /**
     * 初始化轮播图
     */
    init_swiper: function init_swiper() {
      var vthis = this
      if (vthis.vote.param.vote_banners.length < 2) return
      new Swiper(".swiper-container1", {
        pagination: vthis.vote.param.page_banner_pagination
          ? {
              el: ".swiper-pagination1",
            }
          : false,
        autoplay: vthis.vote.param.page_banner_auto
          ? {
              delay: vthis.vote.param.page_banner_second * 1000,
            }
          : false,
        effect: vthis.vote.param.page_banner_effect,
        loop: true,
        autoHeight: true,
      })
    },

    /**
     * 初始化插屏
     * @param callback
     * @param time
     */
    init_screen: function init_screen(callback) {
      var vthis = this // 是否已展示过插屏 page_ad_show_times=1 表示每次都显示

      vthis.show_screen_ed =
        !vthis.vote.param.page_ad_show_times && $.cookie("show_screen_ed")

      if (!window.init_screen_time) {
        window.init_screen_time = setInterval(function () {
          vthis.vote.param.page_ad_second--

          if (vthis.vote.param.page_ad_second < 1) {
            clearInterval(window.init_screen_time)
            vthis.set_show_screen_ed_cookie()
            if (callback) callback()
          }
        }, 1000)
      } else {
        //页面没有刷新(window.init_screen_time就一直在)就一直不显示
        vthis.show_screen_ed = 1
      }
    },

    /**
     * 已经展示过插屏
     */
    set_show_screen_ed_cookie: function set_show_screen_ed_cookie() {
      var vthis = this
      if (vthis.vote.param.page_ad_show_times)
        //每次显示，就不存cookies了
        return
      var date = new Date()
      var sec = date.getSeconds()
      date.setSeconds(sec + vthis.vote.param.page_ad_show_minute * 60 + 1)
      $.cookie("show_screen_ed", 1, {
        expires: date,
        path: "/",
      })
    },

    /**
     * 关闭插屏
     */
    close_screen: function close_screen() {
      var vthis = this

      if (vthis.vote.param.page_ad_close) {
        vthis.vote.param.page_ad_second = 0
        vthis.set_show_screen_ed_cookie()
      }
    },

    /**
     * 获取选手分类
     */
    get_vote_item_types: function get_vote_item_types() {
      var vthis = this
      return new Promise(function (resolve, reject) {
        if (
          vthis.current_page !== "index" &&
          vthis.current_page !== "rank" &&
          vthis.current_page !== "sign"
        )
          return resolve()
        vthis.vote_item_types = utils.storage("vote_item_types", undefined, [])
        utils.request(
          vthis.api.get_vote_item_types,
          null,
          "get",
          function (data) {
            if (data.code !== 1) {
              vthis.error_msg = data.msg
              utils.show_tips(data.msg)
              return reject()
            }
            vthis.vote_item_types = data.data
            utils.storage("vote_item_types", vthis.vote_item_types)
            resolve(data)
          },
          function (data) {
            vthis.error_msg = data && data.msg ? data.msg : "加载选手分类失败"
          },
          true
        )
      })
    },

    /**
     * 获取当前页选手
     * 选手详情页面执行
     */
    get_vote_item: function get_vote_item() {
      var vthis = this
      return new Promise(function (resolve, reject) {
        var iid = utils.url_param("iid")
        if (vthis.current_page !== "detail" || !iid) return resolve()
        utils.request(
          vthis.api.get_vote_item,
          {
            iid: iid,
          },
          "get",
          function (data) {
            if (data.code !== 1) {
              vthis.error_msg = data.msg
              utils.show_tips(data.msg)
              return reject()
            }

            if (/&amp;/.test(data.data.title)) {
              data.data.title = data.data.title.replace(/&amp;/g, "&")
            }
            if (/&amp;/.test(data.data.slogan)) {
              data.data.slogan = data.data.slogan.replace(/&amp;/g, "&")
            }

            vthis.vote_item = data.data
            vthis.init_pjax()
            resolve()
          },
          function (data) {
            vthis.error_msg = data && data.msg ? data.msg : "加载选手失败"
            vthis.vote_items.running = false
            reject()
          },
          true
        )
      })
    },

    /**
     * 获取当前微信报名的选手
     */
    get_sign_vote_items: function get_sign_vote_items() {
      var vthis = this
      return new Promise(function (resolve, reject) {
        utils.request(
          vthis.api.get_sign_vote_items,
          {
            sign: 1,
          },
          "get",
          function (data) {
            if (data.code !== 1) {
              return reject()
            }

            vthis.sign_vote_items = data.data.vote_items
            resolve()
          },
          function (data) {
            reject()
          },
          true
        )
      })
    },

    /**
     * 获取选手列表
     */
    get_vote_items: function get_vote_items() {
      var vthis = this
      return new Promise(function (resolve, reject) {
        if (vthis.vote_items.done || vthis.vote_items.running) return resolve()
        if (vthis.current_page !== "index" && vthis.current_page !== "rank")
          return resolve()
        vthis.vote_items.running = true // 默认是否显示全部分类按钮

        if (!vthis.vote_items.vote_item_type_id) {
          if (
            vthis.vote_item_types.length > 0 &&
            vthis.vote.param[
              "display_" + vthis.current_page + "_vote_item_type_all_button"
            ] === 2
          ) {
            vthis.vote_items.vote_item_type_id = vthis.vote_item_types
              ? vthis.vote_item_types[0].id
              : 0
          }
        }

        var cache_key =
          "vote_items_" +
          vthis.current_page +
          "_" +
          vthis.vote_items.page +
          "_" +
          (vthis.vote_items.vote_item_type_id
            ? vthis.vote_items.vote_item_type_id
            : "0") // 缓存key，避免闪烁

        var cache_vote_items = utils.storage(cache_key, undefined, [])

        if (
          vthis.vote_items.page === 1 &&
          cache_vote_items &&
          cache_vote_items.length > 0
        ) {
          vthis.vote_items.data = cache_vote_items
        }

        utils.request(
          vthis.api.get_vote_items,
          {
            page: vthis.vote_items.page,
            keyword:
              vthis.current_page === "rank" ? "" : vthis.vote_items.keyword,
            vote_item_type_id: vthis.vote_items.vote_item_type_id,
            order:
              vthis.current_page === "index"
                ? vthis.vote.param.display_index_sort
                : 3,
            version: vthis.vote.param.page_vote_item_load_type == 2 ? 2 : "",
            size: vthis.vote_items.size,
          },
          "get",
          function (data) {
            if (data.code !== 1) {
              vthis.error_msg = data.msg
              utils.show_tips(data.msg)
              return reject()
            }
            if (vthis.vote.param.page_vote_item_load_type == 2) {
              vthis.vote_items.page_total = data.data.total
            }
            if (vthis.vote.param.page_vote_item_load_type == 1) {
              data.data.forEach(function (val) {
                if (/&amp;/.test(val.title)) {
                  val.title = val.title.replace(/&amp;/g, "&")
                }
                if (/&amp;/.test(val.slogan)) {
                  val.slogan = val.slogan.replace(/&amp;/g, "&")
                }
              })
              if (data.data.length > 0) {
                if (vthis.vote_items.page === 1) {
                  vthis.vote_items.data = data.data // 存储第一页选手

                  utils.storage(cache_key, vthis.vote_items.data, 300) // 存储第一页缓存
                } else {
                  data.data.forEach(function (e) {
                    vthis.vote_items.data.push(e)
                  })
                }

                vthis.vote_items.page++
                vthis.init_pjax() //重新初始化pjax
              } else {
                if (vthis.vote_items.page === 1) {
                  vthis.vote_items.data = data.data
                  utils.storage(cache_key, vthis.vote_items.data, 300) // 存储第一页缓存
                }

                vthis.vote_items.done = true
              }
            } else if (vthis.vote.param.page_vote_item_load_type == 2) {
              data.data.vote_items.forEach(function (val) {
                if (/&amp;/.test(val.title)) {
                  val.title = val.title.replace(/&amp;/g, "&")
                }
                if (/&amp;/.test(val.slogan)) {
                  val.slogan = val.slogan.replace(/&amp;/g, "&")
                }
              })
              if (data.data.vote_items.length > 0) {
                if (vthis.vote_items.page === 1) {
                  vthis.vote_items.data = data.data.vote_items
                  // 存储第一页选手
                  utils.storage(cache_key, vthis.vote_items.data, 300) // 存储第一页缓存
                } else {
                  vthis.vote_items.data = data.data.vote_items
                }
                vthis.init_pjax() //重新初始化pjax
              } else {
                if (vthis.vote_items.page === 1) {
                  vthis.vote_items.data = data.data.vote_items
                  utils.storage(cache_key, vthis.vote_items.data, 300) // 存储第一页缓存
                }
                vthis.vote_items.done = true
              }
            }
            vthis.vote_items.running = false
            resolve()
          },
          function (data) {
            vthis.error_msg = data && data.msg ? data.msg : "加载选手失败"
            vthis.vote_items.running = false
            reject()
          },
          true
        )
      })
    },

    /**
     * 根据选中的分类获取选手
     * @param vote_item_type
     * @param index
     */
    get_vote_items_by_type: function get_vote_items_by_type(
      vote_item_type,
      index
    ) {
      var _this = this

      if (this.vote_items.running) {
        // 正则加载中，还不行
        return
      }

      this.vote_items.vote_item_type_id = vote_item_type ? vote_item_type.id : 0
      this.vote_items.page = 1
      this.vote_items.done = false
      this.vote_items.keyword = ""
      this.get_vote_items().then(function () {
        if (_this.vote.param.display_index_show_type == 1) {
          _this.sleep(950).then(function () {
            _this.$redrawVueMasonry()
          })
        }
      })
    },

    /**
     * 根据搜索关键词获取选手
     * @returns {*}
     */
    get_vote_items_by_search: function get_vote_items_by_search() {
      var _this2 = this

      this.vote_items.keyword = this.$refs.keyword_input.value

      if (this.current_page !== "index") {
        utils.set_stor("search_keyword", this.vote_items.keyword)
        this.clear_layer()
        return this.pjax_go_page(this.api.index)
      }

      this.vote_items.vote_item_type_id = "0"
      this.vote_items.page = 1
      this.vote_items.done = false
      this.get_vote_items().then(function () {
        if (_this2.vote.param.display_index_show_type == 1) {
          _this2.sleep(950).then(function () {
            _this2.$redrawVueMasonry()
          })
        }

        _this2.clear_layer()
      })
    },
    sleep: function sleep(ms) {
      return new Promise(function (resolve) {
        return setTimeout(resolve, ms)
      })
    },

    /**
     * 关闭弹窗
     */
    clear_layer: function clear_layer() {
      $(".layui-layer").removeClass("anim-swing")
      layer.closeAll()
    },

    /**
     * 弹出搜索框
     */
    alert_search: function alert_search() {
      var searchImg = $(".widget-search-box").find(".search-icon img")

      if (searchImg.attr("src") == "") {
        searchImg.attr("src", searchImg.attr("data-src"))
      }

      utils.show_div_box(
        "",
        ".widget-search-box",
        null,
        null,
        null,
        [this.vote.param.style_tpl == 49 ? "100%" : "80%"],
        0.3,
        true,
        null,
        true,
        null,
        null,
        "skin-customer"
      )
    },

    /**
     * 清除搜索关键词
     */
    clear_search: function clear_search() {
      this.vote_items.vote_item_type_id = 0
      this.vote_items.page = 1
      this.vote_items.keyword = ""
      this.vote_items.done = false
      this.get_vote_items()
      utils.set_stor("search_keyword", "")
    },
    goPageCount: function goPageCount(n) {
      var that = this
      this.vote_items.page = n
      this.get_vote_items().then(function () {
        if (that.vote.param.display_index_show_type == 1) {
          that.sleep(950).then(function () {
            that.$redrawVueMasonry()
          })
        }
      })
    },
    /**
     * 页面滚动到底部时
     */
    init_scroll: function init_scroll() {
      var vthis = this
      if (vthis.current_page !== "index" && vthis.current_page !== "rank")
        return

      window.onscroll = function () {
        var scroll_top =
          document.documentElement.scrollTop || document.body.scrollTop
        var window_height =
          document.documentElement.clientHeight || document.body.clientHeight
        var scroll_height =
          document.documentElement.scrollHeight || document.body.scrollHeight

        if (
          scroll_top + window_height >=
          scroll_height - vthis.vote_items.scroll_bottom
        ) {
          vthis.get_vote_items()
        }
      }
    },

    /**
     * 初始化跑马灯
     */
    init_marquee: function init_marquee() {
      var vthis = this
      var mq = $(vthis.elements.marquee)
      mq[0] && mq.marquee()
      $(document).scroll(function () {
        var scroll_top =
          document.documentElement.scrollTop || document.body.scrollTop

        if (scroll_top > 25) {
          mq.css({
            opacity: 0.35,
          })
        } else {
          mq.removeAttr("style")
        }
      })
    },

    /**
     * 初始化倒计时
     * @param time
     */
    init_count_down: function init_count_down() {
      var vthis = this
      var box = $(vthis.elements.count_down_box)
      if (!box[0]) return

      if (!window.init_count_down_time) {
        // 定义一个定时器
        window.init_count_down_time = setInterval(function () {
          vthis.init_count_down()
        }, 1000)
      }

      var left_second = vthis.vote.param.diff_time
      var day = Math.floor(left_second / (60 * 60 * 24))
      var hour = Math.floor((left_second - day * 24 * 60 * 60) / 3600)
      var minute = Math.floor(
        (left_second - day * 24 * 60 * 60 - hour * 3600) / 60
      )
      var second = Math.floor(
        left_second - day * 24 * 60 * 60 - hour * 3600 - minute * 60
      )

      if (vthis.vote.param.style_tpl == 30) {
        box.html(
          '<span class="time-color">' +
            day +
            '</span> 天 <span class="time-color">' +
            hour +
            '</span> 时 <span class="time-color">' +
            minute +
            '</span> 分 <span class="time-color">' +
            second +
            "</span> 秒"
        )
      } else if (
        vthis.vote.param.style_tpl == 34 ||
        vthis.vote.param.style_tpl == 36 ||
        vthis.vote.param.style_tpl == 37 ||
        vthis.vote.param.style_tpl == 38 ||
        vthis.vote.param.style_tpl == 46 ||
        vthis.vote.param.style_tpl == 49
      ) {
        box.html(
          '<span class="time-color">' +
            day +
            '</span> 天 <span class="time-color">' +
            hour +
            '</span> 时 <span class="time-color">' +
            minute +
            '</span> 分 <span class="time-color">' +
            second +
            "</span> 秒"
        )
      } else {
        var vote_minute = vthis.vote.id == "04o65xa18nvwl" ? " 小时 " : " 时 "
        box.html(
          '<i class="fa fa-clock-o"></i> <span class="time-color">' +
            vthis.vote.param.diff_type +
            '</span> 倒计时 <span class="time-color">' +
            day +
            '</span> 天 <span class="time-color">' +
            hour +
            "</span>" +
            vote_minute +
            '<span class="time-color">' +
            minute +
            '</span> 分 <span class="time-color">' +
            second +
            "</span> 秒"
        )
      }

      vthis.vote.param.diff_time--

      if (vthis.vote.param.diff_time <= 0) {
        clearInterval(window.init_count_down_time)
        box.text("活动已" + vthis.vote.param.diff_type)
      }
    },

    /**
     * 分享海报弹窗 废弃
     * @param vote_item
     */
    create_share_img: function create_share_img(vote_item) {
      var vthis = this
      utils.request(
        vthis.api.create_share_img,
        {
          iid: vote_item.id,
        },
        "get",
        function (data) {
          if (data.code !== 1) {
            return utils.show_tips(data.msg)
          }

          vthis.create_share_img_result.data.img_url = data.data.img_url
          setTimeout(function () {
            // 投票结果弹窗
            utils.show_div_box(
              "",
              ".widget-create-share-img-result-box",
              null,
              null,
              false,
              "80%",
              0.3,
              true,
              false,
              true,
              data && data.code === 1 ? 0 : 6
            )
          }, 100)
        }
      )
    },

    /**
     * 分享海报弹窗
     */
    create_share_img2: function create_share_img2() {
      var vthis = this
      if (!vthis.vote_item) return
      utils.show_div_box(
        "",
        ".widget-share-box",
        function () {
          if ($(".poster .poster-img").length < 1) {
            var ly = utils.show_loading()
            setTimeout(function () {
              var qrcanvas = $(".poster .qrcode .canvas")
              qrcanvas.html("")
              qrcanvas.qrcode({
                width: 80,
                height: 80,
                correctLevel: 0,
                text: window.location.href,
              })
              html2canvas(document.querySelector(".poster"), {
                allowTaint: false,
                useCORS: true,
                scale: 2,
              })
                .then(function (canvas) {
                  utils.close_layer(ly)
                  var src = canvas.toDataURL("image/png", 1.0)
                  $(".poster").html(
                    '<img class="poster-img" style="width:100%;height:100%;" src="'.concat(
                      src,
                      '" />'
                    )
                  )
                })
                .catch(function () {
                  utils.close_layer(ly)
                  utils.show_tips("海报生成失败，请截图保存")
                })
            }, 500)
          }
        },
        null,
        false,
        "80%",
        0.3,
        true,
        false,
        true,
        0
      )
    },
    /**
     * 分享海报弹窗2
     */
    create_share_img_old3: function create_share_img_old3() {
      var vthis = this
      if (!this.isWeixin()) {
        utils.show_tips("请在微信中打开")
        return
      }
      if (!vthis.vote_item) return
      utils.show_div_box(
        "",
        ".share-box-wrapper",
        function () {
          if ($(".share-container .poster-img").length < 1) {
            var ly = utils.show_loading()
            var imgsrc = $(".share-container .share-icon img")
            imgsrc.attr("src", imgsrc.attr("data-src"))
            setTimeout(function () {
              var qrcanvas = $(".share-container .share-qrcode-img")
              qrcanvas.html("")
              qrcanvas.qrcode({
                width: 130,
                height: 130,
                correctLevel: 0,
                text: window.location.href,
              })
              html2canvas(document.querySelector(".share-container"), {
                allowTaint: false,
                useCORS: true,
                scale: 2,
              })
                .then(function (canvas) {
                  utils.close_layer(ly)
                  var src = canvas.toDataURL("image/png", 1.0)
                  $(".share-container").html(
                    '<img class="poster-img" style="width:100%;height:100%;" src="'.concat(
                      src,
                      '" />'
                    )
                  )
                })
                .catch(function () {
                  utils.close_layer(ly)
                  utils.show_tips("海报生成失败，请截图保存")
                })
            }, 500)
          }
        },
        null,
        false,
        "90%",
        [0.6, "#000"],
        true,
        false,
        true,
        0,
        null,
        "skin"
      )
    },

    // create_share_img3: function create_share_img3() {
    //   if (!this.isWeixin()) {
    //     utils.show_tips("请在微信中打开")
    //     return
    //   }
    //   this.showSharing = true
    // },
    /**
     * 分享海报弹窗3
     */
    create_share_img4: function create_share_img4() {
      var vthis = this
      if (!this.isWeixin()) {
        utils.show_tips("请在微信中打开")
        return
      }
      if (!vthis.vote_item) return
      utils.show_div_box(
        "",
        ".share-box-wrapper1",
        function () {
          if ($(".share-container1 .poster-img").length < 1) {
            var ly = utils.show_loading()
            setTimeout(function () {
              var qrcanvas = $(".share-container1 .share-qrcode-img1")
              qrcanvas.html("")
              qrcanvas.qrcode({
                width: 130,
                height: 130,
                correctLevel: 0,
                text: window.location.href,
              })
              html2canvas(document.querySelector(".share-container1"), {
                allowTaint: false,
                useCORS: true,
                scale: 2,
              })
                .then(function (canvas) {
                  utils.close_layer(ly)
                  var src = canvas.toDataURL("image/png", 1.0)
                  $(".share-container1").html(
                    '<img class="poster-img" style="width:100%;height:100%;" src="'.concat(
                      src,
                      '" />'
                    )
                  )
                })
                .catch(function () {
                  utils.close_layer(ly)
                  utils.show_tips("海报生成失败，请截图保存")
                })
            }, 500)
          }
        },
        null,
        false,
        "90%",
        [0.6, "#000"],
        true,
        false,
        true,
        0,
        null,
        "skin"
      )
    },
    /**
     * 定制海报弹窗
     */
    create_share_img5: function create_share_img5() {
      var vthis = this
      if (!this.isWeixin()) {
        utils.show_tips("请在微信中打开")
        return
      }
      if (!vthis.vote_item) return
      utils.show_div_box(
        "",
        ".share-box-wrapper2",
        function () {
          if ($(".share-container2 .poster-img").length < 1) {
            var ly = utils.show_loading()
            setTimeout(function () {
              var qrcanvas = $(".share-container2 .share-qrcode-img2")
              qrcanvas.html("")
              qrcanvas.qrcode({
                width: 62,
                height: 62,
                correctLevel: 0,
                text: window.location.href,
              })
              html2canvas(document.querySelector(".share-container2"), {
                allowTaint: false,
                useCORS: true,
                scale: 2,
              })
                .then(function (canvas) {
                  utils.close_layer(ly)
                  var src = canvas.toDataURL("image/png", 1.0)
                  $(".share-container2").html(
                    '<img class="poster-img" style="width:100%;height:100%;" src="'.concat(
                      src,
                      '" />'
                    )
                  )
                })
                .catch(function () {
                  utils.close_layer(ly)
                  utils.show_tips("海报生成失败，请截图保存")
                })
            }, 500)
          }
        },
        null,
        false,
        "90%",
        [0.6, "#000"],
        true,
        false,
        true,
        0,
        null,
        "skin"
      )
    },
    /**
     * 定制海报弹窗
     */
    create_share_img6: function create_share_img6() {
      var vthis = this
      if (!this.isWeixin()) {
        utils.show_tips("请在微信中打开")
        return
      }
      if (!vthis.vote_item) return
      utils.show_div_box(
        "",
        ".share-box-wrapper3",
        function () {
          if ($(".share-container3 .poster-img").length < 1) {
            var ly = utils.show_loading()
            setTimeout(function () {
              var qrcanvas = $(".share-container3 .share-qrcode-img3")
              qrcanvas.html("")
              qrcanvas.qrcode({
                width: 78,
                height: 78,
                correctLevel: 0,
                text: window.location.href,
              })
              html2canvas(document.querySelector(".share-container3"), {
                allowTaint: false,
                useCORS: true,
                scale: 4,
              })
                .then(function (canvas) {
                  utils.close_layer(ly)
                  var src = canvas.toDataURL("image/png", 1.0)
                  $(".share-container3").html(
                    '<img class="poster-img" style="width:100%;height:100%;" src="'.concat(
                      src,
                      '" />'
                    )
                  )
                })
                .catch(function () {
                  utils.close_layer(ly)
                  utils.show_tips("海报生成失败，请截图保存")
                })
            }, 500)
          }
        },
        null,
        false,
        "90%",
        [0.6, "#000"],
        true,
        false,
        true,
        0,
        null,
        "skin"
      )
    },
    /**
     * 定制海报弹窗
     */
    create_share_img7: function create_share_img7() {
      var vthis = this
      if (!this.isWeixin()) {
        utils.show_tips("请在微信中打开")
        return
      }
      if (!vthis.vote_item) return
      utils.show_div_box(
        "",
        ".share_yzjy-wrapper",
        function () {
          if ($(".share_yzjy-container .poster-img").length < 1) {
            var ly = utils.show_loading()
            var imgsrc = $(".share_yzjy-container .share_yzjy-icon img")
            imgsrc.attr("src", imgsrc.attr("data-src"))
            setTimeout(function () {
              var qrcanvas = $(".share_yzjy-container .share_yzjy-qrcode-img")
              qrcanvas.html("")
              qrcanvas.qrcode({
                width: 130,
                height: 130,
                correctLevel: 0,
                text: window.location.href,
              })
              html2canvas(document.querySelector(".share_yzjy-container"), {
                allowTaint: false,
                useCORS: true,
                scale: 3,
              })
                .then(function (canvas) {
                  utils.close_layer(ly)
                  var src = canvas.toDataURL("image/png", 1.0)
                  $(".share_yzjy-container").html(
                    '<img class="poster-img" style="width:100%;height:100%;" src="'.concat(
                      src,
                      '" />'
                    )
                  )
                })
                .catch(function () {
                  utils.close_layer(ly)
                  utils.show_tips("海报生成失败，请截图保存")
                })
            }, 500)
          }
        },
        null,
        false,
        "90%",
        [0.6, "#000"],
        true,
        false,
        true,
        0,
        null,
        "skin"
      )
    },
    /**
     * 新版海报弹窗
     */
    create_share_img3: function create_share_img3() {
      var vthis = this
      if (!this.isWeixin()) {
        utils.show_tips("请在微信中打开")
        return
      }
      if (!vthis.vote_item) return
      utils.show_div_box(
        "",
        ".share-new-box-wrapper",
        function () {
          if ($(".share-new-container .poster-img").length < 1) {
            var ly = utils.show_loading()
            setTimeout(function () {
              var qrcanvas = $(".share-new-container .share-new-qrcode-img")
              qrcanvas.html("")
              qrcanvas.qrcode({
                width: 80,
                height: 80,
                correctLevel: 0,
                text: window.location.href,
              })
              html2canvas(document.querySelector(".share-new-container"), {
                allowTaint: false,
                useCORS: true,
                scale: 2,
              })
                .then(function (canvas) {
                  utils.close_layer(ly)
                  var src = canvas.toDataURL("image/png", 1.0)
                  $(".share-new-container").html(
                    '<img class="poster-img" style="width:100%;height:100%;" src="'.concat(
                      src,
                      '" />'
                    )
                  )
                })
                .catch(function () {
                  utils.close_layer(ly)
                  utils.show_tips("海报生成失败，请截图保存")
                })
            }, 500)
          }
        },
        null,
        false,
        "90%",
        [0.6, "#000"],
        true,
        false,
        true,
        0,
        null,
        "skin"
      )
    },
    /**
     * 展示验证码
     * @param captcha_type
     * @param vote_item
     * @param index
     * @param submit_captcha
     */
    show_captcha: function show_captcha(
      captcha_type,
      vote_item,
      index,
      submit_captcha
    ) {
      var vthis = this

      switch (captcha_type) {
        case 1:
          // 验证码1
          vthis.init_captcha()
          utils.show_div_box(
            "",
            ".widget-captcha-box",
            null,
            null,
            false,
            "80%",
            0.3,
            true,
            false,
            true
          )
          break

        case 2:
          // 验证码2
          var bb = _dx.Captcha($(".widget-dx-captcha")[0], {
            appId: "1a4fcdbfbf13cef0df002b232315533d",
            style: "popup",
            success: function success(token) {
              vthis.send_vote_request.dx_captcha_token = token
              vthis.send_vote(vote_item, index, submit_captcha)
              bb.hide()
            },
          })

          bb.show()
          break
      }
    },

    /**
     * 开始投票
     * @param vote_item
     * @param index
     * @param submit_captcha
     * @returns {*|void}
     */
    send_vote: function send_vote(vote_item, index, submit_captcha) {
      var vthis = this

      if (vthis.vote.param.vote_rule.rule_type === 1) {
        //单选
        vthis.send_vote_request.id = vote_item
          ? vote_item.id
          : vthis.send_vote_request.id
      } else {
        //多选
        if (
          vthis.check_vote_item_ids.length < vthis.vote.param.vote_rule.rule_min
        )
          return utils.show_tips(
            "最少选择" +
              vthis.vote.param.vote_rule.rule_min +
              "个" +
              vthis.vote.param.text_vote_item_alias
          )
        if (
          vthis.check_vote_item_ids.length > vthis.vote.param.vote_rule.rule_max
        )
          return utils.show_tips(
            "最多选择" +
              vthis.vote.param.vote_rule.rule_max +
              "个" +
              vthis.vote.param.text_vote_item_alias
          )
        vthis.send_vote_request.id = vthis.check_vote_item_ids
      }

      if (vthis.vote.param.captcha && !submit_captcha) {
        // 验证码
        return vthis.show_captcha(
          vthis.vote.param.captcha,
          vote_item,
          index,
          submit_captcha
        )
      }

      utils.request(
        vthis.api.send_vote,
        {
          data: vthis.send_vote_request,
        },
        "post",
        function (data) {
          vthis.vote_result = data // 这个延迟可能导致重复点击，加上加载中图标

          var ly_load = utils.show_loading()
          setTimeout(function () {
            // 关闭加载中图标
            utils.close_layer(ly_load) // 投票成功跳转链接

            if (data.data && data.data.jump_link) {
              return utils.show_tips(
                data.msg,
                function () {
                  data.data.jump_link = data.data.jump_link.replace(
                    /&amp;/g,
                    "&"
                  )
                  utils.go_page(data.data.jump_link)
                },
                vthis.vote.param.vote_jump_second * 1000
              )
            } // 需要二次验证

            if (data.data && data.data.has_captcha) {
              return vthis.show_captcha(
                data.data.has_captcha,
                vote_item,
                index,
                submit_captcha
              )
            } // 检查是否显示广告

            vthis.ad_show_check()

            if (
              vthis.vote_result &&
              vthis.vote_result.msg == "页面停留时间过久，请刷新页面后重新操作"
            ) {
              vthis.vote_result.msg =
                "页面需要刷新后再操作，页面将于2秒后自动刷新"
              setTimeout(function () {
                window.location.reload()
              }, 2000)
            } // 投票结果弹窗

            var reg = /请在公众号内/g

            console.log(vthis.vote_result)
            console.log(reg.test(vthis.vote_result.msg))
            if (vthis.vote_result && reg.test(vthis.vote_result.msg)) {
              vthis.vote_result.msg = vthis.vote_result.msg.replace(
                reg,
                "长按识别上方二维码，"
              )
            }
            utils.show_div_box(
              "",
              ".widget-vote-result-box",
              null,
              null,
              false,
              vthis.vote.param.style_tpl == 49 ? "100%" : "80%",
              0.3,
              true,
              false,
              true,
              data && data.code === 1 ? 0 : 6,
              null,
              "skin-customer"
            )
          }, 100)

          if (data.code === 1) {
            // 投票成功，界面上票数加1
            if (
              vthis.vote_item &&
              vthis.send_vote_request.id.indexOf(vthis.vote_item.id) >= 0
            ) {
              var new_count = vthis.vote_item.vote_count
              new_count += 1
              vthis.$set(vthis.vote_item, "vote_count", new_count)
            }
            for (var i = 0; i < vthis.vote_items.data.length; i++) {
              if (
                vthis.send_vote_request.id.indexOf(
                  vthis.vote_items.data[i].id
                ) >= 0
              ) {
                vthis.vote_items.data[i].vote_count += 1
                vthis.vote.vote_count += 1
              }
            }

            vthis.clear_check_vote_item_ids() // 投完清理已选择的选手
          }
        }
      )
    },

    /**
     * 检查是否显示广告
     *  */
    ad_show_check: function ad_show_check() {
      var vthis = this
      if (!vthis.ad_config.show) return
      var count = utils.storage("show_times_count")

      if (!count) {
        count = 0
        utils.storage("show_times_count", count)
      }

      var next_date = utils.storage("next_date")

      var _nextDate = new Date(
        new Date().getTime() +
          86400000 -
          (new Date().getHours() * 60 * 60 +
            new Date().getMinutes() * 60 +
            new Date().getSeconds()) *
            1000
      ).getTime()

      if (!next_date) {
        next_date = _nextDate
        utils.storage("next_date", _nextDate)
      }

      var startDate = new Date().getTime()

      if (startDate >= next_date) {
        count = 0
        utils.storage("next_date", _nextDate)
      }

      count = parseInt(count) + 1
      utils.storage("show_times_count", count)
      var ad_url1 = utils.storage("ad_url1")

      if (!ad_url1) {
        ad_url1 = vthis.ad_config.ad1_link
        utils.storage("ad_url1", vthis.ad_config.ad1_link, 3600)
      }

      var ad_img1 = utils.storage("ad_img1")

      if (!ad_img1) {
        ad_img1 = vthis.ad_config.ad1_img_url
        utils.storage("ad_img1", vthis.ad_config.ad1_img_url, 3600)
      }

      // if (count == 2) {
      //   vthis.ad_config.ad1_link = vthis.ad_url2
      //   vthis.ad_config.ad1_img_url = vthis.ad_img2
      // } else if (count >= 3) {
      //   vthis.ad_config.ad1_link = ad_url1
      //   vthis.ad_config.ad1_img_url = ad_img1
      // }
      var ad_clicked = utils.storage("ad_clicked")

      if (count == 2) {
        vthis.ad_config.ad1_link = vthis.ad_url2
        vthis.ad_config.ad1_img_url = vthis.ad_img2
      } else if (count == 3) {
        vthis.ad_config.ad1_link = vthis.ad_url3
        // var ad_img3 = utils.storage("ad_img1")
        //   ? utils.storage("ad_img1")
        //   : "https://cdn.youtoupiao.com/pdddt1.gif"
        vthis.ad_config.ad1_img_url = vthis.ad_img3
      } else if (count >= 4) {
        vthis.ad_config.ad1_link = vthis.ad_url2
        var ad_img3 = utils.storage("ad_img1")
          ? utils.storage("ad_img1")
          : "https://cdn.youtoupiao.com/pdddt1.gif"
        vthis.ad_config.ad1_img_url = ad_img3
      }

      if (ad_clicked) return

      var ad_show_times_hour = utils.storage("ad_show_times_hour", undefined, 0)
      var ad_show_times_day = utils.storage("ad_show_times_day", undefined, 0)
      // vthis.show_ad = ad_show_times_hour < 2 && ad_show_times_day < 5
      vthis.show_ad = true

      if (vthis.show_ad) {
        utils.storage("ad_show_times_hour", ad_show_times_hour + 1, 3600)
        utils.storage("ad_show_times_day", ad_show_times_day + 1, 24 * 3600)
        vthis.ad_show()
      }
    },

    /**
     * 点击了广告
     */
    ad_click: function ad_click() {
      var vthis = this
      utils.storage("ad_clicked", true, 24 * 3600)
      utils.request(
        this.api.ad_statistics,
        {
          type: 2,
        },
        "post",
        function () {
          utils.go_page(vthis.ad_config.ad1_link)
        },
        function () {
          utils.go_page(vthis.ad_config.ad1_link)
        },
        true
      )
    },

    /**
     * 展示了广告
     */
    ad_show: function ad_show() {
      utils.request(
        this.api.ad_statistics,
        {
          type: 1,
        },
        "post",
        function () {},
        function () {},
        true
      )
    },

    /**
     * 提交验证码
     */
    submit_captcha: function submit_captcha() {
      var vthis = this

      if (!vthis.send_vote_request.captcha) {
        utils.anim_layer(6)
        return
      }

      vthis.clear_layer()
      vthis.send_vote(null, null, true)
    },

    /**
     * 选中投票
     * @param vote_item
     * @param index
     * @returns {*|void}
     */
    check_vote: function check_vote(vote_item, index) {
      var vthis = this

      if (vthis.check_vote_item_ids.indexOf(vote_item.id) >= 0) {
        // 取消
        vthis.check_vote_item_ids.removeByValue(vote_item.id)
      } else {
        if (
          vthis.check_vote_item_ids.length >=
          vthis.vote.param.vote_rule.rule_max
        ) {
          return utils.show_tips(
            "最多选择" +
              vthis.vote.param.vote_rule.rule_max +
              "个" +
              vthis.vote.param.text_vote_item_alias
          )
        }

        vthis.check_vote_item_ids.push(vote_item.id)
      }

      vthis.set_check_vote_item_ids(vthis.check_vote_item_ids)
    },

    /**
     * 选中选手
     * @param arr
     */
    set_check_vote_item_ids: function set_check_vote_item_ids(arr) {
      if (arr && arr.length > 0) utils.set_stor("check_vote_item_ids", arr)
      else utils.set_stor("check_vote_item_ids", [])
    },

    /**
     * 清除选中的选手
     */
    clear_check_vote_item_ids: function clear_check_vote_item_ids() {
      this.check_vote_item_ids = []
      this.set_check_vote_item_ids(null)
    },

    /**
     * 返回上一页
     */
    page_back: function page_back() {
      utils.go_back(this.api.index)
    },
    init_captcha: function init_captcha() {
      this.send_vote_request.captcha = ""
      utils.captcha()
    },
    handler_share_text: function handler_share_text(text) {
      var vthis = this
      if (text)
        return text
          .replace("{活动标题}", vthis.vote.title)
          .replace("{活动简介}", vthis.vote.describe)
          .replace("{选手编号}", vthis.vote_item ? vthis.vote_item.index : "")
          .replace("{选手标题}", vthis.vote_item ? vthis.vote_item.title : "")
          .replace(
            "{当前票数}",
            vthis.vote_item ? vthis.vote_item.vote_count : ""
          )
      return text
    },

    /**
     * 微信jssdk
     */
    init_wx_js_sdk: function init_wx_js_sdk() {
      var vthis = this
      wx.config(vthis.wx_js_config)
      setTimeout(function () {
        // 分享接口
        wx.ready(function () {
          if (!vthis.vote.param.share_open) {
            wx.hideAllNonBaseMenuItem()
          } else {
            var share_title = vthis.handler_share_text(
              vthis.vote_item
                ? vthis.vote.param.share_vote_item_title
                : vthis.vote.param.share_title
            )
            var share_desc = vthis.handler_share_text(
              vthis.vote_item
                ? vthis.vote.param.share_vote_item_desc
                : vthis.vote.param.share_desc
            )
            var share_link = location.href
            var share_img_url = vthis.vote.param.share_img
              ? vthis.vote.param.share_img.thumb
              : ""

            if (!share_img_url) {
              var regShare = /^<img/
              if (vthis.vote_item && regShare.test(vthis.vote_item.cover_bom)) {
                share_img_url = $(
                  "<div>" + vthis.vote_item.cover_bom + "</div>"
                )
                  .find("img")
                  .attr("src")
                if (share_img_url.indexOf("http") !== 0) share_img_url = ""
              } else if (
                vthis.vote.param.vote_banners &&
                vthis.vote.param.vote_banners.length > 0
              ) {
                share_img_url = vthis.vote.param.vote_banners[0].thumb_url
              }
            } // // 设置分享给微信、qq好友
            // wx.updateAppMessageShareData({
            //     title: share_title,
            //     desc: share_desc,
            //     link: share_link,
            //     imgUrl: share_img_url,
            //     success: function () {
            //     }
            // });
            // // 设置分享到朋友圈、qq空间等
            // wx.updateTimelineShareData({
            //     title: share_title,
            //     link: share_link,
            //     imgUrl: share_img_url,
            //     success: function () {
            //     }
            // });
            // 获取分享给微信好友，即将废弃

            wx.onMenuShareAppMessage({
              title: share_title,
              desc: share_desc,
              link: share_link,
              imgUrl: share_img_url,
              type: "",
              // 分享类型,music、video或link，不填默认为link
              dataUrl: "",
              // 如果type是music或video，则要提供数据链接，默认为空
              success: function success() {
                utils.request(
                  vthis.api.share,
                  {
                    type: 1,
                    iid: vthis.vote_item ? vthis.vote_item.id : "",
                  },
                  "post",
                  null,
                  null,
                  true
                )
              },
            }) // 获取分享到朋友圈，即将废弃

            wx.onMenuShareTimeline({
              title: share_title,
              link: share_link,
              imgUrl: share_img_url,
              success: function success() {
                utils.request(
                  vthis.api.share,
                  {
                    type: 2,
                    iid: vthis.vote_item ? vthis.vote_item.id : "",
                  },
                  "post",
                  null,
                  null,
                  true
                )
              },
            })
          }

          wx.getNetworkType({
            success: function success(res) {
              vthis.send_vote_request.network = res.networkType
            },
          })
        })
        wx.error(function (res) {
          console.log(res)
        }) // 微信图片预览

        var vote_item_content_box = $(".vote-item-content-box")

        if (vote_item_content_box) {
          var urls = []
          var imgs = vote_item_content_box.find("img")
          imgs.each(function (index, item) {
            var src = $(item).attr("src")
            urls.push(src)
          })
          imgs.bind("click", function (e) {
            wx.previewImage({
              current: $(e.currentTarget).attr("src"),
              urls: urls,
            })
          })
        }
      }, 100)
    },

    /**
     * pjax
     */
    init_pjax: function init_pjax() {
      if (!window.history || !history.pushState) return
      var vthis = this
      setTimeout(function () {
        $("section a[target!=_blank]")
          .off("click")
          .on("click", function () {
            var a = $(this)
            var href = a.attr("href")
            if (href && href.indexOf("javascript") === 0) return true
            window.onscroll = null
            vthis.pjax_go_page(href, function () {
              vthis.init_pjax()
              vthis.init_wx_js_sdk()
            })
            return false
          })
      }, 100)
    },
    pjax_go_page: function pjax_go_page(url, callback) {
      var _this = this
      utils.request(
        url,
        null,
        "get",
        function (data) {
          if (typeof data === "string") {
            if (_this.ad_config.show) {
              history.replaceState(null, null, url) // 替换当前url
            } else {
              history.pushState(null, null, url) // 替换当前url
            }

            var section = data.match(
              eval("/<section[^>]*>([\\s\\S.]*)<\\/section>/i")
            )[1] // 截取所需dom内容

            var title = data.match(/<title[^>]*>([\s\S.]*)<\/title>/i)[1] // 截取title

            $("section").eq(0).html(section) // 替换dom内容

            $("title").html(title) // 替换title

            $(window).scrollTop(0) // 初始化一下

            setTimeout(function () {
              utils.init()
            }, 500)
            if (callback) callback()
          }
        },
        function () {
          // 失败后刷新页面
          utils.reload_page()
        },
        true
      )
    },

    /**
     * 背景音乐
     */
    init_audio: function init_audio() {
      var vthis = this

      if (vthis.vote.param.bg_audio) {
        var audio_icon = $(vthis.elements.bg_audio)
        audio_icon.show()
        var audio = $("audio")

        if (audio.length <= 0) {
          audio = $(
            '<audio style="display: none;" loop="loop" controls="controls"><source src="' +
              vthis.vote.param.bg_audio.url +
              '" type="audio/mpeg" /></audio>'
          )
          audio.appendTo("body")
          document.addEventListener(
            "WeixinJSBridgeReady",
            function () {
              // 手动暂停的不自动播放
              if (!utils.get_stor("audio_pause", 0)) audio[0].play()
              if (audio[0].paused) audio_icon.removeClass("animation-rotate")
              else audio_icon.addClass("animation-rotate")
            },
            false
          )
        }

        audio_icon.bind("click", function () {
          if (audio[0].paused) {
            audio_icon.addClass("animation-rotate")
            audio[0].play()
            utils.del_stor("audio_pause") // 手动播放
          } else {
            audio_icon.removeClass("animation-rotate")
            audio[0].pause()
            utils.set_stor("audio_pause", 1) // 手动暂停
          }
        })

        if (audio[0].paused) {
          audio_icon.removeClass("animation-rotate")
        } else {
          audio_icon.addClass("animation-rotate")
        }
      }
    },

    /**
     * 背景图片
     */
    init_bg_img: function init_bg_img() {
      var vthis = this
      if (!vthis.vote.param.bg_img || vthis.vote.param.style_tpl == 2) return
      var bg_img_url = vthis.vote.param.bg_img.url
      $("body").css({
        "background-attachment": vthis.vote.param.bg_img_attachment
          ? vthis.vote.param.bg_img_attachment
          : "fixed",
        "background-size": vthis.vote.param.bg_img_size
          ? vthis.vote.param.bg_img_size
          : "100%",
        "background-image":
          vthis.vote.param.bg_img_attachment === "fixed"
            ? "none"
            : 'url("' + bg_img_url + '")',
        "background-color":
          vthis.vote.param.bg_img_attachment === "fixed" ? "transparent" : "",
        "background-position": "0 0",
      })

      if (vthis.vote.param.bg_img_attachment === "fixed") {
        $("body").append(
          "<style>body:before{content:'';position:fixed;z-index:-1;top:0;right:0;bottom:0;left:0;background-image:url(".concat(
            bg_img_url,
            ");background-size:inherit;}</style>"
          )
        )
      }
    },

    /**
     * 报名文件上传
     */
    sign_upload: function sign_upload(camera) {
      var vthis = this
      if (!vthis.is_login) return utils.show_tips("请在微信中打开")
      var regHttpUrl = /^http:/
      if (regHttpUrl.test(vthis.api.upload_token)) {
        vthis.api.upload_token = vthis.api.upload_token.replace(
          regHttpUrl,
          "https:"
        )
      }
      uploads.init({
        api_token: vthis.api.upload_token, //初始化文件上传工具
      })
      uploads.upfile(
        null,
        vthis.api.upload_sign_param,
        function (data, updata) {
          vthis.sign_uploads.push(data.data)
          utils.set_stor("sign_uploads", vthis.sign_uploads)
        },
        null,
        camera
      )
    },

    /**
     * 删除报名文件
     * @param upload
     * @param index
     */
    delete_sign_upload: function delete_sign_upload(upload, index) {
      var vthis = this
      vthis.sign_uploads.splice(index, 1)
    },

    /**
     * 页面漂浮物
     */
    init_float_img: function init_float_img() {
      var vthis = this
      if (!vthis.vote.param.page_float || $(".float-img-item").length >= 10)
        return
      var float_img_item =
        '<img class="float-img-item" src="' +
        vthis.vote.param.page_float.url +
        '">'

      for (var i = 0; i < 10; i++) {
        $("body").append(float_img_item)
      }

      var param = {
        delay: [400, 12000],
        left: [0, 90],
        duration: [2000, 20000],
        width: [2, 5],
      }
      $(".float-img-item").each(function (index) {
        var i = index + 1
        var delay =
          Math.floor(
            param.delay[0] + Math.random() * (param.delay[1] - param.delay[0])
          ) + Math.floor(200 + Math.random() * (200 - 50))
        var left = Math.floor(
          param.left[0] + Math.random() * (param.left[1] - param.left[0])
        )
        var duration =
          Math.floor(
            param.duration[0] +
              Math.random() * (param.duration[1] - param.duration[0])
          ) + Math.floor(1000 + Math.random() * (1000 - 200))
        var width = Math.floor(
          param.width[0] + Math.random() * (param.width[1] - param.width[0])
        )
        $(".float-img-item")
          .eq(i)
          .css({
            left: left + "%",
            animationDelay: delay + "ms",
            animationDuration: duration + "ms",
            width: width + "rem",
            fontSize: width + "rem",
          })
      })
    },

    /**
     * 弹出评论框
     */
    alert_comment: function alert_comment() {
      utils.show_div_box(
        null,
        ".widget-comment-box",
        null,
        null,
        null,
        ["100%"],
        0.3,
        true,
        false
      )
    },

    /**
     * 提交评论
     */
    comment_submit: function comment_submit() {
      var vthis = this
      var value = vthis.$refs.comment_textarea.value
      utils.request(
        vthis.api.send_comment,
        {
          content: value,
          iid: vthis.vote_item.id,
        },
        "post",
        function (data) {
          if (data.code === 1) {
            vthis.clear_layer()
            vthis.vote_item_comments.unshift(data.data.vote_item_comment)
          }

          utils.show_tips(data.msg)
        }
      )
    },

    /**
     * 获取选手评论列表
     */
    get_vote_item_comments: function get_vote_item_comments() {
      var vthis = this
      return new Promise(function (resolve, reject) {
        if (vthis.current_page !== "detail") return resolve()
        utils.request(
          vthis.api.get_vote_item_comments,
          {
            iid: vthis.vote_item.id,
          },
          "get",
          function (data) {
            if (data.code === 1) vthis.vote_item_comments = data.data.comments
            resolve()
          }
        )
      })
    },

    /**
     * 软键盘输入验证码
     */
    input_captcha: function input_captcha(val) {
      switch (val) {
        case "cancel":
          utils.close_layer()
          this.send_vote_request.captcha = ""
          break

        case "delete":
          var captcha = this.send_vote_request.captcha
          if (captcha.length > 0)
            this.send_vote_request.captcha = captcha.substring(
              0,
              captcha.length - 1
            )
          break

        default:
          this.send_vote_request.captcha += val

          if (this.send_vote_request.captcha.length >= 4) {
            this.submit_captcha()
          }

          break
      }
    },
    isAndroid: function isAndroid() {
      var u = navigator.userAgent
      var isAndroid = u.indexOf("Android") > -1
      return isAndroid
    },
    frame2img: function frame2img(val) {
      if (/^<iframe/.test(val)) {
        return '<img class="vote-item-cover" src="https://static2.weitoupiao.com/assets/common/img/video_icon.png">'
      }

      return val
    },
    voteComment: function voteComment(comment, index) {
      var _this3 = this

      if (!this.is_login) return utils.show_tips("请在微信中打开")
      utils.request(
        this.api.comment_like,
        {
          id: comment.id,
          like: comment.is_like ? 0 : 1,
        },
        "post",
        function (data) {
          if (data.code === 1) {
            if (!comment.is_like) {
              comment.is_like = 1
              comment.like_num++
            } else {
              comment.is_like = 0
              comment.like_num--
            }

            Vue.set(_this3.vote_item_comments, index, comment)
          }
        },
        function () {
          utils.show_tips("点赞失败")
        },
        true
      )
    },
    generateClassName: function generateClassName(index) {
      if (index + 1 >= 10 && index + 1 <= 20) {
        return "animate-delay-10"
      } else if (index + 1 > 20) {
        return ""
      }
      return "animate-delay-" + (index + 1)
    },
    isTvideo: function isTvideo(str) {
      return /^\<iframe.*v\.qq\.com/.test(str)
    },
    getVid: function getVid(str) {
      var reg = /^\<iframe.*v\.qq\.com.*\?vid=(\w+)\"/
      var vid = ""

      if (reg.test(str)) {
        vid = str.match(reg)[1]
      }

      return vid
    },
    generateVideo: function generateVideo(str, objId) {
      if (!this.isTvideo(str)) {
        return
      }

      var TvideoVid = this.getVid(str)
      var video = new tvp.VideoInfo()
      video.setVid(TvideoVid)
      var player = new tvp.Player("100%", "100%")
      player.setCurVideo(video)
      player.addParam("autoplay", "0")
      player.addParam("adplay", "0")
      player.addParam("player", "html5")
      player.write(objId)
    },
    strReplace: function strReplace(str) {
      var reg = /&amp;/g
      if (reg.test(str)) {
        return str.replace(reg, "&")
      }
      return str
    },
    regArr: function regArr(str) {
      var imgReg = /<img.*?(?:>|\/>)/gi
      var srcReg = /src=[\'\"]?([^\'\"]*)[\'\"]?/i
      var srcArr = []
      if (imgReg.test(str)) {
        var arr = str.match(imgReg)
        for (var i = 0; i < arr.length; i++) {
          srcArr.push(arr[i].match(srcReg)[1])
        }
      }
      if (
        this.vote_item &&
        this.vote_item.cover_bom &&
        imgReg.test(this.vote_item.cover_bom) &&
        srcReg.test(this.vote_item.cover_bom)
      ) {
        srcArr.unshift(this.vote_item.cover_bom.match(srcReg)[1])
      }
      return srcArr
    },
    replaceContent: function replaceContent(str) {
      var imgReg = /<img.*?(?:>|\/>)/gi
      if (imgReg.test(str)) {
        return str.replace(imgReg, "")
      }
      return str
    },
    init_detail_swiper: function init_detail_swiper() {
      var vthis = this
      if (!vthis.vote_item || !vthis.vote_item.content) return
      if (vthis.regArr(vthis.vote_item.content).length < 1) return
      new Swiper(".swiper-container", {
        pagination: {
          el: ".swiper-pagination",
        },
        autoplay: {
          delay: 2000,
        },
        loop: true,
        autoHeight: true,
      })
    },
    isWeixin: function isWeixin() {
      //判断是否是微信
      var ua = navigator.userAgent.toLowerCase()
      return ua.match(/MicroMessenger/i) == "micromessenger"
    },
    replaceTitle(str) {
      var reg = /\|/g
      if (reg.test(str)) {
        return str.replace(reg, "<br/>")
      }
      return str
    },
  },
})
