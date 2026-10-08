import uuid
from datetime import datetime, timezone
from collectors.git_collector import get_git_provenance
from collectors.artifact_collector import get_file_provenance
from sender.api_client import send_provenance_payload

def run_pipeline(input_dataset_path, output_figure_path):
    print("--- 1. Thu thập thông tin mã nguồn (Git) ---")
    git_info = get_git_provenance(".")
    
    print("--- 2. Thu thập tệp đầu vào (Dataset) ---")
    dataset_info = get_file_provenance(input_dataset_path)
    
    print("--- 3. Thu thập tệp đầu ra (Figure/Artifact) ---")
    figure_info = get_file_provenance(output_figure_path)

    # Đóng gói thành một lượt chạy hoàn chỉnh (Execution Activity)
    execution_id = str(uuid.uuid4())
    now_iso = datetime.now(timezone.utc).isoformat()

    payload = {
        "execution": {
            "executionId": execution_id,
            "provType": "Activity",
            "name": "Model Training & Evaluation",
            "executedAt": now_iso
        },
        "codeRevision": git_info,
        "inputDataset": dataset_info,
        "outputFigure": figure_info
    }

    print("\n--- Gói dữ liệu đã đóng gói chuẩn bị gửi đi ---")
    print(payload)

    print("\n--- 4. Gửi về Backend ---")
    send_provenance_payload(payload)

if __name__ == "__main__":
    # Chạy thử với 2 file mẫu có sẵn trong thư mục
    dataset_sample = "requirements.txt"
    figure_sample = ".gitignore"
    
    run_pipeline(dataset_sample, figure_sample)