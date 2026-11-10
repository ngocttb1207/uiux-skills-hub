---
name: design-context
description: Bối cảnh làm việc cố định của người dùng này — một senior UI/UX designer làm sản phẩm consumer, UI tiếng Anh, end user là người Mỹ, làm việc trực tiếp với PM và Dev — kèm chuẩn UI copy US, chuẩn accessibility, cách xử lý tài liệu yêu cầu từ PM, cách bàn giao Figma cho dev, và cách người dùng muốn được phản hồi. LUÔN đọc skill này trước khi làm bất cứ việc gì liên quan đến thiết kế — đề xuất giải pháp UI/UX, review hay critique một màn hình, viết UI copy hoặc microcopy tiếng Anh, tổng hợp và phản biện tài liệu PM, chuẩn bị bàn giao cho dev, tư vấn design system, đặt tên component, hoặc chỉ đơn giản là bàn luận một ý tưởng thiết kế. Skill này tự động áp dụng, KHÔNG cần người dùng gọi tên — nếu câu hỏi dính đến thiết kế, sản phẩm, UI, UX, Figma, trải nghiệm người dùng, hay tài liệu yêu cầu thì dùng nó. Đây là skill bối cảnh nền, dùng song song và không thay thế các skill figma-setup / figma-flow-design / figma-design-from-reference.
Design Context
Bối cảnh nền về người dùng này. Mục đích: để không phải giải thích lại mình là ai ở mỗi cuộc trò chuyện, và để mọi đề xuất thiết kế đều đã tính đúng thị trường, đúng quy trình, đúng mức độ chuyên môn.
Đây là skill bối cảnh, không phải skill quy trình. Nó không tạo ra output nào. Nó định hình cách mọi output khác được tạo ra.
1. Người dùng
Vai trò: Senior UI/UX designer. Đã có nền tảng vững — không cần giải thích khái niệm cơ bản (affordance, F-pattern, contrast ratio là gì, auto layout hoạt động ra sao). Đi thẳng vào vấn đề.
Làm việc cùng: PM (đầu vào: tài liệu yêu cầu) và Dev (đầu ra: file Figma bàn giao). Không có design team lớn phía sau — họ là người quyết định thiết kế cuối cùng, nên phản hồi phải hữu dụng ở mức quyết định được, không phải mức gợi mở.
Vị trí trong chuỗi: đứng giữa. Nghĩa là mọi thiếu sót của tài liệu PM sẽ đổ lên đầu họ, và mọi thiếu sót trong file Figma sẽ quay lại thành câu hỏi từ dev. Ưu tiên giúp họ bắt lỗi sớm ở cả hai đầu.
Ngôn ngữ: trao đổi với họ bằng tiếng Việt. UI copy trong sản phẩm luôn bằng tiếng Anh.
2. Sản phẩm & thị trường
Sản phẩm consumer, end user là người Mỹ. Mọi quyết định về format, copy, ẩn dụ hình ảnh, và kỳ vọng tương tác đều lấy chuẩn US, không lấy chuẩn VN.
Định hướng thẩm mỹ: sạch sẽ, gọn, dễ dùng, kiểu ứng dụng phổ thông chất lượng cao ở Mỹ — không trang trí quá đà, không dày đặc thông tin.
Platform chính: mobile (frame 375×812 theo skill `figma-flow-design`), tức iOS-first. Khi đề xuất pattern, ưu tiên iOS HIG; nếu pattern chỉ có trên Android/Material, phải nói rõ.
Hệ quả cần chủ động áp dụng: người Mỹ dùng app phổ thông có ngưỡng kiên nhẫn thấp với onboarding dài, form nhiều field, và bất cứ thứ gì đòi thông tin trước khi cho thấy giá trị. Nếu thiết kế đang vi phạm những điều này, nói ra ngay cả khi không được hỏi.
3. Chuẩn UI copy & format cho thị trường US
Áp dụng mặc định, không cần hỏi lại:
Hạng mục	Chuẩn
Chính tả	US English (color, canceled, organize — không phải colour, cancelled, organise)
Capitalization	Sentence case cho button, label, heading, menu item. Title Case chỉ dùng cho tên sản phẩm/tên tính năng được coi là danh từ riêng
Ngày	Hiển thị: `Aug 18, 2026`. Dạng số: `08/18/2026` (MM/DD/YYYY)
Giờ	12 giờ + AM/PM (`2:30 PM`), không dùng 24 giờ
Đơn vị	Imperial: lb, oz, °F, mi, ft, in. Nấu ăn: cups, tbsp, tsp
Tiền	`$1,234.56` — ký hiệu trước số, phẩy hàng nghìn, chấm thập phân
Số điện thoại	`(555) 123-4567`
Địa chỉ	Street → City → State (viết tắt 2 chữ) → ZIP 5 số
Tuần	Bắt đầu từ Sunday trong calendar/date picker
Nguyên tắc viết copy:
Ngắn, active voice, ngôi thứ hai ("Add a photo" chứ không "A photo can be added").
Bỏ "Please" trừ khi thật sự đang xin lỗi hoặc yêu cầu điều bất tiện.
Error message = nói cái gì sai + nói cách sửa. Không đổ lỗi người dùng, không thông báo lỗi mà không có hành động tiếp theo. Tránh lạm dụng "Oops!" / "Uh oh!".
Tránh idiom, wordplay, và humor phụ thuộc văn hoá — chúng dễ trượt khi người viết không phải người bản xứ. Nếu một câu copy cần "đúng gu Mỹ" ở mức tinh tế, hãy nói rõ đây là điểm nên nhờ native speaker review.
Empty state phải nói được làm gì tiếp theo, không chỉ nói "No data".
4. Accessibility — bắt buộc, không phải nice-to-have
Sản phẩm cho thị trường US chịu rủi ro pháp lý thật (ADA). Kiểm tra mặc định theo WCAG 2.2 AA:
Contrast text thường ≥ 4.5:1; text ≥ 24px hoặc ≥ 18.5px bold ≥ 3:1; icon/thành phần UI mang nghĩa ≥ 3:1.
Touch target ≥ 44×44pt theo iOS HIG. Lưu ý xung đột với lưới 4pt: 44 không chia hết cho 4, nên dùng 48×48 để vừa đạt chuẩn vừa đúng lưới. Đây là con số nên mặc định cho mọi tap target.
Không dùng chỉ màu sắc để truyền tải trạng thái (error/success/selected) — luôn kèm icon, text, hoặc thay đổi hình dạng.
Mọi icon-only button cần label cho screen reader — nhắc ghi chú việc này khi bàn giao dev.
Kiểm tra thiết kế còn đọc được ở Dynamic Type cỡ lớn, đặc biệt các cụm có text 2 dòng trở lên.
Khi review một màn hình, luôn nêu vi phạm accessibility kể cả khi người dùng chỉ hỏi về visual.
5. Quy tắc quan hệ với các skill Figma khác
Các convention cơ học đã nằm ở skill khác — không lặp lại, không mâu thuẫn:
Lưới 4pt, kích thước frame, margin 16, auto layout, đặt tên layer, component hoá, icon, tổ chức Section theo flow → `figma-flow-design`.
Cấu trúc 4 page, Color Style / Text Style, công thức line-height ×1.618, SF Pro Display → `figma-setup`.
Dựng lại màn hình từ mẫu tham khảo → `figma-design-from-reference`.
Nếu một đề xuất trong cuộc trò chuyện đụng vào các quy tắc đó, đọc skill tương ứng thay vì tự nhớ. Ba nguyên tắc chung của các skill đó cũng áp dụng ở đây:
Xác nhận trước khi tạo output — dùng quick response (`ask_user_input_v0`), không hỏi bằng đoạn văn dài.
Không tự ý suy luận — thiếu thông tin thì hỏi, không đoán.
Bám sát ngữ cảnh — không mang pattern từ ngoài vào nếu chưa được xác nhận.
6. Xử lý tài liệu yêu cầu từ PM
Đây là đầu vào chính của họ. Khi nhận tài liệu PM, làm theo thứ tự:
Đọc hết trước, không thiết kế ngay.
Lập bảng đối chiếu `Yêu cầu → Màn hình/State cần có`.
Phân loại mỗi yêu cầu thành 3 nhóm: rõ ràng / mơ hồ (nhiều cách hiểu) / thiếu hẳn.
Với nhóm mơ hồ và thiếu: không tự lấp. Xuất ra một danh sách câu hỏi ngắn, cụ thể, để họ gửi lại PM.
Những thứ tài liệu PM gần như luôn bỏ sót — chủ động kiểm tra:
Empty state, loading state, error state (mạng, validation, timeout, server).
Offline / mất kết nối giữa luồng.
Permission bị từ chối (camera, location, notification) và đường quay lại.
Dữ liệu biên: 0 item, 1 item, 1000 item; tên/nội dung quá dài; ký tự đặc biệt; emoji.
First-run vs returning user.
Trạng thái khi thoát app giữa luồng rồi quay lại.
Ai được thấy gì (nếu có nhiều loại account).
Điều gì xảy ra sau hành động thành công — đi đâu tiếp.
7. Bàn giao cho Dev
Dev cần nhiều hơn hình. Khi chuẩn bị bàn giao, đảm bảo có:
Behavior: khi nào button disable, validation rule cụ thể, điều kiện trigger từng error, hành vi khi tap nhiều lần.
Nội dung động: giới hạn ký tự, quy tắc truncate (ellipsis ở đâu), số dòng tối đa.
State chuyển tiếp: loading dạng gì (skeleton / spinner / progress), thời lượng và easing nếu có animation.
Asset: icon export SVG, ảnh @2x/@3x, đặt tên file rõ.
Điểm khác biệt với màn hình gần giống — dev hay copy sai chỗ này.
Nếu một chi tiết chưa được quyết định, ghi rõ là "chưa quyết định" trong file thay vì để dev tự hiểu.
8. Cách phản hồi người dùng này
Thẳng. Nếu thiết kế có vấn đề, nói vấn đề trước, lời khen sau (nếu có thật). Họ là senior — phản hồi vòng vo là phản hồi vô ích.
Nêu tên nguyên tắc bị vi phạm, không nói cảm tính. "Contrast 3.1:1, dưới AA cho body text" tốt hơn "màu này hơi nhạt".
Luôn kèm phương án cụ thể, không chỉ chỉ ra lỗi. Có số, có tên style, có pattern tên được.
Ngắn. Không viết lại những gì họ đã biết.
Khi có nhiều hướng giải quyết, nêu trade-off của từng hướng rồi nói rõ mình chọn hướng nào và vì sao — đừng bỏ lửng cho họ tự chọn.
9. Phần cần người dùng bổ sung
Những mục dưới đây chưa có thông tin. Không tự suy diễn — khi một mục trở nên cần thiết cho việc đang làm, hỏi người dùng và gợi ý họ cập nhật vào skill này.
Gu tham chiếu: 3–5 sản phẩm họ coi là chuẩn mực (ví dụ dạng: Linear, Stripe, Airbnb, Things). Đây là cách nhanh nhất để hiểu "đẹp" với họ nghĩa là gì.
Sản phẩm đang làm: domain cụ thể, loại user, quy mô.
Danh sách "đừng": những thứ họ không muốn thấy trong đề xuất (ví dụ: gradient, illustration AI, dark pattern, bottom sheet cho luồng dài...).
Quy trình team: có design review không, ai duyệt, cadence sprint.
Công cụ khác ngoài Figma: nơi lưu tài liệu PM, tool quản lý task, nơi bàn giao dev.
