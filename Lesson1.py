# Hiển thị dữ liệu / In ra màn hình
print("Hello, World!")

# Khai báo biến số - declare variables
    # Lưu trữ dữ liệu
    # Có thể thay đổi được giá trị trong khi lập trình
name = "Duc Trung"
age = 2
a, b, c = 5, 10, 15         # Khai báo nhiều biến trong một dòng

# Kiểu dữ liệu cơ bản - Data Types
    # String: chuỗi ký tự / xâu ký tự
name = "Lâm Khánh"
    # int (integer): số nguyên
age = 3
    # float: số thực
height = 1.2
    # bool / boolean: True/False - Đúng/Sai
male = True

# Cách cách hiển thị dữ liệu
    # cách 1: Sử dụng dấu + (chỉ áp dụng với string)
print("Họ tên: " + name)
    # cách 2: Sử dụng dấu , 
print('Tuổi:', age)
    # Cách 3: Sử dụng f - truyền dữ liệu vào string
print(f"Tôi tên là {name}, tôi {age} tuổi.")
    # cách 4: Hiển thị trên nhiều dòng
print(f"""
======= THÔNG TIN =======
Họ tên: {name}
Tuổi: {age}
Chiều cao: {height}m
=========================""")

# Kiểm tra kiểu dữ liệu - type()
print("Kiểu dữ liệu của biến name:", type(name))
print("Kiểu dữ liệu của biến age:", type(age))
print("Kiểu dữ liệu của biến height:", type(height))
print("Kiểu dữ liệu của biến male:", type(male))

# Nhập dữ liệu từ bàn phím - input()
# food = input("Nhập đồ ăn bạn thích: ")
# print(type(food))
#     # Ép kiểu dữ liệu khi nhập
# score = float(input("Nhập điểm số của bạn: "))
# print(type(score))

# Các phép toán
    # Cơ bản:           + - * /
    # Chia lấy nguyên:  //
    # Chia lấy dư:      %
    # Lũy thừa:         **

# Toán tử quan hệ (phép so sánh) => True/False
    # ==  : bằng
print(5 == 5)      # True
print(5 == 3)      # False
    # !=  : khác
print(5 != 3)      # True
print(5 != 5)      # False
    # >   : lớn hơn
    # <   : nhỏ hơn
    # >=  : lớn hơn hoặc bằng
    # <=  : nhỏ hơn hoặc bằng

# Toán tử logic: and - or - not
    # Ví dụ trà sữa - gà rán

# Câu điều kiện
    # Dạng thiếu
age = int(input("Nhập tuổi của bạn: "))
if age >= 18:
    print("Bạn đã đủ 18 tuổi")

    # Dạng đủ
number = int(input("Nhập một số nguyên bất kỳ: "))
if number % 2 == 0:
    print(f"Số {number} là số chẵn")
else:
    print(number, "là số lẻ")

    # Dạng đa nhánh
        # [8, 10]: Giỏi, [6.5, 8): Khá, [5, 6.5): TB, [0, 5): Yếu
score = float(input("Nhập điểm số của bạn: "))
if 8 <= score <= 10:
    print('Giỏi')
elif 6.5 <= score < 8:
    print('Khá')
elif 5 <= score < 6.5:
    print('Trung bình')
elif 0 <= score < 5:
    print('Yếu')
else:
    print("Điểm số không hợp lệ")