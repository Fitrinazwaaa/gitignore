try:
    print(x)
except:
    print('Something went wrong')
finally:
    print('The 'try except' is finished')

#5
x = -1
if x < 0:
    raise Exception('Sorry, your number below zero')

print(' ')
#6
x = 'hello'
if not type(x) is int:
    raise TypeError('Only integers are allowed')







#python File Handling
#1
f = open('demofile.txt')
f = open("demofile.txt", 'rt')
print(f.read())
f = open("pertemuan_1.py", 'r')
print(f.read())

print(' ')
#3
import os
os.rmdid("myfolder")