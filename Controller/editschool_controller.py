import os

from PIL import Image

from DataAccess.user_model import UserModel
from View.home_view import HomeView
from View.homeadmin_view import HomeAdminView
from DataAccess.university_model import UniversityModel
from tkinter import messagebox


def save_image_to_project(image_path: str, destination_folder: str, new_name: str):
    """
        Chuyển đổi ảnh sang định dạng WebP và lưu vào thư mục dự án.

        Args:
            image_path (str): Đường dẫn ảnh nguồn.
            destination_folder (str): Thư mục lưu ảnh đích.
            new_name (str): Tên mới của ảnh.
        """
    # Kiểm tra xem đường dẫn ảnh có tồn tại không
    if not isinstance(image_path, str) or not os.path.exists(image_path):
        messagebox.showerror("Lỗi", "Không tìm thấy ảnh")
        return

    # Kiểm tra xem thư mục đích có tồn tại không, nếu không thì tạo
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
    new_name = str(new_name)
    # Mở ảnh bằng Pillow (PIL)
    try:
        with Image.open(image_path) as img:
            # Tạo đường dẫn đích với đuôi .webp
            destination_path = os.path.join(destination_folder, new_name + ".webp")

            # Chuyển đổi và lưu ảnh dưới định dạng WebP
            img.save(destination_path, format="WEBP", quality=95)  # Quality có thể chỉnh sửa (0-100)
            print(f"Ảnh đã được chuyển đổi và lưu tại: {destination_path}")
            return True
    except Exception as e:
        messagebox.showerror("Lỗi", f"Lỗi {e}")


class EditSchoolController:
    def __init__(self, root, view):
        self.root = root
        self.model = UniversityModel()
        self.view = view
        self.dbUser = UserModel()

    def get_data(self):
        # Lấy dữ liệu từ model
        return self.model.get_all_universities()

    def edit_university(self, name, location, region, focus, country_fee, global_fee, SAT, TOEFL, description, idUser,
                        image):
        # Xử lý sự kiện khi nhấn vào item
        try:
            idAdmin = self.dbUser.get_idAdmin(idUser)
            if image != "":
                print(name, location, region, focus
                      , country_fee, global_fee, SAT, TOEFL, description, idUser)
                cleaned_path = image.strip().strip("\u202a").strip("\u202c")
                source_image = cleaned_path.replace("\\", "/")
                source_image = os.path.normpath(source_image)
                destination_folder = "./Image"
                idUni = self.model.get_university_id(idAdmin)
                new_image_name = f"{idUni}"
                save_image_to_project(source_image, destination_folder, new_image_name)
            self.model.edit_university(name, location, region, focus
                                       , country_fee, global_fee, SAT, TOEFL, description, idAdmin)
            self.return_main(idAdmin)
            return True
        except Exception as e:
            print(e)
            return False

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

    def return_main(self, idUser):
        from Controller.homeadmin_controller import HomeAdminController
        from Tmp.user import userId
        from Tmp.university import set_university
        # Xóa view hiện tại
        for widget in self.root.winfo_children():
            widget.destroy()

        self.model.get_universities_by_user(userId)
        set_university(self.model.get_universities_by_user(idUser))
        home_view = HomeAdminView(self.root, None)  # Ban đầu không truyền Controller
        home_controller = HomeAdminController(self.root, home_view)
        home_view.controller = home_controller
        self.view = home_view
        self.display_view()

    def home(self):
        from Controller.homeadmin_controller import HomeAdminController
        # Xóa view hiện tại
        for widget in self.root.winfo_children():
            widget.destroy()
        regis_view = HomeAdminView(self.root, None)  # Ban đầu không truyền Controller
        regis_controller = HomeAdminController(self.root, regis_view)
        regis_view.controller = regis_controller
        self.view = regis_view
        self.display_view()
