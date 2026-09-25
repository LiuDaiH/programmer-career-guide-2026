# 程序员职业方向与核心技术栈全景指南（2026 版）

一份面向「想搞清楚该往哪个方向走」的技术地图。按**五大主流方向**拆解，每个方向回答三个问题：

- **它在干什么** —— 一句话说清岗位实质
- **要学什么** —— 核心语言 / 框架引擎 / 关键工具 / 数据存储
- **怎么上手** —— 前 90 天的学习顺序，以及这个方向的反面（门槛、淘汰率、常见学习顺序错误）

覆盖方向：**前端 · 后端 · 大数据 · AI/算法 · DevOps/云原生**

---

## 内容

| 文件 | 说明 |
| --- | --- |
| [`article.md`](article.md) | **正文**（Markdown） |
| [`illustration-plan.md`](illustration-plan.md) | 配图方案：每张图的类型、需要的官方 Logo 与来源、版权注意 |
| [`publishing-guide.md`](publishing-guide.md) | 发布到微信公众号的操作说明 |
| [`wechat.html`](wechat.html) | 公众号可用的排版版本（全内联样式） |
| [`images/cover.png`](images/cover.png) | 封面（900×383，公众号首图标准比例） |
| [`images/cheatsheet.png`](images/cheatsheet.png) | 技术栈速查长图（1080 宽，适合手机阅读与截图收藏） |
| [`images/screenshots/`](images/screenshots/) | 16 张真实软件界面截图 |
| [`scripts/make_images.py`](scripts/make_images.py) | 生成封面与速查表的脚本（PIL，可传 JSON 配置） |

## 技术栈速览

| 方向 | 核心语言 | 必备框架 / 引擎 | 关键工具 | 数据库 / 存储 |
| --- | --- | --- | --- | --- |
| 前端 | TypeScript | React / Next.js、Vue | Vite、Rspack | — |
| 后端 | Java / Go / Python | Spring Boot、Gin、FastAPI | Docker、Kafka | PostgreSQL、Redis |
| 大数据 | SQL / Python / Scala | Spark、Flink | Kafka、Airflow / DolphinScheduler | HDFS、Hive、Iceberg |
| 算法 | Python | PyTorch、TensorFlow | LangChain、MLflow、vLLM | 向量数据库 |
| DevOps | Go / Python / Bash | Kubernetes | Docker、Terraform、Argo CD | Prometheus、Grafana |

## 图片来源

`images/screenshots/` 下的界面截图**全部来自各项目官方文档站**，是真实软件界面，非宣传图。

> 图片来自各项目官网，仅用于技术介绍，版权归原作者所有。

**没有图标站的二次绘制版本** —— 技术类文章的配图越素越可信。

## 重新生成配图

```bash
python scripts/make_images.py --config spec.json --out ./images
```

不传 `--config` 会用内置示例数据。依赖 Pillow；中文字体用系统的微软雅黑（`msyhbd.ttc`）。

## 说明

- 文中的份额、采用率等数字来自公开行业报告与各项目官方数据，不同来源口径可能存在差异，仅供参考。
- 正文里的「官网」链接在成稿时逐个访问验证过可达性。
