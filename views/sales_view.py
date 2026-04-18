import customtkinter as ctk
from tkinter import ttk


class SalesPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, fg_color="#f1f5f9", corner_radius=0)

        # --- Cấu hình Grid ---
        self.grid_columnconfigure(0, weight=3)  # Cột sản phẩm
        self.grid_columnconfigure(1, weight=2)  # Cột hóa đơn
        self.grid_rowconfigure(0, weight=1)

        # === BÊN TRÁI: DANH SÁCH SẢN PHẨM ===
        left_panel = ctk.CTkFrame(self, fg_color="transparent")
        left_panel.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

        # Thanh tìm kiếm nhanh sản phẩm
        search_box = ctk.CTkEntry(left_panel, placeholder_text="🔍 Nhập tên hoặc quét mã vạch...",
                                  height=45, corner_radius=10)
        search_box.pack(fill="x", pady=(0, 15))

        # Khu vực hiển thị sản phẩm (Dạng bảng hoặc Grid)
        prod_container = ctk.CTkFrame(left_panel, fg_color="white", corner_radius=15)
        prod_container.pack(fill="both", expand=True)

        cols = ("ID", "Name", "Price", "Stock")
        self.tree_prod = ttk.Treeview(prod_container, columns=cols, show="headings")
        for col in cols: self.tree_prod.heading(col, text=col)
        self.tree_prod.pack(fill="both", expand=True, padx=15, pady=15)

        # === BÊN PHẢI: GIỎ HÀNG & THANH TOÁN ===
        right_panel = ctk.CTkFrame(self, fg_color="white", corner_radius=0)
        right_panel.grid(row=0, column=1, sticky="nsew")

        ctk.CTkLabel(right_panel, text="🛒 GIỎ HÀNG", font=("Arial", 20, "bold")).pack(pady=20)

        # Bảng giỏ hàng nhỏ gọn
        cart_container = ctk.CTkFrame(right_panel, fg_color="transparent")
        cart_container.pack(fill="both", expand=True, padx=20)

        # Khu vực tổng tiền
        summary_frame = ctk.CTkFrame(right_panel, fg_color="#f8fafc", height=200, corner_radius=15)
        summary_frame.pack(fill="x", padx=20, pady=20)

        ctk.CTkLabel(summary_frame, text="Tổng cộng:", font=("Arial", 14)).place(x=20, y=20)
        ctk.CTkLabel(summary_frame, text="450,000đ", font=("Arial", 24, "bold"), text_color="#3b82f6").place(x=20, y=50)

        btn_pay = ctk.CTkButton(right_panel, text="THANH TOÁN (F12)", fg_color="#10b981",
                                hover_color="#059669", height=60, font=("Arial", 16, "bold"))
        btn_pay.pack(fill="x", padx=20, pady=(0, 20))