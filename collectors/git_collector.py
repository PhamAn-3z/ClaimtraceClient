import git

def get_git_provenance(repo_path="."):
    """
    Trích xuất commit hash và metadata của commit hiện tại
    để tạo node CodeRevision theo chuẩn PROV-DM.
    """
    repo = git.Repo(repo_path, search_parent_directories=True) 
    """search_parent_directories=True giúp tìm kiếm thư mục cha nếu không tìm thấy repo trong thư mục hiện tại."""
    commit = repo.head.commit
    """HEAD trong Git đại diện cho "trạng thái hiện tại bạn đang đứng". Dòng này lấy ra đúng lần commit mới nhất mà bạn vừa thực hiện."""
    
    return {
        "commitHash": commit.hexsha,
        "name": f"Code: Commit {commit.hexsha[:7]}",
        "provType": "Entity",
        "author": commit.author.name,
        "message": commit.message.strip(),
        "committedAt": commit.committed_datetime.isoformat()
    }

if __name__ == "__main__":
    try:
        data = get_git_provenance(".")
        print("--- KET QUA THU THAP GIT (CodeRevision) ---")
        for key, value in data.items():
            print(f"{key}: {value}")
    except Exception as e:
        print(f"Loi: {e}")