# Checklist tiêu chí từng sheet

Mỗi ô so sánh nên viết như một UI/UX Designer viết cho team sản phẩm: cụ thể, có bằng chứng, có "so what". Ưu tiên bullet `- ` xuống dòng bằng `\n`. Khi một ô có nhiều phần, mở đầu mỗi phần bằng nhãn kết thúc bằng dấu `:` (script tự in đậm nhãn); trong câu thường dùng `—` thay vì `:`.

Mục lục: 1. Chân dung người dùng · 2. Phân tích UI · 3. UX & Tính năng · 4. SWOT · 5. Ma trận chiến lược · 6. Mô hình giá · 7. Đề xuất sản phẩm · 8. Bảng thuật ngữ

## 1. 👤 Chân dung người dùng (`persona`)

Hàng "App icon + Link store" do script tự thêm từ `apps[].store_url` — không khai báo trong JSON.

| Tiêu chí | Viết gì |
|---|---|
| Đối tượng chính | 2–3 nhóm, mỗi nhóm có độ tuổi + nghề nghiệp/hoàn cảnh + lý do dùng app. Suy ra từ mô tả store, review, kênh quảng cáo. |
| Thu nhập & Tech level | Mức thu nhập ước tính (dựa trên giá & thị trường) + mức thành thạo công nghệ + độ nhạy cảm về giá. |
| Mục tiêu chính | 4–5 job-to-be-done, bắt đầu bằng động từ. |
| Pain points | 4–5 nỗi đau ngoài đời mà app giải quyết. Thêm 1 dòng "(Pain do chính app gây ra)" lấy từ review tiêu cực — đây là insight giá trị nhất cho designer. |
| Hành vi sử dụng | Tần suất, thời điểm, độ dài phiên, luồng thao tác điển hình, free vs. trả phí. |
| Mức độ sẵn sàng trả phí | Mức (Thấp/Trung bình/Cao) + giá thực tế + động lực nâng cấp chính. |

## 2. 🎨 Phân tích UI (`ui`)

Hàng "Home Screen" (ô trống để chèn screenshot) do script tự thêm.

| Tiêu chí | Viết gì |
|---|---|
| Style Graphic, App Style | Hai đoạn: `Graphic Style: <3 từ khoá>` + 2–3 bullet; `App Style: <2 từ khoá>` + 2–3 bullet. |
| Brand Color, Themes | Màu chủ đạo (tên màu, có hex nếu chắc chắn) + vai trò màu (CTA, trạng thái) + Light/Dark mode (xác nhận qua mục Accessibility của App Store nếu có). |
| Typography | Serif/sans-serif, cách phân cấp, mật độ chữ, cỡ chữ. |
| Phong cách icon | Outline/filled/line, đơn sắc hay nhiều màu, mức đồng bộ. |
| Home screen: Layout and Architecture Information | Bốn nhãn bắt buộc: `Bố cục:`, `Thể hiện thông tin:`, `Điều hướng:` (Bottom Nav gồm tab nào, nút nổi), `Phân cấp thông tin:`. |
| Điểm mạnh UI | 3–4 bullet, nêu lý do vì sao tốt. |
| Điểm yếu UI | 3–4 bullet, nêu tác động tới người dùng. |

Không mở được app thật thì ghi rõ "(cần xác minh)" cạnh nhận định về màu, tên tab, dark mode. Không bịa mã màu hex.

## 3. ⚙️ UX & Tính năng (`ux`)

| Tiêu chí | Viết gì |
|---|---|
| Số lượng tính năng | Mức (Ít/Trung bình/Nhiều) + ước lượng số + trọng tâm. |
| Core/main Function | 4 bullet dạng `- Tên tính năng: mô tả`. |
| Extra/Sub Function | 5–7 bullet tính năng phụ. |
| AI Assistant | Tính năng AI + `- Giá trị:` + `- Chất lượng:` (theo review). Không có AI thì nói rõ và nêu cơ hội. |
| Usability | Năm nhãn: `- Khả năng tiếp cận Core:`, `- Quy trình sử dụng:`, `- Tốc độ & chất lượng:`, `- Hướng dẫn & Feedback:`, `- Khả năng mở rộng:`. |
| Khác | Bốn nhãn: `- Điểm nổi bật:`, `- Điểm yếu:`, `- Điểm học hỏi:`, `- Tối ưu đề xuất:`. |
| Chiến lược thông báo | Loại push/widget/email, tần suất, mục đích (nhắc streak, nhắc hết trial…). |

## 4. 📊 SWOT (`swot`)

Đúng 4 góc theo thứ tự `ĐIỂM MẠNH`, `ĐIỂM YẾU`, `CƠ HỘI`, `THÁCH THỨC`. Mỗi góc 3 chiều, mỗi chiều một ô cho mỗi app:

- ĐIỂM MẠNH: Định vị & uy tín · Tính năng · Nền tảng
- ĐIỂM YẾU: Uy tín & social proof · UX & Sản phẩm · Giá & Giữ chân
- CƠ HỘI: Khoảng trắng thị trường · Địa lý · Công nghệ
- THÁCH THỨC: Nền tảng & Cạnh tranh · Uy tín & Pháp lý · Hành vi người dùng

Dùng số liệu cụ thể (rating, số đánh giá, thứ hạng, số ngôn ngữ, phiên bản iOS tối thiểu, dung lượng).

## 5. ♟️ Ma trận chiến lược (`matrix`)

Đúng 4 phần theo thứ tự `SO Điểm mạnh × Cơ hội`, `WO Điểm yếu × Cơ hội`, `ST Điểm mạnh × Thách thức`, `WT Điểm yếu × Thách thức`. Mỗi phần 3–4 hướng. Cột "Cơ sở lập luận" phải dẫn ngược về app cụ thể (App 01, App 02…) và ô SWOT tương ứng.

## 6. 💰 Mô hình giá (`pricing`)

Chín tiêu chí: Gói tuần / tháng · Gói năm · Gói trọn đời · Tầng miễn phí · Cơ chế chuyển đổi · Chiến lược giữ chân · USP bán hàng chính · Rủi ro bán hàng · Kênh thu hút chính.

- Lấy giá từ mục In-App Purchases của App Store: liệt kê khoảng giá khi có nhiều mức.
- "Cơ chế chuyển đổi" viết dạng luồng `A → B → C`.
- Chỉ dùng từ so sánh tuyệt đối ("cao nhất", "duy nhất", "lớn nhất") sau khi đã đối chiếu với **tất cả** app trong bảng.

## 7. 💡 Đề xuất sản phẩm (`proposal`)

Đặt tên concept và viết 13 hạng mục: Tên & định vị · Đối tượng mục tiêu · Value proposition · Tính năng cốt lõi (MVP) · Tính năng khác biệt · Học hỏi từ đối thủ · Định hướng UI · Kiến trúc điều hướng · Onboarding · Paywall & giá · Retention loop · KPI mục tiêu (giả định cần kiểm chứng) · Rủi ro & giảm thiểu.

Concept phải truy ngược được về SO/WO trong ma trận và về pain point trong sheet Chân dung. Nếu người dùng nêu thị trường mục tiêu, bám theo thị trường đó.

## 8. 📖 Bảng thuật ngữ (`glossary`)

25–30 thuật ngữ gồm 4 nhóm: UI/UX chung, thuật ngữ đặc thù ngành của các app đang phân tích, kinh doanh/tăng trưởng, marketing. Cột "Ví dụ" phải gắn với app trong bảng.
