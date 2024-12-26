from DataAccess.user_model import UserModel
from View.home_view import HomeView
from View.homeadmin_view import HomeAdminView
from View.homeappadmin_view import HomeAppAdminView
from View.homestudent_view import HomeStudentView
from View.newhomeadmin_view import NewHomeAdminView
from View.registration_view import RegistrationView


class RegistrationController:
    def __init__(self, root, view):
        # Danh sách người dùng mẫu
        self.root = root
        self.users = {"admin": "12345", "user": "password"}
        self.view = view
        self.dbUser = UserModel()

    def register_user(self, username, password, email, account_type, location, sat, toefl):
        try:
            self.dbUser.add_user(username, password, email)
            idUser = self.dbUser.get_last_user()

            from Tmp.user import set_userId
            from Controller.home_controller import HomeController
            from Controller.newhomeadmin_controller import NewHomeAdminController
            from Controller.homeappadmin_controller import HomeAppAdminController
            from Controller.homestudent_controller import HomeStudentController

            set_userId(idUser)
            if account_type == "Học sinh":
                self.dbUser.add_student(idUser, location, sat, toefl)
                # Xóa view hiện tại
                for widget in self.root.winfo_children():
                    widget.destroy()
                home_view = HomeStudentView(self.root, None)  # Ban đầu không truyền Controller
                home_controller = HomeStudentController(self.root, home_view)
                home_view.controller = home_controller
                self.view = home_view
                self.display_view()
            elif account_type == "Quản lý":
                self.dbUser.add_adminschool(idUser)
                for widget in self.root.winfo_children():
                    widget.destroy()
                home_view = NewHomeAdminView(self.root, None)  # Ban đầu không truyền Controller
                home_controller = NewHomeAdminController(self.root, home_view)
                home_view.controller = home_controller
                self.view = home_view
                self.display_view()
            elif account_type == "Đánh giá viên":
                self.dbUser.add_adminapp(idUser)
                for widget in self.root.winfo_children():
                    widget.destroy()
                home_view = HomeAppAdminView(self.root, None)  # Ban đầu không truyền Controller
                home_controller = HomeAppAdminController(self.root, home_view)
                home_view.controller = home_controller
                self.view = home_view
                self.display_view()

            print("Đăng ký thành công!")
            return True
        except Exception as e:
            return False

    def check_username(self, username):
        return self.dbUser.check_username(username)

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
