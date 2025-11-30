#  Đề bài: Tạo Mysterious Game
    # Yêu cầu: tạo ra 1 số đặc biệt để đoán (random)
    # Người chơi cần nhập đến khi nào đoán đúng số đặc biệt thì dừng game

import random
number = random.randint(0,100)
# print('Số bí mật:', number)
count = 1
n = int(input('Nhập dự đoán của bạn: '))
while n != number:
    if n < number:
        print('Đoán sai, hãy nhập số lớn hơn!')
    if n > number:
        print('Đoán sai, hãy nhập số nhỏ hơn!')
    n = int(input('\nNhập dự đoán của bạn: '))
    count = count + 1
print(f'Bạn đã đoán đúng sau {count} lần nhập !!!')