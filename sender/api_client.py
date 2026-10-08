import json
import os

DB_FILE = "db.txt"

def save_to_file_db(payload):
    """
    Ghi một bản ghi provenance vào file db.txt dưới dạng JSON.
    """
    try:
        # Mở file ở chế độ 'a' (append - ghi nối tiếp vào cuối file)
        with open(DB_FILE, "a", encoding="utf-8") as f:
            # Chuyển payload dict thành chuỗi JSON trên 1 dòng
            line = json.dumps(payload, ensure_ascii=False)
            f.write(line + "\n")
        print(f"Đã lưu thành công bản ghi vào {DB_FILE}!")
        return True
    except Exception as e:
        print(f"Lỗi khi ghi vào db.txt: {e}")
        return False