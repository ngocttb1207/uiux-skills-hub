---
name: app-competitor-analysis
description: Tạo bản Competitor Analysis ứng dụng mobile dưới góc nhìn UI/UX Designer thành file Excel 9 sheet (Tổng quan, Chân dung người dùng, Phân tích UI, UX & Tính năng, SWOT, Ma trận chiến lược SO/WO/ST/WT, Mô hình giá, Đề xuất sản phẩm, Bảng thuật ngữ). Dùng skill này bất cứ khi nào người dùng muốn phân tích, so sánh, đánh giá đối thủ hay benchmark các app trên App Store / Google Play — kể cả khi chỉ gửi link app rồi hỏi "phân tích đối thủ", "so sánh các app tương tự", "làm competitor analysis", "phân tích UI/UX app X", hoặc nhắc tới file/format competitor analysis UXUI. Also use for English requests like "competitor analysis of these apps", "benchmark app X against competitors".
---

# App Competitor Analysis (UI/UX)

Skill này tạo ra một workbook Excel phân tích cạnh tranh theo format cố định mà team UI/UX dùng: mỗi app là một cột, mỗi tiêu chí là một hàng, kèm SWOT, ma trận chiến lược và đề xuất concept sản phẩm mới. Nội dung viết bằng tiếng Việt (giữ nguyên thuật ngữ tiếng Anh chuyên ngành), trừ khi người dùng yêu cầu ngôn ngữ khác.

Nội dung do bạn nghiên cứu và viết; phần dựng file, định dạng, in đậm nhãn, link, thiết lập in do `scripts/build_workbook.py` làm. Tách như vậy để mọi bản phân tích có giao diện giống hệt nhau và bạn dồn sức vào chất lượng phân tích.

## Quy trình

### 1. Xác định phạm vi

Cần biết: app chính (thường người dùng gửi link store), 2–5 đối thủ, thị trường mục tiêu cho phần đề xuất (nếu có).

- Người dùng đã gửi link/tên app → dùng luôn, không hỏi lại.
- Chưa có đối thủ → tự tìm (xem bước 2), chọn 3 đối thủ trực tiếp nhất về định dạng sản phẩm và giải thích ngắn gọn lý do chọn trong câu trả lời cuối. Không dừng lại để hỏi trừ khi lĩnh vực thật sự mơ hồ.
- Tổng số app trong bảng: 2–6 (khuyến nghị 4).
- Nếu người dùng gửi file mẫu riêng có tiêu chí khác, đọc file đó và bám theo tiêu chí của họ; dùng `references/criteria.md` cho những phần trùng.

### 2. Thu thập dữ liệu

Với **mỗi** app, `web_fetch` trang App Store (và Google Play nếu là app Android-first). Từ trang store lấy:

- Tên, nhà phát triển, rating, số lượt đánh giá, thứ hạng danh mục, Editors' Choice.
- Mô tả tính năng, các gói trong mục **In-App Purchases** (giá thật), ngôn ngữ, phiên bản OS tối thiểu, dung lượng, nền tảng (Watch, Mac…).
- Mục Accessibility (xác nhận Dark Interface, VoiceOver…).
- Review nổi bật (khen & chê) và phản hồi của nhà phát triển — nguồn chính cho pain point "do app gây ra".
- Version history — cho biết hướng đi gần đây.
- Mục "You Might Also Like" — gợi ý đối thủ.

Bổ sung bằng `web_search`: bài review, so sánh "X vs Y", "X alternatives", số người dùng, doanh thu ước tính. Lưu ý nhiều bài so sánh do chính đối thủ viết (blog của Headway, Nibble, BeFreed…) nên có thể thiên vị — dùng làm gợi ý, ưu tiên số liệu từ store. Nếu người dùng có connector Sensor Tower, có thể đề xuất dùng để lấy lượt tải/doanh thu.

### 3. Viết nội dung JSON

Đọc `references/criteria.md` (checklist từng tiêu chí và cách viết) và `references/json_schema.md` (cấu trúc file). Xem `assets/example_deepstash.json` làm mẫu về độ sâu và giọng văn.

Những nguyên tắc rút ra từ các lần làm trước:

- **So sánh tuyệt đối phải đúng với cả bảng.** Trước khi viết "cao nhất", "duy nhất", "lớn nhất", đối chiếu với mọi app trong bảng. Lần đầu làm mẫu Deepstash đã ghi nhầm Imprint "giá cao nhất nhóm" trong khi Blinkist Pro đắt hơn — lỗi này lặp ở 3 sheet.
- **Phân biệt dữ liệu chắc chắn và suy luận.** UI (mã màu, tên tab, layout) thường không xác minh được khi không mở app thật → ghi "(cần xác minh)", không bịa mã hex. Giá, rating, tính năng lấy từ store là dữ liệu chắc chắn.
- **Mỗi nhận định có "so what"** cho designer: vì sao tốt/kém, tác động tới người dùng, học được gì.
- **Nhất quán chéo giữa các sheet:** điểm yếu ở UX phải xuất hiện lại ở SWOT; ma trận chiến lược dẫn ngược về SWOT; đề xuất sản phẩm dẫn ngược về ma trận.
- Ghi nguồn & ngày truy cập trong `sources_note`.

Ghi JSON vào `/home/claude/<ten-app>_analysis.json`. File dài nên viết bằng Python (`json.dump(..., ensure_ascii=False)`) hoặc chia nhiều lần ghi nếu cần.

### 4. Dựng file Excel

```bash
python /path/to/skill/scripts/build_workbook.py /home/claude/<ten-app>_analysis.json "/mnt/user-data/outputs/[UXUI] Competitor Analysis <Tên app>.xlsx"
```

Script kiểm tra dữ liệu trước (thiếu khoá, sai số lượng giá trị so với số app, SWOT/ma trận sai cấu trúc) và in danh sách lỗi — sửa JSON rồi chạy lại.

### 5. Tự review trước khi giao

Render ra ảnh để soát trình bày:

```bash
cd /home/claude && cp "<file>.xlsx" qa.xlsx && soffice --headless --convert-to pdf qa.xlsx >/dev/null 2>&1 && pdftoppm -r 80 -png qa.pdf qa
```

Xem vài trang (Tổng quan, UI, SWOT). Soát nội dung theo checklist:

- [ ] Mọi từ so sánh tuyệt đối đã đối chiếu với tất cả app.
- [ ] Giá khớp mục In-App Purchases.
- [ ] Nhận định UI chưa chắc đều có "(cần xác minh)".
- [ ] Không có ô trống ngoài hàng Home Screen.
- [ ] Nhãn in đậm đúng chỗ — câu thường không bị in đậm nhầm (đổi `:` trong câu thành `—`).

### 6. Giao file

Gọi `present_files` với file xlsx. Trả lời ngắn gọn bằng văn xuôi: các app đã phân tích (và lý do chọn nếu bạn tự chọn), phần nào là dữ liệu chắc chắn và phần nào cần xác minh, hàng Home Screen để trống cho screenshot. Có thể đề nghị tải lên Google Drive nếu người dùng có connector Drive.

## Tài nguyên

- `scripts/build_workbook.py` — dựng workbook từ JSON (2–6 app), validate dữ liệu.
- `references/criteria.md` — checklist tiêu chí & cách viết từng sheet. Đọc trước khi viết nội dung.
- `references/json_schema.md` — cấu trúc JSON đầu vào.
- `assets/example_deepstash.json` — bản phân tích mẫu hoàn chỉnh (Deepstash, Headway, Imprint, Blinkist).
