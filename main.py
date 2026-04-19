import customtkinter as ctk
from tkinter import messagebox
import os
import sys

# Cấu hình đường dẫn project
root_path = os.path.dirname(os.path.abspath(__file__))
if root_path not in sys.path:
    sys.path.append(root_path)

from models.database import ProductModel


# --- 1. GIAO DIỆN ĐĂNG NHẬP CHUYÊN NGHIỆP ---
class LoginView(ctk.CTk):
    def __init__(self, on_login_success):
        super().__init__()
        self.on_login_success = on_login_success
        self.title("MINH TRÍ STORE - LOGIN")
        self.geometry("400x600")
        self.resizable(False, False)
        self.configure(fg_color="#f8fafc")

        # Căn giữa
        self.update_idletasks()
        x = (self.winfo_screenwidth() // 2) - (400 // 2)
        y = (self.winfo_screenheight() // 2) - (600 // 2)
        self.geometry(f"+{x}+{y}")

        # Card chứa form (Bo góc, trắng tinh tế)
        self.card = ctk.CTkFrame(self, fg_color="white", corner_radius=25, border_width=1, border_color="#e2e8f0")
        self.card.pack(fill="both", expand=True, padx=30, pady=40)

        # Header
        ctk.CTkLabel(self.card, text="MINH TRÍ STORE", font=("Segoe UI", 28, "bold"), text_color="#1e293b").pack(
            pady=(40, 5))
        ctk.CTkLabel(self.card, text="Hệ thống quản lý thông minh", font=("Segoe UI", 13), text_color="#64748b").pack(
            pady=(0, 40))

        # Nhập liệu với hiệu ứng bo tròn hiện đại
        self.user_entry = ctk.CTkEntry(self.card, placeholder_text="Tên đăng nhập", width=300, height=48,
                                       corner_radius=12, fg_color="#f1f5f9", border_color="#cbd5e1")
        self.user_entry.pack(pady=12)

        self.pass_entry = ctk.CTkEntry(self.card, placeholder_text="Mật khẩu", show="*", width=300, height=48,
                                       corner_radius=12, fg_color="#f1f5f9", border_color="#cbd5e1")
        self.pass_entry.pack(pady=12)

        # Nút Đăng nhập màu xanh chuẩn công nghệ
        self.btn_login = ctk.CTkButton(self.card, text="ĐĂNG NHẬP", width=300, height=52,
                                       corner_radius=12, font=("Segoe UI", 15, "bold"),
                                       fg_color="#2563eb", hover_color="#1d4ed8",
                                       command=self.on_login_success)
        self.btn_login.pack(pady=(35, 20))


# --- 2. BỘ ĐIỀU KHIỂN CHÍNH (Xử lý Click Menu) ---
class MainController:
    def __init__(self):
        ctk.set_appearance_mode("light")
        self.model = ProductModel()
        self.view = None
        self.pages = {}
        self.current_user_role = None
        self.run_login()

    def run_login(self):
        self.login_screen = LoginView(on_login_success=self.check_login_role)
        self.login_screen.mainloop()

    def check_login_role(self):
        u = self.login_screen.user_entry.get().strip()
        p = self.login_screen.pass_entry.get().strip()

        if (u == "admin" and p == "123456") or (u == "khachhang" and p == "123456"):
            self.current_user_role = "admin" if u == "admin" else "customer"
            self.login_screen.quit()
            self.login_screen.destroy()

            # Reset hoàn toàn luồng Tkinter để tránh lỗi "invalid command"
            root = ctk.CTk()
            root.withdraw()
            root.after(100, lambda: [root.destroy(), self.start_application()])
            root.mainloop()
        else:
            messagebox.showerror("Lỗi", "Thông tin tài khoản không chính xác!")

    def start_application(self):
        if self.current_user_role == "admin":
            self.init_admin_app()
        else:
            self.init_customer_app()

    def init_admin_app(self):
        """Khởi tạo Admin với đầy đủ các trang và gán lệnh Click"""
        from views.main_view import MainView
        from views.dashboard_view import DashboardPage
        from views.product_view import ProductPage
        from views.sales_view import SalesPage
        from views.report_view import ReportPage
        from views.customer_view import CustomerPage
        from views.dangxuat_view import LogoutPage

        self.view = MainView(self)

        # Đăng ký các trang
        admin_page_list = (DashboardPage, SalesPage, ProductPage, CustomerPage, ReportPage, LogoutPage)
        for PageClass in admin_page_list:
            page_name = PageClass.__name__
            frame = PageClass(parent=self.view.container, controller=self)
            self.pages[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # GÁN LỆNH CHO CÁC NÚT SIDEBAR ADMIN
        # (Lưu ý: Tên biến nút như btn_dash, btn_prod phải khớp với file main_view.py của bạn)
        if hasattr(self.view, 'btn_dash'): self.view.btn_dash.configure(
            command=lambda: self.show_frame("DashboardPage"))
        if hasattr(self.view, 'btn_sales'): self.view.btn_sales.configure(command=lambda: self.show_frame("SalesPage"))
        if hasattr(self.view, 'btn_prod'): self.view.btn_prod.configure(command=lambda: self.show_frame("ProductPage"))
        if hasattr(self.view, 'btn_cust'): self.view.btn_cust.configure(command=lambda: self.show_frame("CustomerPage"))
        if hasattr(self.view, 'btn_report'): self.view.btn_report.configure(
            command=lambda: self.show_frame("ReportPage"))
        if hasattr(self.view, 'btn_logout'): self.view.btn_logout.configure(command=self.logout_process)

        self.show_frame("DashboardPage")
        self.view.mainloop()

    def init_customer_ui(self):
        """Khởi tạo Khách hàng với đầy đủ các trang và gán lệnh Click"""
        from views_customer.main_customer_view import MainCustomerView
        from views_customer.shop_page import ShopPage
        from views_customer.cart_page import CartPage
        from views_customer.fav_page import FavPage
        from views_customer.profile_page import ProfilePage
        from views_customer.dangxuat_view import LogoutPage

        self.view = MainCustomerView(self)

        customer_page_list = (ShopPage, CartPage, FavPage, ProfilePage, LogoutPage)
        for PageClass in customer_page_list:
            page_name = PageClass.__name__
            frame = PageClass(parent=self.view.container, controller=self)
            self.pages[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # GÁN LỆNH CHO CÁC NÚT SIDEBAR KHÁCH HÀNG
        if hasattr(self.view, 'btn_shop'): self.view.btn_shop.configure(command=lambda: self.show_frame("ShopPage"))
        if hasattr(self.view, 'btn_cart'): self.view.btn_cart.configure(command=lambda: self.show_frame("CartPage"))
        if hasattr(self.view, 'btn_fav'): self.view.btn_fav.configure(command=lambda: self.show_frame("FavPage"))
        if hasattr(self.view, 'btn_profile'): self.view.btn_profile.configure(
            command=lambda: self.show_frame("ProfilePage"))
        if hasattr(self.view, 'btn_logout'): self.view.btn_logout.configure(command=self.logout_process)

        self.show_frame("ShopPage")
        self.view.mainloop()

    def show_frame(self, page_name):
        """Đưa trang được chọn lên phía trước"""
        page = self.pages.get(page_name)
        if page:
            page.tkraise()
            if page_name == "ProductPage":
                self.refresh_product_data()

    def refresh_product_data(self):
        if "ProductPage" in self.pages:
            all_products = self.model.get_all_products()
            self.pages["ProductPage"].update_table(all_products)

    def open_add_popup(self):
        """Tránh lỗi Attribute"""
        print("Mở popup thêm sản phẩm...")

    def logout_process(self):
        """Xử lý đăng xuất quay về Login sạch sẽ"""
        if messagebox.askyesno("Đăng xuất", "Bạn muốn đăng xuất khỏi hệ thống?"):
            if self.view:
                self.view.destroy()
            python = sys.executable
            os.execl(python, python, *sys.argv)


if __name__ == "__main__":
    app = MainController()