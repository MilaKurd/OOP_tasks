# Класс Студенты
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    # Метод добавления законченного курса
    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    # Метод оценки курса - задание № 2 => student оценивает курс
    def rate_lecture(self, lecturer, course, grade):
        if (isinstance(lecturer, Lecturer)
                and course in lecturer.courses_attached
                and course in self.courses_in_progress):
            if course in lecturer.grades:
                lecturer.grades[course].append(grade)
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    # Метод подсчета средней оценки - задание № 3 =>
    def _avg_grade(self):
        if not self.grades:
            return 0
        all_grades = [g for grades in self.grades.values() for g in grades]
        return sum(all_grades) / len(all_grades) if all_grades else 0

    # Вывод - задание № 3
    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за домашние задания: {self._avg_grade()}\n'
                f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
                f'Завершенные курсы: {", ".join(self.finished_courses)}')

    # возможность сравнивать между собой по средней оценке за домашнее задание - задание № 3 пункт 2
    def __eq__(self, other):
        if isinstance(other, Student):
            return self._avg_grade() == other._avg_grade()
        else:
            return 'Ошибка'

    # возможность сравнивать между собой по средней оценке за домашнее задание - задание № 3 пункт 2
    def __lt__(self, other):
        if isinstance(other, Student):
            return self._avg_grade() < other._avg_grade()
        else:
            return 'Ошибка'

# Родительский Класс Преподаватели
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

# Дочерний Класс Лекторы - задание № 1 => создали дочерний класс
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades = {}

    # Метод подсчета средней оценки - задание № 3
    def _avg_grade_lecture(self):
        all_grades = [g for grades in self.grades.values() for g in grades]
        return sum(all_grades) / len(all_grades) if all_grades else 0

    # Вывод - задание № 3
    def __str__(self):
        return(
            f'Имя: {self.name}\n'
              f'Фамилия: {self.surname}\n'
              f'Средняя оценка за лекции: {self._avg_grade_lecture()}'
        )
    # возможность сравнивать между собой по средней оценке за лекции - задание № 3 пункт 2
    def __eq__(self, other):
        if isinstance(other, Lecturer):
            return self._avg_grade_lecture() == other._avg_grade_lecture()
        else:
            return 'Ошибка'

    # возможность сравнивать между собой по средней оценке за лекции - задание № 3 пункт 2
    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self._avg_grade_lecture() < other._avg_grade_lecture()
        else:
            return 'Ошибка'

# Дочерний Класс Рецензенты - задание № 1 => создали дочерний класс
class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    # Метод вывода информации о Рецензентах => задание № 3
    def __str__(self):
        return(
            f'Имя: {self.name}\n'
            f'Фамилия: {self.surname}'
        )

    # Метод выставления оценок за домашнюю работу - Задание № 2 => только reviewer выставляет оценки за домашнюю работу
    def rate_hw(self, student, course, grade):
        if (isinstance(student, Student)
                and course in self.courses_attached
                and course in student.courses_in_progress):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
# Задание № Функция 1: средняя оценка за домашние задания по всем студентам в рамках курса
def avg_hw_course(students, course_name):
    grades = []
    for s in students:
        if course_name in student.grades:
            grades.extend(student.grades[course_name])
    return sum(grades) / len(grades) if grades else 0


# Функция 2: средняя оценка за лекции всех лекторов в рамках курса
def avg_lecture_course(lecturers, course_name):
    grades = []
    for l in lecturers:
        if course_name in lecturer.grades:
            grades.extend(lecturer.grades[course_name])
    return sum(grades) / len(grades) if grades else 0


# Задание № 1 - выполнено, проверено
lecturer = Lecturer('Иван', 'Иванов')
reviewer = Reviewer('Пётр', 'Петров')
print(isinstance(lecturer, Mentor)) # True
print(isinstance(reviewer, Mentor)) # True
print(lecturer.courses_attached)    # []
print(reviewer.courses_attached)    # []

# Задание № 2 - выполнено, проверено
student = Student('Алёхина', 'Ольга', 'Ж')
student.courses_in_progress += ['Python', 'Java']
lecturer.courses_attached += ['Python', 'C++']
reviewer.courses_attached += ['Python', 'C++']
print(student.rate_lecture(lecturer, 'Python', 7))  # None
print(student.rate_lecture(lecturer, 'Java', 8))  # Ошибка
print(student.rate_lecture(lecturer, 'С++', 8))  # Ошибка
print(student.rate_lecture(reviewer, 'Python', 6))  # Ошибка
print(lecturer.grades)  # {'Python': [7]}

# Задание № 4: по 2 экземпляра каждого класса
lecturer_1 = Lecturer('Олег', 'Олегов')
lecturer_2 = Lecturer('Илья', 'Ильин')

reviewer_1 = Reviewer('Василий', 'Васильев')
reviewer_2 = Reviewer('Алексей', 'Алексеев')

student_1 = Student('Алёхина', 'Ольга', 'Ж')
student_2 = Student('Петра', 'Петрова', 'Ж')

# Назначение курсо
lecturer_1.courses_attached += ['Python', 'C++']
lecturer_2.courses_attached += ['Python', 'Java']

reviewer_1.courses_attached += ['Python', 'C++', 'Git']
reviewer_2.courses_attached += ['Python', 'Java']

student_1.courses_in_progress += ['Python', 'Java']
student_2.courses_in_progress += ['Python', 'Git']

# Вызов методов
student_1.add_courses('Введение в программирование')
student_2.add_courses('Введение в программирование')

# Оценки за домашние задания
reviewer_1.rate_hw(student_1, 'Python', 9)
reviewer_2.rate_hw(student_1, 'Java', 8)
reviewer_1.rate_hw(student_2, 'Git', 10)
reviewer_2.rate_hw(student_2, 'Python', 8)

# Оценки лекторам от студентов
student_1.rate_lecture(lecturer_1, 'Python', 9)
student_1.rate_lecture(lecturer_2, 'Java', 8)
student_2.rate_lecture(lecturer_1, 'Python', 10)
student_2.rate_lecture(lecturer_2, 'Python', 9)

# Вывод информации
print(student_1)
print(student_2)
print(reviewer_1)
print(reviewer_2)
print(lecturer_1)
print(lecturer_2)

# Сравнения
print('student_1 > student_2:', student_1 > student_2)
print('lecturer_1 < lecturer_2:', lecturer_1 < lecturer_2)

# Подсчёт средних оценок по курсам
print('Средняя оценка за ДЗ по Python:', avg_hw_course([student_1, student_2], 'Python'))
print('Средняя оценка за лекции по Python:', avg_lecture_course([lecturer_1, lecturer_2], 'Python'))