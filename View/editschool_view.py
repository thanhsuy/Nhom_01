from tkinter import messagebox

from PIL import Image
import customtkinter as ctk

from DataAccess.user_model import UserModel


class EditSchoolView:
    def __init__(self, root, controller):
        from Tmp.university import university
        from Tmp.user import userId

        self.root = root
        self.controller = controller
        self.dbUser = UserModel()

        # Thanh điều hướng trên cùng
        self.navbar = ctk.CTkFrame(root, height=50, corner_radius=0, fg_color="#444")
        self.navbar.pack(fill="x")

        buttons = ["Quản lý trường"]

        self.butXepHang = ctk.CTkButton(self.navbar, text=buttons[0], width=100, fg_color="orange", command=self.home)
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
        ctk.CTkLabel(self.content_frame, text="Trường học của bạn:", font=("Arial", 14, "bold")).grid(row=0, column=0,
                                                                                                      sticky="w",
                                                                                                      padx=10,
                                                                                                      pady=5)

        # Các thông tin cụ thể
        ctk.CTkLabel(self.content_frame, text="Tên trường", anchor="w", font=("Arial", 14, "bold")).grid(row=1,
                                                                                                         column=0,
                                                                                                         sticky="w",
                                                                                                         padx=10,
                                                                                                         pady=5)
        self.name_school_entry = ctk.CTkEntry(self.content_frame)
        self.name_school_entry.insert(ctk.END, university[1])
        self.name_school_entry.grid(row=1, column=1, columnspan=3, pady=5, padx=10, sticky="we")

        ctk.CTkLabel(self.content_frame, text="Quốc gia", anchor="w", font=("Arial", 14, "bold")).grid(row=2, column=0,
                                                                                                       sticky="w",
                                                                                                       padx=10,
                                                                                                       pady=5)
        self.country_school_entry = ctk.CTkEntry(self.content_frame)
        self.country_school_entry.insert(ctk.END, university[2])
        self.country_school_entry.grid(row=2, column=1, columnspan=1, pady=5, padx=10, sticky="w")

        ctk.CTkLabel(self.content_frame, text="Khu vực", anchor="w", font=("Arial", 14, "bold")).grid(row=2, column=2,
                                                                                                      sticky="w",
                                                                                                      padx=10,
                                                                                                      pady=5)
        self.location_school_entry = ctk.CTkEntry(self.content_frame)
        self.location_school_entry.insert(ctk.END, university[3])
        self.location_school_entry.grid(row=2, column=3, columnspan=1, pady=5, padx=10, sticky="w")

        ctk.CTkLabel(self.content_frame, text="Ảnh", anchor="w", font=("Arial", 14, "bold")).grid(row=3, column=0,
                                                                                                  sticky="w",
                                                                                                  padx=10,
                                                                                                  pady=5)
        self.image_entry = ctk.CTkEntry(self.content_frame)
        self.image_entry.grid(row=3, column=1, columnspan=3, pady=5, padx=10, sticky="we")

        # Mô tả
        ctk.CTkLabel(self.content_frame, text="Mô tả", font=("Arial", 14, "bold")).grid(row=4, column=0, sticky="w",
                                                                                        padx=10,
                                                                                        pady=5)
        self.description_entry = ctk.CTkEntry(self.content_frame)
        self.description_entry.insert(ctk.END, university[33])
        self.description_entry.grid(row=5, column=0, columnspan=4, pady=5, padx=10, sticky="ew")

        # Học phí và yêu cầu đầu vào
        ctk.CTkLabel(self.content_frame, text="Học phí", font=("Arial", 14, "bold")).grid(row=6, column=0, sticky="w",
                                                                                          padx=10,
                                                                                          pady=5)
        self.country_fee = ctk.CTkEntry(self.content_frame)
        if university[17]:
            self.country_fee.insert(ctk.END, university[17])
        self.country_fee.grid(row=7, column=0, sticky="ew", pady=5, padx=10)

        self.global_fee = ctk.CTkEntry(self.content_frame)
        if university[18]:
            self.global_fee.insert(ctk.END, university[17])
        self.global_fee.grid(row=7, column=1, sticky="ew", pady=5, padx=10)

        ctk.CTkLabel(self.content_frame, text="Yêu cầu đầu vào", font=("Arial", 14, "bold")).grid(row=6, column=2,
                                                                                                  sticky="w",
                                                                                                  padx=10, pady=5)
        self.SAT = ctk.CTkEntry(self.content_frame)
        if university[19]:
            self.SAT.insert(ctk.END, university[19])
        self.SAT.grid(row=7, column=2, sticky="ew", pady=5, padx=10)

        self.TOEFL = ctk.CTkEntry(self.content_frame)
        if university[20]:
            self.TOEFL.insert(ctk.END, university[20])
        self.TOEFL.grid(row=7, column=3, sticky="ew", pady=5, padx=10)

        # Mức độ tập trung chuyên ngành
        ctk.CTkLabel(self.content_frame, text="Mức độ tập trung", font=("Arial", 14, "bold")).grid(row=8,
                                                                                                   column=0,
                                                                                                   sticky="w",
                                                                                                   padx=10,
                                                                                                   pady=5)
        ctk.CTkLabel(self.content_frame, text="chuyên ngành:", font=("Arial", 14, "bold")).grid(row=9,
                                                                                                column=0,
                                                                                                sticky="w",
                                                                                                padx=10,
                                                                                                pady=0)
        self.focus_entry = ctk.CTkEntry(self.content_frame)
        if university[5] == "CO":
            self.focus_entry.insert(ctk.END, "Comprehensive")
        elif university[5] == "FC":
            self.focus_entry.insert(ctk.END, "Full Comprehensive")
        elif university[5] == "FO":
            self.focus_entry.insert(ctk.END, "Focused")
        elif university[5] == "SP":
            self.focus_entry.insert(ctk.END, "Specialist")
        self.focus_entry.grid(row=8, column=1, columnspan=2, pady=5, padx=10, rowspan=2, sticky="wesn")

        # Nút "Chỉnh sửa"
        edit_button = ctk.CTkButton(self.content_frame, text="Xác nhận", fg_color="orange", command=self.edit_info)
        edit_button.grid(row=10, column=1, columnspan=2, pady=15)

    def show(self):
        # Cập nhật giao diện nếu cần thiết
        pass

    def edit_info(self):
        from Tmp.user import userId

        name = self.name_school_entry.get()
        location = self.country_school_entry.get()
        region = self.location_school_entry.get()
        focus = self.focus_entry.get()
        if focus == "Comprehensive":
            focus = "CO"
        elif focus == "Full Comprehensive":
            focus = "FC"
        elif focus == "Focused":
            focus = "FO"
        elif focus == "Specialist":
            focus = "SP"
        else:
            focus = ""

        country_fee = self.country_fee.get()
        global_fee = self.global_fee.get()
        SAT = self.SAT.get()
        TOEFL = self.TOEFL.get()
        description = self.description_entry.get()
        image = self.image_entry.get()
        idUser = userId

        if not (country_fee.isnumeric() and global_fee.isnumeric() and SAT.isnumeric() and TOEFL.isnumeric()):
            messagebox.showerror("Lỗi", "Các trường nhập số sai định dạng!")

        self.controller.edit_university(name, location, region, focus,
                                        country_fee, global_fee, SAT, TOEFL, description, idUser, image)

    def logout(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        self.controller.logout()

    def home(self):
        self.controller.home()
