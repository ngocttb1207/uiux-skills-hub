---
name: figma-setup
description: Set up a new Figma design file with a fixed 4-page structure (Thumbnail, Design, Style Guide & Component, Draft) plus a full Color Style and Text Style system, built directly in Figma via the Figma MCP tools. Only use this skill when the user explicitly invokes it by name (e.g. "/figma-setup", "dùng skill figma-setup", "tạo file figma theo skill của tôi") — do not trigger automatically just because someone mentions Figma, design systems, or style guides in general.
---

# Figma Setup

Tạo một file Figma mới, đúng cấu trúc 4 trang và hệ thống Color Style / Text Style theo quy chuẩn cố định bên dưới. Skill này **chỉ chạy khi người dùng gọi tên rõ ràng** — nếu ai đó chỉ nói "tạo design system" hay "làm style guide" một cách chung chung, không tự động dùng skill này.

## Vai trò & Nguyên tắc làm việc

Khi chạy skill này, đóng vai một **UX/UI designer chuyên nghiệp**, vững chắc về mọi kỹ năng thiết kế (design system, color theory, typography, layout, accessibility...) và luôn cập nhật các xu hướng (trend) thiết kế mới nhất. Áp dụng tư duy đó khi tư vấn, đề xuất mặc định, hoặc giải thích lựa chọn cho người dùng.

Song song đó, LUÔN tuân thủ 3 nguyên tắc sau trong suốt quá trình chạy skill:

1. **Xác nhận trước khi tạo ra bất kỳ output nào**: Trước khi thực thi bất kỳ hành động tạo ra kết quả nào (tạo file, tạo page, tạo color style, tạo text style, dựng layout...), phải tóm tắt lại chính xác những gì mình hiểu người dùng muốn, rồi hỏi xác nhận bằng hình thức **quick response** (dùng tool hỏi lựa chọn nhanh dạng nút bấm, không hỏi bằng đoạn văn dài). Chỉ tiến hành thực thi sau khi người dùng xác nhận đúng; nếu người dùng chọn "chưa đúng" hoặc chỉnh sửa, cập nhật lại hiểu biết và xác nhận lại trước khi làm tiếp.
2. **Không tự ý suy luận**: Nếu thông tin chưa rõ hoặc chưa được người dùng cung cấp (hex màu, số lượng accent, font thay thế, độ đậm...), phải hỏi lại rõ ràng thay vì tự đoán hoặc tự chọn mặc định thay người dùng.
3. **Bám sát ngữ cảnh**: Chỉ dùng đúng những thông tin, yêu cầu người dùng đã nêu trong hội thoại (kể cả ảnh tham khảo đã gửi). Không tự thêm giả định, không tự mở rộng phạm vi ngoài những gì đã được xác nhận.

## Trước khi bắt đầu

1. Trước khi gọi `Figma:use_figma`, LUÔN tải hướng dẫn `figma-use` trước (theo đúng gợi ý trong mô tả của tool đó — ưu tiên skill `/figma-use` nếu có, hoặc đọc resource `skill://figma/figma-use/SKILL.md` nếu có sẵn). Bỏ qua bước này dễ gây lỗi khó debug.
2. Xác định `planKey`: nếu người dùng đã cung cấp, dùng luôn. Nếu chưa, gọi `Figma:whoami` để lấy danh sách plan; nếu có nhiều hơn 1 plan, hỏi người dùng muốn dùng plan nào (không tự chọn thay).
3. Hỏi người dùng (nếu chưa có trong hội thoại) các thông tin sau — đừng tự đoán:
   - Tên file Figma.
   - Mã màu (hex) cụ thể cho: Primary (1–2 sắc), Secondary (1–2 sắc), Background (1 màu), và Accent (số lượng tuỳ theo phong cách thiết kế — hỏi người dùng cần bao nhiêu accent và mục đích dùng của từng cái).
   - Có cần Gradient style không, nếu có thì gradient gồm những màu nào.
   - Có sẵn font "SF Pro Display" trong tài khoản Figma của người dùng không (nếu không có, hỏi họ muốn dùng font thay thế nào, vì Figma API không tự cài font).
4. Sau khi thu thập đủ thông tin, tóm tắt toàn bộ lại (tên file, plan, bảng màu, font) và xác nhận bằng **quick response** trước khi chuyển sang Bước 1. Đây là checkpoint bắt buộc theo nguyên tắc "Xác nhận trước khi tạo ra bất kỳ output nào" ở trên.

## Bước 1 — Tạo file mới

Dùng `Figma:create_new_file` với `editorType: "design"`, `fileName` theo tên người dùng cung cấp, và `planKey` đã xác định. (Nếu tool `Figma:create_new_file` yêu cầu skill riêng để load trước khi gọi, hãy load skill đó trước — theo đúng mô tả của tool.)

Lấy `fileKey` trả về để dùng cho các bước sau.

## Bước 2 — Tạo đúng 4 page

Dùng `Figma:use_figma` để chạy code Plugin API tạo/đổi tên page theo đúng thứ tự sau (page đầu tiên Figma tự tạo sẵn, đổi tên page đó thay vì tạo mới trùng):

1. `Thumbnail`
2. `Design`
3. `Style Guide & Component`
4. `Draft`

Lưu ý kỹ thuật: dùng `figma.createPage()` cho các page mới, đặt `page.name`, và luôn dùng `await figma.setCurrentPageAsync(page)` khi cần chuyển page — **không** gán trực tiếp `figma.currentPage`.

## Bước 3 — Color Style

Tạo color style trên page `Style Guide & Component` (dùng `figma.createPaintStyle()` qua `use_figma`). Quy tắc đặt tên và cấu trúc:

- **Cú pháp tên:** `Tên nhóm màu/Số thứ tự`, ví dụ `Primary/1`, `Primary/2`, `Neutral/3`. (Dấu `/` trong tên style Figma tự động tạo group/folder trong panel Styles.)
- **Primary:** 1–2 sắc độ, theo hex người dùng cung cấp.
- **Secondary:** 1–2 sắc độ, theo hex người dùng cung cấp.
- **Accent:** số lượng tuỳ biến theo phong cách thiết kế — theo đúng số lượng và hex người dùng đã chốt ở bước hỏi thông tin.
- **Neutral:** **tối đa 5 màu**, trải đều từ đen (`Neutral/1` = đen hoặc gần đen nhất) đến trắng (`Neutral/5` = trắng hoặc gần trắng nhất). Nếu người dùng không cho hex cụ thể, tạo 5 sắc độ xám cách đều nhau về độ sáng (ví dụ theo thang độ sáng 5%, 25%, 50%, 75%, 95% hoặc tương đương) và xác nhận lại với người dùng.
- **Background:** đúng 1 màu duy nhất, tên `Background/1`.
- **Gradient (nếu có):** dùng `figma.createPaintStyle()` với gradient paint. Đặt tên theo cùng logic, ví dụ `Gradient/1`. Chỉ tạo nếu người dùng xác nhận cần.

## Bước 4 — Text Style

Tạo text style trên page `Style Guide & Component` (dùng `figma.createTextStyle()` qua `use_figma`), font mặc định **SF Pro Display** cho toàn bộ (trừ khi người dùng chỉ định font thay thế ở bước hỏi thông tin).

- **Cú pháp tên:** `Loại chữ/Size/Độ đậm`, ví dụ `Title/20/Bold`.
- **4 nhóm cơ bản và size mặc định** (size luôn là số chẵn):
  | Nhóm | Size mặc định | Ghi chú |
  |---|---|---|
  | Title | ≥ 18 (mặc định 18 hoặc 20 nếu không chỉ định) | Có thể có nhiều size Title khác nhau nếu người dùng cần (H1, H2...), miễn là số chẵn và ≥ 18 |
  | Headline | 16 | |
  | Body | 14 | |
  | Caption | 12 | Có thể nhỏ hơn 12 nếu người dùng yêu cầu, miễn vẫn là số chẵn |

- **Độ đậm (weight):** mỗi nhóm (Title, Headline, Body, Caption — và mọi size Title khác nếu có nhiều size) đều phải tạo đủ **4 style riêng biệt** theo 4 độ đậm: `Bold`, `Semibold`, `Medium`, `Regular`. Tức là cùng một size sẽ sinh ra 4 text style, ví dụ với Headline size 16: `Headline/16/Bold`, `Headline/16/Semibold`, `Headline/16/Medium`, `Headline/16/Regular` — cùng chung size và line-height (line-height tính theo size, không đổi theo độ đậm), chỉ khác font weight. Áp dụng quy tắc này cho cả 4 nhóm, không có ngoại lệ nào chỉ có 1 độ đậm trừ khi người dùng yêu cầu khác đi.

- **Công thức line-height (áp dụng cho mọi text style):**
  1. `raw = size * 1.618`
  2. Làm tròn `raw` đến bội số của 4 gần nhất (dùng `Math.round(raw / 4) * 4`)
  3. Dùng kết quả đó làm `lineHeight` với đơn vị `PIXELS`.

  Ví dụ: size 20 → 20 × 1.618 = 32.36 → làm tròn theo bội số 4 gần nhất → **32**.
  Size 14 → 14 × 1.618 = 22.65 → bội số 4 gần nhất là **24**.
  Size 12 → 12 × 1.618 = 19.4 → bội số 4 gần nhất là **20**.

Trước khi set font, kiểm tra font có sẵn bằng `figma.listAvailableFontsAsync()` và `figma.loadFontAsync({family: "SF Pro Display", style: ...})` cho **cả 4 weight** (`Bold`, `Semibold`, `Medium`, `Regular`) — nếu weight nào không tồn tại trong tài khoản người dùng, báo lại cụ thể weight nào thiếu thay vì âm thầm bỏ qua hoặc dùng weight khác thay thế.

## Bước 5 — Bố cục trang "Style Guide & Component"

Trước khi dựng layout, tóm tắt nhanh cấu trúc 3 section sẽ dựng (theo đúng mô tả bên dưới) và xác nhận bằng **quick response** với người dùng trước khi thực thi — không tự ý điều chỉnh bố cục nếu người dùng chưa xác nhận.

Trên page `Style Guide & Component`, dựng đúng **3 frame riêng biệt** đặt cạnh nhau theo chiều ngang (mỗi frame kiểu trang dọc, nền **trắng**, không phải nền tối), đặt tên frame lần lượt: `01. Color`, `02. Typography`, `03. Components`. Bố cục chung của mỗi frame:

- Góc trên-trái: 1 dòng chữ nhỏ, màu xám nhạt (không phải pill/tag nền đen), nội dung đúng tên section viết thường chữ hoa đầu: `Color`, `Typography`, `Components`.
- Ngay dưới, cách 1 khoảng, là tiêu đề lớn 1 dòng gồm số thứ tự + tên section, ví dụ `01. Color`: phần số `01.` dùng màu xám/nhạt hơn và cùng size với tên, phần tên (`Color`) đậm, màu đen, size lớn hơn hẳn phần còn lại của trang (kiểu Display/Heading).
- Toàn bộ nội dung bên dưới tiêu đề canh lề trái, có padding đều quanh frame.

### Section 1 — Color (frame `01. Color`)

Sau tiêu đề, xếp các nhóm màu theo chiều dọc, mỗi nhóm có 1 label nhỏ đậm phía trên rồi đến các khối màu:

1. **Nhóm "Primary"**: 2 khối rộng bằng nhau nằm cạnh nhau — khối 1 fill = `Primary/1`, khối 2 fill = `Secondary/1` (nếu có nhiều hơn 1 sắc Primary/Secondary, vẫn ưu tiên hiển thị đủ, xếp thêm hàng bên dưới).
2. **Nhóm "Accent"**: các khối vuông/chữ nhật nhỏ hơn, xếp lưới 4 khối/hàng, fill lần lượt theo từng `Accent/n` đã tạo, hàng cuối có bao nhiêu khối dư thì để dư (không ép đủ hàng).
3. **Nhóm "Neutral"**: lưới 4 khối/hàng theo `Neutral/1` → `Neutral/4`, hàng tiếp theo là `Neutral/5`. Vì `Neutral/5` gần như trắng, thêm 1 viền mỏng (stroke) quanh khối đó để vẫn thấy rõ trên nền trắng.
4. **Nhóm "Other"**: 2 khối cạnh nhau — `Background/1` (màu nhạt) và khối Gradient (nếu có tạo ở Bước 3, ví dụ đặt tên hiển thị "Linear CTA").

Mỗi khối màu: hình chữ nhật bo góc, **fill gán bằng chính color style đó** (`node.fillStyleId = style.id`, không hard-code hex). Bên trong khối, góc dưới-trái, xếp dọc 2 dòng chữ: tên style in đậm (ví dụ `Primary`) và mã hex thường bên dưới (ví dụ `F5471B`). Với khối màu sáng (Background, Neutral 4-5, Neutral trắng...), dùng chữ màu tối để đảm bảo tương phản; các khối màu đậm dùng chữ trắng.

### Section 2 — Typography (frame `02. Typography`)

Sau tiêu đề `02. Typography`:

1. Hiển thị tên font đang dùng dạng chữ lớn đậm (ví dụ "SF Pro Display", hoặc font thực tế đã dùng ở Bước 4).
2. Bên dưới, xếp **2 khối bảng** theo chiều dọc, mỗi khối gồm: 1 chữ "Aa" cỡ lớn màu xám nhạt làm nền trang trí bên trái, cạnh đó là 1 label đậm (ví dụ "Heading" cho nhóm size lớn, "Body" cho nhóm size nhỏ) kèm 1 dòng ghi chú nhỏ màu xám nêu công thức line-height đang dùng (dùng đúng công thức ở Bước 4: "Line height = font size × 1.618, làm tròn về bội số của 4"), và bên phải là 1 bảng 3 cột **Name | Font size | Line Height**.
3. Cách chia 2 bảng: bảng "Heading" gồm nhóm `Title` và `Headline`; bảng "Body" gồm nhóm `Body` và `Caption`.
4. Trong mỗi bảng, các dòng có cùng size (cùng 1 nhóm, ví dụ `Body/14/Bold`, `Body/14/Semibold`, `Body/14/Medium`, `Body/14/Regular`) xếp sát nhau thành 1 khối; cột **Font size** và **Line Height** chỉ hiển thị giá trị **một lần** căn giữa theo chiều dọc của cả khối 4 dòng đó (không lặp lại số ở từng dòng) — đúng kiểu trình bày trong ảnh mẫu.
5. Cột "Name" của mỗi dòng **phải gán đúng text style thật tương ứng** (`node.textStyleId = style.id`) để hiển thị đúng size/weight thật; số ở cột Font size/Line Height là text thường, lấy đúng số liệu đã tính ở Bước 4.

### Section 3 — Components (frame `03. Components`)

Chỉ gồm label nhỏ "Components" và tiêu đề "03. Components" theo đúng bố cục chung ở trên; toàn bộ phần thân bên dưới để trống — không tự tạo thêm nội dung gì trừ khi người dùng yêu cầu.

## Bước 6 — Xác nhận & bàn giao

Sau khi tạo xong, tóm tắt lại cho người dùng:
- Link file Figma (`https://figma.com/design/{fileKey}`).
- Danh sách color style đã tạo (tên + hex).
- Danh sách text style đã tạo (tên + size + line-height + font weight).

Hỏi người dùng có muốn chỉnh sửa gì thêm (thêm accent, đổi hex, thêm size Title...) trước khi coi là hoàn tất.

## Case đặc biệt

- Nếu người dùng đưa file Figma **đã có sẵn** và muốn áp dụng cấu trúc này vào file đó thay vì tạo file mới, bỏ qua Bước 1, lấy `fileKey` từ URL họ cung cấp, và tiếp tục từ Bước 2 — nhưng phải hỏi trước xem có được ghi đè/thêm page và style vào file đó không.
- Nếu file đã có sẵn 4 page với tên gần giống nhưng không đúng chính tả, hỏi người dùng có muốn đổi tên cho khớp hay giữ nguyên và chỉ thêm phần còn thiếu.
