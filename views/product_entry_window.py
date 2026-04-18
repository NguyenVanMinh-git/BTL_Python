import customtkinter as ctk
from tkinter import messagebox


class ProductEntryWindow(ctk.CTkToplevel):
    def __init__(self, parent, callback):
        super().__init__(parent)
        self.callback = callback  # Đây là cầu nối sang MainController

        self.title("Thêm sản phẩm")
        self.geometry("400x500")
        self.attributes("-topmost", True)
        self.grab_set()

        # Ô nhập liệu
        self.name_ent = ctk.CTkEntry(self, placeholder_text="Tên sản phẩm", width=250)
        self.name_ent.pack(pady=15)

        self.price_ent = ctk.CTkEntry(self, placeholder_text="Giá", width=250)
        self.price_ent.pack(pady=15)

        # Nút Lưu
        self.btn_save = ctk.CTkButton(self, text="LƯU LẠI", fg_color="#10b981", command=self._on_save_click)
        self.btn_save.pack(pady=20)

    def _on_save_click(self):
        # 1. Thu thập dữ liệu
        name = self.name_ent.get()
        price = self.price_ent.get()

        if not name or not price:
            messagebox.showwarning("Lỗi", "Vui lòng nhập đủ tên và giá!")
            return

        # 2. Đóng gói dữ liệu (6 cột như Database yêu cầu)
        data_to_save = (name, price, "L", 10, "Áo", "")

        # 3. Gửi dữ liệu qua callback về Controller
        self.callback(data_to_save)

        # 4. Đóng popup
        self.destroy()