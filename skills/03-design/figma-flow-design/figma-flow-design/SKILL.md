---
name: figma-flow-design
description: Thiết kế đầy đủ một luồng UI (bao gồm happy path và toàn bộ edge case) trực tiếp trong Figma qua Figma MCP, tuân thủ nghiêm ngặt hệ lưới 4pt, style guide có sẵn, quy tắc auto layout, đặt tên, component hoá và tổ chức theo flow. Chỉ dùng skill này khi người dùng gọi tên rõ ràng (ví dụ "/figma-flow-design", "dùng skill figma-flow-design", "thiết kế luồng theo skill của tôi") — không tự động trigger chỉ vì ai đó nhắc đến thiết kế UI hay Figma nói chung.
---

# Figma Flow Design

Thiết kế toàn bộ một luồng chức năng (multi-screen flow) trực tiếp trong file Figma của người dùng, đảm bảo không sót trạng thái, bám sát design system có sẵn, và tổ chức file rõ ràng, dễ maintain. Skill này **chỉ chạy khi người dùng gọi tên rõ ràng**.

## Vai trò

Trong suốt skill này, đóng vai một **UX/UI Designer chuyên nghiệp**, vững kỹ năng toàn diện (visual design, interaction design, information architecture, design system, accessibility) và luôn nắm bắt các xu hướng (trend) thiết kế mới nhất. Mọi đề xuất, cách đặt tên, cách tổ chức layout đều phải thể hiện tư duy của một designer có kinh nghiệm thực chiến, không phải một công cụ generate hình ảnh đơn thuần.

## Nguyên tắc bắt buộc (áp dụng xuyên suốt mọi bước)

- **Luôn confirm trước khi generate:** Trước khi tạo ra bất kỳ output nào (danh sách state, thiết kế UI, component, thay đổi trong Figma...), phải xác nhận lại cách hiểu yêu cầu với người dùng trước. Xác nhận dưới dạng **quick response** — dùng tool đưa lựa chọn nhanh (ví dụ `ask_user_input_v0`) với các phương án ngắn gọn để người dùng chọn/xác nhận, thay vì hỏi bằng đoạn văn dài hoặc tự hiểu rồi làm luôn. Chỉ sau khi có xác nhận mới được tiếp tục sang bước generate thực sự.
- **Không tự ý suy luận:** Không tự đoán, không tự bổ sung yêu cầu, tính năng, trạng thái, hay ý nghĩa mà người dùng chưa nói rõ. Nếu có điểm chưa rõ, hỏi lại (dạng quick response) thay vì tự suy diễn rồi thực hiện.
- **Bám sát ngữ cảnh:** Mọi quyết định thiết kế phải dựa trên đúng những gì đã có trong hội thoại, style guide, design context đã lấy từ file Figma. Không mang ý tưởng, pattern, hay phong cách từ bên ngoài ngữ cảnh đã cung cấp vào thiết kế.

## Bước 0 — Chuẩn bị trước khi thiết kế

1. Trước khi gọi `Figma:use_figma`, LUÔN tải hướng dẫn `figma-use` trước (ưu tiên skill `/figma-use` nếu có, hoặc đọc resource `skill://figma/figma-use/SKILL.md` nếu có sẵn). Bỏ qua bước này dễ gây lỗi khó debug.
2. Xác định file Figma đang làm việc (fileKey từ URL người dùng cung cấp, hoặc file đang mở).
3. Lấy design context hiện có trong file bằng `Figma:get_design_context` và/hoặc `Figma:search_design_system` để nắm:
   - Toàn bộ Color Style đã định nghĩa (không được dùng màu ngoài danh sách này).
   - Toàn bộ Text Style đã định nghĩa.
   - Component/icon set đã có sẵn trong file (đặc biệt là page "Style Guide & Component" nếu file dùng cấu trúc theo skill `figma-setup`).
4. Nếu thiếu thông tin (style guide, icon set, hoặc mô tả luồng chức năng cụ thể), hỏi lại người dùng trước khi thiết kế — không tự đoán.

## Bước 1 — Liệt kê toàn bộ trạng thái (state) trước khi vẽ UI

**Không thiết kế ngay.** Trước tiên liệt kê dạng danh sách text toàn bộ state cần có cho luồng, gồm:
- Happy path (các bước chính từ đầu đến cuối luồng).
- Empty state (chưa có dữ liệu).
- Loading state.
- Error state (lỗi mạng, input sai, timeout...).
- Permission denied / cần quyền truy cập.
- Giới hạn dữ liệu (danh sách rỗng, danh sách quá dài, ký tự vượt giới hạn...).
- Trạng thái đặc biệt khác nếu có (offline, session hết hạn, v.v.).

Trình bày danh sách này cho người dùng **review và xác nhận** trước khi bắt đầu tạo bất kỳ frame nào trong Figma — xác nhận dưới dạng quick response (lựa chọn nhanh: "Đúng, tiếp tục" / "Cần chỉnh sửa" / liệt kê state nào cần thêm-bớt), không tự suy luận rồi thiết kế luôn.

## Bước 2 — Quy tắc lưới 4pt (bắt buộc, không ngoại lệ)

- MỌI giá trị spacing (padding, margin, gap) PHẢI chia hết cho 4: 4, 8, 12, 16, 20, 24, 32, 40, 48, 56, 64.
- MỌI kích thước thành phần (chiều cao, chiều rộng, đường kính icon, kích thước button, ô input) PHẢI chia hết cho 4.
- Border-radius PHẢI chia hết cho 4.
- Cấm dùng số không chia hết cho 4 (VD: 5, 6, 10, 15, 18, 22, 25, 30). Nếu một giá trị tham chiếu (từ style guide, từ ảnh mẫu...) không chia hết cho 4, làm tròn đến bội số 4 gần nhất và ghi chú lại rõ ràng giá trị gốc → giá trị đã làm tròn.
- Margin 2 bên màn hình luôn là **16**. Padding bên trong mọi element luôn là **số chẵn** (ưu tiên bội số 4 khi có thể).

**Tự kiểm tra trước khi báo hoàn tất:** rà lại từng con số đã dùng trong thiết kế. Nếu phát hiện giá trị nào không chia hết cho 4, sửa ngay trong Figma trước khi báo cáo kết quả cho người dùng.

## Bước 3 — Bám sát style guide

- Chỉ dùng màu sắc đã có trong Color Style của file. Không tự tạo màu mới.
- Nếu cảm thấy cần một màu không có sẵn (VD: màu semantic cho error/success chưa được định nghĩa), dừng lại và hỏi xác nhận người dùng trước khi tạo thêm, không tự ý thêm màu.
- Text style, spacing, component đều ưu tiên tái sử dụng những gì đã có trong Style Guide & Component page thay vì tạo mới.

## Bước 4 — Kích thước màn hình & bố cục

- Frame màn hình: **375 × 812**, là frame thường (không áp dụng auto layout cho toàn bộ frame màn hình).
- Margin 2 bên: **16**.
- Padding bên trong các element: luôn là số chẵn.

## Bước 5 — Auto layout

- Frame màn hình 375×812: **frame thường**, KHÔNG áp auto layout cho toàn màn hình.
- Chỉ áp dụng auto layout cho các **cụm nội dung bên trong**, gộp phần tử liên quan thành từng cụm có tên ngữ nghĩa rõ ràng, ví dụ:
  - `Header` (top bar + progress).
  - `Title block` (title + subtitle).
  - Cụm chính chứa nội dung/card/option (đặt tên theo ngữ nghĩa cụ thể của màn hình đó, không đặt chung chung).
  - `Footer` (button chính + ghi chú phụ, neo cách đáy 24px).
- Các phần tử nổi (dim overlay, dialog, tooltip, spotlight...) đặt vị trí tự do, nằm ngoài các cụm auto layout.

## Bước 6 — Đặt tên

- Đặt tên từng màn hình (frame) theo đúng chức năng của nó (VD: "Add Recipe - Step 1 Import", "Add Recipe - Empty State"), không để tên mặc định "Frame 1", "Frame 2".
- Đặt tên rõ ràng cho mọi layer/element/nhóm auto layout theo ngữ nghĩa. Tuyệt đối không để tên mặc định như "Frame", "Group", "Rectangle" còn sót lại.

## Bước 7 — Component hoá

- Trong quá trình thiết kế, nếu một thành phần (button, card, tag, input...) được dùng **trên 2 lần**, tạo component cho nó (`figma.createComponent()` qua `use_figma`).
- Sau khi tạo component, **phải sử dụng lại component đó** (tạo instance) cho các lần xuất hiện tiếp theo, không copy-paste layer thô.
- Đặt tên component theo quy ước rõ ràng, có thể theo nhóm (VD: `Button/Primary/Default`, `Card/Recipe/Default`).

## Bước 8 — Icon

- Chỉ dùng icon đã có sẵn trong file (thường ở page Style Guide & Component).
- Nếu thiếu icon cần thiết cho luồng, tạo icon mới nhưng **giữ đúng style** (stroke width, kích thước lưới, bo góc) của bộ icon hiện có trong file — không dùng style icon khác lạ.

## Bước 9 — Tính nhất quán giữa các state

- Cùng một loại lỗi phải dùng chung 1 pattern hiển thị trên toàn bộ luồng.
- Cùng loại empty state dùng chung illustration style.
- Loading state, error state, permission state... nếu lặp lại ở nhiều màn hình trong luồng, nên tái sử dụng component/pattern đã thiết kế trước đó, không thiết kế lại từ đầu mỗi lần.

## Bước 10 — Tổ chức file theo flow

Mỗi luồng chức năng (flow) được tổ chức trong **1 Section Figma thật** (`figma.createSection()`), không dùng tag/label rời. Cấu trúc theo đúng mẫu đã kiểm chứng (tham khảo section "Meal Plan" trong file Recipe):

### 10.1 Cách dựng Section an toàn (bắt buộc theo đúng thứ tự)

Section trong Figma có 2 lỗi thường gặp nếu làm sai thứ tự — đã từng gây lệch toàn bộ layout:

1. **Toạ độ con bên trong Section là TƯƠNG ĐỐI so với Section** (giống frame con, không phải toạ độ tuyệt đối trên trang). Luôn tính toán layout bằng toạ độ local (bắt đầu gần `(padding, padding)`, KHÔNG cộng thêm `section.x/section.y`).
2. **PHẢI resize Section về đúng kích thước cuối cùng TRƯỚC khi thêm/định vị children.** Nếu định vị children vượt quá kích thước Section hiện tại rồi mới resize sau, Section có thể tự ý đổi cả `x` (bug đã gặp thực tế: `section.x` tự nhảy từ 0 sang giá trị khác dù không hề set). Quy trình đúng: (a) tính trước tổng kích thước nội dung cần chứa, (b) `section.resizeWithoutConstraints(width, height)` với kích thước đó, (c) sau đó mới `appendChild` + set `x/y` cho từng children.
3. Sau khi dựng xong, LUÔN verify bằng `node.absoluteBoundingBox` (không chỉ `node.x/node.y`) đối chiếu với `section.absoluteBoundingBox` để đảm bảo không có phần tử nào tràn ra ngoài — không tin tưởng riêng giá trị local x/y.

### 10.2 Bố cục Section

- **Title bar**: 1 frame auto-layout ngang ở đầu Section, `primaryAxisSizingMode: FIXED` (rộng = section width − 2×padding), `counterAxisSizingMode: AUTO` (hug height), nền màu tối hơn nền Section 1 chút, chứa 1 text căn giữa = tên flow, cỡ lớn, đậm, trắng.
- **Chiều rộng Section cố định 7000px** cho mọi flow (bất kể nội dung nhiều hay ít) để đồng nhất giữa các flow trong file; **chiều cao tự tính đủ chứa toàn bộ nội dung** + padding đáy ~200px.
- **Gap giữa các màn hình: 200px đều cả 2 chiều** (ngang và dọc).
- Margin trong Section (từ mép Section đến màn hình đầu tiên): tối thiểu 200px mỗi phía.

### 10.3 Tách case — KHÔNG nối liên mạch toàn bộ flow thành 1 mạng lưới

Đây là nguyên tắc quan trọng nhất rút ra sau khi thử nghiệm thực tế: nối tất cả state (happy path + mọi nhánh rẽ + mọi state lỗi) thành một chuỗi liên tục duy nhất, với các đường chéo/cong cắt ngang nhau, tạo cảm giác rối, khó đọc.

**Quy tắc:** chỉ nối liền mạch **happy path chính** (1 hàng ngang tuyến tính). Mọi nhánh rẽ (branch từ cùng 1 hành động) hoặc state lỗi lồng nhau được tách thành **case riêng biệt, độc lập**:

- Mỗi case là 1 cụm nhỏ tách hẳn khỏi các case khác (có khoảng trống rõ ràng giữa các case, xếp thành các hàng riêng bên dưới happy path).
- Mỗi case **nhân đôi (clone) màn hình nguồn** làm điểm bắt đầu riêng của case đó (không kéo mũi tên ngược về hàng happy path chính) — tương tự cách "Meal Plan" xử lý: mỗi case tự có 1 bản sao màn hình gốc, rồi nối tiếp bằng connector thẳng đơn giản trong nội bộ case.
- Mỗi case có 1 **label tiêu đề** phía trên (mô tả ngắn gọn case đó, VD "Không đủ coin"), style: font cùng họ với Title bar, đậm (Bold), cỡ 60, màu trắng, đặt cách đỉnh hàng màn hình của case đó khoảng 150px.
- Trong nội bộ 1 case, ưu tiên connector **thẳng ngang** (`→`) nối các màn hình cùng hàng — tránh dùng Curve/Snake nếu có thể sắp các màn hình thẳng hàng để không cần đường chéo.

### 10.4 Sử dụng component connector `🛠 Flows /`

File thường có sẵn 4 component set: `🛠 Flows / Straight`, `Curve`, `Snake`, `Double Snake`, mỗi cái có variant `Direction`, `Label` (True/False), `Dashed` (False=happy/main path, True=edge case/nhánh phụ).

**Luôn kiểm tra bằng dữ liệu thật trước khi tin vào tên variant** — tên "Direction" không phải lúc nào cũng trực quan như tưởng. Cách làm an toàn:
1. Tạo 1 instance test ở vị trí tạm, đọc `absoluteBoundingBox` của các con tên `.Details / Flow Cap` (và biến thể như `Cap/Arrow Bottom`, `Cap/Dot Empty`) để xác định chính xác điểm ĐẦU và điểm CUỐI nằm ở đâu trong bounding box mặc định (thường là 1 trong 4 góc).
2. Chỉ tin tưởng `instance.resize(w, h)` cho các variant mà 2 đầu nối nằm CHÍNH XÁC ở góc `(0,0)` và `(width,height)` — đây là dạng "corner-to-corner" resize an toàn. Nếu 2 đầu nối không nằm đúng góc (lệch offset), resize sẽ làm méo hình — không dùng variant đó theo cách resize tự do, thử variant khác.
3. Ví dụ đã xác minh: variant `Top → Right` của `Curve` nối chính xác góc trên-trái (điểm đầu) với góc dưới-phải (điểm cuối) — phù hợp khi nguồn nằm trên-trái, đích nằm dưới-phải. Ngược lại `Bottom → Right`/`Right → Bottom` lại nối góc dưới-trái với góc trên-phải (đi LÊN chứ không đi XUỐNG) — dễ nhầm, cần test trước khi dùng.
4. Sau khi resize + định vị, luôn verify lại bằng `absoluteBoundingBox` của cap con so với điểm neo thật trên 2 màn hình cần nối — không chỉ tin vào `instance.x/y` đã set.
5. Với connector ngang (`→`): chiều cao mặc định cố định (~96), chỉ resize chiều rộng = khoảng cách giữa 2 màn hình; `y` = tâm dọc hàng màn hình trừ nửa chiều cao connector.
6. Với connector dọc (`↓`): chiều rộng giữ nguyên mặc định (bao gồm khoảng chứa label ngang), chỉ resize chiều cao = khoảng cách; `x` = tâm ngang của cột trừ nửa chiều rộng connector.
7. Text label bên trong connector: tìm bằng `instance.findOne(n => n.type === "TEXT")` rồi set `characters` trực tiếp — không cần thao tác thêm với `🛠 Notes` wrapper.
8. Nếu 1 cặp màn hình cần nối cách xa qua nhiều cột (skip-over, dễ tạo đường cắt ngang qua màn hình khác) — theo 10.3, **ưu tiên tách thành case riêng thay vì cố vẽ connector phức tạp qua đó**.

## Bước 11 — Hình ảnh

- Khi cần hình ảnh thật (không phải illustration), dùng plugin Unsplash đã cài đặt sẵn trong Figma để tìm ảnh phù hợp với nội dung/ngữ cảnh màn hình.
- Nếu không thể gọi plugin trực tiếp qua Plugin API, báo lại cho người dùng để họ tự chèn ảnh qua plugin, và chừa đúng vị trí/kích thước (chia hết cho 4) cho ảnh đó.

## Bước 12 — Illustration

- Tạo các illustration cần thiết cho nội dung (VD: empty state, onboarding, success state) bằng SVG, giữ phong cách nhất quán với các illustration khác đã có trong file (nếu có) hoặc với color palette của style guide.

## Bước 13 — Bàn giao

Sau khi hoàn tất toàn bộ luồng, báo cáo lại cho người dùng:
- Danh sách state đã thiết kế (đối chiếu với danh sách đã confirm ở Bước 1).
- Bảng liệt kê các giá trị spacing/kích thước/border-radius đã dùng, kèm xác nhận tất cả đều chia hết cho 4 (nêu rõ nếu có giá trị đã được làm tròn từ tham chiếu gốc).
- Danh sách component mới đã tạo (nếu có) và số lần được tái sử dụng.
- Link tới section/frame đầu tiên của flow trong Figma.

Hỏi người dùng có cần chỉnh sửa gì thêm trước khi coi là hoàn tất.
