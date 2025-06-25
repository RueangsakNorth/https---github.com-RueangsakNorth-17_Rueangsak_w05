import os
from pathlib import Path

# os_name = os.name
# os_path = os.getcwd()
# os_user = os.getenv("username")
# print(os_path)
# print(os_user)

current_path = Path.cwd()

# สร้างโพเดอร์
make_folder = current_path / "test456.py"
make_folder.mkdir(exist_ok=True)

# สร้างไฟล์
make_file = current_path / "test456.txt"
make_file.write_text("from datetime import datetime,date, timedelta")
make_file.stat()
print(f"{make_file.stat().st_size}")

content = make_file.read_text()

content_test = make_file
content = content_test.read_text
print(content)


