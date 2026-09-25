<p align="center">
  <img src="images/cover.png" alt="程序员职业方向与核心技术栈全景指南（2026 版）" width="720">
</p>

# 程序员职业方向与核心技术栈全景指南（2026 版）

一份面向「想搞清楚该往哪个方向走」的技术地图。按**五大主流方向**拆解，每个方向回答三个问题：

- **它在干什么** —— 一句话说清岗位实质
- **要学什么** —— 核心语言 / 框架引擎 / 关键工具 / 数据存储
- **怎么上手** —— 前 90 天的学习顺序，以及这个方向的反面（门槛、淘汰率、常见学习顺序错误）

覆盖方向：**前端 · 后端 · 大数据 · AI/算法 · DevOps/云原生**

---

## 目录

| 你想找什么 | 去哪 |
| --- | --- |
| **正文** | [article.md](article.md) |
| 配图怎么做的（Logo 来源、版权） | [publishing/illustration-plan.md](publishing/illustration-plan.md) |
| 发到微信公众号 | [publishing/wechat-guide.md](publishing/wechat-guide.md) · [publishing/wechat.html](publishing/wechat.html) |
| 封面 / 速查表怎么生成的 | [scripts/make_images.py](scripts/make_images.py) |
| 全部配图 | [images/](images/) |

> 如果你是**只想读文章**，直接点 [article.md](article.md) 就行，其余都是制作过程。

## 五个方向速览

| 方向 | 主要做什么 | 入行门槛 | 招聘热度 |
| --- | --- | --- | --- |
| 前端 | 把产品呈现给用户，并保证它好用 | 中低 | 高 |
| 后端 | 承载业务逻辑与数据，互联网的底层基石 | 中 | 最高 |
| 大数据 | 让海量数据能被存下、算清、用起来 | 中高 | 中高 |
| AI / 算法 | 让机器从数据里学到能力 | 最高 | 高（增长最快） |
| DevOps / 云原生 | 让代码可靠地跑起来、发出去、看得见 | 中 | 中高 |

## 技术栈速查（可直接截图收藏）

<p align="center">
  <img src="images/cheatsheet.png" alt="2026 技术栈速查表" width="560">
</p>

## 仓库结构

```
.
├── article.md                     正文（从这里开始）
├── images/
│   ├── cover.png                  封面（900×383）
│   ├── cheatsheet.png             技术栈速查长图（1080 宽）
│   └── screenshots/               16 张软件界面截图，按方向命名
│       ├── frontend-*.png         前端：VS Code / Chrome DevTools
│       ├── backend-*.png          后端：Postman
│       ├── bigdata-*.png          大数据：Airflow / Spark UI
│       ├── ai-*.png               算法：JupyterLab
│       └── devops-*.png           DevOps：Argo CD / Grafana
├── publishing/                    制作与发布（不是文章本身）
│   ├── illustration-plan.md       配图方案
│   ├── wechat-guide.md            公众号发布说明
│   └── wechat.html                公众号排版版本
└── scripts/
    └── make_images.py             生成封面与速查表
```

**命名的用意**：截图前缀就是它所属的方向。想看某方向的界面图，按前缀找即可。

## 图片来源与版权

`images/screenshots/` 下的界面截图**全部来自各项目官方文档站**，是真实软件界面，不是宣传图。

> 图片来自各项目官网，仅用于技术介绍，版权归原作者所有。

没有使用图标站的二次绘制版本 —— 技术类文章的配图越素越可信。

## 重新生成配图

```bash
python scripts/make_images.py --config spec.json --out ./images
```

不传 `--config` 会用内置示例数据。依赖 Pillow；中文字体用系统自带的微软雅黑。

## 说明

- 文中的份额、采用率等数字来自公开行业报告与各项目官方数据，不同来源口径可能存在差异，仅供参考。
- 正文里的「官网」链接在成稿时逐个访问验证过可达性。
