import random
from dataclasses import dataclass
from typing import List

GRADES_PER_STUDENT = 5


@dataclass
class Student:
    identifier: int
    name: str
    final_grades: List[int]
    is_promoted: bool = False

    @property
    def grades_avg(self) -> float:
        return sum(self.final_grades) / len(self.final_grades)

    def __str__(self) -> str:
        return f"Student with ID: {self.identifier} | promoted: {self.is_promoted} | grades_avg: {self.grades_avg}"


def generate_students(number_of_students: int) -> List[Student]:
    students = []
    for student_id in range(number_of_students):
        student_grades = [random.randint(1, 6) for _ in range(GRADES_PER_STUDENT)]
        students.append(
            Student(
                identifier=student_id,
                name=f"Student-{student_id}",
                final_grades=student_grades
            )
        )
    return students


def print_students(students: List[Student]):
    for student in students:
        print(student)
    print("-" * 30)


# def student_cmp_key(student: Student) -> float:
#     return student.grades_avg


def run_example():
    students = generate_students(5)
    print_students(students)

    # students.sort()
    # print_students(students)

    # students.sort(key=student_cmp_key)
    # print_students(students)

    # students.sort(key=lambda student: student.grades_avg)
    # print_students(students)


if __name__ == '__main__':
    run_example()
