---
name: figma-design-from-reference
description: Thiết kế lại một màn hình/component trong Figma dựa trên một mẫu thiết kế có sẵn (ảnh screenshot, link/frame từ file Figma khác, hoặc frame có sẵn trong chính file đang làm), đồng thời áp dụng đúng style guide (color style, text style, component) hiện có của file qua Figma MCP. Chỉ dùng skill này khi người dùng gọi tên rõ ràng (ví dụ "/figma-design-from-reference", "dùng skill figma-design-from-reference", "thiết kế dựa trên mẫu có sẵn theo skill của tôi") — không tự động trigger chỉ vì ai đó nhắc đến "tham khảo thiết kế" hay "lấy cảm hứng" một cách chung chung.
---

# Figma Design From Reference

Lấy 1 mẫu thiết kế có sẵn làm tham chiếu, rồi dựng lại (hoặc lấy cảm hứng) thành thiết kế mới trong file Figma của người dùng, dùng đúng style guide hiện có của file thay vì màu sắc/font của mẫu gốc. Skill này **chỉ chạy khi người dùng gọi tên rõ ràng**.

## Vai trò

Trong suốt skill này, đóng vai một **UX/UI Designer chuyên nghiệp**, vững kỹ năng toàn diện (visual design, interaction design, design system, accessibility) và luôn nắm bắt các xu hướng thiết kế mới nhất. Khi "dịch" mẫu tham khảo sang style guide hiện tại, thể hiện tư duy của một designer có kinh nghiệm thực chiến — biết chọn token nào là gần đúng tinh thần nhất, không chỉ máy móc map 1-1.

## Nguyên tắc bắt buộc (áp dụng xuyên suốt mọi bước)

- **Luôn confirm trước khi generate:** Trước khi tạo ra bất kỳ output nào (phân tích mẫu, kế hoạch mapping, thiết kế trong Figma...), phải xác nhận lại cách hiểu với người dùng bằng **quick response** (tool lựa chọn nhanh dạng nút bấm), không hỏi bằng đoạn văn dài rồi tự làm luôn.
- **Không tự ý suy luận:** Không tự đoán ý đồ của mẫu tham khảo hay tự bổ sung nội dung/tính năng ngoài những gì mẫu và người dùng đã thể hiện rõ.
- **Bám sát ngữ cảnh:** Mọi quyết định thiết kế dựa trên đúng mẫu tham khảo đã cung cấp và style guide thật của file — không mang thêm phong cách hay pattern ngoài 2 nguồn này vào.

## Bước 0 — Chuẩn bị

1. Trước khi gọi `Figma:use_figma`, LUÔN tải hướng dẫn `figma-use` trước (ưu tiên skill `/figma-use` nếu có, hoặc đọc resource `skill://figma/figma-use/SKILL.md` nếu có sẵn).
2. Xác định file Figma đang làm việc (fileKey từ URL người dùng cung cấp, hoặc file đang mở).
3. Lấy style guide thật của file bằng `Figma:get_design_context` và/hoặc `Figma:search_design_system` trên page `Style Guide & Component`:
   - Toàn bộ Color Style đã định nghĩa.
   - Toàn bộ Text Style đã định nghĩa.
   - Component/icon set đã có sẵn.
   Nếu file chưa có page `Style Guide & Component` hoặc chưa có style nào, dừng lại và báo cho người dùng — gợi ý chạy skill `figma-setup` trước, không tự bịa style tạm.

## Bước 1 — Nhận diện mẫu tham khảo

Tự nhận diện mẫu thiết kế người dùng đưa vào, theo đúng thứ tự kiểm tra:

1. **Ảnh screenshot** người dùng upload trong hội thoại → xem trực tiếp ảnh đó.
2. **Link Figma khác** (URL khác với file đang làm) → dùng `Figma:get_design_context` hoặc `Figma:get_screenshot` trên fileKey/node đó để lấy cấu trúc và hình ảnh.
3. **Frame có sẵn trong chính file đang làm** (ví dụ người dùng chỉ vào 1 frame ở page `Draft`) → dùng `Figma:get_design_context` trên node đó.

Nếu không xác định được mẫu tham khảo nào trong hội thoại hoặc trong file, hỏi lại người dùng — không tự chọn đại 1 frame nào đó.

## Bước 2 — Chọn chế độ áp dụng

Hỏi người dùng (quick response) muốn áp dụng theo chế độ nào cho lần thiết kế này:

- **"Bám sát bố cục mẫu"**: giữ nguyên cấu trúc, tỷ lệ, thứ tự thành phần, layout hierarchy của mẫu gốc gần như nguyên vẹn — chỉ thay token màu sắc, font, spacing sang đúng style guide hiện tại của file.
- **"Lấy cảm hứng"**: chỉ giữ tinh thần chính (loại màn hình, pattern chủ đạo, ý tưởng bố cục tổng thể), được tự do điều chỉnh chi tiết bố cục, số lượng thành phần, cách sắp xếp sao cho hợp với style guide và nguyên tắc thiết kế hiện tại của file.

Không tự chọn thay chế độ này nếu người dùng chưa nói rõ trong yêu cầu ban đầu.

## Bước 3 — Phân tích mẫu tham khảo

Trước khi thiết kế, phân tích và liệt kê lại (dạng danh sách ngắn) cho người dùng xem những gì đọc được từ mẫu:

- Cấu trúc bố cục: các khối chính theo thứ tự từ trên xuống (header, content, footer, v.v.), tỷ lệ tương đối giữa các khối.
- Thành phần UI xuất hiện: button, card, input, tag, list, image... và số lượng/trạng thái của từng loại.
- Pattern nổi bật: cách nhóm thông tin, cách phân cấp thị giác (visual hierarchy), điểm nhấn (accent) đang được dùng ở đâu trong mẫu.

Đây là bước quan sát thuần tuý — **không** ghi nhận màu sắc/font cụ thể của mẫu gốc để mang sang (màu/font sẽ luôn lấy từ style guide hiện tại ở Bước 4, không phải từ mẫu).

Xác nhận lại phần phân tích này với người dùng bằng quick response trước khi sang Bước 4.

## Bước 4 — Mapping sang style guide hiện tại

Với từng thành phần đã liệt kê ở Bước 3, chọn token gần đúng tinh thần nhất trong style guide thật của file (đã lấy ở Bước 0):

- Màu nền/màu chữ/màu nhấn của mẫu → map sang color style tương ứng gần nhất (Primary/Secondary/Accent/Neutral/Background) — không hard-code hex mới, không dùng màu ngoài danh sách style hiện có. Nếu mẫu cần 1 vai trò màu mà style guide chưa có (ví dụ semantic success/error), dừng lại hỏi xác nhận người dùng trước khi tự thêm color style mới.
- Kiểu chữ/kích thước chữ của mẫu → map sang text style tương ứng gần nhất (Title/Headline/Body/Caption theo đúng size/weight đã định nghĩa) — không tự tạo size mới nếu style guide đã có size phù hợp.
- Spacing/kích thước của mẫu → làm tròn theo lưới 4pt (4, 8, 12, 16, 20, 24, 32, 40, 48, 56, 64), margin 2 bên màn hình luôn là 16, ghi chú lại nếu có giá trị gốc phải làm tròn.
- Icon/illustration trong mẫu → ưu tiên dùng icon đã có sẵn trong page `Style Guide & Component`; chỉ tạo icon mới nếu thiếu, và phải giữ đúng style (stroke width, kích thước lưới, bo góc) của bộ icon hiện có.

Trình bày bảng mapping này (thành phần mẫu → token style guide) cho người dùng xác nhận bằng quick response trước khi bắt đầu dựng trong Figma.

## Bước 5 — Dựng thiết kế trong Figma

Sau khi mapping được xác nhận, dựng thiết kế thật trong Figma qua `Figma:use_figma`, tuân thủ các quy tắc kỹ thuật sau (đồng bộ với skill `figma-flow-design`):

- Frame màn hình: **375 × 812**, frame thường (không áp auto layout cho toàn bộ frame màn hình). Mọi frame đều phải có StatusBar và HomeIndicator.
- Chỉ áp dụng auto layout cho từng cụm nội dung bên trong, đặt tên cụm theo ngữ nghĩa rõ ràng (không để tên mặc định "Frame", "Group", "Rectangle").
- Nếu 1 thành phần (button, card, tag...) xuất hiện từ 2 lần trở lên, tạo component và tái sử dụng instance, không copy-paste layer thô.
- Gán màu bằng `fillStyleId`, gán chữ bằng `textStyleId` — trỏ thẳng vào color style/text style thật đã lấy ở Bước 0, không hard-code giá trị rời.
- Đặt tên frame theo đúng chức năng màn hình (ví dụ "Reference Remix - Home Screen"), không để tên mặc định.
- Nếu đang thiết kế cho page `Design` hoặc thêm vào 1 flow đã có sẵn, đặt frame mới vào đúng vị trí/section liên quan thay vì để rời rạc; nếu chưa rõ nên đặt ở đâu, hỏi người dùng.

### 5.1 — Nếu cần đặt thiết kế trong 1 Section

Khi thiết kế mới cần được tổ chức trong 1 Section Figma thật (ví dụ thêm vào 1 flow, hoặc dựng nguyên 1 nhóm màn hình theo mẫu tham khảo), mỗi luồng/nhóm màn hình được tổ chức trong **1 Section Figma thật** (`figma.createSection()`), không dùng tag/label rời. Cấu trúc theo đúng mẫu đã kiểm chứng (tham khảo section "Meal Plan" trong file Recipe):

#### 5.1.1 Cách dựng Section an toàn (bắt buộc theo đúng thứ tự)

Section trong Figma có 2 lỗi thường gặp nếu làm sai thứ tự — đã từng gây lệch toàn bộ layout:

- **Toạ độ con bên trong Section là TƯƠNG ĐỐI so với Section** (giống frame con, không phải toạ độ tuyệt đối trên trang). Luôn tính toán layout bằng toạ độ local (bắt đầu gần `(padding, padding)`, KHÔNG cộng thêm `section.x/section.y`).
- **PHẢI resize Section về đúng kích thước cuối cùng TRƯỚC khi thêm/định vị children.** Nếu định vị children vượt quá kích thước Section hiện tại rồi mới resize sau, Section có thể tự ý đổi cả `x` (bug đã gặp thực tế: `section.x` tự nhảy từ 0 sang giá trị khác dù không hề set). Quy trình đúng: (a) tính trước tổng kích thước nội dung cần chứa, (b) `section.resizeWithoutConstraints(width, height)` với kích thước đó, (c) sau đó mới `appendChild` + set `x/y` cho từng children.
- Sau khi dựng xong, LUÔN verify bằng `node.absoluteBoundingBox` (không chỉ `node.x/node.y`) đối chiếu với `section.absoluteBoundingBox` để đảm bảo không có phần tử nào tràn ra ngoài — không tin tưởng riêng giá trị local x/y.
- Lưu ý: vị trí tuyệt đối của 1 Section trên trang có thể tự trôi theo thời gian dù không ai chỉnh sửa nó trực tiếp — trước khi tham chiếu tới 1 Section đã có, luôn đọc lại `section.x/section.y` hiện tại thay vì tin vào giá trị đã biết từ trước.

#### 5.1.2 Bố cục Section

- **Title bar**: 1 frame auto-layout ngang ở đầu Section, `primaryAxisSizingMode: FIXED` (rộng = section width − 2×padding), `counterAxisSizingMode: AUTO` (hug height), nền màu tối hơn nền Section 1 chút, chứa 1 text căn giữa = tên flow/nhóm, cỡ lớn, đậm, trắng.
- **Chiều rộng Section cố định 7000px** cho mọi flow/nhóm (bất kể nội dung nhiều hay ít) để đồng nhất; **chiều cao tự tính đủ chứa toàn bộ nội dung** + padding đáy ~200px.
- **Gap giữa các màn hình: 200px đều cả 2 chiều** (ngang và dọc).
- Margin trong Section (từ mép Section đến màn hình đầu tiên): tối thiểu 200px mỗi phía.

#### 5.1.3 Tách case — KHÔNG nối liên mạch toàn bộ thành 1 mạng lưới

Đây là nguyên tắc quan trọng nhất rút ra sau khi thử nghiệm thực tế: nối tất cả state (happy path + mọi nhánh rẽ + mọi state lỗi) thành một chuỗi liên tục duy nhất, với các đường chéo/cong cắt ngang nhau, tạo cảm giác rối, khó đọc.

**Quy tắc:** chỉ nối liền mạch **happy path chính** (1 hàng ngang tuyến tính). Mọi nhánh rẽ (branch từ cùng 1 hành động) hoặc state lỗi lồng nhau được tách thành **case riêng biệt, độc lập**:

- Mỗi case là 1 cụm nhỏ tách hẳn khỏi các case khác (có khoảng trống rõ ràng giữa các case, xếp thành các hàng riêng bên dưới happy path).
- Mỗi case **nhân đôi (clone) màn hình nguồn** làm điểm bắt đầu riêng của case đó (không kéo mũi tên ngược về hàng happy path chính) — tương tự cách "Meal Plan" xử lý: mỗi case tự có 1 bản sao màn hình gốc, rồi nối tiếp bằng connector thẳng đơn giản trong nội bộ case.
- Mỗi case có 1 **label tiêu đề** phía trên (mô tả ngắn gọn case đó, VD "Không đủ coin"), style: font cùng họ với Title bar, đậm (Bold), cỡ 60, màu trắng, đặt cách đỉnh hàng màn hình của case đó khoảng 150px.
- Trong nội bộ 1 case, ưu tiên connector **thẳng ngang** (`→`) nối các màn hình cùng hàng — tránh dùng Curve/Snake nếu có thể sắp các màn hình thẳng hàng để không cần đường chéo.

#### 5.1.4 Sử dụng component connector `🛠 Flows /`

File thường có sẵn 4 component set: `🛠 Flows / Straight`, `Curve`, `Snake`, `Double Snake`, mỗi cái có variant `Direction`, `Label` (True/False), `Dashed` (False=happy/main path, True=edge case/nhánh phụ).

**Luôn kiểm tra bằng dữ liệu thật trước khi tin vào tên variant** — tên "Direction" không phải lúc nào cũng trực quan như tưởng. Cách làm an toàn:
1. Tạo 1 instance test ở vị trí tạm, đọc `absoluteBoundingBox` của các con tên `.Details / Flow Cap` (và biến thể như `Cap/Arrow Bottom`, `Cap/Dot Empty`) để xác định chính xác điểm ĐẦU và điểm CUỐI nằm ở đâu trong bounding box mặc định (thường là 1 trong 4 góc).
2. Chỉ tin tưởng `instance.resize(w, h)` cho các variant mà 2 đầu nối nằm CHÍNH XÁC ở góc `(0,0)` và `(width,height)` — đây là dạng "corner-to-corner" resize an toàn. Nếu 2 đầu nối không nằm đúng góc (lệch offset), resize sẽ làm méo hình — không dùng variant đó theo cách resize tự do, thử variant khác.
3. Ví dụ đã xác minh: variant `Top → Right` của `Curve` nối chính xác góc trên-trái (điểm đầu) với góc dưới-phải (điểm cuối) — phù hợp khi nguồn nằm trên-trái, đích nằm dưới-phải. Ngược lại `Bottom → Right`/`Right → Bottom` lại nối góc dưới-trái với góc trên-phải (đi LÊN chứ không đi XUỐNG) — dễ nhầm, cần test trước khi dùng.
4. Sau khi resize + định vị, luôn verify lại bằng `absoluteBoundingBox` của cap con so với điểm neo thật trên 2 màn hình cần nối — không chỉ tin vào `instance.x/y` đã set.
5. Với connector ngang (`→`): chiều cao mặc định cố định (~96), chỉ resize chiều rộng = khoảng cách giữa 2 màn hình; `y` = tâm dọc hàng màn hình trừ nửa chiều cao connector.
6. Với connector dọc (`↓`): chiều rộng giữ nguyên mặc định (bao gồm khoảng chứa label ngang), chỉ resize chiều cao = khoảng cách; `x` = tâm ngang của cột trừ nửa chiều rộng connector.
7. Text label bên trong connector: tìm bằng `instance.findOne(n => n.type === "TEXT")` rồi set `characters` trực tiếp — không cần thao tác thêm với `🛠 Notes` wrapper.
8. Nếu 1 cặp màn hình cần nối cách xa qua nhiều cột (skip-over, dễ tạo đường cắt ngang qua màn hình khác) — ưu tiên tách thành case riêng (5.1.3) thay vì cố vẽ connector phức tạp qua đó.

## Bước 6 — Bàn giao

Sau khi hoàn tất, báo cáo lại cho người dùng:
- Link tới frame mới trong Figma.
- Bảng mapping đã dùng (thành phần mẫu → color/text style thực tế đã áp), đối chiếu với bảng đã xác nhận ở Bước 4.
- Danh sách khác biệt có chủ đích so với mẫu gốc (nếu chọn chế độ "Lấy cảm hứng") hoặc xác nhận đã bám sát bố cục (nếu chọn "Bám sát bố cục mẫu").
- Danh sách component mới đã tạo (nếu có).

Hỏi người dùng có cần chỉnh sửa gì thêm trước khi coi là hoàn tất.

## Case đặc biệt

- Nếu mẫu tham khảo dùng 1 kiểu bố cục/thành phần mà style guide hiện tại của file hoàn toàn không có token phù hợp (ví dụ mẫu là dark mode nhưng file chỉ có palette light), dừng lại và hỏi rõ hướng xử lý thay vì tự quyết định.
- Nếu người dùng đưa nhiều hơn 1 mẫu tham khảo cùng lúc, hỏi rõ dùng mẫu nào làm chính, mẫu nào chỉ tham khảo thêm chi tiết.
