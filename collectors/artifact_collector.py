import hashlib
import os

def get_file_provenance(file_path):
    """
    Doc tep tin, tinh ma bam SHA-256 va trich xuat metadata
    de tao node Entity (DatasetVersion / Figure).
    """
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"Khong tim thay tep: {file_path}")

    # Tinh toan ma bam SHA-256
    sha256 = hashlib.sha256()
    with open(file_path, "rb") as f:
        while chunk := f.read(8192):
            sha256.update(chunk)
    file_hash = sha256.hexdigest()

    file_name = os.path.basename(file_path)
    file_size = os.path.getsize(file_path)

    return {
        "fileHash": file_hash,
        "name": file_name,
        "provType": "Entity",
        "sizeBytes": file_size,
        "filePath": os.path.abspath(file_path)
    }

if __name__ == "__main__":
    # Chay thu nghiem bang cach doc chinh file requirements.txt
    try:
        sample_file = r"D:\Program\Buget"
        data = get_file_provenance(sample_file)
        print("--- KET QUA THU THAP ARTIFACT (SHA-256) ---")
        for key, value in data.items():
            print(f"{key}: {value}")
    except Exception as e:
        print(f"Loi: {e}")