import customtkinter as ctk
from Controller.addschool_controller import AddSchoolController
from Controller.compare_controller import CompareController
from Controller.homeadmin_controller import HomeAdminController
from Controller.homeappadmin_controller import HomeAppAdminController
from Controller.login_controller import LoginController
from Controller.registration_controller import RegistrationController
from Controller.home_controller import HomeController
from View.addschool_view import AddSchoolView
from View.compare_view import CompareView
from View.home_view import HomeView
from View.homeadmin_view import HomeAdminView
from View.homeappadmin_view import HomeAppAdminView

# Thiết lập giao diện
# ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

if __name__ == "__main__":
    # Tạo root
    root = ctk.CTk()
    root.geometry("720x512")
    root.title("Quản lý trường đại học")
    root.resizable(False, False)

    # Khởi tạo View và Controller
    home_view = HomeView(root, None)  # Ban đầu không truyền Controller
    home_controller = HomeController(root, home_view)

    # Kết nối View với Controller
    home_view.controller = home_controller

    # Hiển thị HomeView
    home_controller.display_view()

    # Chạy ứng dụng
    root.mainloop()
