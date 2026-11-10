---
name: pm-spec-review
description: Đọc và phản biện tài liệu yêu cầu từ PM trước khi bắt tay thiết kế — lập bảng đối chiếu yêu cầu sang màn hình/state, audit những thứ tài liệu PM thường bỏ sót (empty/loading/error, offline, permission, dữ liệu biên, điểm vào-ra, phân quyền), phát hiện mâu thuẫn nội bộ và scope creep, rồi phân loại thành 3 nhóm hành động (câu hỏi chặn tiến độ / giả định designer tự chốt / việc ngoài phạm vi) kèm danh sách câu hỏi viết sẵn để gửi PM. Dùng skill này bất cứ khi nào người dùng đưa vào một tài liệu yêu cầu, spec, PRD, user story, ticket, mô tả tính năng, hay ảnh chụp tài liệu và muốn hiểu-tổng-hợp-kiểm tra nó trước khi thiết kế — kể cả khi họ chỉ nói "đọc cái này giúp tôi", "PM vừa gửi cái này", "tính năng này thiết kế thế nào", hay dán một đoạn yêu cầu vào chat. Cũng dùng khi tài liệu được cập nhật và cần so sánh với bản trước. Output của skill này là đầu vào trực tiếp cho Bước 1 của skill figma-flow-design. KHÔNG dùng cho các câu hỏi thiết kế chung không có tài liệu yêu cầu kèm theo.
---

# PM Spec Review

Audit tài liệu yêu cầu **trước khi** dựng một pixel nào. Mục đích: chuyển rủi ro từ "phát hiện sau khi dựng xong 12 màn hình" sang "phát hiện trong 20 phút đọc".

Skill này luôn chạy song song với `design-context` (bối cảnh người dùng, chuẩn US, accessibility). Đọc cả hai.

## Nguyên tắc

Ba nguyên tắc chung của bộ skill này vẫn áp dụng:

1. **Xác nhận trước khi tạo output** — dùng quick response (`ask_user_input_v0`), không hỏi bằng đoạn văn dài.
2. **Không tự ý suy luận** — nhưng lưu ý phân biệt: *Claude* không được tự đoán ý PM. *Designer* thì có quyền tự chốt một số thứ. Bước 4 tồn tại để phân định ranh giới này.
3. **Bám sát ngữ cảnh** — chỉ audit dựa trên tài liệu thật, không phát minh yêu cầu mới.

Thêm một nguyên tắc riêng của skill này:

4. **Không dội câu hỏi lên PM.** Một danh sách 40 câu hỏi sẽ không được trả lời. Giá trị của một senior designer là biết câu nào thật sự cần PM, câu nào tự chốt được rồi thông báo. Ưu tiên số lượng câu hỏi ít nhưng đúng chỗ chặn.

## Bước 0 — Thu thập đầu vào

1. Xác định tài liệu ở dạng nào và đọc đúng cách:
   - File `.docx` / `.pdf` / `.xlsx` upload → dùng skill `file-reading`, rồi `docx` / `pdf-reading` / `xlsx` tương ứng. Không `cat` file binary.
   - Google Docs / Sheets → dùng connector Google Drive nếu có.
   - Slack → dùng connector Slack nếu yêu cầu nằm trong tin nhắn/thread.
   - Ảnh chụp tài liệu → đọc trực tiếp từ ảnh.
   - Đoạn text dán vào chat → dùng luôn.
2. Hỏi người dùng 2 điều nếu chưa rõ (quick response):
   - **Phạm vi lần này**: audit toàn bộ tài liệu, hay chỉ một tính năng/luồng cụ thể trong đó?
   - **Có tài liệu/thiết kế nền trước đó không**: sản phẩm đã có sẵn màn hình liên quan chưa? Nếu có, yêu cầu mới phải được đối chiếu với hành vi hiện tại, không audit trong chân không.
3. Nếu tài liệu thiếu hẳn phần cần thiết để hiểu tính năng (không có mô tả luồng, chỉ có tên tính năng), nói ngay thay vì cố audit một tài liệu rỗng.

## Bước 1 — Đọc hết trước, chưa phán xét

Đọc toàn bộ trước khi viết nhận xét đầu tiên. Lý do: nhiều thứ trông như "thiếu" ở mục 2 lại được nói ở mục 7, và báo thiếu sai sẽ làm mất uy tín toàn bộ bản review.

Trong lượt đọc này chỉ ghi lại 3 thứ:
- **Mục tiêu thật của tính năng** (không phải mô tả tính năng — mà PM đang muốn thay đổi hành vi gì của người dùng). Nếu tài liệu không nói được điều này, đó là phát hiện quan trọng nhất của cả bản review.
- **Danh sách hành động người dùng** có thể thực hiện.
- **Chỗ nào có số liệu, quy tắc, ràng buộc cụ thể** — đây là phần dev sẽ hỏi lại, cần bám chặt.

## Bước 2 — Bảng đối chiếu Yêu cầu → Màn hình/State

Lập bảng này trước khi audit. Nó biến văn xuôi của PM thành đơn vị thiết kế đếm được.

| # | Yêu cầu (trích nguyên văn, ngắn) | Vị trí trong tài liệu | Màn hình / State cần có | Mức độ rõ |
|---|---|---|---|---|
| 1 | "User can import a recipe from a URL" | mục 2.1 | Import screen, Paste URL, Parsing, Parse success, Parse failed | Mơ hồ |

Quy tắc lập bảng:
- **Trích nguyên văn** phần yêu cầu, không diễn giải lại. Diễn giải làm mất đúng cái sự mơ hồ mình đang muốn chỉ ra.
- Ghi **vị trí trong tài liệu** để PM tra lại được — đây là chi tiết khiến bản review được đọc thay vì bị bỏ qua.
- Một yêu cầu thường nở ra nhiều state. Nếu một yêu cầu chỉ ra đúng 1 màn hình, khả năng cao là đang bỏ sót.
- Mức độ rõ: **Rõ** (chỉ có một cách hiểu và một cách dựng) / **Mơ hồ** (nhiều cách hiểu hợp lý) / **Thiếu** (được nhắc tên nhưng không có nội dung).

Chỉ một cách hiểu **và** một cách dựng mới được tính là Rõ. "User can share the recipe" nghe rõ nhưng share qua đâu, share cái gì, ai xem được — là Mơ hồ.

## Bước 3 — Audit theo checklist

Rà tài liệu theo từng nhóm dưới đây. Với mỗi nhóm, kết quả là: *có nói rồi* / *nói chưa đủ* / *không nói*.

Đừng liệt kê hết mọi mục cho mọi tính năng — chọn nhóm thật sự liên quan. Một checklist dán nguyên xi là dấu hiệu của review máy móc.

**Vòng đời dữ liệu**
- Empty state (lần đầu, và sau khi người dùng xoá hết — hai thứ khác nhau)
- Loading (skeleton / spinner / progress — và loading lần đầu vs loading khi refresh)
- Error: lỗi mạng, lỗi validation, lỗi server, timeout — mỗi loại có message và đường thoát riêng
- Partial success (import 8/10 item thành công thì sao)
- Dữ liệu cũ / stale — có hiện không, có báo không

**Kết nối & quyền**
- Offline hoàn toàn, và mất kết nối *giữa* luồng đang thực hiện
- Permission bị từ chối (camera, photo, location, notification) và đường quay lại xin lại quyền
- Trạng thái chưa đăng nhập nhưng chạm vào tính năng cần đăng nhập

**Dữ liệu biên**
- 0 item / 1 item / rất nhiều item (có phân trang không, ngưỡng bao nhiêu)
- Nội dung quá dài: tên, tiêu đề, mô tả — truncate ở đâu, tối đa mấy dòng
- Ký tự đặc biệt, emoji, text không phải Latin
- Giá trị bằng 0, số âm, ngày trong quá khứ

**Người dùng & phân quyền**
- Có nhiều loại account/tier không, ai thấy gì
- First-run vs returning user
- Tính năng có giới hạn theo gói trả phí không — và màn hình khi chạm giới hạn

**Điểm vào & điểm ra**
- Người dùng vào luồng này từ những đâu (thường nhiều hơn PM viết)
- Sau khi hoàn tất thành công thì đi đâu
- Nút back / cancel giữa luồng — dữ liệu đã nhập có mất không, có confirm không
- Thoát app giữa luồng rồi quay lại — resume hay bắt đầu lại

**Nội dung & thị trường**
- Copy đã có sẵn trong tài liệu chưa, hay designer phải viết
- Có ràng buộc format nào theo chuẩn US chưa được nêu (xem `design-context` mục 3)
- Có yêu cầu accessibility nào bị bỏ qua (xem `design-context` mục 4)

**Mâu thuẫn & phạm vi** — hai mục này thường giá trị nhất:
- **Mâu thuẫn nội bộ**: hai chỗ trong tài liệu nói khác nhau. Trích cả hai, cạnh nhau.
- **Mâu thuẫn với sản phẩm hiện tại**: yêu cầu mới phá vỡ hành vi đang có ở nơi khác.
- **Scope creep ngầm**: câu ngắn của PM kéo theo khối lượng thiết kế lớn không được tính. Ví dụ "and users can manage their saved items" — một câu, có thể là 6 màn hình. Chỉ ra rõ để bảo vệ tiến độ.

## Bước 4 — Phân loại 3 nhóm hành động

Đây là bước quan trọng nhất. Mọi điểm Mơ hồ/Thiếu ở Bước 2–3 phải rơi vào đúng một nhóm:

**A. Câu hỏi chặn tiến độ** — không có câu trả lời thì không thiết kế được, hoặc thiết kế sai sẽ phải làm lại toàn bộ. Đặc trưng: liên quan đến business rule, quyền, tiền, dữ liệu, hoặc mục tiêu tính năng. Nhóm này gửi PM. **Giữ dưới 8 câu.** Nếu nhiều hơn, tài liệu có vấn đề ở tầng cao hơn — nói thẳng điều đó thay vì gửi danh sách dài.

**B. Giả định designer tự chốt** — thuộc chuyên môn thiết kế, không cần PM quyết. Loading dùng skeleton hay spinner, empty state viết gì, thứ tự field trong form, pattern hiển thị lỗi. Với nhóm này: **tự chốt, ghi rõ giả định, thông báo cho PM ở dạng "tôi sẽ làm X, nói nếu không đúng"** — không hỏi.

**C. Ngoài phạm vi** — việc kéo theo nhưng không nằm trong yêu cầu lần này. Nêu ra, đề xuất tách sang sau, không tự làm.

Cách phân định khi lưỡng lự: hỏi "nếu tôi chốt sai điều này, ai là người phải sửa?" Nếu là dev hoặc business → nhóm A. Nếu chỉ là designer → nhóm B.

## Bước 5 — Viết câu hỏi gửi PM

PM trả lời mơ hồ khi bị hỏi mơ hồ. Mỗi câu hỏi nhóm A phải là **câu hỏi đóng có phương án kèm nghiêng hướng**.

**Kém:**
> Phần import từ URL xử lý thế nào khi lỗi?

**Tốt:**
> Khi parse URL thất bại (trang không hỗ trợ), mình chọn hướng nào?
> **(a)** Báo lỗi và cho nhập tay từ đầu — tôi nghiêng hướng này, ít màn hình hơn và người dùng không bị kẹt.
> **(b)** Báo lỗi và cho thử URL khác, giữ nguyên màn hình.
> Ảnh hưởng: hướng (b) cần thêm 1 state và quy tắc retry.

Cấu trúc mỗi câu: **tình huống cụ thể → 2–3 phương án → hướng mình nghiêng và lý do → ảnh hưởng nếu chọn khác**. Câu hỏi dạng này thường được trả lời bằng một chữ, nên tỉ lệ hồi đáp cao hơn nhiều.

Xuất phần này ở dạng **copy-paste được nguyên khối** để người dùng gửi thẳng cho PM. Nếu tiện, dùng tool soạn tin nhắn để họ gửi luôn.

## Bước 6 — Xuất danh sách state cho bước thiết kế

Kết thúc bằng danh sách state ở đúng định dạng mà **Bước 1 của `figma-flow-design`** cần — happy path + empty + loading + error + permission + giới hạn dữ liệu + state đặc biệt. Đây là điểm nối giữa hai skill; làm đúng thì người dùng chuyển sang dựng Figma không phải tổng hợp lại lần nữa.

Đánh dấu state nào đang **phụ thuộc câu hỏi nhóm A chưa được trả lời** — để không dựng sớm những màn hình có thể bị bỏ.

## Định dạng output

Xuất một file `.md` (tên theo tính năng, ví dụ `spec-review-recipe-import.md`) theo đúng cấu trúc:

```markdown
# Spec Review — [Tên tính năng]
Nguồn: [tên tài liệu, ngày/phiên bản]

## 1. Mục tiêu tính năng (theo cách tôi hiểu)
## 2. Bảng đối chiếu Yêu cầu → Màn hình/State
## 3. Mâu thuẫn & scope creep
## 4. Câu hỏi cần PM trả lời (chặn tiến độ)
## 5. Giả định tôi tự chốt (thông báo, không cần duyệt)
## 6. Đề xuất tách khỏi phạm vi lần này
## 7. Danh sách state để thiết kế
```

Trong chat, chỉ tóm tắt: số yêu cầu đã rà, số điểm mơ hồ/thiếu, số câu hỏi chặn tiến độ, và **phát hiện đáng lo nhất**. Không lặp lại toàn bộ file trong chat.

Trước khi xuất file, xác nhận với người dùng bằng quick response — ít nhất là mục 1 (mục tiêu tính năng theo cách hiểu của mình). Nếu hiểu sai mục tiêu, toàn bộ phần còn lại sẽ lệch.

## Case đặc biệt

- **Tài liệu được PM cập nhật, cần review lại:** đừng làm lại từ đầu. So sánh với bản review trước và xuất phần diff — yêu cầu nào mới, nào bị đổi, nào đã được trả lời, và **màn hình nào đã dựng giờ bị ảnh hưởng**. Mục cuối là mục người dùng cần nhất.
- **Yêu cầu đến rời rạc qua Slack/ticket, không có tài liệu:** vẫn chạy skill, nhưng nêu rõ đầu vào không phải tài liệu chính thức và bản review chỉ phản ánh những gì đã được nói ra. Đề xuất người dùng gửi lại bảng đối chiếu như một cách chốt yêu cầu bằng văn bản.
- **Tài liệu quá tốt, không có gì để phản biện:** nói thẳng là tài liệu đủ rõ, xuất luôn danh sách state ở Bước 6 và bỏ các mục trống. Không bịa ra vấn đề để bản review trông có giá trị.
- **Tài liệu đã kèm sẵn thiết kế/wireframe của PM:** audit yêu cầu trước, đánh giá wireframe sau và tách riêng — đừng để wireframe của PM đóng khung cách hiểu yêu cầu.
