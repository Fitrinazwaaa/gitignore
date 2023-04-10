print(" ") #--1
thislist = ["apple","banana", "cherry", "orange", "kiwi", "melon", 'manggo']
print(thislist[2:5])                       # === ['cherry', 'orange', 'kiwi']

print(" ")#--2

thislist = ["apple","banana", "cherry", "orange", "kiwi", "melon", 'manggo']
print(thislist[:4])

print(" ")#--3

thislist = ["apple","banana", "cherry", "orange", "kiwi", "melon", 'manggo']
print(thislist[2:])

print(" ")#--4

thislist = ["apple","banana", "cherry", "orange", "kiwi", "melon", 'manggo']
print(thislist[-4:-1])

print(" ")#--5

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

print(" ")#--6

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)


print(" ")#--7


#EXAMPLE
#1
thislist = ["apple", "banana", "cherry"]
thislist.append("manggo")
print(thislist)

#  thislist = ["apple", "banana", "cherry"]
#  thislist.append(0,"manggo")
#print(thislist)

print(" ")#--8
print(" yyyyyyyyy ")

#2
thislist = ["apple", "banana", "cherry"]
thislist2 = ["manggo", "stroberry"]
thislist2.extend(thislist)
print(thislist2)

print(" ")#--9
#3
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

print(" ")#--10
#4
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
thislist.pop(0)
print(thislist)

print(" ")#--11
#4
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

print(" ")#--12



#python - loop list
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
    print(thislist[i])

#thislist = ["apple", "banana", "cherry"]
#i = 0
#while i < len(thislist):
#   print(thislist[i])    #  i = i + 1

#thislist = ["apple", "banana", "cherry"]
#[print(x) for x in thislist]
#assert() == ['apple', 'mango']
#assert() == ['apple', 'mango', 'kiwi']

print(" ")#--13

new_list = ["apple", "apple", "apple", "apple", 
            "mango", "kiwi", "apple", "apple", "apple", "apple"]
print(new_list[4:6])                       # === ['mango', 'kiwi']

print(" ")#--14

list1 = ["mango"]
list2 = ["apple"]

#list1.extend(list2)
#list1 = list1 + list2
list1 += list2 # equal to list = list1 + list2
print(list1)


print(" ")#--15

list1 = [1, 4, 5, 6, 2, 4]
list1.sort(reverse = True)
print(list1)

print(" ")#--16

list1 = [1, 4, 5, 6, 2, 4]
list1.reverse()
print(list1)

print(" ")#--17

list1 = ["apple", "banana", "mango"]
list1.reverse()
print(list1)

print(" ")#--18

list1 = [1, 4, 5, 6, 2, 4]
list2 = list1.copy()
list2.pop()

print(list1, list2)

list = [1, 4, 5, 7]

list3 = list1.copy()
list3.pop()

print(" ")#--19

#latihan
list1 = [1, 4, 5, 6, 2, 4]
assert([x for x in list1 if x == 4]) == [4,4]



fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)

print(" ")#--20
print("===========================================")
#1
def my_function(fname) :
    print (fname + " Refsnes ")

my_function ("Email")
my_function ("Tobias")
my_function ("Linus")

print(" ")

#def my_function(fname) :
#    return fname + " Refsnes "

#result = my_function("email", "Refsnes")
#print(result)
#print(my_function("Tobias", "Refsnes"))

print("-")

#def my_function(*kids):
#    print(kids)
#    for kid in kids:
#    print(kid)

#my_function("Email", "Tobias")

#2
def my_function(child3, child2, child1):
    print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

print(" ")

#3
def my_function(**kid) :
   print ("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

print(" ")

#4
def detail_people(**data):
    print(data)

detail_people(
    nama_depan = "Email",
    nama_belakang = "Tobias",
    umur = 20,
    status = "Bekerja"
)

print(" ")

#5
def my_function(country = "Norway"):
    print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

print(" ")

#6
def my_function(x):
    return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))

print(" ")

#7
def multiply_by_two(a):
    return a * 2

assert(multiply_by_two(3)) == 6

print(" ")

#8
def multiply_by_x(w, x = 2):
    return w * x
assert(multiply_by_x(3))  == 6 
assert(multiply_by_x(3, 1))  == 3

print(" ")
#9
user_input = input("input dikali dengan 2:") #data bisa kita tambahkan saat run(terminal), dengan menambakan angka
print(multiply_by_two(int(user_input)))

print(" ")

#10
how_many_input = input("Berapa kali ingin input data?")
i = 0
while True :
    if i == 0:
        break

    user_input = input ("input dikali dengan 2:") 
    print(multiply_by_two(int(user_input)))
    i += 1

print(" ")

#11
"""
Enter the number of students in your class: 3
Enter the name of student 1: Emil
Enter the grades of student 1 (comma-separated): 85,90,92
Enter the name of student 2: Tobiaz
Enter the grades of student 2 (comma-separated): 78,80,84
Enter the name of student 3: Refsnes
Enter the grades of student 3 (comma-separated): 92,95,98

Average grades:
Alice: 89.0
Bob: 80.67
Charlie: 95.0
"""

def totalGrades(grades):
    grade = 0
    grades = grades.split(",")
    for i in grades:
        grade += float(i)
    grade = grade/len(grades)
    return grade
how_many_input = input('Enter the number of students in your class: ')
students = []
for i in range(int(how_many_input)):
    name = input("Enter the name of student: ")
    grades = input ("Enter the grades of student (comma-separated): ")
    students.append(
        {
        "nama":name,
        "grade":grades,
        "average_grade" : totalGrades(grades)
        }
    )
print()
print("Average grades: ")
for z in students:
    print(z["nama"], ":", z["average_grade"])

print("===========================================================================================")