# OOP: Object-Oriented Programming
# Lập trình hướng đối tượng

# Tổng quát: OOP là cách mà chúng ta mô tả thế giới thực vào chương trình máy tính

# Class (lớp):          Đối tượng tổng quát
# Object (đối tượng):   Đối tượng cụ thể

# Ví dụ: mô phỏng Human (con người)
    # Thuộc tính (đặc điểm): tên, tuổi, giới tính, ...
    # Phương thức (hành động): ăn, ngủ, nói chuyện, ...

# Khai báo lớp đối tượng (class)
class Human:
    # Khởi tạo giá trị (thuộc tính) - đây là hàm có sẵn
    def __init__(self, name, age, gender):
        # name, age, gender là thuộc tính (đặc điểm)
        self.name = name      
        self.age = age        
        self.gender = gender  

    # Phương thức hiển thị thông tin
    def __str__(self):
        return f"{self.name} - {self.age} - {self.gender}"
    
    def display_info(self):
        print(f"""
===== MY INFO =====
Name: {self.name}
Age: {self.age}
Gender: {self.gender}
==================""")

# Khởi tạo đối tượng cụ thể
human1 = Human("Duc Trung", 2, "male")
human2 = Human("Minh Anh", 14, "male")
# Hiển thị thông tin
print(human1)
print("Name:", human1.name)
human1.display_info()
human2.display_info()