from View.evaluate_view import EvaluateView
from View.home_view import HomeView
from tkinter import messagebox
from DataAccess.university_model import UniversityModel
from View.homeappadmin_view import HomeAppAdminView
from View.registration_view import RegistrationView


class HomeAppAdminController:
    def __init__(self, root, view):
        self.root = root
        self.model = UniversityModel()
        self.view = view
        self.data = self.get_data()

    def get_data(self):
        # Lấy dữ liệu từ model
        return self.model.get_all_universities()

    def update_view(self):
        # Cập nhật dữ liệu cho View
        self.view.display_page(self.data)

    def update_search_view(self, name):
        # Cập nhật dữ liệu cho View
        self.data = self.model.get_all_universities_by_name(name)

    def on_item_click(self, item_id):
        from Controller.evaluate_controller import EvaluateController
        from Tmp.university import set_university
        # Xử lý sự kiện khi nhấn vào item
        print(f"Clicked on ID: {item_id}")
        set_university(self.model.get_university_by_id(item_id))
        # Xóa view hiện tại
        for widget in self.root.winfo_children():
            widget.destroy()
        regis_view = EvaluateView(self.root, None)  # Ban đầu không truyền Controller
        regis_controller = EvaluateController(self.root, regis_view)
        regis_view.controller = regis_controller
        self.view = regis_view
        self.display_view()

    def del_item_click(self, item_id):
        # Hiển thị messagebox xác nhận
        result = messagebox.askyesno("Xác nhận!", "Bạn có chắc muốn xóa không?")
        if result:
            from Tmp.university import set_university
            # Xử lý sự kiện khi nhấn vào item
            print(f"Clicked on ID: {item_id}")
            self.model.del_university_by_id(item_id)
            # Xóa view hiện tại
            for widget in self.root.winfo_children():
                widget.destroy()
            regis_view = HomeAppAdminView(self.root, None)  # Ban đầu không truyền Controller
            self.view = regis_view
            self.data = self.get_data()
            regis_view.controller = self
            self.view = regis_view
            self.display_view()

    def display_view(self):
        self.view.show()

    def logout(self):
        from Controller.home_controller import HomeController
        from Tmp.user import set_userId
        set_userId(-1)

        # Xóa view hiện tại
        for widget in self.root.winfo_children():
            widget.destroy()
        regis_view = HomeView(self.root, None)  # Ban đầu không truyền Controller
        regis_controller = HomeController(self.root, regis_view)
        regis_view.controller = regis_controller
        self.view = regis_view
        self.display_view()

