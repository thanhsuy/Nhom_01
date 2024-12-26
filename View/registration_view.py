import customtkinter as ctk
from tkinter import messagebox

class RegistrationView:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller

        # Tạo khung nền (background frame)
        frame_background = ctk.CTkFrame(
            master=self.root,
            fg_color="white",  # Màu xám nền
            corner_radius=0
        )
        frame_background.pack(fill="both", expand=True)

        menu_frame = ctk.CTkFrame(
            master=frame_background,
            fg_color="#454545",  # Màu xám đậm
            corner_radius=0,
            height=10
        )
        menu_frame.pack(fill="both", expand=True)

        # Nút "Trang chủ"
        home_button = ctk.CTkButton(
            master=menu_frame,
            text="Trang chủ",
            text_color="white",
            fg_color="#f7941d",  # Màu cam
            hover_color="#f6a549",  # Màu cam nhạt khi hover
            corner_radius=10,
            width=100,
            height=40,
            font=("Arial", 14, "bold"),
            command=self.home
        )
        home_button.place(x=10, y=10)

        # Tạo khung chính giữa (main frame)
        frame_main = ctk.CTkFrame(
            master=frame_background,
            width=720,
            height=450,
            fg_color="white",  # Màu trắng của khung chính
            corner_radius=15
        )
        frame_main.pack()

        # Tọa độ ban đầu cho các nhãn và entry
        label_x = 70
        entry_x = 220
        y_spacing = 60  # Giảm khoảng cách giữa các dòng
        current_y = 30

        # Nhãn và Entry "Tên đăng nhập"
        username_label = ctk.CTkLabel(
            master=frame_main,
            text="Tên đăng nhập:",
            text_color="#454545",
            font=("Arial", 12, "bold")  # Font nhỏ hơn
        )
        username_label.place(x=label_x, y=current_y)

        self.username_entry = ctk.CTkEntry(
            master=frame_main,
            width=350,
            height=30,  # Chiều cao nhỏ hơn
            placeholder_text="Nhập tên đăng nhập",
            border_color="#dcdcdc",
            corner_radius=5
        )
        self.username_entry.place(x=entry_x, y=current_y)

        # Nhãn và Entry "Mật khẩu"
        current_y += y_spacing
        password_label = ctk.CTkLabel(
            master=frame_main,
            text="Mật khẩu:",
            text_color="#454545",
            font=("Arial", 12, "bold")  # Font nhỏ hơn
        )
        password_label.place(x=label_x, y=current_y)

        self.password_entry = ctk.CTkEntry(
            master=frame_main,
            width=350,
            height=30,  # Chiều cao nhỏ hơn
            placeholder_text="Nhập mật khẩu",
            border_color="#dcdcdc",
            corner_radius=5,
            show="*"
        )
        self.password_entry.place(x=entry_x, y=current_y)

        # Nhãn và Entry "Email"
        current_y += y_spacing
        email_label = ctk.CTkLabel(
            master=frame_main,
            text="Email:",
            text_color="#454545",
            font=("Arial", 12, "bold")  # Font nhỏ hơn
        )
        email_label.place(x=label_x, y=current_y)

        self.email_entry = ctk.CTkEntry(
            master=frame_main,
            width=350,
            height=30,  # Chiều cao nhỏ hơn
            placeholder_text="Nhập email",
            border_color="#dcdcdc",
            corner_radius=5
        )
        self.email_entry.place(x=entry_x, y=current_y)

        # Dòng cho RadioButton
        current_y += y_spacing
        radio_label = ctk.CTkLabel(
            master=frame_main,
            text="Loại tài khoản:",
            text_color="#454545",
            font=("Arial", 12, "bold")  # Font nhỏ hơn
        )
        radio_label.place(x=label_x, y=current_y)

        self.gender_var = ctk.StringVar(value="Nam")  # Biến lưu trạng thái
        radio_SV = ctk.CTkRadioButton(
            master=frame_main,
            text="Học sinh",
            variable=self.gender_var,
            value="Học sinh",
            text_color="#454545",
            font=("Arial", 12, "bold"),
            command=self.toggle_student_fields
        )
        radio_QL = ctk.CTkRadioButton(
            master=frame_main,
            text="Quản lý",
            variable=self.gender_var,
            value="Quản lý",
            text_color="#454545",
            font=("Arial", 12, "bold"),
            command=self.toggle_student_fields
        )

        radio_DG = ctk.CTkRadioButton(
            master=frame_main,
            text="Đánh giá viên",
            variable=self.gender_var,
            value="Đánh giá viên",
            text_color="#454545",
            font=("Arial", 12, "bold"),
            command=self.toggle_student_fields
        )

        radio_SV.place(x=entry_x, y=current_y)
        radio_QL.place(x=entry_x + 100, y=current_y)
        radio_DG.place(x=entry_x + 200, y=current_y)

        # Nhãn và Entry "Nơi ở"
        current_y += y_spacing
        self.location_label = ctk.CTkLabel(
            master=frame_main,
            text="Nơi ở:",
            text_color="#454545",
            font=("Arial", 12, "bold")  # Font nhỏ hơn
        )
        self.location_label.place(x=label_x, y=current_y)

        self.location_entry = ctk.CTkEntry(
            master=frame_main,
            width=350,
            height=30,  # Chiều cao nhỏ hơn
            placeholder_text="Nhập nơi ở",
            border_color="#dcdcdc",
            corner_radius=5
        )
        self.location_entry.place(x=entry_x, y=current_y)

        # Nhãn và Entry "SAT"
        current_y += y_spacing

        self.sat_label = ctk.CTkLabel(
            master=frame_main,
            text="SAT:",
            text_color="#454545",
            font=("Arial", 12, "bold")  # Font nhỏ hơn
        )
        self.sat_label.place(x=label_x, y=current_y)

        self.sat_entry = ctk.CTkEntry(
            master=frame_main,
            width=150,
            height=30,  # Chiều cao nhỏ hơn
            placeholder_text="Điểm SAT",
            border_color="#dcdcdc",
            corner_radius=5
        )
        self.sat_entry.place(x=entry_x, y=current_y)

        # Nhãn và Entry "TOEFL"
        self.toefl_label = ctk.CTkLabel(
            master=frame_main,
            text="TOEFL:",
            text_color="#454545",
            font=("Arial", 12, "bold")  # Font nhỏ hơn
        )
        self.toefl_label.place(x=label_x + 300, y=current_y)

        self.toefl_entry = ctk.CTkEntry(
            master=frame_main,
            width=150,
            height=30,  # Chiều cao nhỏ hơn
            placeholder_text="Điểm TOEFL",
            border_color="#dcdcdc",
            corner_radius=5
        )
        self.toefl_entry.place(x=entry_x + 200, y=current_y)

        # Nút "Đăng ký"
        register_button = ctk.CTkButton(
            master=frame_main,
            text="Đăng ký",
            text_color="white",
            fg_color="#f7941d",  # Màu cam
            hover_color="#f6a549",  # Màu cam nhạt khi hover
            corner_radius=10,
            width=120,
            height=40,
            font=("Arial", 14, "bold"),
            command=self.register
        )
        register_button.place(relx=0.5, rely=0.9, anchor="center")

    def register(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        email = self.email_entry.get()
        typeUser = self.gender_var.get()
        location = self.location_entry.get()
        SAT = self.sat_entry.get()
        TOEFL = self.toefl_entry.get()
        if typeUser == "Học sinh":
            if not SAT.isnumeric():
                messagebox.showerror("Dang ky that bai", "SAT khong nhap dung dinh dang")
                return
            if not TOEFL.isnumeric():
                messagebox.showerror("Dang ky that bai", "TOEFL khong nhap dung dinh dang")
                return
        if self.controller.check_username(username):
            messagebox.showerror("Dang ky that bai", "Da ton tai username nay")
            return
        if not self.controller.register_user(username, password, email, typeUser, location, SAT, TOEFL):
            messagebox.showerror("Dang ky that bai", "Co loi khi dang ky")
            return
        # Xử lý logic đăng ký tại đây
        pass

    def show(self):
        # Hiển thị thông báo nếu cần (có thể mở rộng)
        pass

    def home(self):
        self.controller.home()

    def toggle_student_fields(self):
        # Hiển thị hoặc ẩn các ô liên quan đến "Học sinh"
        if self.gender_var.get() == "Học sinh":
            self.sat_entry.place(x=220, y=330)
            self.toefl_entry.place(x=420, y=330)
            self.location_entry.place(x=220, y=270)
            self.location_label.place(x=70, y=270)
            self.toefl_label.place(x=370, y=330)
            self.sat_label.place(x=70, y=330)
        else:
            self.location_entry.place_forget()
            self.location_label.place_forget()
            self.toefl_label.place_forget()
            self.sat_label.place_forget()
            self.sat_entry.place_forget()
            self.toefl_entry.place_forget()
