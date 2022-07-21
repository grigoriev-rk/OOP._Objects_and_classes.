"""
The HW for the lecture 'Objects and classes. Encapsulation, inheritance and polymorphism'.
For the purpose of focusing on OOP, there is no user interface, data entry, or data correction.
"""

from pprint import pprint

class Student:
    
    def __init__(self, name, surname, gender):           # Initial Student class initialization. 
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    
    def rate_hw(self, lecturer, course, grade):          # Method of rating lecturers (task 2).
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
    
    def __str__ (self):                                   # Overloading the str method for Student class (task 3).
        __name = f'\nИмя: {self.name}\n'
        __surname = f'Фамилия: {self.surname}\n'          
        average_rate = f'Средняя оценка за лекции: {rate_count(self)}\n'    # Сalling an external function common for Student and Lecturer classes.        
        __courses_list = (", ".join(self.courses_in_progress))
        __courses_in_progress = f'Курсы в процессе изучения: {__courses_list}\n' 
        __finished_courses_list = (", ".join(self.finished_courses))
        __finished_courses = f'Завершенные курсы: {__finished_courses_list}\n' 
        __grades = f'Оценки: {self.grades}\n'
        return '{}{}{}{}{}{}'.format(__name, __surname, average_rate, __courses_in_progress, __finished_courses, __grades)
    
    def __lt__(self, other):                              # Overloading less than method for comparing students by rate (task 3).
        if not isinstance (other, Student):
            print('\nЭто не студент!')
            return
        return rate_count(self) < rate_count(other)

        
class Mentor:                                             # Parent class for Lecturer and Reviewer classes (task 1).
    def __init__(self, name, surname):                    # Initial Mentor class initialization.
        self.name = name
        self.surname = surname
        self.courses_attached = []

        
class Lecturer (Mentor):                                  # Inherited Lecturer class from Mentor class (task 1).
    def __init__(self, name, surname):                    # Initial Lecturer class initialization.
        super().__init__(name, surname)
        self.grades = {}                                  # New Lecturer class attribute, lucturers has grades (task 2).

    def __str__ (self):                                   # Overloading the str method for Lecturer class (task 3).
        __name = f'\nИмя: {self.name}\n'
        __surname = f'Фамилия: {self.surname}\n'          
        __average_rate = f'Средняя оценка за лекции: {rate_count(self)}\n'          
        return '{}{}{}'.format(__name, __surname, __average_rate)

    def __lt__(self, other):                              # Overloading less than method for comparing lecturers by rate (task 3).
        if not isinstance (other, Lecturer):
            print('\nЭто не лектор!')
            return
        return rate_count(self) < rate_count(other)

    
class Reviewer (Mentor):                                  # Inherited Reviewer class from Mentor class (task 1).      
    
    def rate_hw(self, student, course, grade):            # Method of rating students hw (task 2).
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__ (self):                                   # Overloading the str method for Reviewer class (task 3).
        __name = f'\nИмя: {self.name}\n'
        __surname = f'Фамилия: {self.surname}\n'          
        return '{}{}'.format(__name, __surname)


def rate_count(__person):                                 # Common method for calculating student or lecturer average rate (task 3).
    all_rate_list = list(__person.grades.values())
    number_of_elements = sum([len(element) for element in all_rate_list])
    total_count = 0 
    for _ in range (0, len(all_rate_list)):
        count = sum(all_rate_list[_])
        total_count += count
    return (round((total_count/number_of_elements), 2))


def average_rate_course(__person_list, __course_list):    # Common method for calculating student or lecturer average rate of course (task 3).

    for __course in __course_list:          
        count_all = 0
        count = 0
        for person in __person_list:
            print(person.name, person.surname, person.grades[__course])
            count_all += ((sum(person.grades[__course]))/3)
            count +=1
        print (f'Cредний бал за курс {__course} равен: {round((count_all/count), 2)}')

def attached_courses(__person_list):    # Common method for printing Menotrs attached courses.
    for person in __person_list:
        print(f'{person.name} {person.surname} {person.courses_attached}')
    #return('') 

    
best_student = Student('Ruoy', 'Eman', 'your_gender')               # Part of the students personal information.
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']
best_student.finished_courses += ['Введение в программирование']

student_1 = Student('Bender', 'Rodriguez', 'bendergender')
student_1.courses_in_progress += ['Python']
student_1.courses_in_progress += ['Git']
student_1.finished_courses += ['Введение в программирование']

student_2 = Student('Philip J.', 'Fry', 'humangender')
student_2.courses_in_progress += ['Python']
student_2.courses_in_progress += ['Git']
student_2.finished_courses += ['Введение в программирование']


cool_reviewer = Reviewer('Amy', 'Wong')                              # Part of the reviewers personal information.
cool_reviewer.courses_attached += ['Python']
cool_reviewer.courses_attached += ['Git']

reviewer_1 = Reviewer('Some', 'Buddy')   
reviewer_1.courses_attached += ['Python']
reviewer_1.courses_attached += ['Git']

reviewer_2 = Reviewer('Once', 'Toldme')   
reviewer_2.courses_attached += ['Python']
reviewer_2.courses_attached += ['Git']

 
cool_lecturer = Lecturer('Hubert J.', 'Farnsworth')                  # Part of the lecturers personal information. 
cool_lecturer.courses_attached += ['Python']
cool_lecturer.courses_attached += ['Git']

lecturer_1 = Lecturer('Theworld', 'Has')  
lecturer_1.courses_attached += ['Python']
lecturer_1.courses_attached += ['Git']

lecturer_2 = Lecturer('Gonna', 'Rollme')   
lecturer_2.courses_attached += ['Python']
lecturer_2.courses_attached += ['Git']


cool_reviewer.rate_hw(best_student, 'Python', 1)                     # Part of the lecturers rating students hw.
reviewer_1.rate_hw(best_student, 'Python', 1)
reviewer_2.rate_hw(best_student, 'Python', 1)

cool_reviewer.rate_hw(best_student, 'Git', 2)
reviewer_1.rate_hw(best_student, 'Git', 2)
reviewer_2.rate_hw(best_student, 'Git', 2)

cool_reviewer.rate_hw(student_1, 'Python', 3)
reviewer_1.rate_hw(student_1, 'Python', 3)
reviewer_2.rate_hw(student_1, 'Python', 3)

cool_reviewer.rate_hw(student_1, 'Git', 4)
reviewer_1.rate_hw(student_1, 'Git', 4)
reviewer_2.rate_hw(student_1, 'Git', 4)

cool_reviewer.rate_hw(student_2, 'Python', 5)
reviewer_1.rate_hw(student_2, 'Python', 5)
reviewer_2.rate_hw(student_2, 'Python', 5)

cool_reviewer.rate_hw(student_2, 'Git', 6)
reviewer_1.rate_hw(student_2, 'Git', 6)
reviewer_2.rate_hw(student_2, 'Git', 6)

 
best_student.rate_hw(cool_lecturer, 'Python', 10)                     # Part of the students rating lecturers hw.
student_1.rate_hw(cool_lecturer, 'Python', 10)
student_2.rate_hw(cool_lecturer, 'Python', 10)

best_student.rate_hw(cool_lecturer, 'Git', 9)   
student_1.rate_hw(cool_lecturer, 'Git', 9)
student_2.rate_hw(cool_lecturer, 'Git', 9)

best_student.rate_hw(lecturer_1, 'Python', 8)   
student_1.rate_hw(lecturer_1, 'Python', 8)
student_2.rate_hw(lecturer_1, 'Python', 8)

best_student.rate_hw(lecturer_1, 'Git', 7)   
student_1.rate_hw(lecturer_1, 'Git', 7)
student_2.rate_hw(lecturer_1, 'Git', 7)

best_student.rate_hw(lecturer_2, 'Python', 6)   
student_1.rate_hw(lecturer_2, 'Python', 6)
student_2.rate_hw(lecturer_2, 'Python', 6)

best_student.rate_hw(lecturer_2, 'Git', 5)   
student_1.rate_hw(lecturer_2, 'Git', 5)
student_2.rate_hw(lecturer_2, 'Git', 5)


students_list = [best_student, student_1, student_2]                # List of all students.
lecturers_list = [cool_lecturer, lecturer_1, lecturer_2]            # List of all lecturers.
reviewers_list = [cool_reviewer, reviewer_1, reviewer_2]            # List of all reviewers.
course_list = ['Python', 'Git']                                     # List of all courses.

print('\tВывод основной информации:\n')
print('\tПерегрузка метода str для все классов:')

print ('\nСтуденты:')
print(best_student, student_1, student_2)         
print ('\nЭксперты:')
print(cool_reviewer, reviewer_1, reviewer_2)
print ('\nЛекторы:')
print(cool_lecturer, lecturer_1, lecturer_2)    

print('\tПерегрузка метода lt для все классов лекторов и студентов:')   # Print lt method for comparing students by rate, lecturers by rate, and with each other.

print (f' \nСравнение {lecturer_1.name}  ({rate_count(lecturer_1)}) c {lecturer_2.name} ({rate_count(lecturer_2)}) дает результат: {lecturer_1 < lecturer_2}')
print (f' \nСравнение {lecturer_2.name}  ({rate_count(lecturer_2)}) c {cool_lecturer.name} ({rate_count(cool_lecturer)}) дает результат: {lecturer_2 < cool_lecturer}')

print (f' \nСравнение {student_1.name}  ({rate_count(student_1)}) c {student_2.name} ({rate_count(student_2)}) дает результат: {student_1 < student_2}')
print (f' \nСравнение {student_2.name}  ({rate_count(student_2)}) c {best_student.name} ({rate_count(best_student)}) дает результат: {student_2 < best_student}')

print (f'Сравнение {student_2.name}  ({rate_count(student_2)}) c {cool_lecturer.name} ({rate_count(cool_lecturer)}) дает результат: {student_2 < cool_lecturer}')
print (f'Сравнение {cool_lecturer.name}  ({rate_count(cool_lecturer)}) c {student_2.name} ({rate_count(student_2)}) дает результат: {cool_lecturer < student_2}')

print(f'\n\tПрикрепленные курсы лекторов и экспертов:\n')               # Print Mentors attached courses.
print(f'\nЭксперты:\n') 
attached_courses(reviewers_list)
print(f'\nЛекторы:\n') 
attached_courses(lecturers_list)

print(f'\n\tСредний бал за курс студентов и лекторов:\n')               # Print students and lectors average rate of courses.
print(f'\nСтуденты:\n') 
average_rate_course(students_list, course_list)                         
print(f'\nЛекторы:\n') 
average_rate_course(lecturers_list, course_list)