from PIL import Image
import customtkinter as ctk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.ticker as ticker

from DataAccess.university_model import UniversityModel
from DataAccess.user_model import UserModel


class UniversityDetailView:
    def __init__(self, root, controller):
        from Tmp.user import userId
        from Tmp.university import university

        self.root = root
        self.controller = controller
        self.dbUser = UserModel()
        self.dbUniversity = UniversityModel()

        self.university = university
        try:
            image = Image.open(f"Image/{university[0]}.webp")
        except Exception:
            image = Image.open("Image/1.jpg")
        image = image.resize((150, 150))
        photo = ctk.CTkImage(light_image=image, dark_image=image, size=(150, 150))

        # Thanh điều hướng trên cùng
        self.navbar = ctk.CTkFrame(root, height=50, corner_radius=0, fg_color="#444")
        self.navbar.pack(fill="x")

        if userId != -1:
            buttons = ["Xếp hạng", "So sánh", "Chat bot"]

            self.butXepHang = ctk.CTkButton(self.navbar, text=buttons[0], width=100,
                                            fg_color="orange", hover_color="#666", command=self.home)
            self.butXepHang.pack(side="left", padx=10)

            self.butSoSanh = ctk.CTkButton(self.navbar, text=buttons[1], width=100,
                                           fg_color="#555", hover_color="#666", command=self.compare)
            self.butSoSanh.pack(side="left", padx=10)

            self.butChatBot = ctk.CTkButton(self.navbar, text=buttons[2], width=100, fg_color="#555",
                                            hover_color="#666", command=self.chatbot)
            self.butChatBot.pack(side="left", padx=10)

            self.butLogout = ctk.CTkButton(self.navbar, text="Đăng xuất", width=80,
                                           fg_color="orange", command=self.logout)
            self.butLogout.pack(side="right", padx=5)

            username = self.dbUser.get_username(userId)
            self.usernameLabel = ctk.CTkLabel(self.navbar, text=f"Xin chào {username}", width=80, fg_color="#444",
                                              text_color="white")
            self.usernameLabel.pack(side="right", padx=5)

        else:
            buttons = ["Xếp hạng", "So sánh", "Chat bot"]

            self.butXepHang = ctk.CTkButton(self.navbar, text=buttons[0], width=100,
                                            fg_color="orange", hover_color="#666", command=self.home)
            self.butXepHang.pack(side="left", padx=10)

            self.butSoSanh = ctk.CTkButton(self.navbar, text=buttons[1], width=100,
                                           fg_color="#555", hover_color="#666", command=self.compare)
            self.butSoSanh.pack(side="left", padx=10)

            self.butChatBot = ctk.CTkButton(self.navbar, text=buttons[2], width=100,
                                            fg_color="#555", hover_color="#666", command=self.chatbot)
            self.butChatBot.pack(side="left", padx=10)

            self.butLogin = ctk.CTkButton(self.navbar, text="Đăng nhập", width=80, fg_color="orange",
                                          command=self.login)
            self.butLogin.pack(side="right", padx=5)

            self.butRegister = ctk.CTkButton(self.navbar, text="Đăng ký", width=80, fg_color="orange",
                                             command=self.regis)
            self.butRegister.pack(side="right", padx=5)

        # Khu vực nội dung
        self.content_frame = ctk.CTkScrollableFrame(root, fg_color="#E0E0E0", corner_radius=10)
        self.content_frame.pack(fill="both", expand=True, pady=10, padx=10)

        # Thông tin trường học
        ctk.CTkLabel(
            self.content_frame,
            text="Trường học của bạn:",
            font=("Arial", 18, "bold"),
            anchor="w",
        ).grid(row=0, column=0, columnspan=2, sticky="w", padx=10, pady=10)

        # Ảnh trường học
        ctk.CTkLabel(self.content_frame, image=photo, text="").grid(
            row=1, column=0, rowspan=3, padx=10, pady=10, sticky="w"
        )

        self.entry_ten_truong = ctk.CTkEntry(self.content_frame)
        self.entry_ten_truong.insert(ctk.END, university[1])
        self.entry_ten_truong.configure(state="disabled")

        self.entry_quoc_gia = ctk.CTkEntry(self.content_frame)
        self.entry_quoc_gia.insert(ctk.END, university[2])
        self.entry_quoc_gia.configure(state="disabled")

        self.entry_khu_vuc = ctk.CTkEntry(self.content_frame)
        self.entry_khu_vuc.insert(ctk.END, university[3])
        self.entry_khu_vuc.configure(state="disabled")

        self.entry_mo_ta = ctk.CTkEntry(self.content_frame)
        self.entry_mo_ta.insert(ctk.END, university[33])
        self.entry_mo_ta.configure(state="disabled")

        self.entry_hoc_phi1 = ctk.CTkEntry(self.content_frame)
        if university[17]:
            self.entry_hoc_phi1.insert(ctk.END, university[17])
        self.entry_hoc_phi1.configure(state="disabled")

        self.entry_hoc_phi2 = ctk.CTkEntry(self.content_frame)
        if university[18]:
            self.entry_hoc_phi2.insert(ctk.END, university[18])
        self.entry_hoc_phi2.configure(state="disabled")

        self.entry_yeu_cau1 = ctk.CTkEntry(self.content_frame)
        if university[19]:
            self.entry_yeu_cau1.insert(ctk.END, university[19])
        self.entry_yeu_cau1.configure(state="disabled")

        self.entry_yeu_cau2 = ctk.CTkEntry(self.content_frame)
        if university[20]:
            self.entry_yeu_cau2.insert(ctk.END, university[20])
        self.entry_yeu_cau2.configure(state="disabled")

        self.entry_muc_do = ctk.CTkEntry(self.content_frame)
        if university[5] == "CO":
            self.entry_muc_do.insert(ctk.END, "Comprehensive")
        elif university[5] == "FC":
            self.entry_muc_do.insert(ctk.END, "Full Comprehensive")
        elif university[5] == "FO":
            self.entry_muc_do.insert(ctk.END, "Focused")
        elif university[5] == "SP":
            self.entry_muc_do.insert(ctk.END, "Specialist")
        self.entry_muc_do.configure(state="disabled")

        # Thêm nhãn và các ô nhập liệu tương ứng
        ctk.CTkLabel(self.content_frame, text="Tên trường:", font=("Arial", 14, "bold")).grid(
            row=1, column=1, sticky="w", padx=10, pady=5
        )
        self.entry_ten_truong.grid(row=1, column=2, columnspan=2, sticky="we", padx=10, pady=5)

        ctk.CTkLabel(self.content_frame, text="Quốc gia:", font=("Arial", 14, "bold")).grid(
            row=2, column=1, sticky="w", padx=10, pady=5
        )
        self.entry_quoc_gia.grid(row=2, column=2, sticky="we", padx=10, pady=5)

        ctk.CTkLabel(self.content_frame, text="Khu vực:", font=("Arial", 14, "bold")).grid(
            row=3, column=1, sticky="w", padx=10, pady=5
        )
        self.entry_khu_vuc.grid(row=3, column=2, sticky="we", padx=10, pady=5)

        ctk.CTkLabel(self.content_frame, text="Mô tả:", font=("Arial", 14, "bold")).grid(
            row=4, column=0, sticky="w", padx=10, pady=0
        )
        self.entry_mo_ta.grid(row=4, column=1, columnspan=4, sticky="we", padx=10, pady=0)

        # Học phí và yêu cầu đầu vào - Tách thành hai ô liền kề
        ctk.CTkLabel(self.content_frame, text="Học phí:", font=("Arial", 14, "bold")).grid(
            row=5, column=0, sticky="w", padx=10, pady=5
        )
        self.entry_hoc_phi1.grid(row=5, column=1, sticky="we", padx=10, pady=5)
        self.entry_hoc_phi2.grid(row=6, column=1, sticky="we", padx=10, pady=5)

        ctk.CTkLabel(self.content_frame, text="Yêu cầu", font=("Arial", 14, "bold")).grid(
            row=5, column=2, sticky="w", padx=10, pady=5
        )
        ctk.CTkLabel(self.content_frame, text="đầu vào:", font=("Arial", 14, "bold")).grid(
            row=6, column=2, sticky="w", padx=10, pady=5
        )
        self.entry_yeu_cau1.grid(row=5, column=3, sticky="we", padx=10, pady=5)
        self.entry_yeu_cau2.grid(row=6, column=3, sticky="we", padx=10, pady=5)

        # Mức độ tập trung chuyên ngành
        ctk.CTkLabel(self.content_frame, text="Mức độ tập trung chuyên ngành:", font=("Arial", 14, "bold")).grid(
            row=7, column=0, sticky="w", padx=10, pady=5
        )
        self.entry_muc_do.grid(row=7, column=1, columnspan=2, sticky="we", padx=10, pady=5)

        # Cấu hình lưới
        self.content_frame.grid_rowconfigure(4, weight=1)
        self.content_frame.grid_columnconfigure(2, weight=1)  # Các trường nhập liệu mở rộng

        self.graph_frame = ctk.CTkFrame(self.content_frame, fg_color="lightblue", corner_radius=10)
        self.graph_frame.grid(row=8, column=0, columnspan=5, sticky="we", padx=10, pady=5)
        data = {2012: university[21], 2014: university[22], 2015: university[23], 2016: university[24],
                2017: university[25], 2018: university[26], 2019: university[27], 2020: university[28],
                2021: university[29], 2022: university[30], 2023: university[31], 2024: university[32]}

        # Tạo một Figure cho biểu đồ
        fig = Figure(figsize=(5, 4), dpi=100)
        ax = fig.add_subplot(111)

        # Dữ liệu
        years = list(data.keys())
        values = list(data.values())

        # Vẽ biểu đồ dạng đường
        ax.plot(years, values, marker='o', color='blue', linestyle='-', label="Data")
        ax.set_title("Thứ hạng của trường qua các năm")
        ax.set_xlabel("Year")
        ax.set_ylabel("Rank")
        ax.legend()

        # Đảm bảo trục X chỉ hiển thị số nguyên
        ax.xaxis.set_major_locator(ticker.MaxNLocator(integer=True))
        ax.yaxis.set_major_locator(ticker.MaxNLocator(integer=True))

        # Đảo ngược trục Y
        ax.invert_yaxis()

        # Nhúng biểu đồ vào CustomTkinter
        canvas = FigureCanvasTkAgg(fig, master=self.graph_frame)  # Nhúng Figure vào root
        canvas.draw()
        canvas.get_tk_widget().pack(pady=20)

    def show(self):
        # Cập nhật giao diện nếu cần thiết
        pass

    def home(self):
        self.controller.home()

    def logout(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        self.controller.logout()

    def login(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        self.controller.login()

    def regis(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        self.controller.regis()

    def compare(self):
        self.controller.compare_uni()

    def chatbot(self):
        self.controller.chatbot()
