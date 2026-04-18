import customtkinter as ctk
from tkinter import filedialog
from PIL import Image


class ProductEntryWindow(ctk.CTkToplevel):
    def __init__(self, parent, callback, data=None):
        super().__init__(parent)
        self.title("Thông tin sản phẩm")
        self.geometry("400x550")
        self.callback = callback
        self.image_path = data[5] if data else ""

        # Giao diện Entry
        self.name_entry = ctk.CTkEntry(self, placeholder_text="Tên sản phẩm")
        self.name_entry.pack(pady=10, padx=20, fill="x")

        self.price_entry = ctk.CTkEntry(self, placeholder_text="Giá bán")
        self.price_entry.pack(pady=10, padx=20, fill="x")

        # Nút chọn ảnh
        self.btn_img = ctk.CTkButton(self, text="Chọn hình ảnh", command=self.upload_image)
        self.btn_img.pack(pady=10)

        # Nút Lưu
        self.btn_save = ctk.CTkButton(self, text="Lưu sản phẩm", fg_color="#10b981", command=self.save)
        self.btn_save.pack(pady=20)

        if data:  # Nếu là sửa, nạp dữ liệu cũ
            self.name_entry.insert(0, data[1])
            self.price_entry.insert(0, data[2])

    def upload_image(self):
        file = filedialog.askopenfilename(filetypes=[("Image Files", "*.png *.jpg *.jpeg")])
        if file:
            self.image_path = file

    def save(self):
        # Lấy dữ liệu và gửi về cho Controller qua callback
        data = (self.name_entry.get(), self.price_entry.get(), self.image_path)
        self.callback(data)
        self.destroy()