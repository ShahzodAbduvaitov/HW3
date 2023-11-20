class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

teacher = Person('Fathullo', '23')
student = Person('Shahzod', '20')
tyutor = Person('Albert', '21')

print(teacher.name, teacher.age)
print(student.name, student.age)
print(tyutor.name, tyutor.age)