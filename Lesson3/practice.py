# Bài 1: Viết một hàm sum_odd(numbers) để tính tổng các số lẻ trong một danh sách numbers.
# 	YC1: Hàm nhận vào một danh sách các số nguyên.
# 	YC2: Hàm trả về tổng các số lẻ trong danh sách đó.
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def sum_odd(numbers):
    sum = 0                 # Khai báo biến lưu tổng
    for item in arr:        # Duyệt danh sách, cách 2 - chỉ có giá trị
        if item % 2 != 0:   # Kiểm tra số lẻ
            sum += item     # Cộng giá trị phần tử vào biến sum
    return sum              # Trả về giá trị sum khi duyệt xong vòng lặp

print("Tổng các số lẻ trong danh sách là:", sum_odd(arr))

# Bài 2: Viết một hàm count_words(s) để đếm số lượng từ trong một chuỗi s.
# 	YC1: Hàm nhận vào một chuỗi ký tự s.
# 	YC2: Hàm trả về số lượng từ trong chuỗi đó.

sentence = "Đây là lớp học lập trình tại MindX"

def count_words(s:str):
    # strip(): Loại bỏ khoảng trắng ở đầu và cuối chuỗi
    # split(): Tách chuỗi thành danh sách các từ dựa trên khoảng trắng
    arr = s.strip().split()
    return len(arr)  # Trả về độ dài của danh sách từ

print("Số lượng từ trong chuỗi là:", count_words(sentence))