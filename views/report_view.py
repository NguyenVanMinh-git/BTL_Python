import customtkinter as ctk


class ReportPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, fg_color="#f1f5f9", corner_radius=0)

        # --- Header ---
        header = ctk.CTkFrame(self, fg_color="white", height=80, corner_radius=0)
        header.pack(fill="x", pady=(0, 20))
        ctk.CTkLabel(header, text="📈 BÁO CÁO DOANH THU", font=("Arial", 22, "bold")).pack(side="left", padx=40)

        # --- Bộ lọc thời gian ---
        filter_frame = ctk.CTkFrame(self, fg_color="transparent")
        filter_frame.pack(fill="x", padx=30, pady=10)
        ctk.CTkSegmentedButton(filter_frame, values=["Hôm nay", "Tuần này", "Tháng này", "Năm nay"]).pack(side="left")

        # --- Thẻ báo cáo chi tiết ---
        cards_frame = ctk.CTkFrame(self, fg_color="transparent")
        cards_frame.pack(fill="x", padx=30, pady=10)
        cards_frame.grid_columnconfigure((0, 1, 2), weight=1)

        self.create_report_card(cards_frame, 0, "LỢI NHUẬN GỘP", "125,000,000đ", "#10b981", "📈 +12%")
        self.create_report_card(cards_frame, 1, "CHI PHÍ VẬN HÀNH", "45,000,000đ", "#f43f5e", "📉 -5%")
        self.create_report_card(cards_frame, 2, "GIÁ TRỊ TB ĐƠN", "1,200,000đ", "#f59e0b", "✨ Ổn định")

        # --- Khu vực biểu đồ và Top sản phẩm ---
        bottom_frame = ctk.CTkFrame(self, fg_color="transparent")
        bottom_frame.pack(fill="both", expand=True, padx=30, pady=20)
        bottom_frame.grid_columnconfigure(0, weight=2)
        bottom_frame.grid_columnconfigure(1, weight=1)

        # Giả lập Top sản phẩm bán chạy
        top_selling = ctk.CTkFrame(bottom_frame, fg_color="white", corner_radius=15)
        top_selling.grid(row=0, column=1, sticky="nsew", padx=10)
        ctk.CTkLabel(top_selling, text="Top Sản Phẩm Bán Chạy", font=("Arial", 14, "bold")).pack(pady=15)

        for i in range(5):
            item = ctk.CTkFrame(top_selling, fg_color="#f8fafc", height=40, corner_radius=8)
            item.pack(fill="x", padx=15, pady=5)
            ctk.CTkLabel(item, text=f"Top {i + 1}: Áo thun Polo Classy").pack(side="left", padx=10)

    def create_report_card(self, parent, col, title, val, color, subtext):
        card = ctk.CTkFrame(parent, fg_color="white", corner_radius=15, height=150)
        card.grid(row=0, column=col, padx=10, sticky="nsew")

        ctk.CTkLabel(card, text=title, font=("Arial", 12, "bold"), text_color="gray").pack(pady=(20, 5))
        ctk.CTkLabel(card, text=val, font=("Arial", 24, "bold"), text_color="#1e293b").pack()
        ctk.CTkLabel(card, text=subtext, font=("Arial", 12), text_color=color).pack(pady=5)