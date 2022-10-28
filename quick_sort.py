# 73173004
from dataclasses import dataclass, field


@dataclass(order=True)
class Student:
    score: int = field(compare=False)
    score_to_compare: int = field(init=False, repr=False)
    penalty: int
    login: str

    def __post_init__(self):
        self.score_to_compare = self.score * (-1)

    def __str__(self):
        return self.login

def partition(stud_list, low, high):
    # print(f' patition low-{low}, high {high}')
    i = low
    pivot: Student = stud_list[high]
    for j in range(low, high):
        if stud_list[j] <= pivot:
            stud_list[i], stud_list[j] = stud_list[j], stud_list[i]
            i += 1
    stud_list[i], stud_list[high] = stud_list[high], stud_list[i]
    return i


def quicksort_inplace(student_list, low: int = 0, high: int = None):
    # print(f'low-{low}, high {high}')
    if high is None:
        high = len(student_list) - 1
    if low < high:
        # print(f'if low < high:')
        pivot_index = partition(student_list, low, high)
        quicksort_inplace(student_list, low, pivot_index - 1)
        quicksort_inplace(student_list, pivot_index, high)
    return student_list

def read_input():
    count_student = int(input())
    student_list = []
    for _ in range(count_student):
        temp = input().split()
        student = Student(
            login=temp[0], score=int(temp[1]),
            penalty=int(temp[2]))
        student_list.append(student)
    return student_list


def main():
    student_list = read_input()
    sort_stud_list = quicksort_inplace(student_list)
    # [print(st.login) for st in student_list]
     
    print(*sort_stud_list, sep='\n')

if __name__ == '__main__':
    main()
