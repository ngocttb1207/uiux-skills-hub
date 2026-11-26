---
name: figma-screen-naming
description: "Dùng khi cần xây dựng hoặc áp dụng quy ước đặt tên Section/Frame/sub-frame trong Figma cho BẤT KỲ dự án nào — suy ra tên từ cấu trúc và vai trò thật của dự án đó, không phải copy nguyên từ vựng của dự án PDF_IOS_2026. Kèm ví dụ áp dụng thực tế từ dự án PDF_IOS_2026 của Nghia ở phần Phụ lục."
---

# Phương pháp đặt tên Section/Frame/Sub-frame trong Figma (dùng cho mọi dự án)

Đây là 1 PHưƠNG PHÁP chung, không phải bộ từ vựng cố định của riêng 1 app nào. Dùng được cho bất kỳ dự án Figma nào — chỉ cần thay các ví dụ cụ thể (tên Section, tên tính năng...) bằng đúng cấu trúc thật của dự án bạn đang làm. Phần ví dụ minh họa ở cuối skill (Phụ lục) lấy từ dự án PDF_IOS_2026 của Nghia — đọc để hiểu cách áp dụng, KHÔNG copy nguyên các tên đó sang dự án khác.

## Bước 0 — Xác định cấu trúc thật của dự án bạn trước khi đặt tên bất cứ gì

Trước khi áp dụng bất kỳ rule nào dưới đây, xác định:
1. Danh sách Section/tính năng lớn THẬT của file bạn đang làm (không dùng danh sách Section của PDF_IOS_2026 nếu đây là 1 dự án khác, ví dụ Word-Office-iOS-2026 hay Identifier Food/Avo).
2. Team bạn đã có convention prefix icon riêng chưa (ví dụ `ic_`, `icon-`, `Icon/`...)? Nếu đã có, giữ theo convention đó, không ép theo ví dụ `ic_` của PDF_IOS_2026.
3. Design token thật của dự án bạn (cornerRadius, spacing, font...) — dùng đúng token thật của dự án đó, không copy số từ ví dụ PDF_IOS_2026.

Nếu chưa có câu trả lời rõ cho 3 ý trên, hỏi lại người yêu cầu trước khi đặt tên bất kỳ frame nào.

## 1. Section = nhóm theo tính năng/luồng lớn (nguyên tắc chung)

Mỗi file Figma nên chia theo các **Section** cấp cao nhất, mỗi Section đại diện cho 1 tính năng/luồng lớn THẬT của chính dự án đó — không phải 1 danh sách cố định áp dụng cho mọi nơi. Mỗi dự án sẽ có tập Section khác nhau, tùy theo nó có những tính năng gì.

Một Section cấp cao có thể chứa các **sub-Section** lồng bên trong, nhóm theo 1 sub-task hẹp hơn trong tính năng đó. Tên sub-Section ngắn, mô tả thẳng, không có dấu "/".

Nguyên tắc chung: nếu nó là 1 container gom nhiều màn hình/trạng thái cho 1 sub-task, đó là Section, không phải frame. **Con trực tiếp của 1 Section chỉ nên là sub-Section và frame màn hình thật (mục 2) — không bao giờ là 1 icon/sub-component nằm rời (xem mục 6).**

*(Xem danh sách Section thật của PDF_IOS_2026 làm ví dụ minh họa ở Phụ lục cuối skill.)*

## 2. Đặt tên Frame (màn hình) — đường dẫn 3 cấp, suy ra từ cấu trúc thật của dự án bạn

Mỗi màn hình/trạng thái thật là 1 **frame**, đặt tên đúng theo pattern:

```
<Tính năng/Luồng thật> / <Sub-flow hoặc Tab/Trạng thái thật> / <Mô tả màn hình hoặc trạng thái cụ thể>
```

**Trước khi đặt tên 1 frame màn hình, luôn suy ra Level 1 và Level 2 từ chính dự án đang làm:**
1. Xem frame này thực sự đang nằm trong Section nào, ở chính dự án này. Level 1 = tên Section thật đó (hoặc dạng rút ngắn gần đúng).
2. Xem sub-flow, tab, hoặc chế độ tương tác thật của frame này trong Section đó. Level 2 = hành vi thật đó, mô tả bằng đúng chức năng màn hình này thực sự làm.
3. **Không bao giờ dán nguyên từ vựng của 1 dự án khác** (ví dụ các từ `Home`, `Scan`, `Default`, `Camera` của PDF_IOS_2026) vào dự án bạn đang làm chỉ vì "nhìn cho giống" — những chữ đó chỉ đúng với chính PDF_IOS_2026, vì đó là tên Section/chức năng thật của nó.

Dùng dấu cách quanh "/" (` / `, không phải `/`liền). Ví dụ minh họa tổng quát (không gắn với dự án cụ thể, chỉ để thấy hình dạng pattern):
- `<Feature> / Default / <Tên tab gốc>`
- `<Feature> / <Sub-flow> / Bottom Sheet Open`
- `<Feature> / <Sub-flow> / Empty State`

Level 1 = Section tính năng/luồng THẬT mà frame này đang nằm trong, ở dự án bạn.
Level 2 = tab, sub-flow, hoặc chế độ tương tác THẬT mà màn hình này đại diện.
Level 3 = màn hình, trạng thái, hoặc bottom sheet cụ thể — mô tả rõ, có thể nhiều chữ.

### Variant (biến thể)
Khi 2 frame đại diện cùng 1 màn hình nhưng khác trạng thái/dữ liệu, thêm hậu tố variant trong dấu ngoặc vào Level 3, tăng số khi có từ 3 variant trở lên:
- `(Variant)` cho biến thể thứ 2
- `(Variant 2)`, `(Variant 3)`,... cho các biến thể tiếp theo
- Có thể dùng mô tả cụ thể trong ngoặc thay cho "Variant" khi rõ nghĩa hơn, ví dụ `(With Files List)`, `(Yearly Plan)`, `(Keyboard Closed)`.

### Luồng theo bước (Onboarding...)
Với các luồng tuyến tính theo bước (onboarding, paywall intro), Level 3 dùng:
```
Step <N> — <mô tả ngắn>
```

### Frame dùng lại cho mục đích khác (ảnh chụp App Store, bản QA tham khảo, tài liệu marketing...)
Nếu 1 frame màn hình được copy để dùng cho mục đích khác ngoài việc là bản thiết kế đang sống, **không bao giờ giữ nguyên tên y hệt bản gốc** — vì sẽ không thể biết bản nào là bản thiết kế thật đang được maintain khi tìm trong layer panel. Đổi namespace theo đúng mục đích sử dụng:
```
<Ngữ cảnh sử dụng> / <tên màn gốc rút gọn> / <mô tả cụ thể>
```

## 3. Đặt tên theo Vai trò cho sub-frame bên trong 1 màn hình (Role Vocabulary)

**Nguyên tắc cốt lõi, áp dụng cho mọi dự án:** tên của 1 sub-frame/element bên trong màn hình phải mô tả đúng **vai trò chức năng** của nó, không phải mô tả tùy hứng. Nếu 2 frame ở 2 màn hình khác nhau đóng cùng 1 vai trò, chúng PHẢI dùng chung 1 tên — quy tắc này bắt buộc ở bất kỳ dự án nào, không chỉ PDF_IOS_2026.

Dưới đây là danh sách vai trò phổ biến trong hầu hết app di động — dùng làm điểm khởi đầu, rồi bổ sung thêm vai trò riêng của dự án bạn khi cần:

| Vai trò | Tên chuẩn gợi ý | Khi nào dùng |
|---|---|---|
| Thanh trạng thái giả / dòng giờ | `Status_Bar` | Đầu mọi frame full-screen |
| Thanh điều hướng trên cùng | `Header` | Mọi màn có nav bar |
| Vùng xem trước nội dung chính | `Preview-Container` hoặc `Content-Container` | Mọi màn có vùng nội dung/preview riêng |
| Dãy nút hành động cho chức năng hiện tại | `Action-Container` | Mọi toolbar/bottom sheet có action button |
| Khung bọc layout chung, không có ý nghĩa riêng | `Layout Container` (thêm số nếu nhiều cấp: `Layout Container 2`) | Wrapper kỹ thuật thuần |
| Nền bo góc phía sau sheet/popup | `Background Shape` | Mọi bottom sheet/dialog |
| Tab switcher | `Segmented Control` | Mọi nơi có tab 2-3 lựa chọn |
| Icon nền cho 1 tính năng trong grid | `Icon_Bg` (chứa icon bên trong) | Feature grid, tool grid |
| Khung bọc trạng thái Empty / Loading / Error | `<State>_State_Container` (ví dụ `Empty_State_Container`) | Mọi màn có trạng thái đó |

Khi gặp 1 vai trò MỚI chưa có trong bảng của dự án bạn: đặt tên theo format `<Vai trò>_<mô tả ngắn>` (giữ style viết hoa/thường đang dùng trong dự án đó), rồi bổ sung thêm vào bảng vai trò của dự án đó để lần sau dùng lại — không tự nghĩ tên mới mỗi lần cho cùng 1 vai trò đã có.

*(Xem bảng vai trò đầy đủ đang dùng thật trong PDF_IOS_2026 ở Phụ lục.)*

## 4. Đặt tên Icon

Chọn 1 prefix cố định cho icon của dự án bạn và áp dụng nhất quán tuyệt đối, không ngoại lệ — nếu team đã có convention riêng thì giữ nguyên, nếu chưa có thì dùng `ic_...` làm mặc định (ví dụ trong PDF_IOS_2026: `ic_flash`, `ic_grid`, `ic_arrow`). Khi audit phát hiện 1 icon không theo đúng prefix đã chọn, đổi lại ngay khi đụng tới — không có trướng hợp nào được coi là ngoại lệ.

## 5. Marker cho flow connector (nếu dự án có dùng)

Nếu dự án dùng instance mũi tên/connector nối luồng trong prototype Figma, đặt 1 tên đại diện cố định, dễ filter, dùng xuyên suốt dự án — không đặt tên khác nhau mỗi lần. Ví dụ thực tế: PDF_IOS_2026 dùng `🛠 Flows / Snake`. Đây không phải màn hình thật — bỏ qua khi audit hoặc đếm số frame thật.

## 6. Không để frame/icon nằm rời trực tiếp trong 1 Section

Mọi icon, component, hoặc sub-frame phải nằm lồng bên trong đúng frame màn hình (hoặc frame vai trò) mà nó thuộc về. Không bao giờ để icon hay container nằm thẳng ở cấp gốc của Section, cùng cấp với các frame màn hình — vì sẽ không biết nó thuộc màn nào, và dễ bị bỏ quên khi sửa layout.

*(Xem ví dụ lỗi thật đã phát hiện ở PDF_IOS_2026 trong Phụ lục.)*

## 7. Xử lý khi audit phát hiện tên trùng

Khi audit thấy 2+ frame có tên (theo pattern "/") giống hệt nhau:
1. Kiểm tra chúng có thực sự là CÙNG 1 vai trò/nội dung không (bị copy-paste rồi quên đổi tên) → nếu đúng vậy, hợp nhất lại hoặc xóa bản dư, chỉ giữ 1 bản.
2. Nếu chúng là các state/variant thực sự khác nhau của cùng 1 màn → thêm hậu tố phân biệt theo mục 2 (Variant/mô tả).
3. Nếu chúng tồn tại cho các NGỮ CẢNH SỬ DỤNG khác nhau (bản thiết kế thật vs bản dùng cho Review app/App Store/QA/marketing) → đổi namespace theo ngữ cảnh, theo đúng rule "Frame dùng lại cho mục đích khác" ở mục 2 — không giữ tên gốc y hệt trên bản copy.
4. Nếu chúng là component chia sẻ có chủ đích, dùng lại ở nhiều entry point → giữ tên giống nhau là ĐÚNG, không phải lỗi — không cần sửa.

## 8. Checklist trước khi đặt tên 1 frame hoặc sub-frame mới

1. Đây là frame màn hình (mục 2) hay sub-frame/element bên trong 1 màn hình (mục 3)?
2. Nếu là frame màn hình: xác định trước Section THẬT nó đang nằm trong và sub-flow/chức năng THẬT của nó ở chính dự án này, rồi viết tên theo `<Section thật> / <Sub-flow thật> / <Mô tả màn>`. Nếu là bản copy dùng cho mục đích khác (App Store, QA...), đổi namespace theo mục đích đó thay vì giữ tên gốc.
3. Nếu là sub-frame/element: xác định VAI TRÒ chức năng trước, tra Bảng Vai trò (mục 3) của chính dự án bạn — nếu đã có vai trò tương ứng, DÙNG LẠI ĐÚNG TÊN ĐÓ, không đặt tên khác.
4. Không để icon/component nằm rời ở cấp gốc Section — luôn lồng vào đúng frame màn hình sử dụng nó.
5. Phát hiện trùng tên thật do copy-paste? Xử lý theo mục 7.
6. Icon luôn theo đúng 1 prefix cố định của dự án; flow connector (nếu có) luôn dùng 1 tên cố định.

---

## Phụ lục — Ví dụ áp dụng thực tế: dự án PDF_IOS_2026 (Nghia)

**Phần này chỉ là VÍ DỤ cụ thể từ 1 dự án, không phải quy tắc áp dụng chung.** Khi làm 1 dự án khác (Word-Office-iOS-2026, Identifier Food/Avo...), thay toàn bộ các tên dưới đây bằng cấu trúc thật của dự án đó (theo Bước 0).

Quy ước này được rút ra từ page "UI/UX Design" thật trong file Figma PDF_IOS_2026 (fileKey `u943g05n7En0kIMu7pNTNG`), bổ sung thêm sau 1 lần audit (18/09/2026).

**Section thật đang có:** `Home`, `Files`, `Scan`, `Search`, `FAB`, `File action`, `AI`, `PDF Editor`, `User Settings`, `Tools`, `Onboarding`, `Review app`.

**Sub-Section ví dụ:**
- `Scan` → `Camera & Scan Setting`, `Scan Mode`, `Add photos to scan`, `Save`, `Review`, `Manage Pages`
- `File action` → `Upload`, `Reduce File Size`, `Share`, `Convert`, `Save as copy`, `Email`, `Set Password`, `Change Password`, `Rename`, `Show Info`
- `Tools` → `Convert to PDF`, `Convert from PDF`, `Toolbox`
- `PDF Editor` → `Manage Pages`, `Search in PDF`, `Edit Tools`

**Frame màn hình thật đang dùng:**
- `Home / Default / Recent Tab`
- `Home / Search / Active No Query`
- `Home / Create / Bottom Sheet Open`
- `Scan / Camera / Single Mode Active`
- `Scan / Sign & Stamp / Add Sign Bottom Sheet`
- `AI Search / Chat History / New Chat`
- `Edit PDF / Fill & Sign / History Sign Empty`
- `Files / Cloud List / Default (With Files List)`
- `Onboarding / Intro / Step 1 — Everything for PDFs`
- Copy cho App Store: `Review app / Home Recent Tab / Screenshot 1` (không giữ y nguyên `Home / Default / Recent Tab`)

**Bảng vai trò đầy đủ đang dùng thật:** `Row — 9:41` (status bar), `Header` (`Header_editpdf` cho Edit PDF), `Preview-Container`, `Action-Container`, `Row — Apply to all pages`, `Layout Container`/`Layout Container 2`, `popup pick color`, `Background Shape`, `Segmented Control`, `Icon_Bg`.

**Icon:** prefix `ic_...`, ví dụ `ic_flash`, `ic_scan crop`, `ic_grid`, `ic_auto photo`, `ic_arrow`.

**Flow connector:** instance `🛠 Flows / Snake`.

**Lỗi thật đã phát hiện khi audit (18/09/2026), giữ lại làm bài học:**
- `ic_flash`, `ic_scan crop`, `ic_grid`, `ic_auto photo`, `Quality icon` nằm thẳng trong section `Scan` (đúng ra phải nằm trong frame `Scan / Camera / Single Mode Active`); `Quality icon` còn sai luôn prefix icon, đúng ra là `ic_quality`.
- `Home / Default / Recent Tab` bị trùng tên 9 lần (rải ở `Home`, `Home > View Style`, và `Review app`) không có gì phân biệt.
- `Edit PDF / Manage Pages / With Tabs` trùng tên 6 lần trong cùng `PDF Editor > Manage Pages`.
- `Edit PDF / Tool Selection / Dropdown Open` trùng tên 8 lần.