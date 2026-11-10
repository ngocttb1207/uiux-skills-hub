# Cấu trúc file nội dung JSON

`scripts/build_workbook.py` đọc một file JSON (UTF-8) với cấu trúc dưới đây. Ví dụ đầy đủ: `assets/example_deepstash.json`. Với N app (2–6), mọi mảng `values` phải có đúng N phần tử, cùng thứ tự với `apps`.

```json
{
  "title": "Phân tích cạnh tranh ứng dụng <Lĩnh vực> — UI/UX & Chiến lược",
  "subtitle": "Phân tích SWOT · Chân dung người dùng · UI/UX · Chiến lược bán hàng · Đề xuất sản phẩm mới",
  "analysis_date": "dd/mm/yyyy",
  "apps": [
    {"name": "App 01 · <Tên>", "developer": "<Nhà phát triển>",
     "rating": "⭐ 4,7 · ~84 nghìn lượt đánh giá trên iOS (US)\n#6 Education",
     "store_url": "https://apps.apple.com/..."}
  ],
  "sources_note": "Nguồn dữ liệu: ... (hiển thị ở cuối sheet Tổng quan)",
  "ui_note": "(tuỳ chọn) ghi chú dưới tiêu đề sheet UI",
  "pricing_note": "(tuỳ chọn) ghi chú dưới tiêu đề sheet Mô hình giá",
  "glossary_subtitle": "(tuỳ chọn)",

  "persona": [{"criterion": "Đối tượng chính", "values": ["...", "..."]}],
  "ui":      [{"criterion": "Style Graphic, App Style", "values": ["...", "..."]}],
  "ux":      [{"criterion": "Số lượng tính năng", "values": ["...", "..."]}],
  "pricing": [{"criterion": "Gói tuần / tháng", "values": ["...", "..."]}],

  "swot": [
    {"quadrant": "ĐIỂM MẠNH",
     "dims": [{"dimension": "Định vị & uy tín", "values": ["...", "..."]}]}
  ],
  "matrix": [
    {"quadrant": "SO Điểm mạnh × Cơ hội",
     "items": [{"strategy": "...", "rationale": "..."}]}
  ],
  "proposal": {
    "name": "<Tên concept>",
    "subtitle": "Concept app mới tổng hợp điểm mạnh của ...",
    "items": [{"item": "Tên & định vị", "value": "..."}]
  },
  "glossary": [
    {"term": "UI (User Interface)", "type": "Thiết kế", "definition": "...", "example": "..."}
  ]
}
```

Quy ước:

- `quadrant` của SWOT phải là một trong `ĐIỂM MẠNH`, `ĐIỂM YẾU`, `CƠ HỘI`, `THÁCH THỨC` (quyết định màu nền).
- `matrix` cần đúng 4 phần tử theo thứ tự SO, WO, ST, WT.
- Xuống dòng trong ô dùng `\n`. Ô bắt đầu bằng `https://` được hiển thị thành link "Mở trên Store ↗".
- Nhãn đầu dòng kết thúc bằng `:` (ví dụ `Bố cục:`, `- Điểm yếu:`) sẽ được in đậm; trong câu thường dùng `—`.
- Không khai báo hàng "App icon + Link store" và "Home Screen" — script tự thêm.
