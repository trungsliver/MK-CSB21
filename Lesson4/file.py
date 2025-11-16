import json

students = [
    {"name": "Minh Anh", "age": 15, "gender": "Male"},
    {"name": "Thu Hương", "age": 16, "gender": "Female"},
    {"name": "Lâm Khánh", "age": 15, "gender": "Male"},
    {"name": "Tuấn Linh", "age": 16, "gender": "Male"},
    {"name": "Đức Trung", "age": 2, "gender": "Male"}
]

# Ghi nội dung vào file JSON
with open("data.json", "w", encoding="utf-8") as f:
    # indent=4: định dạng giúp file dễ đọc
    # ensure_ascii=False: để giữ nguyên ký tự Unicode (giữ nguyên tiếng việt)
    json.dump(students, f, indent=4, ensure_ascii=False)

# Đọc nội dung từ file JSON
with open("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)
print(data)
