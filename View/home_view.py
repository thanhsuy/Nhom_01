import customtkinter as ctk


class HomeView:
    def __init__(self, root, controller):
        from Controller.home_controller import HomeController
        self.root = root
        self.controller = controller

        # Biến quản lý trạng thái phân trang
        self.current_page = 0
        self.frames_per_page = 3

        # Thanh điều hướng trên cùng
        self.navbar = ctk.CTkFrame(root, height=50, corner_radius=0, fg_color="#444")
        self.navbar.pack(fill="x")

        buttons = ["Xếp hạng", "So sánh", "Chat bot"]

        self.butXepHang = ctk.CTkButton(self.navbar, text=buttons[0], width=100, fg_color="orange", hover_color="#666")
        self.butXepHang.pack(side="left", padx=10)

        self.butSoSanh = ctk.CTkButton(self.navbar, text=buttons[1], width=100,
                                       fg_color="#555", hover_color="#666", command=self.compare)
        self.butSoSanh.pack(side="left", padx=10)

        self.butChatBot = ctk.CTkButton(self.navbar, text=buttons[2], width=100,
                                        fg_color="#555", hover_color="#666", command=self.chatbot)
        self.butChatBot.pack(side="left", padx=10)

        self.butLogin = ctk.CTkButton(self.navbar, text="Đăng nhập", width=80, fg_color="orange", command=self.login)
        self.butLogin.pack(side="right", padx=5)

        self.butRegister = ctk.CTkButton(self.navbar, text="Đăng ký", width=80, fg_color="orange", command=self.regis)
        self.butRegister.pack(side="right", padx=5)

        # Thanh tìm kiếm
        self.search_frame = ctk.CTkFrame(root, height=50)
        self.search_frame.pack(fill="x", pady=10, padx=10)

        self.search_label = ctk.CTkLabel(self.search_frame, text="Tìm kiếm:")
        self.search_label.pack(side="left", padx=10)

        self.search_entry = ctk.CTkEntry(self.search_frame)
        self.search_entry.pack(side="left", fill="x", expand=True, padx=10)
        self.search_entry.bind("<Return>", self.search)

        # Khu vực nội dung
        self.content_frame = ctk.CTkFrame(root, height=412, bg_color="black")
        self.content_frame.pack(fill="both", expand=True, pady=10, padx=10)

        # Điều hướng phân trang với hai nút
        self.pagination_frame = ctk.CTkFrame(root, height=50)
        self.pagination_frame.pack(fill="x", pady=10)

        self.prev_button = ctk.CTkButton(self.pagination_frame, text="Previous", width=100, command=self.previous_page)
        self.prev_button.pack(side="left", padx=10)

        self.next_button = ctk.CTkButton(self.pagination_frame, text="Next", width=100, command=self.next_page)
        self.next_button.pack(side="right", padx=10)

    def display_page(self, data):
        # Xóa các frame cũ
        for widget in self.content_frame.winfo_children():
            widget.destroy()

        # Lấy dữ liệu trang hiện tại
        start_index = self.current_page * self.frames_per_page
        end_index = start_index + self.frames_per_page
        page_data = data[start_index:end_index]

        # Tạo frame cho từng mục
        for item in page_data:
            item_id, name, location = item[0], item[1], item[2]
            item_frame = ctk.CTkFrame(self.content_frame, corner_radius=10, height=50)
            item_frame.pack(fill="x", pady=5, padx=10)

            # Hiển thị thông tin trong frame
            ctk.CTkLabel(item_frame, text=f"Name: {name}", anchor="w").pack(side="left", padx=10)
            ctk.CTkLabel(item_frame, text=f"Location: {location}", anchor="w").pack(side="left", padx=10)

            # Sửa lỗi lambda
            item_frame.bind("<Button-1>", lambda e, itemid=item_id: self.controller.on_item_click(itemid))

        # Cập nhật trạng thái nút phân trang
        self.prev_button.configure(state="normal" if self.current_page > 0 else "disabled")
        self.next_button.configure(state="normal" if end_index < len(data) else "disabled")

    def previous_page(self):
        if self.current_page > 0:
            self.current_page -= 1
            self.controller.update_view()

    def next_page(self):
        if (self.current_page + 1) * self.frames_per_page < len(self.controller.data):
            self.current_page += 1
            self.controller.update_view()

    def show(self):
        self.controller.update_view()
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

    def search(self, event):
        self.current_page = 0
        name = self.search_entry.get()
        self.controller.update_search_view(name)
        self.controller.update_view()

    def compare(self):
        self.controller.compare_uni()

    def chatbot(self):
        self.controller.chatbot()
