import customtkinter as ctk
from tkinter import ttk


class CustomerPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, fg_color="#f1f5f9", corner_radius=0)

        # --- Header ---
        header = ctk.CTkFrame(self, fg_color="white", height=80, corner_radius=0)
        header.pack(fill="x", side="top", pady=(0, 20))

        ctk.CTkLabel(header, text="👥 QUẢN LÝ KHÁCH HÀNG",
                     font=ctk.CTkFont(size=22, weight="bold"), text_color="#1e293b").pack(side="left", padx=40)

        self.btn_add = ctk.CTkButton(header, text="+ Thêm Khách Hàng", fg_color="#6366f1",
                                     hover_color="#4f46e5", corner_radius=8, font=("Arial", 13, "bold"))
        self.btn_add.pack(side="right", padx=40)

        # --- Search Bar & Filter ---
        filter_frame = ctk.CTkFrame(self, fg_color="transparent")
        filter_frame.pack(fill="x", padx=30, pady=10)

        self.search_entry = ctk.CTkEntry(filter_frame, placeholder_text="🔍 Tìm tên, SĐT hoặc email...",
                                         width=400, height=40, corner_radius=10)
        self.search_entry.pack(side="left", padx=10)

        self.rank_filter = ctk.CTkComboBox(filter_frame, values=["Tất cả hạng", "Kim cương", "Vàng", "Bạc"],
                                           width=150, height=40, corner_radius=10)
        self.rank_filter.pack(side="left", padx=10)

        # --- Customer Table ---
        container = ctk.CTkFrame(self, fg_color="white", corner_radius=15)
        container.pack(fill="both", expand=True, padx=30, pady=(10, 30))

        cols = ("ID", "Name", "Phone", "Email", "Points", "Rank")
        self.tree = ttk.Treeview(container, columns=cols, show="headings")

        headers = ["MÃ KH", "HỌ VÀ TÊN", "SỐ ĐIỆN THOẠI", "EMAIL", "ĐIỂM TÍCH LŨY", "HẠNG THÀNH VIÊN"]
        for i, col in enumerate(cols):
            self.tree.heading(col, text=headers[i])
            self.tree.column(col, width=120, anchor="center")

        self.tree.pack(fill="both", expand=True, padx=20, pady=20)