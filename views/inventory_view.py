import customtkinter as ctk
from tkinter import ttk


class InventoryPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, fg_color="#f1f5f9", corner_radius=0)

        # --- Header ---
        header = ctk.CTkFrame(self, fg_color="white", height=80, corner_radius=0)
        header.pack(fill="x", side="top", pady=(0, 20))
        ctk.CTkLabel(header, text="🏭 QUẢN LÝ KHO & VẬT TƯ",
                     font=ctk.CTkFont(size=22, weight="bold"), text_color="#1e293b").pack(side="left", padx=40)

        # --- Quick Stats Row (Thẻ chỉ số nhanh) ---
        stats_frame = ctk.CTkFrame(self, fg_color="transparent")
        stats_frame.pack(fill="x", padx=30, pady=10)
        stats_frame.grid_columnconfigure((0, 1, 2, 3), weight=1)

        self.create_stat_widget(stats_frame, 0, "TỔNG TỒN KHO", "14,250", "#3b82f6", "📦")
        self.create_stat_widget(stats_frame, 1, "SẮP HẾT HÀNG", "12", "#ef4444", "⚠️")
        self.create_stat_widget(stats_frame, 2, "GIÁ TRỊ KHO", "1.2B", "#10b981", "💰")
        self.create_stat_widget(stats_frame, 3, "NHẬP TRONG THÁNG", "+145", "#8b5cf6", "📥")

        # --- Main Table Area ---
        container = ctk.CTkFrame(self, fg_color="white", corner_radius=15)
        container.pack(fill="both", expand=True, padx=30, pady=20)

        # Bảng với Style hiện đại
        style = ttk.Style()
        style.configure("Inventory.Treeview", rowheight=40, font=("Segoe UI", 11))
        style.configure("Inventory.Treeview.Heading", font=("Segoe UI", 11, "bold"))

        cols = ("ID", "Name", "Category", "Stock", "Unit", "Status")
        self.tree = ttk.Treeview(container, columns=cols, show="headings", style="Inventory.Treeview")

        headers = ["MÃ LÔ", "TÊN SẢN PHẨM", "DANH MỤC", "SỐ LƯỢNG", "ĐƠN VỊ", "TÌNH TRẠNG"]
        for i, col in enumerate(cols):
            self.tree.heading(col, text=headers[i])
            self.tree.column(col, width=100, anchor="center")

        self.tree.pack(fill="both", expand=True, padx=20, pady=20)

    def create_stat_widget(self, parent, col, title, val, color, icon):
        card = ctk.CTkFrame(parent, fg_color="white", corner_radius=12, height=100)
        card.grid(row=0, column=col, padx=10, sticky="nsew")

        ctk.CTkLabel(card, text=icon, font=("Arial", 24)).place(x=20, y=20)
        ctk.CTkLabel(card, text=title, font=("Arial", 11, "bold"), text_color="gray").place(x=20, y=55)
        ctk.CTkLabel(card, text=val, font=("Arial", 20, "bold"), text_color=color).place(x=20, y=75)