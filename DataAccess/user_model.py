import mysql.connector


class UserModel:
    def __init__(self):
        # Kết nối đến cơ sở dữ liệu MySQL
        self.conn = mysql.connector.connect(
            host="localhost",  # Thay bằng địa chỉ server MySQL
            user="root",  # Thay bằng username của bạn
            password="13092003aA@",  # Thay bằng mật khẩu của bạn
            database="universitymanagement"  # Tên cơ sở dữ liệu
        )
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        # Tạo bảng nếu chưa tồn tại
        query = """
        CREATE TABLE IF NOT EXISTS university (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            location VARCHAR(255) NOT NULL
        )
        """
        self.cursor.execute(query)
        self.conn.commit()

    def get_all_user(self):
        # Lấy tất cả các trường
        query = "SELECT * FROM user"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def check_username(self, username):
        query = "SELECT idUser FROM user WHERE username = %s"
        self.cursor.execute(query, (username, ))
        result = self.cursor.fetchone()
        self.cursor.fetchall()
        return result

    def get_username(self, idUser):
        query = "SELECT userName FROM user WHERE idUser = %s"
        self.cursor.execute(query, (idUser,))
        result = self.cursor.fetchone()
        self.cursor.fetchall()
        return result[0]

    def get_last_user(self):
        # Lấy tất cả các trường
        query = "SELECT idUser FROM user ORDER BY idUser DESC"
        self.cursor.execute(query)
        result = self.cursor.fetchone()
        self.cursor.fetchall()
        return result[0]

    def add_user(self, username, password, email):
        # Thêm một trường mới
        query = ("INSERT INTO `universitymanagement`.`user` (`userName`, `password`, `email`) VALUES (%s, "
                 "%s, %s);")
        self.cursor.execute(query, (username, password, email))
        self.cursor.fetchall()
        self.conn.commit()

    def add_student(self, idUser, location, SAT, TOEFL):
        # Thêm một trường mới
        try:
            query = (
                "INSERT INTO `universitymanagement`.`student` (`idUser`, `location`, `SAT`, `TOEFL`) VALUES (%s, %s, "
                "%s, %s);")
            self.cursor.execute(query, (idUser, location, SAT, TOEFL))
            self.conn.commit()
        except Exception as e:
            print(e)

    def add_adminschool(self, idUser):
        query = "INSERT INTO `universitymanagement`.`adminschool` (`idUser`) VALUES (%s) "
        self.cursor.execute(query, (idUser,))
        self.conn.commit()

    def add_adminapp(self, idUser):
        query = "INSERT INTO `universitymanagement`.`adminapp` (`idUser`) VALUES (%s) "
        self.cursor.execute(query, (idUser,))
        self.conn.commit()

    def get_idAdmin(self, idUser):
        query = "SELECT idAdminSchool FROM adminschool WHERE idUser = %s"
        self.cursor.execute(query, (idUser, ))
        result = self.cursor.fetchone()
        self.cursor.fetchall()
        return result[0]

    def check_user(self, username, password):
        query = "SELECT idUser FROM user WHERE userName = %s AND password = %s"
        query1 = "SELECT idUser FROM student WHERE idUser = %s"
        query2 = "SELECT idUser FROM adminapp WHERE idUser = %s"
        query3 = "SELECT idUser FROM adminschool WHERE idUser = %s"
        self.cursor.execute(query, (username, password))
        result = self.cursor.fetchone()
        self.cursor.fetchall()
        if result:
            self.cursor.execute(query1, (result[0],))
            student = self.cursor.fetchone()
            if student:
                return 0, result[0]
            else:
                self.cursor.execute(query2, (result[0],))
                adminapp = self.cursor.fetchone()
                if adminapp:
                    return 1, result[0]
                self.cursor.execute(query3, (result[0],))
                adminschool = self.cursor.fetchone()
                if adminschool:
                    return 2, result[0]
                return -1, None
        else:
            return -1, None


# Sử dụng class
if __name__ == "__main__":
    model = UserModel()

    # Thêm một trường mới
    # model.add_university("University A", "New York")
    # model.add_university("University B", "California")

    # Lấy và in danh sách các trường
