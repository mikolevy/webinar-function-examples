import random
from dataclasses import dataclass, field
from typing import List, Callable

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
        return f"Student with ID: {self.identifier} | promoted: {self.is_promoted} | grades_avg: {self.grades_avg:.2f}"


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


@dataclass
class StudyYear:
    students: List[Student]
    promoted_students: List[Student] = field(default_factory=list)
    is_completed: bool = False

    def complete(self, promotion_policy: Callable[[Student], bool]):
        for student in self.students:
            is_promoted = promotion_policy(student)

            if is_promoted:
                self.promoted_students.append(student)
                student.is_promoted = True
            else:
                student.is_promoted = False

        self.is_completed = True



def run_example():
    students = generate_students(5)
    first_study_year = StudyYear(students)

    # first_study_year.complete(standard_promote_policy)
    # print_students(first_study_year.promoted_students)

    first_study_year.complete(strict_promote_policy)
    print_students(first_study_year.promoted_students)


def standard_promote_policy(student: Student) -> bool:
    return 1 not in student.final_grades


def strict_promote_policy(student: Student) -> bool:
    if 1 in student.final_grades:
        return False

    return student.grades_avg > 4


if __name__ == '__main__':
    run_example()
