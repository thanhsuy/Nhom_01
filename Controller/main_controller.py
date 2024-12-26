class MainController:
    def __init__(self, root):
        self.root = root
        self.current_view = None  # Quản lý View hiện tại

    def switch_view(self, view_class, *args):
        """
        Chuyển sang View mới.
        :param view_class: Class của View mới.
        :param args: Các tham số cần thiết để khởi tạo View mới.
        """
        # Xóa tất cả widget của View hiện tại
        if self.current_view:
            for widget in self.root.winfo_children():
                widget.destroy()

        # Khởi tạo View mới
        self.current_view = view_class(self.root, *args)
        self.current_view.show()
