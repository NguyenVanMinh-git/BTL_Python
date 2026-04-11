# Dự Án: Phần Mềm Quản Lý Cửa Hàng Thời Trang

## 📝 Giới thiệu
Dự án xây dựng ứng dụng quản lý cửa hàng thời trang giúp tối ưu hóa quy trình bán hàng, kiểm soát kho và theo dõi doanh thu. Ứng dụng được phát triển trên nền tảng Python, sử dụng thư viện PyQt (thiết kế qua Qt Designer).

---

## 🚀 Chức năng chính của ứng dụng

### 1. Quản lý Đăng nhập
* **Xác thực người dùng:** Kiểm tra tài khoản nhân viên/quản lý để truy cập hệ thống.
* **Bảo mật:** Mã hóa mật khẩu và phân quyền truy cập các tính năng.

### 2. Quản lý Sản phẩm (Kho hàng)
* **Danh mục hàng hóa:** Quản lý thông tin chi tiết về quần áo, giày dép (Mã sản phẩm, Tên, Đơn giá).
* **Quản lý thuộc tính:** Hỗ trợ phân loại theo Size (S, M, L, XL) và Màu sắc.
* **Thao tác dữ liệu:** Cho phép Thêm mới, Sửa thông tin hoặc Xóa sản phẩm khỏi hệ thống.

### 3. Nghiệp vụ Bán hàng (POS)
* **Lập hóa đơn:** Chọn sản phẩm vào giỏ hàng và tính tổng tiền tự động.
* **Thanh toán:** Hỗ trợ ghi nhận hình thức thanh toán và xuất hóa đơn cho khách hàng.
* **Tra cứu:** Tìm kiếm nhanh sản phẩm bằng tên hoặc mã vạch.

### 4. Thống kê & Báo cáo
* **Doanh thu:** Xem tổng hợp doanh số theo khoảng thời gian tùy chọn.
* **Tồn kho:** Cảnh báo các mặt hàng sắp hết để có kế hoạch nhập hàng kịp thời.

---

## 🎨 Phác thảo giao diện (UI Mockup)

Giao diện được thiết kế theo phong cách tối giản, tập trung vào trải nghiệm người dùng. Dưới đây là mô tả bố cục các màn hình chính:

### Màn hình Đăng nhập
* **Cấu trúc:** Gồm các khối nhập liệu `Username`, `Password` và nút `Đăng nhập` được căn giữa màn hình.
* **Công cụ thiết kế:** Qt Designer / Draw.io.

### Màn hình Chính (Dashboard)
* **Thanh điều hướng:** Chứa các nút chuyển đổi nhanh giữa các phân hệ (Bán hàng, Sản phẩm, Thống kê).
* **Khu vực hiển thị:** Bảng dữ liệu sản phẩm và các biểu đồ doanh thu trực quan.

---

## 🛠 Công cụ phát triển
* **Ngôn ngữ:** Python.
* **Giao diện:** PyQt5 / Qt Designer (file `.ui`).
* **Cơ sở dữ liệu:** MySQL / SQLite.
* **Quản lý mã nguồn:** Git & GitHub.

