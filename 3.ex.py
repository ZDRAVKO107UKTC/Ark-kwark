def class_room(**students):
    for student, grades in students.items():
        print(student)
        for grade in grades:
            print(grade)

class_room(
    Спиридон=[2, 3, 3, 4, 6],
    Стамат=[6, 6, 6, 2],
    Анджелина=[3, 3, 4, 3, 5]
)