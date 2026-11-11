# Ví dụ: Dòng sản phẩm Calories — Bộ Health (rút gọn)

Đây là bài mẫu đã duyệt, dùng để tham khảo độ sâu, giọng văn và cách dùng bảng. Bài thật đầy đủ hơn ở mỗi mục.

Input người dùng đã gửi:
1. Better Meal — đo calories bữa ăn bằng scan ảnh (Figma AI-Calories-iOS)
2. GLP-1 — log thuốc tiêm giảm cân GLP-1 + calories nạp trong ngày (Figma GLP-1)
3. Moss — theo dõi sức khỏe qua chỉ số Apple Watch (Figma Moss)

---

## I. Overview

Dòng Calories là nhóm app giúp người dùng kiểm soát năng lượng nạp vào – tiêu hao hằng ngày để đạt mục tiêu cân nặng. Dòng gồm 3 sản phẩm, mỗi sản phẩm đánh vào một "đầu vào" khác nhau: ăn gì, dùng thuốc gì, vận động và hồi phục ra sao.

### 1. Dòng Calories là gì, thuộc category nào trên Store

| Sản phẩm | Tên trong thiết kế | Vai trò trong dòng | Category Store |
| --- | --- | --- | --- |
| Better Meal | BetterMeal / AI Calories | AI đếm calories bữa ăn qua ảnh, barcode, nhãn dinh dưỡng | Health & Fitness |
| GLP-1 | Bloomy (mascot hải ly) | Log liều GLP-1, ước tính nồng độ thuốc, kết hợp calories nạp | Health & Fitness |
| Moss | Moss / StressWatch | Đọc dữ liệu Apple Watch: HRV, stress, giấc ngủ, fitness, calories tiêu hao | Health & Fitness |

### 2. Tại sao làm dòng app này?
- Keyword "calorie counter / AI calorie / food scanner" lớn, ổn định quanh năm.
- AI scan cho giá trị "wow" trong vài giây → chuyển đổi paywall tốt.
- Xu hướng thuốc GLP-1 (Ozempic, Wegovy, Mounjaro, Zepbound) tạo ngách mới ít đối thủ.
- Người dùng Apple Watch có dữ liệu nhưng thiếu diễn giải.
- Module Scan Food, Water, Activity, Weight dùng chung giữa các app.

### 3. Vấn đề người dùng, đặc điểm user
| | Better Meal | GLP-1 | Moss |
| --- | --- | --- | --- |
| Chân dung | 20–45 tuổi, muốn giảm/tăng/giữ cân, bận | 30–60 tuổi, đang/sắp dùng GLP-1 theo kê đơn | 25–45 tuổi, văn phòng, có Apple Watch |
| Vấn đề chính | Log thủ công mất thời gian | Quên liều, lo tác dụng phụ, chững cân | Nhiều số liệu nhưng không hiểu |
| Rào cản | Ngại nhập liệu | Lo lắng, nhạy cảm với thông tin y khoa | Khó hiểu thuật ngữ (HRV, RMSSD) |

## II. Yêu cầu về Product

### 1. Model khai thác
Cả dòng đi theo IAP (subscription): thiết kế chỉ có màn IAP, chưa thấy vị trí ads. (Câu hỏi mở: Hybrid cho Android/tier 2–3?)

| Sản phẩm | Model | Kiểu paywall | Gói giá |
| --- | --- | --- | --- |
| Better Meal | IAP | Hard paywall + Last Offer đếm ngược | Weekly, Yearly $99.99 |
| GLP-1 | IAP | Paywall + vòng quay 30% → 80% off + soft paywall trên Home | Weekly, Yearly, trial 3 ngày |
| Moss | IAP | Bản 1 gói và 3 gói | Yearly $33.99 (trial 7 ngày), Monthly $12.99, Weekly $9.99 |

### 2. Yêu cầu về tính năng
Main function chọn theo keyword chính: keyword app đang đẩy ASO thì tính năng đó nằm ở vị trí nổi bật nhất trên Home và là bước đầu tiên sau Onboarding.

- **Better Meal**
    - Keyword chính: AI calorie counter, food scanner
    - Core / Main function: AI Scan Food (ảnh, barcode, nhãn) → kcal + macro; Calories left trên Home
    - Tính năng phụ: log nước, bước chân, cân nặng; AI recipes; Streak
- **GLP-1**
    - Keyword chính: GLP-1 tracker, shot tracker
    - Core / Main function: Log Shot / Medication + Medication Level, nhắc liều
    - Tính năng phụ: Scan/Search Food, vị trí tiêm, tác dụng phụ, Widget
- **Moss**
    - Keyword chính: stress tracker, HRV, Apple Watch
    - Core / Main function: Daily Score (HRV + Real-Time Stress)
    - Tính năng phụ: Sleep, Fitness, Hydration, Caffeine, Bio Age, FaceScan

![Better Meal – Home](blob/…)  ← ảnh dẫn chứng (hoặc link Figma nếu không tải được ảnh)

### 3. Yêu cầu về công nghệ
| Sản phẩm | Công nghệ | Ghi chú thiết kế |
| --- | --- | --- |
| Better Meal | AI nhận diện món, OCR, barcode, LLM | Màn hướng dẫn chụp, trạng thái phân tích, cho sửa kết quả |
| GLP-1 | Mô hình half-life, Apple Health, Widget, BMR/TDEE/MET | Mọi số ghi rõ là ước tính |
| Moss | HealthKit + Apple Watch, HRV RMSSD, stress mỗi 6 phút, FaceScan on-device | Trạng thái Learning/Insufficient Data (cần 30 ngày) |

### 4. Thiết kế UIUX
- Home trả lời ngay câu hỏi chính; log ≤ 3 tap; luôn cho sửa/nhập tay; đủ edge case.
- Luồng Scan Food: Hướng dẫn → Camera → Phân tích → Kết quả (sửa được) → Chọn bữa → Log → Home cập nhật.
- Style: Better Meal clean/sáng/ảnh món ăn thật; GLP-1 mềm, ấm, text to, mascot; Moss thiên nhiên, mỗi chart kèm 1 câu diễn giải.
- Màu: Better Meal xanh mint + đen; GLP-1 tím lavender; Moss xanh rêu pastel; trạng thái xanh → vàng → cam, tránh đỏ gắt.
- Visual, illustration (nguyên tắc chung):
    - Mỗi app có một mascot đi từ Onboarding vào trong app (Home, empty state, paywall) để user luôn có cảm giác có người đồng hành, sẵn sàng hỗ trợ; mascot cũng giúp đồng bộ các element hình ảnh.
    - Một style illustration/icon thống nhất theo màu brand.
    - Dùng hình để giải thích số liệu (quy đổi, so sánh trực quan) thay vì thêm chữ.
    - Tránh hình ảnh y khoa gây lo lắng; ưu tiên hình tích cực, gần gũi.

### 5. Dữ liệu hiển thị
```latex
TDEE = BMR \times (1.2 / 1.375 / 1.55 / 1.725) \qquad Calories\ left = Goal - Food + Exercise
```
- Nguồn: CDC/WHO, Dietary Reference Intakes, FDA labels, Compendium of Physical Activities.
- Không chẩn đoán; GLP-1 không khuyên đổi/bỏ liều; câu mẫu: "Use this number to follow a trend over time, not as a verdict on your health".

### 6. Onboarding
1. Welcome + social proof → 2. Mục tiêu → 3. Thông tin cơ thể → 4. Thói quen ("Did you know?") → 5. Tốc độ + dự đoán (có disclaimer) → 6. Building your plan → 7. Xin quyền → 8. Paywall.
GLP-1 rẽ nhánh Đã dùng / Chưa dùng thuốc; Moss bắt buộc kết nối Watch.

### 7. Paywall
| Thành phần | Yêu cầu | Ví dụ |
| --- | --- | --- |
| Visual | Mascot/mockup theo brand | Moss: cục rêu trên đồng cỏ |
| Gói giá | Yearly chọn sẵn + "Best value", giá/ngày | Moss $0.11/ngày |
| Bắt buộc | Close, Restore, Terms, Privacy, điều khoản gia hạn | Đủ trong Moss |
| Offer khi thoát | 1–2 lớp | Better Meal 60% off; GLP-1 vòng quay |

## III. Tổng kết
| | Better Meal | GLP-1 | Moss |
| --- | --- | --- | --- |
| Main function | AI Scan Food | Log Shot + Medication Level | Daily Score |
| Màu brand | Xanh mint + đen | Tím lavender | Xanh rêu pastel |
| Paywall | Hard + Last Offer | Vòng quay + soft paywall | 1/3 gói, trial 7 ngày |

Nguyên tắc chung: main function theo keyword; log ≤ 3 tap; số liệu có công thức + nguồn + "ước tính"; đủ edge case; onboarding quiz → plan → paywall; tái sử dụng component.
