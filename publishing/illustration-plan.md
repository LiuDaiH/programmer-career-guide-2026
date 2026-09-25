# 配图方案 · 程序员职业方向与核心技术栈全景指南（2026 版）

设计原则：所有配图只用官方 Logo 加极简连线，不放装饰插画。技术类文章的配图越素越可信，越花哨越像营销号。目标是信息密度高、一眼看懂关系。

## 通用规范

**Logo 来源**

一律去各项目官网的 brand / press / media kit 页面下载 SVG 或官方 PNG。不要用图标站（iconfont、iconify 等）的二次绘制版本。

**统一处理**

所有 Logo 统一高度，不要统一宽度。统一宽度会把方形 Logo 拉扁。保持原始比例。

**背景**

统一浅底，白色或极浅灰。深色 Logo 放浅底，浅色 Logo 加圆角底板，不要让 Logo 融进背景。

---

## 一、封面图

**类型**：蓝紫渐变抽象图加标题文字，不放任何具体 Logo。

**做法**

底图用蓝紫渐变配合抽象几何或网格线条，暗示"技术地图"的概念。标题分层，主标题「程序员职业方向与核心技术栈全景指南」，副标题「2026 版」。版面留白要大，文字占三分之一以内。

**为什么不放 Logo**：封面放 Logo 会显得像某家公司的宣传物料，抽象图更中立，也更耐看。

---

## 二、前端开发工程师

**类型**：Logo 矩阵，按"语言 → 框架 → 构建工具"分三层。

| 分组 | Logo | 来源官网 |
| --- | --- | --- |
| 语言 | TypeScript | typescriptlang.org |
| 框架 | React、Vue、Next.js | react.dev、vuejs.org、nextjs.org |
| 构建工具 | Vite、Rspack | vite.dev、rspack.dev |

**版式建议**：三行横排，每行左侧标一个小组名，Logo 在右侧排开。让读者一眼看出构建工具是最新、也最该关注的一层，可以把它单独放在最下面一行做视觉强调。

---

## 三、后端开发工程师

**类型**：语言与框架的对应关系图，下接容器与中间件底座。

| 分组 | Logo | 来源官网 |
| --- | --- | --- |
| 语言 | Java、Go、Python | oracle.com（或 openjdk.org）、go.dev、python.org |
| 框架 | Spring Boot、Gin、FastAPI | spring.io、gin-gonic.com、fastapi.tiangolo.com |
| 容器与中间件 | Docker、Kafka | docker.com、kafka.apache.org |

**版式建议**：上半部分做语言到框架的连线对应，即 Java 对 Spring Boot、Go 对 Gin、Python 对 FastAPI。下半部分把 Docker 与 Kafka 放在一条横条上，视觉上表达"容器化和中间件是所有后端的公共地基"。

**版权提醒**：Java 商标归 Oracle，对变形和改色最敏感，必须按官方原样使用。

---

## 四、大数据 / 数据工程师

**类型**：横向数据流管线图。这是最值得认真画的一张。

| 环节 | Logo | 来源官网 |
| --- | --- | --- |
| 分布式存储 | HDFS（Hadoop） | hadoop.apache.org |
| 批处理与流处理 | Spark、Flink | spark.apache.org、flink.apache.org |
| 数据总线 | Kafka | kafka.apache.org |
| 数仓与查询 | Hive、ClickHouse | hive.apache.org、clickhouse.com |
| 调度 | DolphinScheduler、Airflow | dolphinscheduler.apache.org、airflow.apache.org |

**版式建议**：一条从左到右的主线，HDFS 到 Spark 与 Flink 到 Kafka 到 Hive 与 ClickHouse。在 Spark 与 Flink 之间做分叉，旁边标注"批处理用 Spark，流处理用 Flink"。这一张图能替掉一大段文字。

**版权提醒**：均为 Apache 基金会项目，Logo 需遵守 ASF 的商标政策，不用于商业宣传即可。

---

## 五、AI / 算法工程师

**类型**：纵向管线图，自训练到部署。

| 环节 | Logo | 来源官网 |
| --- | --- | --- |
| 框架 | PyTorch、TensorFlow | pytorch.org、tensorflow.org |
| 应用 | LangChain、Hugging Face | langchain.com、huggingface.co |
| MLOps | MLflow | mlflow.org |
| 部署 | FastAPI、vLLM | fastapi.tiangolo.com、docs.vllm.ai |

**版式建议**：自上而下三层，PyTorch 与 TensorFlow 代表建模，MLflow 代表实验跟踪与模型管理，FastAPI 与 vLLM 代表服务化部署。把 LangChain 与 Hugging Face 放在侧边作为分支，表示"大模型应用"是与传统训练并行的一条路。

---

## 六、DevOps / 云原生工程师

**类型**：横向流水线图。

| 环节 | Logo | 来源官网 |
| --- | --- | --- |
| 代码 | Git | git-scm.com |
| 容器化 | Docker | docker.com |
| 编排 | Kubernetes | kubernetes.io |
| 持续部署 | Argo CD | argoproj.github.io |
| 可观测 | Grafana、Prometheus | grafana.com、prometheus.io |
| 基础设施即代码 | Terraform | hashicorp.com |

**版式建议**：主线为 Git 到 Docker 到 Kubernetes 到 Argo CD 到 Grafana 与 Prometheus。下面用虚线挂一条 Terraform，表示"基础设施即代码"是贯穿全程的底座，不落在某一步上。

**版权提醒**：Kubernetes 与 Prometheus 属 CNCF。HashiCorp 已改用 BUSL 许可，Logo 用于技术介绍没有问题，但不要用它的品牌做产品宣传。

---

## 七、技术栈速查表配图

**类型**：把文末表格重绘成一张竖版长图，适合手机滑动阅读。

**做法**

用 Figma 或 Canva 制作，导出 PNG @2x。五个方向各做成一张卡片，卡片内分四栏：核心语言、框架引擎、关键工具、数据库存储。不要逐格画线，用留白和字号区分层级，比表格线更清爽。宽度 1080px，高度按内容约 2400 至 3200px，字号不低于 28px。

**这张图的定位是让读者能截图收藏**，所以它要能独立看懂，标题写上「2026 技术栈速查」。

---

## 版权注意事项

文末加一句即可：**图片来自各项目官网，仅用于技术介绍，版权归原作者所有。**

三条实操底线：

1. 只用官方原始 Logo，不改色、不拉伸、不加描边。Java（Oracle）与 Kubernetes（CNCF）对变形最敏感
2. 不做暗示背书，图上不要出现"推荐""首选"这类字样，避免被理解为品牌代言
3. 商用需重绘。用于付费课程或商业培训时，Logo 要自己重画，或改用简化的文字标签

---

## 执行清单

| # | 任务 | 产出 |
| --- | --- | --- |
| 1 | 封面：蓝紫渐变加标题 | 1 张，1200×675 |
| 2 | 前端：三层 Logo 矩阵 | 1 张 |
| 3 | 后端：语言与框架连线加底座 | 1 张 |
| 4 | 大数据：横向数据流管线 | 1 张 |
| 5 | 算法：纵向训练到部署管线 | 1 张 |
| 6 | DevOps：横向 CI/CD 流水线 | 1 张 |
| 7 | 速查表长图，Figma 重绘 | 1 张，1080 宽 |
| 8 | 文末加版权声明 | 一句话 |

合计 7 张图，全部采用单色底加官方 Logo 加细连线，视觉语言统一。

---

## 三个容易踩的坑

**Logo 风格不统一**。一部分用彩色正式版，一部分用图标站的单色版，整篇看起来会像网上东拼西凑的。下载时统一选彩色正式版。

**Logo 拉变形**。统一宽度而非高度，是一眼就能看出是外行做的。

**速查表字号太小**。手机上根本看不清，等于白画。宁可加长图片也不缩字号。
