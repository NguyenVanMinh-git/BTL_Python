import customtkinter as ctk


class MainView(ctk.CTk):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.title("MINH TRÍ STORE - ERP System")
        self.geometry("1400x850")

        # --- Sidebar ---
        self.sidebar = ctk.CTkFrame(self, width=260, corner_radius=0, fg_color="#1e293b")
        self.sidebar.pack(side="left", fill="y")

        # Logo
        ctk.CTkLabel(self.sidebar, text="👕 QUA RANG",
                     font=ctk.CTkFont(size=26, weight="bold"),
                     text_color="#f8fafc").pack(pady=(40, 50))

        # Menu điều hướng - Thêm nút Đăng xuất vào danh sách này
        self.btn_dash = self.create_nav_btn("📊  Dashboard", "DashboardPage")
        self.btn_sales = self.create_nav_btn("💰  Bán hàng", "SalesPage")
        self.btn_prod = self.create_nav_btn("📦  Sản phẩm", "ProductPage")
        self.btn_inv = self.create_nav_btn("🏭  Kho hàng", "InventoryPage")
        self.btn_cust = self.create_nav_btn("👥  Khách hàng", "CustomerPage")
        self.btn_report = self.create_nav_btn("📈  Báo cáo", "ReportPage")

        # Nút Đăng xuất (Nằm trong danh sách menu để chắc chắn nhìn thấy)
        self.btn_logout = self.create_nav_btn("🚪  Đăng xuất", "LogoutPage")
        self.btn_logout.configure(text_color="#fb7185")  # Đổi màu chữ sang đỏ/hồng để nổi bật

        # --- Main Content Area ---
        self.container = ctk.CTkFrame(self, fg_color="#f1f5f9", corner_radius=0)
        self.container.pack(side="right", fill="both", expand=True)

    def create_nav_btn(self, text, page_name):
        btn = ctk.CTkButton(self.sidebar, text=text, fg_color="transparent",
                            text_color="#cbd5e1", hover_color="#334155",
                            height=50, anchor="w", corner_radius=10,
                            font=ctk.CTkFont(size=15, weight="bold"),
                            command=lambda: self.controller.show_frame(page_name))
        btn.pack(fill="x", padx=15, pady=8)
        return btn