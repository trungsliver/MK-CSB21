# ============== String - Chuỗi / xâu ký tự ==============
name = "Duc Trung"

    # len(): độ dài string
print("Độ dài chuỗi:", len(name)) 

    # Ký tự thứ n trong chuỗi
print("Ký tự đầu tiên: ", name[0])
print("Ký tự cuối cùng: ", name[-1])
print("Ký tự thứ 5: ", name[4])

    # Duyệt string
        # Cách 1: Dùng cả index và value
for i in range(len(name)):
    print(f"Ký tự {i}: {name[i]}")

        # Cách 2: Chỉ dùng value
for char in name:
    print(char, end=" ")

    # Xâu con (Substring)
str1 = "MinhAnhDepTrai"
str2 = "MinhAnh"
str3 = "VipPro" 

        # Kiểm tra xâu con
print(str2 in str1)  # True
print(str3 in str1)  # False

    # Tìm vị trí xâu con
print(str1.find(str2))      # 0
print(str1.find("VipPro"))  # 7
print(str1.find(str3))      # -1

    # Slicing - cắt chuỗi
name = "NguyenTuanLinh"
        # Cắt từ đầu string
print(name[:6])    # Nguyen
        # Cắt đến cuối string
print(name[6:])    # TuanLinh
        # Cắt giữa string
print(name[6:10])  # Tuan

    # strip(): loại bỏ khoảng trắng ở đầu và cuối
name = "    Thu Huong    "
print(name) 
print(name.strip())  # "Thu Huong"

    # replace(): thay thế ký tự hoặc xâu con
song = "baby shark doo doo doo doo doo doo"
        # Thay thế toàn bộ
song2 = song.replace("doo", "hi")
print(song2)
        # Thay thế với số lượng chỉ định
song3 = song.replace("doo", "hi", 3)
print(song3)

    # join(): nối chuỗi
arr = ['r','o','n','a','l','d','o']
str1 = ' '.join(arr)
str2 = ''.join(arr)
str3 = '-'.join(arr)
print(str1)  # r o n a l d o
print(str2)  # ronaldo  
print(str3)  # r-o-n-a-l-d-o