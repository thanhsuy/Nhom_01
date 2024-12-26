import mysql.connector


class UniversityModel:
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

    def get_all_universities(self):
        # Lấy tất cả các trường
        query = "SELECT * FROM university"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def get_all_universities_by_name(self, name):
        # Lấy tất cả các trường
        query = "SELECT * FROM university WHERE nameUniversity LIKE %s"
        search_name = f"%{name}%"
        self.cursor.execute(query, (search_name,))
        return self.cursor.fetchall()

    def get_university_id(self, idAdmin):
        # Lấy tất cả các trường
        query = "SELECT idUniversity FROM university WHERE idAdmin = %s"
        self.cursor.execute(query, (idAdmin,))
        result = self.cursor.fetchone()
        self.cursor.fetchall()
        return result[0]

    def get_university_by_id(self, idUni):
        # Lấy tất cả các trường
        query = "SELECT * FROM university WHERE idUniversity = %s"
        self.cursor.execute(query, (idUni,))
        result = self.cursor.fetchone()
        self.cursor.fetchall()
        return result

    def get_universities_by_user(self, idUser):
        # Lấy tất cả các trường
        query = "SELECT * FROM university WHERE idAdmin = %s"
        self.cursor.execute(query, (idUser,))
        result = self.cursor.fetchone()
        self.cursor.fetchall()
        return result

    def get_university_by_name(self, name):
        # Lấy tất cả các trường
        query = "SELECT * FROM university WHERE nameUniversity = %s"
        self.cursor.execute(query, (name,))
        result = self.cursor.fetchone()
        self.cursor.fetchall()
        return result

    def get_name_universities(self):
        # Lấy tất cả các trường
        query = "SELECT nameUniversity FROM university"
        self.cursor.execute(query)
        all_name = []
        for i in self.cursor.fetchall():
            all_name.append(i[0])
        return all_name

    def add_university(self, name, location, region, focus, country_fee, global_fee, SAT, TOEFL, description, idUser):
        # Thêm một trường mới
        query = ("INSERT INTO `universitymanagement`.`university` (`nameUniversity`, `location`, `region`, `size`, "
                 "`focus`, `res`, `status`, `academicReputation`, `employerReputation`, `facultyStudent`, "
                 "`citationsPerFaculty`, `internationalFaculty`, `internationalStudents`, "
                 "`internationalResearchNetwork`, `employeeOutcomes`, `sustainability`, `domesticStudentsFee`, "
                 "`internationalStudentsFee`, `SAT`, `TOEFL`, `description`, `idAdmin`) VALUES (%s, %s, %s, "
                 "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, "
                 "%s);")
        self.cursor.execute(query, (name, location, region, "M", focus, "MD", "A", 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                    country_fee, global_fee, SAT, TOEFL, description, idUser))
        self.conn.commit()

    def edit_university(self, name, location, region, focus, country_fee, global_fee, SAT, TOEFL, description, idUser):
        # Thêm một trường mới
        query = ("UPDATE `universitymanagement`.`university` SET `nameUniversity` = %s, `location` = %s, `region` = "
                 "%s, `size` = %s, `focus` = %s, `res` = %s, `status` = %s, `domesticStudentsFee` = %s, "
                 "`internationalStudentsFee` = %s, `SAT` = %s, `TOEFL` = %s, `description` = %s WHERE ("
                 "`idAdmin` = %s);")
        self.cursor.execute(query, (name, location, region, "M", focus, "MD", "A",
                                    country_fee, global_fee, SAT, TOEFL, description, idUser))
        self.conn.commit()

    def evaluate_university(self, acaRe, empRe, facSt, citPe, intFa, intSt, intRe, empOu, sus, idUni):
        query = ("UPDATE `universitymanagement`.`university` SET `academicReputation` = %s, `employerReputation` = "
                 "%s, `facultyStudent` = %s, `citationsPerFaculty` = %s, `internationalFaculty` = %s, "
                 "`internationalStudents` = %s, `internationalResearchNetwork` = %s, `employeeOutcomes` = %s, "
                 "`sustainability` = %s WHERE (`idUniversity` = %s);")
        self.cursor.execute(query, (acaRe, empRe, facSt, citPe, intFa, intSt, intRe, empOu, sus, idUni))
        self.conn.commit()

    def del_university_by_id(self, idUni):
        query = "DELETE FROM `universitymanagement`.`university` WHERE (`idUniversity` = %s);"
        self.cursor.execute(query, (idUni,))
        self.conn.commit()


# Sử dụng class
if __name__ == "__main__":
    model = UniversityModel()

    # Thêm một trường mới
    # model.add_university("University A", "New York")
    # model.add_university("University B", "California")

    # Lấy và in danh sách các trường
    universities = model.get_all_universities()
    for uni in universities:
        print(uni)
