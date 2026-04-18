import customtkinter as ctk

class LogoutPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, fg_color="#f1f5f9")
        self.controller = controller

        # Card xác nhận
        card = ctk.CTkFrame(self, fg_color="white", corner_radius=20, width=500, height=350)
        card.place(relx=0.5, rely=0.5, anchor="center")
        card.pack_propagate(False)

        ctk.CTkLabel(card, text="🚪", font=("Arial", 60)).pack(pady=(40, 10))
        ctk.CTkLabel(card, text="XÁC NHẬN ĐĂNG XUẤT", font=("Arial", 22, "bold")).pack(pady=10)
        ctk.CTkLabel(card, text="Bạn có muốn quay lại màn hình đăng nhập?", font=("Arial", 14), text_color="gray").pack()

        btn_frame = ctk.CTkFrame(card, fg_color="transparent")
        btn_frame.pack(pady=40)

        # Nút Thoát - Gọi hàm xử lý logout trong controller
        btn_exit = ctk.CTkButton(btn_frame, text="THOÁT NGAY",
                                 fg_color="#ef4444", hover_color="#dc2626",
                                 width=150, height=45, font=("Arial", 13, "bold"),
                                 command=self.controller.logout_process)
        btn_exit.pack(side="left", padx=10)

        # Nút Quay lại - Về Dashboard
        btn_back = ctk.CTkButton(btn_frame, text="QUAY LẠI",
                                 fg_color="#94a3b8", hover_color="#64748b",
                                 width=150, height=45, font=("Arial", 13, "bold"),
                                 command=lambda: self.controller.show_frame("DashboardPage"))
        btn_back.pack(side="left", padx=10)