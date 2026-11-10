#!/usr/bin/env python3
"""Build a UI/UX competitor-analysis workbook (.xlsx) from a JSON content file.

Usage:
    python build_workbook.py content.json "/mnt/user-data/outputs/[UXUI] Competitor Analysis <App>.xlsx"

The JSON schema is documented in references/json_schema.md and a full example lives in
assets/example_deepstash.json. The script validates the content first and exits with a
readable error list if something is missing or a row has the wrong number of app values.
"""
import json
import re
import sys

from openpyxl import Workbook
from openpyxl.cell.rich_text import CellRichText, TextBlock
from openpyxl.cell.text import InlineFont
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter

F = "Arial"
DARK, HEAD, LIGHT = "1F2A44", "34495E", "E8EEF7"
thin = Side(style="thin", color="C9D1DE")
BORDER = Border(left=thin, right=thin, top=thin, bottom=thin)
WRAP = Alignment(wrap_text=True, vertical="top")
CENTER = Alignment(wrap_text=True, vertical="center", horizontal="center")

SHEETS = [
    ("📋 Tổng quan", "Sheet này — điều hướng nhanh và tổng hợp toàn bộ nội dung"),
    ("👤 Chân dung người dùng", "Hồ sơ người dùng mục tiêu, pain points, hành vi sử dụng"),
    ("🎨 Phân tích UI", "Phong cách thiết kế, màu sắc, typography, layout từng app"),
    ("⚙️ UX & Tính năng", "Danh sách tính năng, vấn đề được giải quyết, tích hợp AI"),
    ("📊 SWOT", "Điểm mạnh / Điểm yếu / Cơ hội / Thách thức"),
    ("♟️ Ma trận chiến lược", "Hướng đi SO / WO / ST / WT từ phân tích SWOT"),
    ("💰 Mô hình giá", "Giá cả, cơ chế chuyển đổi, chiến lược giữ chân người dùng"),
    ("💡 Đề xuất sản phẩm", None),  # description filled from proposal name
    ("📖 Bảng thuật ngữ", "Giải thích các thuật ngữ chuyên ngành UI/UX & lĩnh vực sản phẩm"),
]
QUAD_FILL = {"ĐIỂM MẠNH": "D9EAD3", "ĐIỂM YẾU": "F4CCCC", "CƠ HỘI": "CFE2F3", "THÁCH THỨC": "FCE5CD"}
MATRIX_FILL = ["D9EAD3", "FFF2CC", "CFE2F3", "F4CCCC"]

# Inline labels such as "Graphic Style:", "- Điểm yếu:", "- Document Scan:" are bolded.
# Write a colon only right after such a label; use "—" for colons inside ordinary sentences.
LBL = re.compile(r"^(- )?([^:\n\d]{2,40}):( |$)")
# A dash label longer than this is usually a sentence that happens to contain a colon.
MAX_DASH_LABEL = 36


def fill(c):
    return PatternFill("solid", start_color=c)


def rich(v):
    if not isinstance(v, str) or ":" not in v:
        return v
    parts, hit = [], False
    for k, line in enumerate(v.split("\n")):
        pre = "\n" if k else ""
        m = LBL.match(line)
        ok = m and not line.startswith("http") and "—" not in m.group(2)
        if ok and m.group(1) and len(m.group(2)) > MAX_DASH_LABEL:
            ok = False
        if ok:
            hit = True
            lab = (m.group(1) or "") + m.group(2) + ":"
            parts.append(TextBlock(InlineFont(rFont=F, sz=10, b=True), pre + lab))
            if line[len(lab):]:
                parts.append(TextBlock(InlineFont(rFont=F, sz=10), line[len(lab):]))
        else:
            parts.append(TextBlock(InlineFont(rFont=F, sz=10), pre + line))
    return CellRichText(parts) if hit else v


def est_height(values, widths):
    lines = 1
    for v, w in zip(values, widths):
        if not v:
            continue
        n = sum(max(1, -(-len(p) // max(1, int(w * 1.2)))) for p in str(v).split("\n"))
        lines = max(lines, n)
    return min(409, 13.5 * lines + 6)


def set_widths(ws, ws_list):
    for i, w in enumerate(ws_list, 1):
        ws.column_dimensions[get_column_letter(i)].width = w


def title(ws, text, sub, ncols):
    ws.merge_cells(start_row=1, start_column=1, end_row=1, end_column=ncols)
    c = ws.cell(1, 1, text)
    c.font = Font(name=F, size=16, bold=True, color="FFFFFF")
    c.fill = fill(DARK)
    c.alignment = Alignment(vertical="center", indent=1)
    ws.row_dimensions[1].height = 34
    if sub:
        ws.merge_cells(start_row=2, start_column=1, end_row=2, end_column=ncols)
        c = ws.cell(2, 1, sub)
        c.font = Font(name=F, size=10, italic=True, color="44546A")
        c.alignment = WRAP
        ws.row_dimensions[2].height = 30


def header(ws, row, values):
    for i, v in enumerate(values, 1):
        c = ws.cell(row, i, v)
        c.font = Font(name=F, bold=True, color="FFFFFF", size=11)
        c.fill = fill(HEAD)
        c.alignment = CENTER
        c.border = BORDER
    ws.row_dimensions[row].height = 26


def body(ws, row, values, label_cols=1, label_fill=LIGHT):
    for i, v in enumerate(values, 1):
        c = ws.cell(row, i)
        c.border = BORDER
        c.alignment = WRAP
        if i <= label_cols:
            c.value = v
            c.font = Font(name=F, bold=True, size=10)
            c.fill = fill(label_fill)
        elif isinstance(v, str) and v.startswith("https://"):
            c.value = "Mở trên Store ↗"
            c.hyperlink = v
            c.font = Font(name=F, size=10, bold=True, color="0563C1", underline="single")
        else:
            c.value = rich(v)
            c.font = Font(name=F, size=10)


def validate(d):
    errs = []
    for key in ["title", "apps", "persona", "ui", "ux", "swot", "matrix", "pricing", "proposal", "glossary"]:
        if key not in d:
            errs.append(f"Thiếu khoá '{key}'")
    if errs:
        return errs
    n = len(d["apps"])
    if not 2 <= n <= 6:
        errs.append(f"Số app phải từ 2–6 (hiện {n})")
    for i, a in enumerate(d["apps"]):
        for k in ["name", "developer", "rating", "store_url"]:
            if not a.get(k):
                errs.append(f"apps[{i}] thiếu '{k}'")
    for sec in ["persona", "ui", "ux", "pricing"]:
        for r in d[sec]:
            if len(r.get("values", [])) != n:
                errs.append(f"{sec} › '{r.get('criterion')}' có {len(r.get('values', []))} giá trị, cần {n}")
    for q in d["swot"]:
        if q.get("quadrant") not in QUAD_FILL:
            errs.append(f"swot quadrant không hợp lệ: {q.get('quadrant')} (dùng {list(QUAD_FILL)})")
        for dim in q.get("dims", []):
            if len(dim.get("values", [])) != n:
                errs.append(f"swot › {q.get('quadrant')} › '{dim.get('dimension')}' cần {n} giá trị")
    if len(d["matrix"]) != 4:
        errs.append("matrix cần đúng 4 góc SO / WO / ST / WT")
    return errs


def criteria_sheet(wb, name, ttl, sub, rows, apps, first="Tiêu chí", extra_top=None, w0=24):
    n = len(apps)
    w = max(34, min(52, 190 // n))
    ws = wb.create_sheet(name)
    set_widths(ws, [w0] + [w] * n)
    title(ws, ttl, sub, n + 1)
    header(ws, 4, [first] + [a["name"] for a in apps])
    r = 5
    for lab, vals in (extra_top or []) + [(x["criterion"], x["values"]) for x in rows]:
        v = [lab] + vals
        body(ws, r, v)
        if lab == "Home Screen":
            ws.row_dimensions[r].height = 120
            for col in range(2, n + 2):
                ws.cell(r, col).alignment = CENTER
                ws.cell(r, col).font = Font(name=F, size=9, italic=True, color="8497B0")
        else:
            ws.row_dimensions[r].height = est_height(v, [w0] + [w] * n)
        r += 1
    ws.freeze_panes = "B5"
    return ws


def build(d, out):
    apps = d["apps"]
    n = len(apps)
    date = d.get("analysis_date", "")
    sheets = [(s, desc or f"{d['proposal']['name']} — concept app mới tổng hợp điểm mạnh {n} sản phẩm") for s, desc in SHEETS]
    wb = Workbook()

    # Overview
    ws = wb.active
    ws.title = sheets[0][0]
    w = max(30, min(42, 170 // n))
    set_widths(ws, [26] + [w] * n)
    title(ws, d["title"], d.get("subtitle"), n + 1)
    r = 4
    ws.cell(r, 1, f"{n} ứng dụng được phân tích").font = Font(name=F, bold=True, size=12)
    r += 1
    header(ws, r, ["Tiêu chí"] + [a["name"] for a in apps])
    r += 1
    for lab, key in [("Nhà phát triển", "developer"), ("Đánh giá & xếp hạng", "rating"), ("Link Store", "store_url")]:
        vals = [lab] + [a[key] for a in apps]
        body(ws, r, vals)
        ws.row_dimensions[r].height = est_height(vals, [26] + [w] * n)
        r += 1
    r += 1
    ws.cell(r, 1, "Danh sách sheet trong workbook").font = Font(name=F, bold=True, size=12)
    r += 1
    header(ws, r, ["Sheet", "Nội dung"])
    ws.merge_cells(start_row=r, start_column=2, end_row=r, end_column=n + 1)
    r += 1
    for name, desc in sheets:
        c = ws.cell(r, 1, name)
        c.hyperlink = f"#'{name}'!A1"
        c.font = Font(name=F, bold=True, size=10, color="0563C1", underline="single")
        c.fill = fill(LIGHT)
        c.border = BORDER
        ws.merge_cells(start_row=r, start_column=2, end_row=r, end_column=n + 1)
        dc = ws.cell(r, 2, desc)
        dc.font = Font(name=F, size=10)
        dc.border = BORDER
        dc.alignment = WRAP
        r += 1
    if d.get("sources_note"):
        r += 1
        ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=n + 1)
        c = ws.cell(r, 1, "⚠️ " + d["sources_note"])
        c.font = Font(name=F, size=9, italic=True, color="7F6000")
        c.fill = fill("FFF4CC")
        c.alignment = WRAP
        ws.row_dimensions[r].height = 80

    criteria_sheet(wb, sheets[1][0], "Chân dung người dùng — Hồ sơ mục tiêu & Pain Point", None, d["persona"], apps,
                   extra_top=[("App icon + Link store", [a["store_url"] for a in apps])])
    criteria_sheet(wb, sheets[2][0], "Phân tích UI — Phong cách, màu sắc, typography, layout",
                   d.get("ui_note", "Nhận định UI dựa trên screenshot Store & trải nghiệm công khai — nên xác minh trên thiết bị và chèn screenshot Home vào hàng đầu."),
                   d["ui"], apps, first="Tiêu chí UI", extra_top=[("Home Screen", ["(Chèn screenshot Home)"] * n)])
    criteria_sheet(wb, sheets[3][0], "UX & Tính năng — Chức năng, vấn đề giải quyết, tích hợp AI", None, d["ux"], apps,
                   first="Tiêu chí UX")

    # SWOT
    ws = wb.create_sheet(sheets[4][0])
    sw = max(32, min(42, 170 // n))
    widths = [16, 22] + [sw] * n
    set_widths(ws, widths)
    title(ws, f"Phân tích SWOT — 4 chiều × {n} sản phẩm", None, n + 2)
    header(ws, 4, ["Góc phần tư", "Chiều phân tích"] + [a["name"] for a in apps])
    r = 5
    for q in d["swot"]:
        start = r
        for dim in q["dims"]:
            v = [q["quadrant"] if r == start else None, dim["dimension"]] + dim["values"]
            for i, val in enumerate(v, 1):
                c = ws.cell(r, i)
                c.border = BORDER
                c.alignment = WRAP
                if i <= 2:
                    c.value = val
                    c.font = Font(name=F, bold=True, size=10)
                    c.fill = fill(QUAD_FILL[q["quadrant"]])
                else:
                    c.value = rich(val)
                    c.font = Font(name=F, size=10)
            ws.row_dimensions[r].height = est_height(v, widths)
            r += 1
        ws.merge_cells(start_row=start, start_column=1, end_row=r - 1, end_column=1)
        ws.cell(start, 1).alignment = CENTER
    ws.freeze_panes = "C5"

    # Strategy matrix
    ws = wb.create_sheet(sheets[5][0])
    set_widths(ws, [22, 38, 90])
    title(ws, "Ma trận chiến lược SWOT — Hướng đi SO / WO / ST / WT", None, 3)
    header(ws, 4, ["Góc phần tư", "Hướng chiến lược", "Cơ sở lập luận & nguồn gốc"])
    r = 5
    for k, q in enumerate(d["matrix"]):
        start = r
        for it in q["items"]:
            v = [q["quadrant"] if r == start else None, it["strategy"], it["rationale"]]
            for i, val in enumerate(v, 1):
                c = ws.cell(r, i, val)
                c.border = BORDER
                c.alignment = WRAP
                c.font = Font(name=F, size=10, bold=(i <= 2))
                if i == 1:
                    c.fill = fill(MATRIX_FILL[k % 4])
            ws.row_dimensions[r].height = est_height(v, [22, 38, 90])
            r += 1
        ws.merge_cells(start_row=start, start_column=1, end_row=r - 1, end_column=1)
        ws.cell(start, 1).alignment = CENTER

    criteria_sheet(wb, sheets[6][0], "Mô hình giá — Bảng giá, cơ chế chuyển đổi, chiến lược giữ chân",
                   d.get("pricing_note", f"Giá niêm yết trên Store tại {date}, thay đổi theo khu vực, khuyến mãi và A/B test."),
                   d["pricing"], apps)

    # Proposal
    p = d["proposal"]
    ws = wb.create_sheet(sheets[7][0])
    set_widths(ws, [30, 110])
    title(ws, f"Đề xuất sản phẩm — {p['name']}", p.get("subtitle"), 2)
    header(ws, 4, ["Hạng mục", "Đề xuất"])
    r = 5
    for it in p["items"]:
        v = [it["item"], it["value"]]
        body(ws, r, v)
        ws.row_dimensions[r].height = est_height(v, [30, 110])
        r += 1

    # Glossary
    ws = wb.create_sheet(sheets[8][0])
    set_widths(ws, [32, 16, 60, 50])
    title(ws, "Bảng thuật ngữ — Giải thích các thuật ngữ chuyên ngành",
          d.get("glossary_subtitle", "UI/UX Design · Chiến lược sản phẩm · Thuật ngữ giữ nguyên tiếng Anh"), 4)
    header(ws, 4, ["Thuật ngữ", "Loại", "Giải thích", "Ví dụ trong ngữ cảnh"])
    r = 5
    for g in d["glossary"]:
        v = [g["term"], g["type"], g["definition"], g["example"]]
        body(ws, r, v)
        ws.row_dimensions[r].height = est_height(v, [32, 16, 60, 50])
        r += 1
    ws.freeze_panes = "A5"

    home = sheets[0][0]
    for s in wb.worksheets:
        s.sheet_view.showGridLines = False
        s.page_setup.orientation = "landscape"
        s.page_setup.paperSize = s.PAPERSIZE_A4
        s.page_setup.fitToWidth = 1
        s.page_setup.fitToHeight = 0
        s.sheet_properties.pageSetUpPr.fitToPage = True
        if s.title != home:
            s.print_title_rows = "4:4"
            c = s.cell(3, 1, "← Về Tổng quan")
            c.hyperlink = f"#'{home}'!A1"
            c.font = Font(name=F, size=9, color="0563C1", underline="single")
    wb.save(out)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    data = json.load(open(sys.argv[1], encoding="utf-8"))
    problems = validate(data)
    if problems:
        print("Nội dung JSON chưa hợp lệ:")
        for p in problems:
            print(" -", p)
        sys.exit(1)
    build(data, sys.argv[2])
    print("saved", sys.argv[2])
