from View.addschool_view import AddSchoolView
from View.home_view import HomeView
from DataAccess.university_model import UniversityModel


class NewHomeAdminController:
    def __init__(self, root, view):
        self.root = root
        self.model = UniversityModel()
        self.view = view

    def get_data(self):
        # Lấy dữ liệu từ model
        return self.model.get_all_universities()

    def on_item_click(self, item_id):
        # Xử lý sự kiện khi nhấn vào item
        print(f"Clicked on ID: {item_id}")

    def display_view(self):
        self.view.show()

    def add_university(self):
        from Controller.addschool_controller import AddSchoolController
        # Xóa view hiện tại
        for widget in self.root.winfo_children():
            widget.destroy()
        regis_view = AddSchoolView(self.root, None)  # Ban đầu không truyền Controller
        regis_controller = AddSchoolController(self.root, regis_view)
        regis_view.controller = regis_controller
        self.view = regis_view
        self.display_view()

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
