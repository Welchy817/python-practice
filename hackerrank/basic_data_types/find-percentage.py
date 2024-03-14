if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    total = float()
    avg = float()
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    for student in student_marks:
        if student == query_name:
            total = sum(student_marks[student])
            avg = total / 3.00
            print(format(avg, ".2f"))