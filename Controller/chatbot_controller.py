from View.compare_view import CompareView
from View.home_view import HomeView
from View.homestudent_view import HomeStudentView
from View.login_view import LoginView
from DataAccess.university_model import UniversityModel
from View.registration_view import RegistrationView
from openai import OpenAI


class ChatbotController:
    def __init__(self, root, view):
        self.root = root
        self.model = UniversityModel()
        self.view = view

        describe = "You are university helper chat bot"
        system = {"role": "system", "content": describe}

        self.message = [system]
        self.client = OpenAI(
            base_url="https://generativelanguage.googleapis.com/v1beta/",
            api_key="AIzaSyDsoyUFDKkeQRA9hh38N4dc1eRSV6AoaXk"
        )

    def get_data(self):
        # Lấy dữ liệu từ model
        return self.model.get_all_universities()

    def home(self):
        from Controller.home_controller import HomeController
        from Controller.homestudent_controller import HomeStudentController
        from Tmp.user import userId
        # Xóa view hiện tại
        for widget in self.root.winfo_children():
            widget.destroy()
        if userId == -1:
            regis_view = HomeView(self.root, None)  # Ban đầu không truyền Controller
            regis_controller = HomeController(self.root, regis_view)
        else:
            regis_view = HomeStudentView(self.root, None)
            regis_controller = HomeStudentController(self.root, regis_view)
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

    def return_message(self, question):

        user_input = question
        self.message.append({"role": "user", "content": user_input})
        response = self.client.chat.completions.create(
            model="gemini-1.5-flash-latest",
            messages=self.message
        )
        bot_reply = str(response.choices[0].message.content)
        # for chunk in response:
        #     bot_reply += chunk.choices[0].delta.content or ""
        #     print(chunk.choices[0].delta.content or "", end="", flush=True)

        self.message.append({"role": "assistant", "content": bot_reply})
        return bot_reply
