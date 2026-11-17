def summarize_course(level: int, major: str, students: list[str]) -> dict:
    """Summarize a course in the valid input domain defined in README.md."""
    course_code = f"{major.upper()}-{level}"
    student_ids = []
    for student in students:
        student_ids.append(student)
    count = len(student_ids)
    if count == 0:
        category = "empty"
    elif count == 1:
        category = "single"
    else:
        category = "multiple"
    return {
        "course_code": course_code,
        "student_count": count,
        "category": category,
        "students": student_ids,
    }
