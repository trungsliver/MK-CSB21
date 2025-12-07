arr = [64, 25, 12, 22, 11, 90, 34, 78, 56, 43]

# ========= SELECTION SORT ==========
def selection_sort(arr):        # Độ phức tạp: O(n^2)
    # Duyệt từ phần từ đầu tiên đên phần tử cuối cùng
    for i in range(len(arr)):
        # Giả sử phần tử min nằm ở vị trí i
        min_index = i
        # Tìm vị trí phần tử nhỏ nhất trong phần còn lại
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        # Đổi chỗ arr[i] với phần tử nhỏ nhất tìm được
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

print("Selection Sort:", selection_sort(arr))