import customtkinter as ctk


class DashboardPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        # Sử dụng màu nền xám nhạt (Light Slate) để làm nổi bật các khối trắng
        super().__init__(parent, fg_color="#f1f5f9", corner_radius=0)

        # --- 1. HEADER CHUYÊN NGHIỆP ---
        self.header_frame = ctk.CTkFrame(self, fg_color="white", height=80, corner_radius=0)
        self.header_frame.pack(fill="x", side="top")

        ctk.CTkLabel(self.header_frame, text="📊 TỔNG QUAN HỆ THỐNG",
                     font=ctk.CTkFont(size=22, weight="bold"),
                     text_color="#1e293b").pack(side="left", padx=40)

        # --- 2. STATS CARDS (THẺ THỐNG KÊ CÓ MÀU) ---
        self.cards_container = ctk.CTkFrame(self, fg_color="transparent")
        self.cards_container.pack(fill="x", padx=30, pady=25)
        self.cards_container.grid_columnconfigure((0, 1, 2, 3), weight=1)

        # Định nghĩa các thẻ với màu sắc hiện đại
        # create_premium_card(cột, tiêu đề, giá trị, màu chủ đạo, icon)
        self.create_premium_card(0, "TỔNG DOANH THU", "45,200,000đ", "#3b82f6", "💰")
        self.create_premium_card(1, "ĐƠN HÀNG MỚI", "128", "#10b981", "📦")
        self.create_premium_card(2, "KHÁCH HÀNG", "1,042", "#8b5cf6", "👥")
        self.create_premium_card(3, "SẢN PHẨM SẮP HẾT", "15", "#ef4444", "⚠️")

        # --- 3. KHU VỰC CHI TIẾT (BIỂU ĐỒ & THÔNG BÁO) ---
        self.detail_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.detail_frame.pack(fill="both", expand=True, padx=30, pady=(0, 30))
        self.detail_frame.grid_columnconfigure(0, weight=2)
        self.detail_frame.grid_columnconfigure(1, weight=1)

        # Biểu đồ giả lập (Bên trái)
        chart_box = ctk.CTkFrame(self.detail_frame, fg_color="white", corner_radius=15)
        chart_box.grid(row=0, column=0, padx=10, sticky="nsew")
        ctk.CTkLabel(chart_box, text="Biểu đồ doanh thu 7 ngày qua", font=("Arial", 16, "bold")).pack(pady=20)

        # Giả lập các cột biểu đồ
        graph_area = ctk.CTkFrame(chart_box, fg_color="transparent")
        graph_area.pack(fill="both", expand=True, padx=20, pady=20)
        for i in range(7):
            h = [0.4, 0.7, 0.5, 0.9, 0.6, 0.8, 0.5][i]
            bar = ctk.CTkFrame(graph_area, fg_color="#e2e8f0", width=40, corner_radius=4)
            bar.place(relx=0.1 + (i * 0.12), rely=1.0, relheight=h, anchor="sw")
            # Cột cuối cùng làm nổi bật bằng màu xanh
            if i == 6: bar.configure(fg_color="#3b82f6")

        # Thông báo hệ thống (Bên phải)
        noti_box = ctk.CTkFrame(self.detail_frame, fg_color="white", corner_radius=15)
        noti_box.grid(row=0, column=1, padx=10, sticky="nsew")
        ctk.CTkLabel(noti_box, text="Thông báo hệ thống", font=("Arial", 16, "bold")).pack(pady=20)

        activities = [("Đơn hàng #1024 vừa thanh toán", "check"), ("SP 'Áo thun' đã nhập thêm 50 chiếc", "box"),
                      ("Cảnh báo: Mã SP003 sắp hết hàng", "warn")]
        for text, icon_type in activities:
            row = ctk.CTkFrame(noti_box, fg_color="#f8fafc", height=45, corner_radius=8)
            row.pack(fill="x", padx=15, pady=5)
            ctk.CTkLabel(row, text=text, font=("Arial", 12)).pack(side="left", padx=10)

    def create_premium_card(self, col, title, value, color, icon):
        # Thẻ trắng có viền màu ở bên trái để nhìn chuyên nghiệp
        card = ctk.CTkFrame(self.cards_container, fg_color="white", height=140, corner_radius=15)
        card.grid(row=0, column=col, padx=10, pady=5, sticky="nsew")
        card.grid_propagate(False)

        # Dải màu nhấn bên trái thẻ
        accent_bar = ctk.CTkFrame(card, fg_color=color, width=5, corner_radius=0)
        accent_bar.place(x=0, y=0, relheight=1)

        # Nội dung bên trong thẻ
        ctk.CTkLabel(card, text=icon, font=("Arial", 28)).place(x=25, y=20)
        ctk.CTkLabel(card, text=title, text_color="gray", font=("Arial", 12, "bold")).place(x=25, y=65)
        ctk.CTkLabel(card, text=value, text_color=color, font=("Arial", 22, "bold")).place(x=25, y=95)