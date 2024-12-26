from View.chatbot_view import ChatBotView
from View.compare_view import CompareView
from View.home_view import HomeView
from View.login_view import LoginView
from DataAccess.university_model import UniversityModel
from View.registration_view import RegistrationView
from View.university_detail_view import UniversityDetailView


class HomeController:
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
        from Tmp.university import set_university
        from Controller.universitydetail_controller import UniversityDetailController
        # Xử lý sự kiện khi nhấn vào item
        print(f"Clicked on ID: {item_id}")
        set_university(self.model.get_university_by_id(item_id))
        # Xóa view hiện tại
        for widget in self.root.winfo_children():
            widget.destroy()
        regis_view = UniversityDetailView(self.root, None)  # Ban đầu không truyền Controller
        regis_controller = UniversityDetailController(self.root, regis_view)
        regis_view.controller = regis_controller
        self.view = regis_view
        self.display_view()

    def display_view(self):
        self.view.show()

    def login(self):
        from Controller.login_controller import LoginController
        # Xóa view hiện tại
        for widget in self.root.winfo_children():
            widget.destroy()
        login_view = LoginView(self.root, None)  # Ban đầu không truyền Controller
        login_controller = LoginController(self.root, login_view)
        login_view.controller = login_controller
        self.view = login_view
        self.display_view()

    def regis(self):
        from Controller.registration_controller import RegistrationController
        # Xóa view hiện tại
        for widget in self.root.winfo_children():
            widget.destroy()
        regis_view = RegistrationView(self.root, None)  # Ban đầu không truyền Controller
        regis_controller = RegistrationController(self.root, regis_view)
        regis_view.controller = regis_controller
        self.view = regis_view
        self.display_view()

    def compare_uni(self):
        from Controller.compare_controller import CompareController
        # Xóa view hiện tại

        for widget in self.root.winfo_children():
            widget.destroy()
        regis_view = CompareView(self.root, None)  # Ban đầu không truyền Controller
        regis_controller = CompareController(self.root, regis_view)
        regis_view.controller = regis_controller
        self.view = regis_view
        self.display_view()

    def chatbot(self):
        from Controller.chatbot_controller import ChatbotController
        # Xóa view hiện tại

        for widget in self.root.winfo_children():
            widget.destroy()
        regis_view = ChatBotView(self.root, None)  # Ban đầu không truyền Controller
        regis_controller = ChatbotController(self.root, regis_view)
        regis_view.controller = regis_controller
        self.view = regis_view
        self.display_view()
