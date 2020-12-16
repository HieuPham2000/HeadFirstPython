
# Bài tập lớn Nhập môn Công nghệ phần mềm - Nhóm 18

## Ứng dụng web: Hệ thống quản lý kiến nghị, phản ánh  
- Với người dân, ứng dụng cho phép gửi kiến nghị và xem phản hồi dễ dàng, nhanh chóng 
- Với tổ trưởng, ứng dụng giúp tiếp nhận, giải quyết và phản hồi kiến nghị hiệu quả và nhanh chóng hơn, ngoài ra cho phép thống kê số lượng kiến nghị theo trạng thái giải quyết. 


## Mục lục
[1. Lý do chọn đề tài](#1-Lý-do-chọn-đề-tài)  
[2. Tính năng chính](#2-Tính-năng-chính)   
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[2.1. Đăng nhập](#21-Đăng-nhập)   
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[2.2. Gửi kiến nghị - phản ánh mới](#22-Gửi-kiến-nghị---phản-ánh-mới)   
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[2.3. Xem danh sách kiến nghị đã gửi](#23-Xem-danh-sách-kiến-nghị-đã-gửi)   
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[2.4. Xem phản hồi từ tổ trưởng](#24-Xem-phản-hồi-từ-tổ-trưởng)   
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[2.5. Phản hồi kiến nghị](#25-Phản-hồi-kiến-nghị)   
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[2.6. Thống kê kiến nghị](#26-Thống-kê-kiến-nghị)   
[3. Hướng dẫn cài đặt](#3)   
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[3.1 Cài đặt NodeJs](#3.1)   
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[3.2 Cài đặt dependences](#3.2)   
[4. Chạy chương trình](#3-Chạy-chương-trình)

## 1. Lý do chọn đề tài  
Tại mỗi khu dân cư, tổ dân phố, hàng ngày đều có rất nhiều hoạt động sinh hoạt diễn ra, và trong đó sẽ xuất hiện những sự cố, bất cập (như vấn đề điện, nước, thu gom rác thải…). Khi đó, người dân sẽ gửi phản ánh, kiến nghị của mình với tổ trưởng tổ dân phố, và thường là gặp mặt trực tiếp trình bày để được giải quyết. Điều này làm mất thời gian, công sức của cả cư dân và tổ trưởng, và có thể không đảm bảo tính cấp bách của vấn đề. Bên cạnh đó, với những khu tổ dân phố có địa bàn rộng, dân cư đông, phức tạp (như có các sinh viên thuê trọ, các gia đình nơi khác đến thuê nhà làm kinh doanh dịch vụ…), việc quản lý cũng như giải quyết phản ánh, kiến nghị sẽ gặp nhiều khó khăn.  

## 2. Tính năng chính
### 2.1. Đăng nhập
Cho phép người dùng lựa chọn đăng nhập với tư cách "Người dân" hoặc "Tổ trưởng"
<p align="center">
  <img src="https://i.ibb.co/MP81wrV/sign-in-user.png" width=600><br>
  Đăng nhập dành cho người dân<br><br>
</p>
<p align="center">
  <img src="https://i.ibb.co/K5KFzLB/sign-in-admin.png" width=600><br>
  Đăng nhập dành cho tổ trưởng<br><br>
</p>

### 2.2. Gửi kiến nghị - phản ánh mới
<p align="center">
  <img src="https://i.ibb.co/YR1jJbc/send-new-request.png" width=600>
</p>

### 2.3. Xem danh sách kiến nghị đã gửi
<p align="center">
  <img src="https://i.ibb.co/02sH45d/list-request.png" width=600>
</p>

### 2.4. Xem phản hồi từ tổ trưởng
<p align="center">
  <img src="https://i.ibb.co/mq5nRTg/feedback.png" width=600>
</p>

### 2.5. Phản hồi kiến nghị
<p align="center">
  <img src="https://i.ibb.co/C2Cd3m7/feedback-request.png" width=600>
</p>

### 2.6. Thống kê kiến nghị
<p align="center">
  <img src="https://i.ibb.co/hH7gbBS/statistic.png" width=800>
  <img src="https://www.linkpicture.com/q/statistic.png" width=800>
</p>

## 3. Hướng dẫn cài đặt
### 3.1. Cài nodejs đối với hệ điều hành phù hợp
[Tại đây](https://nodejs.org/en/download/)
### 3.2. Tải các dependences cần thiết
```bassh
npm install
```
## 3. Chạy chương trình
```bash
npm run start
```
Mở browser truy cập vào http://localhost:8080/
