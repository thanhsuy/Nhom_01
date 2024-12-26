import customtkinter as ctk

from DataAccess.user_model import UserModel
from tkinter import messagebox


class EvaluateView:
    def __init__(self, root, controller):
        from Tmp.user import userId
        from Tmp.university import university
        self.root = root
        self.controller = controller
        self.dbUser = UserModel()

        sum = 0
        for i in range(8, 17):
            if not university[i]:
                sum += 0
            else:
                sum += int(university[i])

        # Thanh điều hướng
        self.navbar = ctk.CTkFrame(root, height=50, corner_radius=0, fg_color="#444")
        self.navbar.pack(fill="x")

        buttons = ["Quản lý các trường học"]

        self.butXepHang = ctk.CTkButton(self.navbar, text=buttons[0],
                                        width=100, fg_color="orange", hover_color="#666", command=self.home)
        self.butXepHang.pack(side="left", padx=10)

        self.butLogout = ctk.CTkButton(self.navbar, text="Đăng xuất", width=80, fg_color="orange", command=self.logout)
        self.butLogout.pack(side="right", padx=5)

        username = self.dbUser.get_username(userId)
        self.usernameLabel = ctk.CTkLabel(self.navbar, text=f"Xin chào {username}", width=80, fg_color="#444",
                                          text_color="white")
        self.usernameLabel.pack(side="right", padx=5)

        # Khu vực nội dung chính
        frame_main = ctk.CTkFrame(root, height=300, bg_color="gray")
        frame_main.pack(fill="both", expand=True, pady=10, padx=10)

        # Tọa độ ban đầu cho các nhãn và entry
        label_x = 70
        entry_x = 220
        label_x1 = 340
        entry_x1 = 470
        y_spacing = 60
        current_y = 10

        # Tên trường
        university_name_label = ctk.CTkLabel(
            master=frame_main,
            text="Tên trường",
            text_color="#454545",
            font=("Arial", 12, "bold")
        )
        university_name_label.place(x=label_x, y=current_y)

        self.university_name_entry = ctk.CTkEntry(
            master=frame_main,
            width=350,
            height=30,
            placeholder_text="Tên trường ",
            border_color="#dcdcdc",
            corner_radius=5
        )
        self.university_name_entry.place(x=entry_x, y=current_y)
        self.university_name_entry.insert(ctk.END, university[1])
        self.university_name_entry.configure(state="disable")

        # 1
        # Academic Reputation + Employer_Reputation
        current_y += y_spacing
        Academic_Reputation_label = ctk.CTkLabel(
            master=frame_main,
            text="Academic Reputation ",
            text_color="#454545",
            font=("Arial", 12, "bold")
        )
        Academic_Reputation_label.place(x=label_x, y=current_y)

        self.Academic_Reputation_entry = ctk.CTkEntry(
            master=frame_main,
            width=100,
            height=30,
            border_color="#dcdcdc",
            corner_radius=5,
        )
        self.Academic_Reputation_entry.place(x=entry_x, y=current_y)
        self.Academic_Reputation_entry.insert(ctk.END, university[8])
        self.Academic_Reputation_entry.bind("<FocusOut>", self.on_key_release)

        Employer_Reputation_label = ctk.CTkLabel(
            master=frame_main,
            text="Employer Reputation",
            text_color="#454545",
            font=("Arial", 12, "bold")
        )
        Employer_Reputation_label.place(x=label_x1, y=current_y)

        self.Employer_Reputation_entry = ctk.CTkEntry(
            master=frame_main,
            width=100,
            height=30,
            border_color="#dcdcdc",
            corner_radius=5,
        )
        self.Employer_Reputation_entry.place(x=entry_x1, y=current_y)
        self.Employer_Reputation_entry.insert(ctk.END, university[9])
        self.Employer_Reputation_entry.bind("<FocusOut>", self.on_key_release)

        # 2
        # Faculty Student + Citations per Faculty
        current_y += y_spacing
        Faculty_Student_label = ctk.CTkLabel(
            master=frame_main,
            text="Faculty Student ",
            text_color="#454545",
            font=("Arial", 12, "bold")
        )
        Faculty_Student_label.place(x=label_x, y=current_y)

        self.Faculty_Student_entry = ctk.CTkEntry(
            master=frame_main,
            width=100,
            height=30,
            border_color="#dcdcdc",
            corner_radius=5,
        )
        self.Faculty_Student_entry.place(x=entry_x, y=current_y)
        self.Faculty_Student_entry.insert(ctk.END, university[10])
        self.Faculty_Student_entry.bind("<FocusOut>", self.on_key_release)

        Citations_per_Faculty_label = ctk.CTkLabel(
            master=frame_main,
            text="Citations per Faculty",
            text_color="#454545",
            font=("Arial", 12, "bold")
        )
        Citations_per_Faculty_label.place(x=label_x1, y=current_y)

        self.Citations_per_Faculty_entry = ctk.CTkEntry(
            master=frame_main,
            width=100,
            height=30,
            border_color="#dcdcdc",
            corner_radius=5,
        )
        self.Citations_per_Faculty_entry.place(x=entry_x1, y=current_y)
        self.Citations_per_Faculty_entry.insert(ctk.END, university[11])
        self.Citations_per_Faculty_entry.bind("<FocusOut>", self.on_key_release)

        # 3
        # International Faculty + International Students
        current_y += y_spacing
        International_Faculty_label = ctk.CTkLabel(
            master=frame_main,
            text="International Faculty",
            text_color="#454545",
            font=("Arial", 12, "bold")
        )
        International_Faculty_label.place(x=label_x, y=current_y)

        self.International_Faculty_entry = ctk.CTkEntry(
            master=frame_main,
            width=100,
            height=30,
            border_color="#dcdcdc",
            corner_radius=5,
        )
        self.International_Faculty_entry.place(x=entry_x, y=current_y)
        self.International_Faculty_entry.insert(ctk.END, university[12])
        self.International_Faculty_entry.bind("<FocusOut>", self.on_key_release)

        International_Students_label = ctk.CTkLabel(
            master=frame_main,
            text="International Students",
            text_color="#454545",
            font=("Arial", 12, "bold")
        )
        International_Students_label.place(x=label_x1, y=current_y)

        self.International_Students_entry = ctk.CTkEntry(
            master=frame_main,
            width=100,
            height=30,
            border_color="#dcdcdc",
            corner_radius=5,
        )
        self.International_Students_entry.place(x=entry_x1, y=current_y)
        self.International_Students_entry.insert(ctk.END, university[13])
        self.International_Students_entry.bind("<FocusOut>", self.on_key_release)

        # 4
        # Employee Outcomes + Sustainability
        current_y += y_spacing
        Employee_Outcomes_label = ctk.CTkLabel(
            master=frame_main,
            text="Employee Outcomes",
            text_color="#454545",
            font=("Arial", 12, "bold")
        )
        Employee_Outcomes_label.place(x=label_x, y=current_y)

        self.Employee_Outcomes_entry = ctk.CTkEntry(
            master=frame_main,
            width=100,
            height=30,
            border_color="#dcdcdc",
            corner_radius=5,
        )
        self.Employee_Outcomes_entry.place(x=entry_x, y=current_y)
        self.Employee_Outcomes_entry.insert(ctk.END, university[15])
        self.Employee_Outcomes_entry.bind("<FocusOut>", self.on_key_release)

        Sustainability_label = ctk.CTkLabel(
            master=frame_main,
            text="Sustainability",
            text_color="#454545",
            font=("Arial", 12, "bold")
        )
        Sustainability_label.place(x=label_x1, y=current_y)

        self.Sustainability_entry = ctk.CTkEntry(
            master=frame_main,
            width=100,
            height=30,
            border_color="#dcdcdc",
            corner_radius=5,
        )
        self.Sustainability_entry.place(x=entry_x1, y=current_y)
        self.Sustainability_entry.insert(ctk.END, university[16])
        self.Sustainability_entry.bind("<FocusOut>", self.on_key_release)

        # 5
        # Overview
        current_y += y_spacing
        International_Research_Network_label = ctk.CTkLabel(
            master=frame_main,
            text="International Research Network",
            text_color="#454545",
            font=("Arial", 12, "bold")
        )
        International_Research_Network_label.place(x=label_x, y=current_y)

        self.International_Research_Network_entry = ctk.CTkEntry(
            master=frame_main,
            width=100,
            height=30,
            border_color="#dcdcdc",
            corner_radius=5,
        )
        self.International_Research_Network_entry.place(x=entry_x + 100, y=current_y)
        self.International_Research_Network_entry.insert(ctk.END, university[14])
        self.International_Research_Network_entry.bind("<FocusOut>", self.on_key_release)

        # 6
        # Overview
        current_y += y_spacing
        Overview_label = ctk.CTkLabel(
            master=frame_main,
            text="Overview",
            text_color="#454545",
            font=("Arial", 12, "bold")
        )
        Overview_label.place(x=label_x, y=current_y)

        self.Overview_entry = ctk.CTkEntry(
            master=frame_main,
            width=100,
            height=30,
            border_color="#dcdcdc",
            corner_radius=5,
        )
        self.Overview_entry.place(x=entry_x, y=current_y)
        self.Overview_entry.insert(ctk.END, int(sum / 9))

        # Nút "Xác nhận"
        confirm_button = ctk.CTkButton(
            master=frame_main,
            text="Xác nhận",
            text_color="white",
            fg_color="#f7941d",
            hover_color="#f6a549",
            corner_radius=10,
            width=120,
            height=40,
            font=("Arial", 14, "bold"),
            command=self.evaluate_uni
        )
        confirm_button.place(relx=0.5, rely=0.93, anchor="center")

    def show(self):
        # Hiển thị thông báo nếu cần (có thể mở rộng)
        pass

    def logout(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        self.controller.logout()

    def home(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        self.controller.home()

    def on_key_release(self, event):
        # Hàm xử lý khi một phím được nhả ra
        acaRe = self.Academic_Reputation_entry.get()
        empRe = self.Employer_Reputation_entry.get()
        facSt = self.Faculty_Student_entry.get()
        citPe = self.Citations_per_Faculty_entry.get()
        intFa = self.International_Faculty_entry.get()
        intSt = self.International_Students_entry.get()
        intRe = self.International_Research_Network_entry.get()
        empOu = self.Employee_Outcomes_entry.get()
        sus = self.Sustainability_entry.get()
        check = acaRe + empRe + facSt + citPe + intFa + intSt + intRe + empOu + sus
        if not check.isnumeric():
            messagebox.showerror("Loi", "Nhap sai dinh dang")
        else:
            result = (int(acaRe) + int(empRe) + int(facSt) + int(citPe) +
                      int(intFa) + int(intSt) + int(intRe) + int(empOu) +
                      int(sus))
            self.Overview_entry.delete(0, ctk.END)
            self.Overview_entry.insert(ctk.END, int(result / 9))

    def evaluate_uni(self):
        # Hàm xử lý khi một phím được nhả ra
        acaRe = self.Academic_Reputation_entry.get()
        empRe = self.Employer_Reputation_entry.get()
        facSt = self.Faculty_Student_entry.get()
        citPe = self.Citations_per_Faculty_entry.get()
        intFa = self.International_Faculty_entry.get()
        intSt = self.International_Students_entry.get()
        intRe = self.International_Research_Network_entry.get()
        empOu = self.Employee_Outcomes_entry.get()
        sus = self.Sustainability_entry.get()

        self.controller.evaluate_uni(acaRe, empRe, facSt, citPe, intFa, intSt, intRe, empOu, sus)
