import customtkinter as ctk
import os
import sys
from tkinter import messagebox

# --- TỰ ĐỘNG CẤU HÌNH ĐƯỜNG DẪN HỆ THỐNG ---
root_path = os.path.dirname(os.path.abspath(__file__))
if root_path not in sys.path:
    sys.path.append(root_path)

try:
    # Import Model và các View
    from models.database import ProductModel
    from views_customer.main_customer_view import MainCustomerView
    from views_customer.shop_page import ShopPage
    from views_customer.cart_page import CartPage
    from views_customer.fav_page import FavPage
    from views_customer.profile_page import ProfilePage
    from views_customer.dangxuat_view import LogoutPage
except ImportError as e:
    print(f"Lỗi Import: {e}")
    sys.exit()


class CustomerController:
    def __init__(self):
        # 1. Cấu hình chủ đề (Theme) chuyên nghiệp
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")

        # 2. Khởi tạo dữ liệu
        self.model = ProductModel()
        self.cart = []

        # 3. Khởi tạo Giao diện chính
        self.view = MainCustomerView(self)
        self.pages = {}

        # 4. Đăng ký các trang vào hệ thống
        for PageClass in (ShopPage, CartPage, FavPage, ProfilePage, LogoutPage):
            page_name = PageClass.__name__
            frame = PageClass(parent=self.view.container, controller=self)
            self.pages[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # 5. Hiển thị Dashboard (ShopPage) ngay khi mở app
        self.show_frame("ShopPage")

        self.view.mainloop()

    def show_frame(self, page_name):
        """Hàm chuyển trang và cập nhật trạng thái Sidebar"""
        page = self.pages.get(page_name)
        if page:
            page.tkraise()

            # --- CẬP NHẬT TRẠNG THÁI NÚT BẤM SIDEBAR ---
            # Giúp người dùng biết họ đang ở trang nào (giống ảnh mẫu bạn gửi)
            for name, btn in self.view.nav_btns.items():
                if name == page_name:
                    # Nút được chọn: Nền xanh đậm, chữ trắng
                    btn.configure(fg_color="#2563eb", text_color="#ffffff")
                else:
                    # Nút không được chọn: Trong suốt, chữ xám Slate
                    btn.configure(fg_color="transparent", text_color="#64748b")

            # --- CẬP NHẬT DỮ LIỆU ---
            if page_name == "ShopPage":
                # Lấy dữ liệu sản phẩm từ Admin đã nhập trong database
                products = self.model.get_all_products()
                # Đổ dữ liệu vào giao diện Card của ShopPage
                self.pages["ShopPage"].load_products(products)
            elif page_name == "CartPage":
                page.refresh_cart(self.cart)

    def add_to_cart(self, product):
        """Xử lý thêm sản phẩm"""
        self.cart.append(product)
        print(f"Hệ thống: Đã thêm {product[1]} vào giỏ.")

    def logout_process(self):
        """Xác nhận đăng xuất và đóng ứng dụng"""
        self.view.destroy()
        print("Hệ thống: Đã thoát.")


if __name__ == "__main__":
    CustomerController()