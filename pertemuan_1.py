import time

for i in range(2):
    print('hallo dunia!')
    time.sleep(1)




#ANGKA PYTHON

#example
x = 5
y = "John"
z = 1j 
print(type(x))
print(type(y))
print(type(z))

#example
x = 1    # int
y = 2.8  # float
z = 1j   # complex
#convert from int to float:
a = float(x)
#convert from float to int:
b = int(y)
#convert from int to complex:
c = complex(x)
print(a)
print(b)
print(c)
print(type(a))
print(type(b))
print(type(c))

"""
Python tidak memiliki random()fungsi untuk membuat angka acak, tetapi Python memiliki modul bawaan yang disebut randomyang dapat digunakan untuk membuat angka acak:"""
#Impor modul acak, dan tampilkan nomor acak antara 1 dan 9:
import random
print(random.randrange(1, 10))


print("===========================================================================")
#PYTHON CASTING

#int() - membuat bilangan integer dari literal integer, literal float (dengan menghapus semua desimal), atau string literal (dengan syarat string mewakili bilangan bulat).
print("example")
x = int(1)                # === 1
y = int (2.8)             # === 2
z = int ("3")             # === 3

#float() -  membuat angka float dari literal integer, literal float, atau string literal (menyediakan string yang mmewakili floet atau integer)
print("example")
x = float (1)             # === 1.0
y = float (2.8)           # === 2.8
z = float ("3")           # === 3.0
w = float ("4.2")         # === 4.2

#str() - membuat string dari berbagia tipe data, termasuk string, literal integer, dan literal float.
print("example")
x = str("s1")             # === 's1'
y = str(2)                # === '2'
z = str(3.0)              # === '3.0'

                   # === Hello, World!

#(LOOPING) - memunculkan huruf - huruf yang ada pada string secara berderet
for x in "Banana":
    print (x) 

#(STRING LENGTH) - mengembalikan panjang string/tali(bayaknya / jumlah) 
a = "Hello, World!"
print(len(a))                                       # === 13

#CHECK STRING
#untuk memeriksa apakah fase atau karakter tertentu ada dalam sebuah string, kita dapat menguunakan kata kunci (in) :
#example
txt = "The best things is life are free!"
print("free" in txt)                                # === true

#gunakan dalam (if) :
#example
txt = "The best things is life are free!"
if "free" in txt:
    print ("yes 'free' is present.")                # === yes 'free' is present.


#CHECK IF NOT
#untuk memriksa apakah frasa atau karakter tertentu tidak ada dalam sebuah string, kita dapat menggunkan kata kunci (not in)
#example
txt = "The best things is life are free!"
print("expensife" not in txt)                       # === true

#gunakan dalam (if)
#example
txt = "The best things is life are free!"
if "expensife" not in txt :
    print ("no, 'expensife' is NOT present.")       # === no, 'expensife' is NOT present.



print("===========================================================================")
#ASSIGN MULTIPLE VALUES

#Banyak Nilai ke Banyak Variabel
X, Y, Z = "Orange", "Banana", "Apple",
print(X)                           # === Orange
print(Y)                           # === Banana
print(Z)                           # === Apple

#satu nilai ke beberapa variabil
x = y = z = "Orange"
print(x)
print(y)
print(z)

#buka kemasan koleksi
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)



print("===========================================================================")
#VARIABLE GLOBAL

#example
x = "awesome"
def myfunc():
      print("Python is " + x)
myfunc()

#example
x = "awesome"
def myfunc():
      x = "fantastic"
print("Python is " + x)
myfunc()
print("Python is " + x)


"""
KATA KUNIC GLOBAL
Biasanya, saat Anda membuat variabel di dalam suatu fungsi, variabel itu bersifat lokal, dan hanya dapat digunakan di dalam fungsi itu.

Untuk membuat variabel global di dalam suatu fungsi, Anda dapat menggunakan globalkata kunci."""

#example
def myfunc():
      global x
x = "fantastic"
myfunc()
print("Python is " + x)

#example
x = "awesome"
def myfunc():
  global x
  x = "fantastic"
myfunc()
print("Python is " + x)


print("===========================================================================")



#unpack colection
fruits = {"Banana", "Orange", "Apple"}
print(fruits)                      # === {'Orange', 'Apple', 'Banana'}




print("===========================================================================")
#OUTPUT VARIABLES
x = "python"
y = "is"
z = "awesome"
print(x, y, z)                     # === python is awesome

x = "python"
y = "is"
z = "awesome"
print(x + y + z)                   # === pythonisawesome

x = "python"
y = "is"
z = "awesome"
print(x + " " + y + " " + z)                   # === python is awesome

#untuk nomor itu berfungsi seperti matematika (+)
x = 2
y = 5
z = 13
print(x + y + z)                   # === 20





print("===========================================================================")
#MODIFY STRING

#huruf besar
a = "HELLO world!"
print(a.lower())                   # === hello world!

#huruf kecil
a = "HELLO world!"
print(a.upper())                   # === HELLO WORLD!

#hapus spasi putih
a = "hello world!"
print(a.strip())                   # === hello world!

#ganti string
a = "hello world!"
print(a.replace("h", "d"))         # === dello world!

#string terpisah
a = "Hello, World!"
print(a.split(","))                # === ['Hello', 'World!']




#example
#1
def sum_int_or_str(a, b):
    return int(a) + int(b)

assert(sum_int_or_str(1, '2')) == 3

#2
def get_second_caracter(a):
    if len(a) > 1:
        return a[1]
    else:
        return 0

assert (get_second_caracter("ab")) == "b"
assert (get_second_caracter("a")) == 0

#3
car = {
    'brand': 'Toyota',
    'year': 2022
}

assert (car['brand']) == 'Toyota'

#4
cars =  [
    {
        'brand': 'Toyota'
    },
    {
        'brand': 'Honda',
        'products': [
            'civic'
        ]
    }
]
assert(cars[1]['products'][0]) == 'civic'

#5
raw_cars = 'toyota,honda,indiacar'
assert(raw_cars.split(',')) == ['toyota', 'honda', 'indiacar'] # turn raw_cars into a list

#6
raw_cars = raw_cars.upper()
assert(raw_cars.split(',')) == ['TOYOTA','HONDA','INDIACAR']

#7
raw_cars = "toyota, honda, indiacar, indiacar, indiacar"
raw_cars = raw_cars.split(",")
raw_cars = set(raw_cars)
raw_cars = len(raw_cars)
assert(raw_cars) == 3



str