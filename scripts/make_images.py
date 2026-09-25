"""生成公众号封面 + 技术栈速查表长图
=====================================

样式约定（与文章一致的克制风格）：
- 无装饰性图案、无 emoji
- 封面：蓝紫渐变 + 极细网格 + 少量几何线，标题居中偏左
- 速查表：浅灰底 + 白色卡片，靠字号与留白分层级，不用表格线

用法：python make_images.py
输出到 C:\\Users\\liuDH\\Desktop\\文章配图\\
"""

from __future__ import annotations

import os
from PIL import Image, ImageDraw, ImageFont

OUT = r"C:\Users\liuDH\Desktop\文章配图"
BOLD = r"C:\Windows\Fonts\msyhbd.ttc"
REG = r"C:\Windows\Fonts\msyh.ttc"


def F(path: str, size: int):
    return ImageFont.truetype(path, size)


def lerp(a, b, t):
    return tuple(int(round(a[i] + (b[i] - a[i]) * t)) for i in range(3))


# --------------------------------------------------------------------------- #
def make_cover(w: int = 900, h: int = 383) -> str:
    """公众号首图 900x383（2.35:1）"""
    # 对角渐变，蓝 -> 紫
    c1, c2 = (24, 27, 84), (98, 62, 168)
    img = Image.new("RGB", (w, h))
    px = img.load()
    for y in range(h):
        for x in range(w):
            t = (x / w * 0.6 + y / h * 0.4)
            px[x, y] = lerp(c1, c2, t)

    ov = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(ov)

    # 极细网格
    for x in range(0, w, 60):
        d.line([(x, 0), (x, h)], fill=(255, 255, 255, 16), width=1)
    for y in range(0, h, 60):
        d.line([(0, y), (w, y)], fill=(255, 255, 255, 16), width=1)

    # 两条斜线做纵深（很淡）
    d.line([(w * 0.62, 0), (w, h * 0.75)], fill=(255, 255, 255, 26), width=1)
    d.line([(w * 0.72, 0), (w, h * 0.55)], fill=(255, 255, 255, 18), width=1)

    # 左侧竖直色块，压住文字区
    d.rectangle([0, 0, 520, h], fill=(0, 0, 0, 38))

    img = Image.alpha_composite(img.convert("RGBA"), ov).convert("RGB")
    d = ImageDraw.Draw(img)

    x0 = 72
    f_main = F(BOLD, 46)
    f_sub = F(REG, 19)

    d.text((x0, 96), "程序员职业方向", font=f_main, fill=(255, 255, 255))
    d.text((x0, 156), "与核心技术栈全景指南", font=f_main, fill=(255, 255, 255))

    # 细分隔线
    d.line([(x0, 232), (x0 + 56, 232)], fill=(255, 255, 255, 130), width=2)

    d.text((x0, 256), "2026 版", font=f_sub, fill=(210, 205, 240))
    d.text((x0 + 86, 256), "五大方向 · 核心工具速览", font=f_sub, fill=(170, 165, 205))

    p = os.path.join(OUT, "封面.png")
    img.save(p, "PNG")
    return p


# --------------------------------------------------------------------------- #
DATA = [
    ("前端开发工程师", [
        ("核心语言", "TypeScript"),
        ("框架 / 引擎", "React / Next.js、Vue"),
        ("关键工具", "Vite、Rspack"),
        ("数据库 / 存储", "—"),
    ]),
    ("后端开发工程师", [
        ("核心语言", "Java / Go / Python"),
        ("框架 / 引擎", "Spring Boot、Gin、FastAPI"),
        ("关键工具", "Docker、Kafka"),
        ("数据库 / 存储", "PostgreSQL、Redis"),
    ]),
    ("大数据 / 数据工程师", [
        ("核心语言", "SQL / Python / Scala"),
        ("框架 / 引擎", "Spark、Flink"),
        ("关键工具", "Kafka、Airflow / DolphinScheduler"),
        ("数据库 / 存储", "HDFS、Hive、Iceberg"),
    ]),
    ("AI / 算法工程师", [
        ("核心语言", "Python"),
        ("框架 / 引擎", "PyTorch、TensorFlow"),
        ("关键工具", "LangChain、MLflow、vLLM"),
        ("数据库 / 存储", "向量数据库"),
    ]),
    ("DevOps / 云原生工程师", [
        ("核心语言", "Go / Python / Bash"),
        ("框架 / 引擎", "Kubernetes"),
        ("关键工具", "Docker、Terraform、Argo CD"),
        ("数据库 / 存储", "Prometheus、Grafana"),
    ]),
]


def make_cheatsheet(width: int = 1080) -> str:
    pad = 48
    card_w = width - pad * 2
    head_h = 210
    card_pad = 34
    row_h = 54
    title_h = 52
    gap = 22

    card_h = card_pad + title_h + len(DATA[0][1]) * row_h + card_pad
    total_h = head_h + len(DATA) * card_h + (len(DATA) - 1) * gap + pad

    img = Image.new("RGB", (width, total_h), (244, 245, 247))
    d = ImageDraw.Draw(img)

    f_h = F(BOLD, 50)
    f_hs = F(REG, 22)
    f_ct = F(BOLD, 33)
    f_lb = F(REG, 21)
    f_vl = F(BOLD, 25)

    d.text((pad, 58), "2026 技术栈速查", font=f_h, fill=(26, 26, 26))
    d.text((pad + 2, 128), "五大方向 · 核心语言 / 框架 / 工具 / 存储", font=f_hs, fill=(140, 143, 150))
    d.line([(pad, head_h - 30), (width - pad, head_h - 30)], fill=(226, 228, 233), width=1)

    y = head_h
    for name, rows in DATA:
        # 白卡片
        d.rounded_rectangle([pad, y, pad + card_w, y + card_h], radius=14, fill=(255, 255, 255))
        # 左侧色条
        d.rounded_rectangle([pad, y + 26, pad + 5, y + card_h - 26], radius=3, fill=(76, 110, 245))

        d.text((pad + card_pad, y + card_pad), name, font=f_ct, fill=(26, 26, 26))
        ry = y + card_pad + title_h + 8
        for lb, vl in rows:
            d.text((pad + card_pad, ry + 8), lb, font=f_lb, fill=(150, 153, 160))
            d.text((pad + card_pad + 210, ry + 4), vl, font=f_vl, fill=(56, 58, 64))
            ry += row_h
        y += card_h + gap

    p = os.path.join(OUT, "速查表.png")
    img.save(p, "PNG")
    return p


if __name__ == "__main__":
    print("  封面  ->", make_cover())
    print("  速查表 ->", make_cheatsheet())
