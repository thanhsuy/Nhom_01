import customtkinter as ctk

from DataAccess.university_model import UniversityModel
from DataAccess.user_model import UserModel


# from tkinter import messagebox


class ChatBotView:
    def __init__(self, root, controller):
        from Tmp.user import userId
        self.root = root
        self.controller = controller
        self.dbUser = UserModel()
        self.dbUni = UniversityModel()
        self.uni_name = self.dbUni.get_name_universities()
        self.university1 = ()
        self.university2 = ()

        # Thanh điều hướng
        self.navbar = ctk.CTkFrame(root, height=50, corner_radius=0, fg_color="#444")
        self.navbar.pack(fill="x")

        # Nút điều hướng
        self.butXepHang = ctk.CTkButton(self.navbar, text="Xếp hạng", width=100, fg_color="#555", hover_color="#666",
                                        command=self.home)
        self.butXepHang.pack(side="left", padx=10)

        self.butSoSanh = ctk.CTkButton(self.navbar, text="So sánh", width=100, fg_color="#555", hover_color="#666",
                                       command=self.compare)
        self.butSoSanh.pack(side="left", padx=10)

        self.butChatBot = ctk.CTkButton(self.navbar, text="Chat bot", width=100, fg_color="orange", hover_color="#666")
        self.butChatBot.pack(side="left", padx=10)

        if userId == -1:

            self.butLogin = ctk.CTkButton(self.navbar, text="Đăng nhập", width=80, fg_color="orange",
                                          command=self.login)
            self.butLogin.pack(side="right", padx=5)

            self.butRegister = ctk.CTkButton(self.navbar, text="Đăng ký", width=80, fg_color="orange",
                                             command=self.regis)
            self.butRegister.pack(side="right", padx=5)

        else:
            self.butLogout = ctk.CTkButton(self.navbar, text="Đăng xuất", width=80,
                                           fg_color="orange", command=self.logout)
            self.butLogout.pack(side="right", padx=5)

            username = self.dbUser.get_username(userId)
            self.usernameLabel = ctk.CTkLabel(self.navbar, text=f"Xin chào {username}", width=80, fg_color="#444",
                                              text_color="white")
            self.usernameLabel.pack(side="right", padx=5)

        # Khu vực nội dung chính
        self.content_frame = ctk.CTkFrame(root, height=300, bg_color="gray")
        self.content_frame.pack(fill="both", expand=True, pady=10, padx=10)

        # Khung trên - Hộp văn bản (Text hệ thống)
        self.bot_frame = ctk.CTkFrame(self.content_frame)
        self.bot_frame.pack(fill="both", expand=True, padx=10, pady=(10, 5))

        self.textbox = ctk.CTkTextbox(
            self.bot_frame,
            height=150,
            wrap="word",
            state="normal",
            font=("Arial", 14, "bold"))
        self.textbox.pack(fill="both", expand=True, padx=5, pady=5)

        # Mặc định là nội dung của hệ thống
        self.textbox.insert("1.0", "Bot: Xin chào! Đây là văn bản của hệ thống...\n")
        self.textbox.configure(state="disabled")  # Chặn sửa từ người dùng

        # Khung dưới - Entry nhập văn bản (Người dùng)
        self.user_frame = ctk.CTkFrame(self.content_frame)
        self.user_frame.pack(fill="x", padx=10, pady=(5, 10))

        # Entry cho người dùng
        self.entry = ctk.CTkEntry(self.user_frame, placeholder_text="Câu trả lời của bạn")
        self.entry.pack(side="left", fill="x", expand=True, padx=(0, 5),
                        pady=5)  # Gắn vào bên trái, chiếm toàn bộ chiều ngang còn lại

        # Nút gửi
        self.send_button = ctk.CTkButton(self.user_frame, fg_color="orange", text="Gửi", command=self.send_message)
        self.send_button.pack(side="left", pady=5)

    def show(self):
        # Hiển thị thông báo nếu cần (có thể mở rộng)
        pass

    def send_message(self):
        # Xử lý khi nhấn nút "Gửi"
        user_message = self.entry.get()
        if user_message.strip():
            self.textbox.configure(state="normal")
            self.textbox.insert("end", f"---------------------------------------------------\n", "user")
            self.textbox.insert("end", f"Bạn: {user_message}\n", "user")
            self.textbox.insert("end", f"---------------------------------------------------\n", "user")
            bot_message = self.controller.return_message(user_message)
            self.textbox.insert("end", f"Bot: {bot_message}\n", "bot")
            self.textbox.configure(state="disabled")
            self.textbox.see("end")  # Cuộn xuống cuối
            self.entry.delete(0, "end")

    def logout(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        self.controller.logout()

    def home(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        self.controller.home()

    def compare(self):
        self.controller.compare_uni()

    def login(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        self.controller.login()

    def regis(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        self.controller.regis()
