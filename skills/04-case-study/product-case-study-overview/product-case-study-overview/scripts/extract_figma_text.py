#!/usr/bin/env python3
"""Rút gọn kết quả get_metadata của Figma thành bản đọc được.

Dùng:  python3 extract_figma_text.py <file.json|file.xml> [--min-len 12] [--top 300]

Input là file JSON mà tool get_metadata lưu ra khi kết quả quá lớn
(danh sách [{"type":"text","text":"<xml...>"}]) hoặc file XML thô.
In ra: các section (nhóm tính năng), tên frame (màn hình) và các text layer
(tên text layer trong Figma thường chính là nội dung chữ), xếp theo tần suất.
"""
import argparse
import html
import json
import re
from collections import Counter


def load_xml(path):
    raw = open(path, encoding="utf-8").read()
    try:
        data = json.loads(raw)
        if isinstance(data, list):
            return "".join(x.get("text", "") for x in data if isinstance(x, dict))
        if isinstance(data, dict):
            return data.get("text", raw)
    except json.JSONDecodeError:
        pass
    return raw


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("path")
    ap.add_argument("--min-len", type=int, default=12, help="độ dài tối thiểu của text layer")
    ap.add_argument("--top", type=int, default=300, help="số text layer tối đa in ra")
    a = ap.parse_args()

    xml = load_xml(a.path)
    tag = re.compile(r'^(\s*)<(section|frame|text|canvas)\s[^>]*?name="([^"]*)"', re.M)

    sections, frames, texts = [], Counter(), Counter()
    for m in tag.finditer(xml):
        indent, kind, name = len(m.group(1)), m.group(2), html.unescape(m.group(3))
        if kind in ("section", "canvas"):
            sections.append(("  " * (indent // 2)) + name)
        elif kind == "frame" and indent <= 6:
            frames[name] += 1
        elif kind == "text" and len(name) >= a.min_len:
            texts[name] += 1

    print("## SECTIONS (nhóm tính năng)")
    print("\n".join(sections) or "(không có)")
    print("\n## FRAMES cấp màn hình (tên × số lần)")
    for n, c in frames.most_common(150):
        print(f"{c:4d}  {n}")
    print("\n## TEXT LAYERS (nội dung chữ × số lần)")
    for n, c in texts.most_common(a.top):
        print(f"{c:4d}  {n}")


if __name__ == "__main__":
    main()
