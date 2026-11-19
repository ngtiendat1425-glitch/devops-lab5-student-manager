"""
Student Manager — DevOps Lab 5
Module: Main Application
"""
from student import Student


def main():
    """Hàm chính của ứng dụng."""
    print("=" * 50)
    print("STUDENT MANAGER — DevOps Lab 5")
    print("=" * 50)

    # Tạo danh sách sinh viên mẫu
    students = [
        Student("SV001", "Nguyen Van A", 20, "K20"),
        Student("SV002", "Tran Thi B", 21, "K20"),
        Student("SV003", "Le Van C", 19, "K21"),
    ]

    # Hiển thị danh sách
    for student in students:
        print(f"  {student}")

    print(f"\nTotal: {len(students)} students")

        # Tim kiem sinh vien
    print("\n--- Tim kiem ---")
    search_student(students, "Van")


if __name__ == "__main__":
    main()

def search_student(students: list, keyword: str) -> list:
    """Tìm kiếm sinh viên theo tên hoặc mã."""

    results = []
    keyword_lower = keyword.lower()

    for s in students:
        if keyword_lower in s.name.lower() or keyword_lower in s.student_id.lower():
            results.append(s)

    if results:
        print(f"Tim thay {len(results)} sinh vien:")
        for s in results:
            print(f"  {s}")
    else:
        print(f"Khong tim thay sinh vien: {keyword}")

    return results