# Bài 1: Nhập 1 số nhuyên từ bàn phím. Nếu đó là số chẵn, in ra màn hình 'đây là số chẵn', các trường hợp còn lại in ra 'đây là số lẻ'.
n = int(input("Nhập một số nguyên: "))
if n % 2 == 0:
    print("Đây là số chẵn")
else:
    print("Đây là số lẻ")

# Bài 2: Viết chương trình nhập số điểm của 3 bạn học sinh, in ra màn hình bạn có điểm thấp nhất và bạn có điểm cao nhất.
scores = [8, 9, 9.5, 6, 7.5, 10, 5]
min_score = min(scores)
max_score = max(scores)
for i in range(len(scores)):
    if scores[i] == min_score:
        print(f"Bạn có điểm thấp nhất: {min_score} tại vị trí {i}")
    if scores[i] == max_score:
        print(f"Bạn có điểm cao nhất: {max_score} tại vị trí {i}")

# Bài 3: Quy đổi thời gian. Nhập vào số giây, in ra màn hình sau chuyển đổi
# VD: 3661s = 1h 1m 1s
time = int(input("Nhập số giây: "))
hours = time // 3600
minites = (time % 3600) // 60
seconds = time % 60
print(f"{time}s = {hours}h {minites}m {seconds}s")

# Bài 4: Nhập 2 số nguyên a và b. Tính tổng các số lẻ trong khoảng [a, b] hoặc ngược lại (nếu b<a).
a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))
sum_odd = 0

if a >= b:
    for i in range(b, a + 1):
        if i % 2 != 0:
            sum_odd += i
else:
    for i in range(a, b + 1):
        if i % 2 != 0:
            sum_odd += i

print(f"Tổng các số lẻ trong khoảng [{a}, {b}] là: {sum_odd}")

# Bài 5: Nhập vào số nguyên dương n. Tính tổng tất cả các chữ số của n
# VD: input: 123 - output: 6
n = int(input("Nhập số nguyên dương n: "))
sum_digits = 0
while n > 0:
    digit = n % 10
    sum_digits += digit
    n = n // 10
print(f"Tổng các chữ số của số nguyên dương là: {sum_digits}")

# Bài 6: Viết một chương trình cho phép người dùng nhập n phần tử. Sau đó thêm các phần tử vừa nhập vào mảng và in ra màn hình mảng đó.
n = int(input("Nhập số phần tử bạn muốn thêm vào mảng: "))
arr = []
for i in range(n):
    a = input(f"Nhập phần tử thứ {i + 1}: ")
    arr.append(a)
print("Mảng sau khi thêm các phần tử là:", arr)

# Bài 7: Cho 1 danh sách gồm các số nguyên từ 10 tến 30. In ra màn hình tổng các số chẵn trong danh sách.
arr = []
for i in range(10, 31):
    arr.append(i)
sum_even = 0
for num in arr:
    if num % 2 == 0:
        sum_even += num
print(f"Tổng các số chẵn trong danh sách là: {sum_even}")

# Bài 8: Tạo Mysterious Game
# Yêu cầu: tạo ra 1 số đặc biệt để đoán (random)
# Người chơi cần nhập đến khi nào đoán đúng số đặc biệt thì dừng game
import random
mysterious_number = random.randint(1, 100)
guess = int(input("Nhập dự đoán của bạn: "))
count = 1
while guess != mysterious_number:
    if guess < mysterious_number:
        print("Số bạn đoán nhỏ hơn số đặc biệt.")
    else:
        print("Số bạn đoán lớn hơn số đặc biệt.")

    guess = int(input("\nHãy nhập lại dự đoán của bạn: "))
    count += 1
    
print(f'Bạn đã đoán đúng sau {count} lần thử!')