# ========== THUẬT TOÁN TÌM KIẾM ==========

arr = [2, 5, 3, 1, 9, 7, 4, 8, 6]
    # Tìm kiếm vị trí của phần tử có giá trị = 7
for i in range(len(arr)):       # O(n)
    if arr[i] == 7:
        print("Phần tử 7 nằm ở vị trí:", i)
        break

# Linear search - tìm kiếm tuần tự
def linnear_search(array, target):
    # Duyệt từng phần tử trong danh sách
    for i in range(len(array)):       # O(n)
        if array[i] == target:
            return i                  # Trả về vị trí tìm thấy
    return -1                         # Nếu không tìm thấy, trả về -1

    # test linear search
result = linnear_search(arr, 7)
if result != -1:
    print("Phần tử 7 nằm ở vị trí:", result)    
else:
    print("Phần tử 7 không được tìm thấy")