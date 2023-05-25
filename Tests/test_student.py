from context import src

def test_create_student_grade():
    student = src.Student()
    assert student.grades == [10]

def test_create_student_average():
    student = src.Student()
    assert student.academic_average == 10

def test_add_grades():
    student = src.Student()
    student.add_grade(12)
    assert student.academic_average == 12