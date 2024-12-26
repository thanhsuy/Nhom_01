from PIL import Image
import customtkinter as ctk

from DataAccess.university_model import UniversityModel
from DataAccess.user_model import UserModel


class NewHomeAdminView:
    def __init__(self, root, controller):
        from Tmp.user import userId
        from Tmp.university import set_university

        self.root = root
        self.controller = controller
        self.dbUser = UserModel()
        self.dbUniversity = UniversityModel()

        university = self.dbUniversity.get_universities_by_user(userId)
        set_university(university)

        # Thanh điều hướng trên cùng
        self.navbar = ctk.CTkFrame(root, height=50, corner_radius=0, fg_color="#444")
        self.navbar.pack(fill="x")

        buttons = ["Quản lý trường học"]

        self.butXepHang = ctk.CTkButton(self.navbar, text=buttons[0], width=100, fg_color="orange")
        self.butXepHang.pack(side="left", padx=10)

        self.butLogout = ctk.CTkButton(self.navbar, text="Đăng xuất", width=80, fg_color="orange", command=self.logout)
        self.butLogout.pack(side="right", padx=5)

        username = self.dbUser.get_username(userId)
        self.usernameLabel = ctk.CTkLabel(self.navbar, text=f"Xin chào {username}", width=80, fg_color="#444",
                                          text_color="white")
        self.usernameLabel.pack(side="right", padx=5)

        # Khu vực nội dung
        self.content_frame = ctk.CTkFrame(root, fg_color="#E0E0E0", corner_radius=10)
        self.content_frame.pack(fill="both", expand=True, pady=10, padx=10)

        # Thông tin trường học
        ctk.CTkLabel(
            self.content_frame,
            text="Bạn không quản lý trường nào? Thêm trường ngay!",
            font=("Arial", 18, "bold"),
            anchor="w",
        ).pack(pady=20)

        add_button = ctk.CTkButton(
            self.content_frame, text="Thêm trường", fg_color="orange", command=self.edit_info
        )
        add_button.pack()

    def show(self):
        # Cập nhật giao diện nếu cần thiết
        pass

    def edit_info(self):
        self.controller.add_university()

    def logout(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        self.controller.logout()
