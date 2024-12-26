from View.editschool_view import EditSchoolView
from View.home_view import HomeView
from DataAccess.university_model import UniversityModel


class HomeAdminController:
    def __init__(self, root, view):
        self.root = root
        self.model = UniversityModel()
        self.view = view

    def get_data(self):
        # Lấy dữ liệu từ model
        return self.model.get_all_universities()

    def edit_university(self):
        from Controller.editschool_controller import EditSchoolController
        # Xóa view hiện tại
        for widget in self.root.winfo_children():
            widget.destroy()
        regis_view = EditSchoolView(self.root, None)  # Ban đầu không truyền Controller
        regis_controller = EditSchoolController(self.root, regis_view)
        regis_view.controller = regis_controller
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
