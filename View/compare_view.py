import customtkinter as ctk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

from DataAccess.university_model import UniversityModel
from DataAccess.user_model import UserModel


class CompareView:
    def __init__(self, root, controller):
        self.listbox = None
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
        self.butXepHang = ctk.CTkButton(self.navbar, text="Xếp hạng", width=100,
                                        fg_color="#555", hover_color="#666", command=self.home)
        self.butXepHang.pack(side="left", padx=10)

        self.butSoSanh = ctk.CTkButton(self.navbar, text="So sánh", width=100, fg_color="orange", hover_color="#666")
        self.butSoSanh.pack(side="left", padx=10)

        self.butChatBot = ctk.CTkButton(self.navbar, text="Chat bot", width=100,
                                        fg_color="#555", hover_color="#666", command=self.chatbot)
        self.butChatBot.pack(side="left", padx=10)

        if userId == -1:

            self.butLogin = ctk.CTkButton(self.navbar, text="Đăng nhập", width=80, fg_color="orange", command=self.login)
            self.butLogin.pack(side="right", padx=5)

            self.butRegister = ctk.CTkButton(self.navbar, text="Đăng ký", width=80, fg_color="orange", command=self.regis)
            self.butRegister.pack(side="right", padx=5)

        else:
            self.butLogout = ctk.CTkButton(self.navbar, text="Đăng xuất", width=80,
                                           fg_color="orange", command=self.logout)
            self.butLogout.pack(side="right", padx=5)

            username = self.dbUser.get_username(userId)
            self.usernameLabel = ctk.CTkLabel(self.navbar, text=f"Xin chào {username}", width=80, fg_color="#444",
                                              text_color="white")
            self.usernameLabel.pack(side="right", padx=5)

        # Thanh tìm kiếm
        self.search_frame = ctk.CTkFrame(root, height=50)
        self.search_frame.pack(fill="x", pady=10, padx=10)

        # Hai ô tìm kiếm
        self.search_entry_1 = ctk.CTkEntry(self.search_frame, placeholder_text="Nhập tên trường 1")
        self.search_entry_1.pack(side="left", fill="x", expand=True, padx=10)

        # Gắn sự kiện khi gõ phím
        self.search_entry_1.bind("<KeyRelease>", self.on_keyrelease)
        self.search_entry_1.bind("<FocusOut>", self.hide_suggestions)

        self.search_entry_2 = ctk.CTkEntry(self.search_frame, placeholder_text="Nhập tên trường 2")
        self.search_entry_2.pack(side="left", fill="x", expand=True, padx=10)

        self.search_entry_2.bind("<KeyRelease>", self.on_keyrelease2)
        self.search_entry_2.bind("<FocusOut>", self.hide_suggestions)

        # Khu vực nội dung chính
        self.content_frame = ctk.CTkFrame(root, height=300, bg_color="lightblue")
        self.content_frame.pack(fill="both", expand=True, pady=10, padx=10)

        # Hàng nút chỉ số
        self.indicator_frame1 = ctk.CTkFrame(root, height=50)
        self.indicator_frame1.pack(fill="x", pady=10)

        self.indicator_frame2 = ctk.CTkFrame(root, height=50)
        self.indicator_frame2.pack(fill="x", pady=10)

        # Các nút "Chỉ số 1"
        for i in range(5):  # Hiển thị 8 nút
            ctk.CTkButton(self.indicator_frame1, text=f"Chỉ số {i+1}",
                          fg_color="orange", width=115,
                          command=lambda index=i+1: self.show_dif(index)).pack(side="left", padx=15)

        for i in range(5):  # Hiển thị 8 nút
            ctk.CTkButton(self.indicator_frame2, text=f"Chỉ số {i+6}",
                          fg_color="orange", width=115,
                          command=lambda index=i+6: self.show_dif(index)).pack(side="left", padx=15)
        self.canvas = None

    def show(self):
        # Hiển thị thông báo nếu cần (có thể mở rộng)
        pass

    def login(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        self.controller.login()

    def regis(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        self.controller.regis()

    def home(self):
        self.controller.home()

    def chatbot(self):
        self.controller.chatbot()

    def logout(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        self.controller.logout()

    def on_keyrelease(self, event):
        value = self.search_entry_1.get()
        if value == "":
            self.hide_suggestions()
        else:
            matching_suggestions = [s for s in self.uni_name if value.lower() in s.lower()]
            matching_suggestions = matching_suggestions[:10]
            self.update_suggestions(matching_suggestions)

    def update_suggestions(self, suggestions):
        if self.listbox:
            self.listbox.destroy()

        if not suggestions:
            return

        # Tạo Frame cho danh sách gợi ý với kích thước cố định
        self.listbox = ctk.CTkFrame(self.root, width=self.search_entry_1.winfo_width())
        self.listbox.place(x=self.search_entry_1.winfo_x() + 5,
                           y=self.search_entry_1.winfo_y() + self.search_entry_1.winfo_height() + 30)

        # Thêm các gợi ý vào danh sách
        for suggestion in suggestions:
            button = ctk.CTkButton(
                self.listbox,
                text=suggestion,
                corner_radius=0,
                command=lambda text=suggestion: self.select_suggestion(text)
            )
            button.pack(fill="x")

    def select_suggestion(self, text):
        self.search_entry_1.delete(0, ctk.END)
        self.search_entry_1.insert(0, text)
        self.hide_suggestions()

    def on_keyrelease2(self, event):
        value = self.search_entry_2.get()
        if value == "":
            self.hide_suggestions()
        else:
            matching_suggestions = [s for s in self.uni_name if value.lower() in s.lower()]
            matching_suggestions = matching_suggestions[:10]
            self.update_suggestions2(matching_suggestions)

    def update_suggestions2(self, suggestions):
        if self.listbox:
            self.listbox.destroy()

        if not suggestions:
            return

        # Tạo Frame cho danh sách gợi ý với kích thước cố định
        self.listbox = ctk.CTkFrame(self.root, width=self.search_entry_2.winfo_width())
        self.listbox.place(x=self.search_entry_2.winfo_x() - 170,
                           y=self.search_entry_2.winfo_y() + self.search_entry_2.winfo_height() + 30)

        # Thêm các gợi ý vào danh sách
        for suggestion in suggestions:
            button = ctk.CTkButton(
                self.listbox,
                text=suggestion,
                corner_radius=0,
                command=lambda text=suggestion: self.select_suggestion2(text)
            )
            button.pack(fill="x")

    def select_suggestion2(self, text):
        self.search_entry_2.delete(0, ctk.END)
        self.search_entry_2.insert(0, text)
        self.hide_suggestions()

    def hide_suggestions(self, event=None):
        self.university1 = self.dbUni.get_university_by_name(self.search_entry_1.get())
        self.university2 = self.dbUni.get_university_by_name(self.search_entry_2.get())
        if self.listbox:
            self.listbox.destroy()
            self.listbox = None

    def show_dif(self, index):
        # Tạo Figure cho biểu đồ
        switch_dict = {
            1: ["Academic Reputation"],
            2: ["Employer Reputation"],
            3: ["Faculty Student"],
            4: ["Citations Per Faculty"],
            5: ["International Faculty"],
            6: ["International Students"],
            7: ["International Research Network"],
            8: ["Employee Outcomes"],
            9: ["Sustainability"],
            10: ["Overview"],
        }
        fig = Figure(figsize=(6, 4), dpi=100)
        if index == 10 and self.university1 and self.university2:
            sum1 = 0
            sum2 = 0
            for i in range(8, 17):
                if not self.university1[i]:
                    sum1 += 0
                else:
                    sum1 += int(self.university1[i])
                if not self.university2[i]:
                    sum2 += 0
                else:
                    sum2 += int(self.university2[i])
            value1 = int(sum1/9)
            value2 = int(sum2/9)
        else:
            value1 = self.university1[index + 7] if self.university1 and len(self.university1) > index + 8 else 0
            value2 = self.university2[index + 7] if self.university2 and len(self.university2) > index + 8 else 0

        name1 = self.university1[1] if self.university1 and len(self.university1) > index + 8 else "Không có"
        name2 = self.university2[1] if self.university2 and len(self.university2) > index + 8 else "Không có"

        ax = fig.add_subplot(111)

        # Tạo biểu đồ cột
        x = range(1)
        ax.bar(x, value1, width=0.4, label=f"{name1}", color="blue", align="center")
        ax.bar([i + 0.4 for i in x], value2, width=0.4, label=f"{name2}", color="orange", align="center")

        # Gắn nhãn
        ax.set_title("Bar Chart")
        ax.set_xlabel("Categories")
        ax.set_ylabel("Điểm số đánh giá")
        ax.set_xticks([i + 0.2 for i in x])  # Đặt nhãn vào giữa các nhóm cột
        ax.set_xticklabels(switch_dict.get(index))
        ax.legend()
        if self.canvas:
            self.canvas.get_tk_widget().destroy()
            self.canvas = None
        # Nhúng biểu đồ vào CustomTkinter
        self.canvas = FigureCanvasTkAgg(fig, master=self.content_frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(pady=20)


