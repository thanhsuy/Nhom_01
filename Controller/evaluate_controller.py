from View.compare_view import CompareView
from View.home_view import HomeView
from View.homeappadmin_view import HomeAppAdminView
from DataAccess.university_model import UniversityModel


class EvaluateController:
    def __init__(self, root, view):
        self.root = root
        self.model = UniversityModel()
        self.view = view

    def display_view(self):
        self.view.show()

    def home(self):
        from Controller.homeappadmin_controller import HomeAppAdminController
        # Xóa view hiện tại
        for widget in self.root.winfo_children():
            widget.destroy()
        regis_view = HomeAppAdminView(self.root, None)  # Ban đầu không truyền Controller
        regis_controller = HomeAppAdminController(self.root, regis_view)
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

    def evaluate_uni(self, acaRe, empRe, facSt, citPe, intFa, intSt, intRe, empOu, sus):
        from Tmp.university import university
        print(acaRe, empRe, facSt, citPe, intFa, intSt, intRe, empOu, sus, university[0])
        # self.model.evaluate_university(acaRe, empRe, facSt, citPe, intFa, intSt, intRe, empOu, sus, 1504)
        self.model.evaluate_university(acaRe, empRe, facSt, citPe, intFa, intSt, intRe, empOu, sus, university[0])

        self.home()

