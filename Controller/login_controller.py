from DataAccess.university_model import UniversityModel
from DataAccess.user_model import UserModel
from View.home_view import HomeView
from View.homeadmin_view import HomeAdminView
from View.homeappadmin_view import HomeAppAdminView
from View.homestudent_view import HomeStudentView
from View.login_view import LoginView
from View.newhomeadmin_view import NewHomeAdminView


class LoginController:
    def __init__(self, root, view):
        # Danh sách người dùng mẫu
        self.root = root
        self.view = view

    def validate_login(self, username, password):
        from Tmp.user import set_userId
        from Tmp.university import set_university

        db = UserModel()
        dbUniversity = UniversityModel()
        role, idUser = db.check_user(username, password)
        set_userId(idUser)
        # Kiểm tra thông tin đăng nhập
        if role == 0:
            from Controller.homestudent_controller import HomeStudentController
            # Xóa view hiện tại
            for widget in self.root.winfo_children():
                widget.destroy()
            home_view = HomeStudentView(self.root, None)  # Ban đầu không truyền Controller
            home_controller = HomeStudentController(self.root, home_view)
            home_view.controller = home_controller
            self.view = home_view
            self.display_view()
            return True
        elif role == 2:
            from Controller.homeadmin_controller import HomeAdminController
            from Controller.newhomeadmin_controller import NewHomeAdminController
            # Xóa view hiện tại
            for widget in self.root.winfo_children():
                widget.destroy()
            idAdmin = db.get_idAdmin(idUser)
            if dbUniversity.get_universities_by_user(idAdmin):
                set_university(dbUniversity.get_universities_by_user(idAdmin))
                home_view = HomeAdminView(self.root, None)  # Ban đầu không truyền Controller
                home_controller = HomeAdminController(self.root, home_view)
                home_view.controller = home_controller
                self.view = home_view
                self.display_view()
            else:
                set_university(dbUniversity.get_universities_by_user(idUser))
                home_view = NewHomeAdminView(self.root, None)  # Ban đầu không truyền Controller
                home_controller = NewHomeAdminController(self.root, home_view)
                home_view.controller = home_controller
                self.view = home_view
                self.display_view()
            return True

        elif role == 1:
            from Controller.homeappadmin_controller import HomeAppAdminController
            # Xóa view hiện tại
            for widget in self.root.winfo_children():
                widget.destroy()
            home_view = HomeAppAdminView(self.root, None)  # Ban đầu không truyền Controller
            home_controller = HomeAppAdminController(self.root, home_view)
            home_view.controller = home_controller
            self.view = home_view
            self.display_view()
            return True

        return False

    def display_view(self):
        self.view.show()

    def home(self):
        from Controller.home_controller import HomeController
        # Xóa view hiện tại
        for widget in self.root.winfo_children():
            widget.destroy()
        home_view = HomeView(self.root, None)  # Ban đầu không truyền Controller
        home_controller = HomeController(self.root, home_view)
        home_view.controller = home_controller
        self.view = home_view
        self.display_view()
