import customtkinter as ctk
from tkinter import messagebox


class LoginView(ctk.CTk):
    def __init__(self, on_login_success):
        super().__init__()
        self.on_login_success = on_login_success

        self.title("HỆ THỐNG QUẢN LÝ")
        self.geometry("450x600")
        self.resizable(False, False)
        self.configure(fg_color="#f8fafc")  # Màu nền xám nhạt cực nhẹ

        # Căn giữa màn hình
        self.update_idletasks()
        x = (self.winfo_screenwidth() // 2) - (450 // 2)
        y = (self.winfo_screenheight() // 2) - (600 // 2)
        self.geometry(f"+{x}+{y}")

        # --- Card Đăng Nhập ---
        self.main_frame = ctk.CTkFrame(self, fg_color="white", corner_radius=25, border_width=1, border_color="#e2e8f0")
        self.main_frame.pack(fill="both", expand=True, padx=30, pady=30)

        # Icon khóa (Dùng icon đơn giản, chuyên nghiệp)
        self.icon_label = ctk.CTkLabel(self.main_frame, text="👤", font=("Arial", 70))
        self.icon_label.pack(pady=(45, 10))

        # Tiêu đề Đăng Nhập
        self.title_label = ctk.CTkLabel(self.main_frame, text="ĐĂNG NHẬP",
                                        font=ctk.CTkFont(size=26, weight="bold"),
                                        text_color="#0f172a")
        self.title_label.pack(pady=5)

        self.subtitle_label = ctk.CTkLabel(self.main_frame, text="Chào mừng bạn quay trở lại",
                                           font=("Arial", 13), text_color="#64748b")
        self.subtitle_label.pack(pady=(0, 35))

        # --- Ô Nhập Tài Khoản ---
        # Label nhỏ phía trên ô nhập (Tạo cảm giác chuyên nghiệp)
        self.user_lbl = ctk.CTkLabel(self.main_frame, text="Tên đăng nhập", font=("Arial", 12, "bold"),
                                     text_color="#1e293b")
        self.user_lbl.pack(anchor="w", padx=45)

        self.user_entry = ctk.CTkEntry(self.main_frame, placeholder_text="Nhập tài khoản của bạn...",
                                       width=320, height=45, corner_radius=10,
                                       fg_color="#f1f5f9", border_color="#cbd5e1")
        self.user_entry.pack(pady=(5, 20))

        # --- Ô Nhập Mật Khẩu ---
        self.pass_lbl = ctk.CTkLabel(self.main_frame, text="Mật khẩu", font=("Arial", 12, "bold"), text_color="#1e293b")
        self.pass_lbl.pack(anchor="w", padx=45)

        self.pass_entry = ctk.CTkEntry(self.main_frame, placeholder_text="Nhập mật khẩu...",
                                       show="*", width=320, height=45, corner_radius=10,
                                       fg_color="#f1f5f9", border_color="#cbd5e1")
        self.pass_entry.pack(pady=(5, 30))

        # --- Nút Đăng Nhập ---
        self.btn_login = ctk.CTkButton(self.main_frame, text="ĐĂNG NHẬP HỆ THỐNG",
                                       fg_color="#2563eb", hover_color="#1d4ed8",
                                       width=320, height=50, corner_radius=10,
                                       font=ctk.CTkFont(size=14, weight="bold"),
                                       command=self.handle_login)
        self.btn_login.pack(pady=10)

    def handle_login(self):
        username = self.user_entry.get().strip()
        password = self.pass_entry.get().strip()

        # Cấu trúc điều kiện mở rộng: Bạn có thể thêm nhiều tài khoản tại đây
        if username == "admin" and password == "123456":
            self.destroy()
            self.on_login_success()
        elif username == "khachhang" and password == "123":
            # Sau này bạn có thể tạo hàm on_customer_success() riêng tại đây
            messagebox.showinfo("Thông báo", "Chức năng dành cho Khách hàng đang phát triển!")
        elif not username or not password:
            messagebox.showwarning("Chú ý", "Vui lòng nhập đầy đủ thông tin!")
        else:
            messagebox.showerror("Lỗi", "Tên đăng nhập hoặc mật khẩu không đúng!")