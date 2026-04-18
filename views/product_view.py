import customtkinter as ctk
from tkinter import ttk


class ProductPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        # Sử dụng nền xám nhạt để tạo chiều sâu cho các khối nội dung trắng
        super().__init__(parent, fg_color="#f1f5f9", corner_radius=0)
        self.controller = controller

        # --- 1. HEADER & ACTIONS ---
        self.header = ctk.CTkFrame(self, fg_color="white", height=100, corner_radius=0)
        self.header.pack(fill="x", side="top", pady=(0, 20))

        title_lbl = ctk.CTkLabel(self.header, text="📦 QUẢN LÝ KHO HÀNG",
                                 font=ctk.CTkFont(size=24, weight="bold"), text_color="#1e293b")
        title_lbl.pack(side="left", padx=40, pady=25)

        self.btn_add = ctk.CTkButton(self.header, text="+ Thêm Sản Phẩm Mới",
                                     fg_color="#10b981", hover_color="#059669",
                                     font=ctk.CTkFont(size=13, weight="bold"),
                                     height=40, corner_radius=8,
                                     command=self.controller.open_add_popup)
        self.btn_add.pack(side="right", padx=40)

        # --- 2. MAIN CONTENT AREA ---
        self.main_container = ctk.CTkFrame(self, fg_color="white", corner_radius=15)
        self.main_container.pack(fill="both", expand=True, padx=30, pady=(0, 30))

        # Thanh tìm kiếm & Lọc (Search & Filter Bar)
        self.filter_bar = ctk.CTkFrame(self.main_container, fg_color="transparent", height=60)
        self.filter_bar.pack(fill="x", padx=20, pady=20)

        self.search_entry = ctk.CTkEntry(self.filter_bar, placeholder_text="🔍 Tìm mã hoặc tên sản phẩm...",
                                         width=350, height=40, corner_radius=10, border_color="#e2e8f0")
        self.search_entry.pack(side="left", padx=10)

        self.category_filter = ctk.CTkComboBox(self.filter_bar, values=["Tất cả danh mục", "Áo", "Quần", "Phụ kiện"],
                                               width=180, height=40, corner_radius=10)
        self.category_filter.pack(side="left", padx=10)

        # --- 3. MODERN TREEVIEW (STYLING) ---
        style = ttk.Style()
        style.theme_use("default")

        # Cấu hình giao diện bảng
        style.configure("Treeview",
                        background="white",
                        foreground="#334155",
                        rowheight=45,
                        fieldbackground="white",
                        borderwith=0,
                        font=("Segoe UI", 11))

        # Cấu hình tiêu đề bảng
        style.configure("Treeview.Heading",
                        background="#f8fafc",
                        foreground="#64748b",
                        font=("Segoe UI", 12, "bold"),
                        relief="flat")

        style.map("Treeview", background=[('selected', '#eff6ff')], foreground=[('selected', '#2563eb')])

        # Tạo bảng
        columns = ("ID", "Name", "Price", "Size", "Stock", "Status")
        self.tree = ttk.Treeview(self.main_container, columns=columns, show="headings", selectmode="browse")

        # Định nghĩa tiêu đề và độ rộng cột
        headers = ["MÃ SP", "TÊN SẢN PHẨM", "GIÁ BÁN", "KÍCH CỠ", "TỒN KHO", "TRẠNG THÁI"]
        widths = [80, 250, 120, 100, 100, 150]

        for i, col in enumerate(columns):
            self.tree.heading(col, text=headers[i], anchor="w" if i == 1 else "center")
            self.tree.column(col, width=widths[i], anchor="w" if i == 1 else "center")

        self.tree.pack(fill="both", expand=True, padx=25, pady=(0, 25))

    def update_table(self, data):
        """Hàm cập nhật dữ liệu với hiệu ứng màu dòng xen kẽ"""
        for item in self.tree.get_children():
            self.tree.delete(item)

        for i, row in enumerate(data):
            tag = "evenrow" if i % 2 == 0 else "oddrow"

            # Chỉnh sửa hiển thị trạng thái chuyên nghiệp hơn
            # row[5] là trạng thái
            display_row = list(row)
            if "Còn hàng" in str(row[5]):
                display_row[5] = "● Còn hàng"
            elif "Hết hàng" in str(row[5]):
                display_row[5] = "○ Hết hàng"

            self.tree.insert("", "end", values=display_row, tags=(tag,))

        self.tree.tag_configure("evenrow", background="#ffffff")
        self.tree.tag_configure("oddrow", background="#f9fafb")  # Màu xám cực nhẹ cho dòng lẻ