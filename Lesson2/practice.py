#  ========== Vòng lặp FOR ==========
# Bài 1: Nhập 2 số nguyên a và b từ bàn phím.
# In ra các số nguyên trong khoảng [a, b]

# a = int(input("Nhập số nguyên a: "))
# b = int(input("Nhập số nguyên b: "))
# for i in range(a, b + 1):
#     print(i, end=' ')

# Bài 2: Nhập 1 số nguyên a trong khoảng [1, 10]
# In ra màn hình bảng cửu chương a
# a = int(input("Nhập số nguyên a: "))
# for i in range(1, 11):
#     print(f"{a} x {i} = {a * i}")

# Bài 3: In ra màn hình bảng cửu chương từ 2 => 9
# for a in range(2, 10):
#     print(f"Bảng cửu chương {a}:")
#     for i in range(1, 11):
#         print(f"{a} x {i} = {a * i}")

# ========== Vòng lặp WHILE ==========
# Bài 1: Nhập số nguyên n trong khoảng [0,100]
# nếu nhập sai (n<0 hoặc n>100) thì yêu cầu nhập lại
# n = int(input("Nhập số nguyên n (0<=n<=100): "))
# while n < 0 or n > 100:
#     print("Nhập sai! Vui lòng nhập lại.")
#     n = int(input("\nNhập số nguyên n (0<=n<=100): "))
# print(f"Nhập n = {n} thành công!")