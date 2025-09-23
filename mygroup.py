def print_students(students):
    print(u"Имя".ljust(15), u"Фамилия".ljust(10), u"Экзамены".ljust(40), u"Оценки".ljust(20))
    for student in students:
        stud_av_mark = sum(student["marks"])/len(student["marks"])
        if stud_av_mark > av_mark:
            print(student["name"].ljust(15), student["surname"].ljust(10), str(student["exams"]).ljust(40), str(student["marks"]).ljust(20))

groupmates = [
    {
        "name": "Александр",
        "surname": "Попов",
        "exams": ["Математика", "Окружающий мир", "ПИС"],
        "marks": [4, 5, 2]
    },
    {
        "name": "Сеня",
        "surname": "Кузин",
        "exams": ["История", "Русский язык", "ПИС"],
        "marks": [4, 2, 1]
    },
    {
        "name": "Олег",
        "surname": "Азаров",
        "exams": ["МИС", "КИС", "Алгебра"],
        "marks": [5, 5, 5]
    },
    {
        "name": "Николай",
        "surname": "Николаев",
        "exams": ["ПИС", "Математика", "История"],
        "marks": [5, 4, 3]
    },
    {
        "name": "Петр",
        "surname": "Петров",
        "exams": ["Алгебра", "Русский язык", "МИС"],
        "marks": [2, 3, 1]
    }
]

av_mark = 3

print_students(groupmates)
