class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_my_name(self):
        print("Hallo my name is " + self.name)

    def change_my_name(self, new_name):
        self.name = new_name


class student(person):
    
    def __init__(self, nisn, name, age):
        super().__init__(name, age)
        self.nisn = nisn

    def say_my_name(self):
        print('I am student with name ' + self.name)


person_1 = person("John", 30)
person_1.name = 'emil'
person_1.change_my_name('krishna')
person_1.say_my_name()

student_1 = student('222316', 'fitri', 14)
student_1.say_my_name()

print(person_1.name)
print(person_1.age)
print(person_1.say_my_name())


class mathematic:
    def __init__(self):
        self.value = 0

    def increment(self):
        self.value += 2

    def decrement(self):
        self.value -= 2

    def add(self, a, b):
        return a + b

    def substractions(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b
    
nath_1 = mathematic()
nath_2 = mathematic()

nath_1.increment()
nath_1.increment()
nath_2.decrement()

print(nath_2.value)



print("=======================================================")



class person:
    def __init__(self, first_name, last_name, age, addres, hobby):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.addres = addres
        self.hobby = hobby

    def my_full_name(self):
        return self.first_name + " " + self.last_name
    
    def my_hobby(self):
        print("My hobby is " + self.hobby)

    def my_age(self):
        print("umur saya " + self.age)

person_1 = person(
    'John',
    'Doe',
    36,
    'Bandung',
    'cook')

person_1.my_hobby

class student(person):

    def __init__(self, nisn, first_name, last_name, age, addres, hobby):
        super().__init__(first_name, last_name, age, addres, hobby)
        self.nisn = nisn

    def my_hobby(self):
        super().my_hobby()
        print("Hobby saya adalah " + self.hobby)

    def my_full_name(self):
        super().my_full_name()
        print("Nama saya " + self.first_name + " " + self.last_name)

    def my_age(self):
        print("umur saya", self.age)

student_1 = student('1234', 'chandra', 'adipraja', 34, 'KAWALI', 'Code')

student_1.my_hobby()
student_1.my_full_name()
student_1.my_age()



str