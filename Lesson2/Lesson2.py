# =========== Vòng lặp hữu hạn - vòng lặp for ===========

# Cú pháp đầy đủ: range(start, stop, step)
    # start: số bắt đầu, không bắt buộc (mặc định là 0)
    # stop: số kết thúc, bắt buộc
    # step: bước nhảy, không bắt buộc (mặc định là 1)
# Lưu ý: chạy từ start đến stop-1

# TH1: range(start, stop, step)
for i in range(1, 10, 2):
    print(i)

# TH2: range(start, stop)
for i in range(5, 15):
    print(i, end=' ')

# TH3: range(stop)
for i in range(7):
    print(i)

# ============= Vòng lặp vô hạn - vòng lặp while =============
    # Đặc điểm: chạy đến khi điều kiện sai
    # Cú pháp:
i = 0
while i <= 5:
    print(i, end=' ')
    i += 1      # i = i + 1 

# =========== Danh sách ===========
# Danh sách: array / list
# Thao tác CRUD: Create - Read - Update - Delete

# Create - Khởi tạo
    # Tạo danh sách rỗng (không có phần tử)
arr = []
    # Tạo danh sách có phần tử
csb21 = ["Minh Anh", "Duy Anh", "Lâm Khánh", "Tuấn Linh", "Thu Hương"]

# Read - Duyệt, hiện phần tử
    # len() - trả về độ dài / số lượng phần tử
print(f"\nSố lượng phần tử trong csb21: {len(csb21)}")
    # hiển phần tử bằng chỉ số index
print("Phần tử đầu tiên:", csb21[0])
print("Phần tử cuối cùng:", csb21[-1])
    # Duyệt và hiện các phần tử
        # Cách 1: Hiện cả index và value 
for i in range(len(csb21)):
    print(f"Index {i}, Value: {csb21[i]}")
        # Cách 2: Hiện value
for item in csb21:
    print("Value:", item)
        # Cách 3: Dùng hàm có sẵn enumerate()
for index, value in enumerate(csb21):
    print(f"Index {index}, Value: {value}")
    # Hiện phần tử (để test)
print(csb21)

# Update - Cập nhật phần tử
    # Thêm phần tử vào cuối danh sách - append()
csb21.append("Duc Trung")
    # Thêm phần tử vào vị trí chỉ định - insert(index, value)
csb21.insert(2, "Imposter")
    # Sửa phần tử tại vị trí chỉ định
csb21[2] = "Imposter (đã sửa)"

# Delete - Xóa phần tử
    # Xóa bằng value - remove(value)
csb21.remove("Duc Trung")
    # Xóa bằng index - pop(index)
csb21.pop(2)
    # Xóa toàn bộ phần tử - clear()
csb21.clear()

# Sắp xếp phần tử
num_list = [5, 2, 9, 7, 1, 6, 3, 8, 4]
    # Sắp xếp tăng dần - sort()
num_list.sort()
    # Sắp xếp giảm dần - sort(reverse=True)
num_list.sort(reverse=True)

# Tìm phần tử lớn nhất & nhỏ nhất
print("Phần tử lớn nhất:", max(num_list))
print("Phần tử nhỏ nhất:", min(num_list))