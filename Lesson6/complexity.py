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