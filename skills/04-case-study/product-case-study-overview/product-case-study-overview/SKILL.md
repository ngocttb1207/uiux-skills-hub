---
name: product-case-study-overview
description: Viết bài tổng quan một DÒNG sản phẩm app (vd. dòng Calories, dòng Health, dòng Stress) từ link Figma / App Store / Google Play / tài liệu của các app cùng dòng, theo template chuẩn của team gồm I. Overview, II. Yêu cầu về Product (model khai thác IAA/IAP/Hybrid, tính năng core/main, công nghệ, UIUX, màu brand, dữ liệu hiển thị và policy, Onboarding, Paywall), III. Tổng kết. Dùng skill này mỗi khi người dùng gửi nhiều link sản phẩm thuộc cùng một dòng và muốn bài viết, tài liệu, guideline, brief, "bài về dòng…", "tổng hợp dòng app", "yêu cầu thiết kế cho dòng…", kể cả khi họ không nói rõ tên template. Write a product-line overview doc from Figma/store links of sibling apps.
---

# Viết bài tổng quan dòng sản phẩm

Người dùng gửi link của 2+ app thuộc cùng một dòng (thường là link Figma, có thể kèm link App Store / Google Play / tài liệu sản phẩm). Đầu ra là MỘT bài viết theo đúng template trong `references/template.md`, viết bằng ngôn ngữ người dùng đang dùng (mặc định tiếng Việt), để designer/PM mới đọc là nắm được dòng sản phẩm và biết phải thiết kế app tiếp theo trong dòng như thế nào.

Bài viết phải dựa trên những gì thật sự có trong thiết kế/tài liệu, không bịa. Chỗ nào không tìm thấy thông tin thì ghi là câu hỏi mở, đừng đoán.

## Input cần có

- Tên dòng (vd. "Calories", "Health"). Nếu người dùng không nói, suy ra từ các app và ghi rõ là suy ra.
- Danh sách app: tên + link + mô tả ngắn của người dùng (nếu có). Mô tả của người dùng là nguồn ưu tiên cho "sản phẩm này làm gì".

Nếu thiếu link hoặc chỉ có 1 app, hỏi lại một câu ngắn trước khi làm.

## Quy trình

### 1. Tạo tài liệu trước, điền sau

Nếu môi trường có công cụ Claude Docs (hoặc skill `docs`), tạo doc ngay đầu tiên với tiêu đề "Dòng sản phẩm <Tên dòng> — <Bộ sản phẩm>" và các khối chờ cho từng phần I, II (Product), II (Thiết kế/Dữ liệu/Onboarding/Paywall), III; mở doc cho người dùng xem rồi điền từng phần một. Nếu không có, viết file Markdown trong outputs. Không dán cả bài vào chat.

### 2. Thu thập thông tin từ Figma

Với mỗi link Figma `https://www.figma.com/design/<fileKey>/<name>?node-id=<a>-<b>`: fileKey = đoạn sau `/design/`, nodeId = `<a>:<b>`.

1. `get_metadata(fileKey)` không nodeId → danh sách page. Page thường tên `UIUX`; node trong link có thể chỉ là một section nhỏ (vd. "Scan Food"), nên hãy đọc cả page UIUX để thấy toàn bộ tính năng.
2. `get_metadata(fileKey, nodeId=<page hoặc node>)`. Kết quả thường quá lớn và được lưu thành file JSON; chạy script để rút gọn:
   ```bash
   python3 <skill-dir>/scripts/extract_figma_text.py <đường-dẫn-file-json> > /home/claude/<app>.txt
   ```
   Script in ra: danh sách section (= nhóm tính năng: Onboarding, IAP, Home, Scan Food, Settings, Edge case…), tên frame, và các text layer (tên text layer gần như luôn là nội dung chữ thật) xếp theo tần suất. Đọc file này để lấy: tính năng, câu chữ onboarding, benefit paywall, giá gói, disclaimer, công thức, nguồn trích dẫn.
3. Chụp màn hình (`get_screenshot`, `enableBase64Response: true`, `maxDimension` 900–1600) cho 2–3 section quan trọng: Home/Dashboard, IAP/Paywall, Onboarding. Dùng ảnh để nhận màu brand, style, mascot/illustration, layout paywall. Đừng chụp cả page rộng hàng chục nghìn px — ảnh sẽ bị thu nhỏ không đọc được; chụp từng section.

Nếu Figma tool không có hoặc không truy cập được file, nói với người dùng và làm tiếp với các nguồn còn lại.

### 3. Nguồn khác (nếu có)

- Link App Store / Google Play: `web_fetch` để lấy category, mô tả, gói IAP, rating.
- Link tài liệu nội bộ (Notion, Google Docs, developers.begamob.com…): đọc bằng connector tương ứng nếu có.
- Không có link store thì category mặc định suy luận từ chức năng (vd. Health & Fitness) và ghi "suy luận".

### 4. Viết bài theo template

Đọc `references/template.md` và giữ nguyên thứ tự, tên mục. Nguyên tắc viết:

- Mỗi mục mở đầu bằng câu kết luận, sau đó mới chi tiết.
- So sánh giữa các app bằng **bảng**: hàng = app, cột = thuộc tính (tính năng, công nghệ, style, màu, paywall…). Đây là giá trị chính của bài: người đọc thấy điểm chung của dòng và khác biệt từng app.
- **Yêu cầu về tính năng viết bằng gạch đầu dòng, KHÔNG dùng bảng** (bảng 4 cột với nội dung dài rất khó đọc). Mở đầu bằng 1 câu nguyên tắc: main function chọn theo keyword chính, tức keyword app đang đẩy ASO thì tính năng đó nằm ở vị trí nổi bật nhất trên Home và là bước đầu tiên sau Onboarding. Sau đó mỗi app là một gạch đầu dòng in đậm tên app, gồm 3 gạch con theo mẫu:
  ```markdown
  - **iCardiac**
      - Keyword chính: heart rate monitor, blood pressure, cardio
      - Core / Main function: đo bằng camera (nhịp tim, huyết áp) + log huyết áp
      - Tính năng phụ: lịch sử, Trends, nhắc đo, export
  ```
- **Yếu tố visual, illustration viết dạng nguyên tắc chung cho cả dòng**, áp dụng được cho app mới; không tả chi tiết từng app (không "app A có hải ly, app B có cục rêu"). Mỗi gạch đầu dòng = một nguyên tắc + lý do với user. Ví dụ:
  - Mỗi app nên có một mascot xuất hiện từ Onboarding đến bên trong app (Home, empty state, thông báo, paywall) để user luôn có cảm giác có người đồng hành, sẵn sàng hỗ trợ; mascot cũng giúp đồng bộ các element hình ảnh trong app.
  - Toàn bộ illustration, icon, ảnh dùng chung một style (cùng nét, cùng bảng màu brand) để app trông nhất quán.
  - Dùng hình ảnh để giải thích số liệu khó hiểu (quy đổi, so sánh trực quan) thay vì thêm chữ.
  - Tránh hình ảnh y khoa gây lo lắng (kim tiêm, máu, cơ thể bệnh); ưu tiên hình ảnh tích cực, gần gũi.
  Ví dụ cụ thể từ các app chỉ được nhắc ngắn trong ngoặc nếu cần, không thành mô tả riêng.
- Main function: chọn theo keyword chính của app trên Store; nêu ví dụ cụ thể "keyword X → tính năng Y nằm ở nút giữa tab bar / card đầu Home".
- Model khai thác: chỉ khẳng định IAA/IAP/Hybrid khi thấy bằng chứng (màn IAP, vị trí ads, banner/native/inter trong tên layer, mô tả store). Nếu chỉ thấy IAP thì ghi vậy và nêu rõ câu hỏi mở về IAA.
- Màu brand: đọc từ ảnh chụp, gắn với keyword/cảm xúc của app (healthy → xanh lá, y tế nhẹ nhàng → tím/xanh dương nhạt, calm → xanh rêu pastel…).
- Dữ liệu hiển thị: liệt kê công thức tìm thấy trong thiết kế (BMR, TDEE, BMI, MET, half-life…) bằng khối ```latex; liệt kê nguồn trích dẫn có trong thiết kế (CDC, WHO, FDA…).
- Phần policy luôn có: không chẩn đoán, không đe dọa/gây hoang mang, ghi "ước tính", disclaimer dưới dự đoán, nguồn cho số liệu marketing, App Store Guideline 1.4.1 (Medical) và 5.1 (Privacy/HealthKit) khi app đụng tới sức khỏe. Trích nguyên văn các câu disclaimer hay trong thiết kế làm ví dụ.
- Onboarding: danh sách đánh số các bước chung của dòng, rồi một đoạn ghi điểm riêng từng app (nhánh rẽ, quyền cần xin…).
- Paywall: bảng "Thành phần | Yêu cầu | Ví dụ trong thiết kế", có đủ: visual, tiêu đề, benefit, gói giá, trial, social proof, CTA, phần bắt buộc của Apple (close, Restore, Terms, Privacy, điều khoản tự gia hạn), offer khi thoát, soft paywall trong app.
- Tổng kết: một bảng so sánh ngắn + 5–6 nguyên tắc chung cho app mới trong dòng + câu hỏi mở.
- Link mỗi tên app tới link Figma/store người dùng gửi.

### 5. Chèn ảnh màn hình dẫn chứng từ Figma

Bài cần ảnh thật từ Figma để người đọc thấy ngay điều đang nói. Các vị trí nên có ảnh: Main function (màn Home / màn tính năng chính của từng app), Luồng tính năng, Style & màu brand, Visual/mascot, Onboarding, Paywall. Mỗi vị trí 1–3 ảnh, mỗi ảnh có caption "<App> – <tên màn>".

1. Trong lúc thu thập (bước 2), ghi lại nodeId của từng frame/section sẽ dùng làm dẫn chứng (lấy từ metadata). Ưu tiên frame một màn hình (375×812) hoặc section nhỏ; ảnh cả page sẽ bị thu nhỏ không đọc được.
2. Viết xong toàn bộ chữ của bài rồi mới chèn ảnh (việc upload ảnh có thể hiện thẻ xin phép, làm dừng lượt).
3. Với mỗi ảnh: `get_screenshot(fileKey, nodeId, maxDimension 1200)` → tải về bằng `curl -f -L -o /home/claude/shots/<app>-<man>.png "<image_url>"` → upload vào doc (Claude Docs: đọc `guide topic.uploads`: upload asset vào link của doc → tạo blob → chèn `![<App> – <tên màn>](blob/<id>)` ngay sau đoạn liên quan). Nếu viết file Markdown thì lưu ảnh cạnh file và chèn bằng đường dẫn tương đối.
4. Nếu không tải được ảnh (curl lỗi do mạng chặn figma.com, hoặc không có Figma tool), không bỏ trống. Chèn link tới đúng frame ngay dưới đoạn đó: `Dẫn chứng: [<App> – <tên màn>](https://www.figma.com/design/<fileKey>/?node-id=<a>-<b>)` (nodeId đổi `:` thành `-`). Sau đó báo người dùng một câu: ảnh chưa chèn được vì mạng chặn figma.com, nhờ owner tổ chức mở domain này, hoặc chạy skill trong Cowork / Claude Code.

### 6. Bàn giao

Trả lời chat 1–2 câu: link tài liệu + những giả định quan trọng cần người dùng xác nhận (vd. model khai thác, category). Không tóm tắt lại bài.

## Ví dụ

Xem `references/example-calories.md` để biết một bài hoàn chỉnh trông như thế nào (dòng Calories: Better Meal, GLP-1, Moss).
