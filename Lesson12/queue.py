# ================== QUEUE - Hàng đợi ==================

# Khái niệm: cấu trúc dữ liệu
# Nguyên tắc hoạt động: FIFO (First In First Out) - Vào trước ra trước
# Ví dụ:
    # Xếp hàng đợi thanh toán trong siêu thị
    # Hàng đợi in tài liệu
    # Xe xếp hàng qua trạm thu phí

# Các thao tác cơ bản:
    # Khởi tạo:
        # Cách 1:
queue1 = []
        # Cách 2:
from collections import deque
queue2 = deque()