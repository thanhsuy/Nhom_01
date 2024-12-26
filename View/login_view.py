import customtkinter as ctk


class LoginView:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller

        # Tạo khung nền
        frame_background = ctk.CTkFrame(master=self.root, fg_color="#3a3a3a", corner_radius=0, height=512)
        frame_background.pack(fill="both", expand=True)

        # Nút "Trang chủ"
        home_button = ctk.CTkButton(
            master=frame_background,
            text="Trang chủ",
            text_color="white",
            fg_color="#f7941d",
            hover_color="#f6a549",
            corner_radius=10,
            width=100,
            height=40,
            font=("Arial", 14),
            command=self.home
        )
        home_button.place(x=10, y=10)

        # Tạo khung chính giữa
        frame_main = ctk.CTkFrame(
            master=frame_background,
            width=350,
            height=250,
            fg_color="white",
            border_width=2,
            border_color="#f7941d",
            corner_radius=15
        )
        frame_main.place(relx=0.5, rely=0.5, anchor="center")

        # Tạo nhãn "Tên đăng nhập"
        username_label = ctk.CTkLabel(
            master=frame_main,
            text="Tên đăng nhập",
            text_color="black",
            font=("Arial", 14)
        )
        username_label.place(x=20, y=30)

        # Tạo entry "Tên đăng nhập"
        self.username_entry = ctk.CTkEntry(
            master=frame_main,
            width=300,
            height=35,
            placeholder_text="Nhập tên đăng nhập",
            border_color="#dcdcdc",
            corner_radius=5
        )
        self.username_entry.place(x=20, y=60)

        # Tạo nhãn "Mật khẩu"
        password_label = ctk.CTkLabel(
            master=frame_main,
            text="Mật khẩu",
            text_color="black",
            font=("Arial", 14)
        )
        password_label.place(x=20, y=110)

        # Tạo entry "Mật khẩu"
        self.password_entry = ctk.CTkEntry(
            master=frame_main,
            width=300,
            height=35,
            placeholder_text="Nhập mật khẩu",
            border_color="#dcdcdc",
            corner_radius=5,
            show="*"
        )
        self.password_entry.place(x=20, y=140)

        # Tạo nút "Đăng nhập"
        login_button = ctk.CTkButton(
            master=frame_main,
            text="Đăng nhập",
            text_color="white",
            fg_color="#f7941d",
            hover_color="#f6a549",
            corner_radius=10,
            width=150,
            height=40,
            font=("Arial", 14),
            command=self.login
        )
        login_button.place(relx=0.5, rely=0.85, anchor="center")

        # Thông báo
        self.message_label = ctk.CTkLabel(frame_background, text="", text_color="red", font=("Arial", 12))
        self.message_label.pack()

    def show(self):
        # Hiển thị thông báo nếu cần (có thể mở rộng)
        pass

    def home(self):
        self.controller.home()

    def login(self):
        # Lấy dữ liệu từ các entry
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Gửi dữ liệu đến controller để xử lý
        if not self.controller.validate_login(username, password):
            print("Sai")
            self.message_label.configure(text="Tên đăng nhập hoặc mật khẩu sai!", text_color="red")

