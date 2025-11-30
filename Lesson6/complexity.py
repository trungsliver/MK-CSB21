# ALGORITHM COMPLEXITY - ĐỘ PHỨC TẠP CỦA THUẬT TOÁN

# Biểu diễn bằng Big-O Notation
    # Độ phức tạp (O) = n * số phép toán
    # n là kích thước dữ liệu đầu vào

# Mô tả hành vi xử lý (thời gian tính toán, bộ nhớ cần dùng)

# Ví dụ về độ phức tạp:

# O(1) - Độ phức tạp hằng số (gán, nhập, xuất)
name = 25
age = input()
print(name)

# O(n) - tuyến tính
arr = [1, 2, 3, 4, 5]       # n = 5
for i in arr:               
    print(i)                # in ra phần tử (5 lần)

# O(n^2) - bình phương
for i in arr:               # vòng lặp ngoài (5 lần)
    for j in arr:           # vòng lặp trong (5 lần)
        print(i, j)        # in ra cặp phần tử (5 * 5 = 25 lần)

# O(log n) - logarit
    # Giống game đoán số (luôn chia đôi)

# Ví dụ:
students = ['Minh Anh', 'Thu Hương', 'Lâm Khánh', 'Duy Anh', 'Tuấn Linh']

for stu1 in students:
    for stu2 in students:
        print(stu1, 'bắt tay' ,stu2)  # O(n^2)