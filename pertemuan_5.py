#python datetime

#1
import datetime
x = datetime.datetime.now()
print(x)
print(x.year)
print(x.strftime("%a"))
print(x.strftime("%A"))
print(x.strftime("%b"))
print(x.strftime("%B"))
print(x.strftime("%y"))
print(x.strftime("%Y"))
print(x.strftime("%W"))
print(x.strftime("%m"))
print(x.strftime("%M"))
print(x.strftime("%H"))
print(x.strftime("%I"))
print(x.strftime("%p"))
print(x.strftime("%S"))
print(x.strftime("%d"))
print(x.strftime("%Y/%B/%A"))

print(' ')
#2
import datetime
x = datetime.datetime(2020, 5, 17)
print(x)

print(' ')
#3
import datetime
dt_now = datetime.datetime.now()
print(dt_now)
print(dt_now.strftime('%d-%m-%Y'))

#4
arr_1 = [5, 78, 2, 0]
assert(min(arr_1)) == 0
assert(max(arr_1)) == 78
# function 5 pangkat 5
assert(pow(5, 5)) == 3125
print(' ')










print('===================================')
#Python Try Except

#1
try:
    print(X)
except NameError:
    print('An exception occurred')
except:
    print('Something else went wrong')

print(' ')
#2
try:
    print(X)
except NameError:
    print('An exception occurred')
except:
    print('Something else went wrong')

print(' ')
#3
try:
    print(X)
except NameError:
    print('An exception occurred')
finally:
    print('Something else went wrong')

print(' ')
#4
try :
    f = open('demofile.txt')
    try:
        f.write('lorum Ipsum')
    except:
        print('Something went wrong when writing to the file')
    finally:
        f.close()
except:
    print('Something went wrong when opening the file')

print(' ')









print('===================================')
#python json
#1
import json
#somw JSON:
x = '{"name":"John", "age":30, "city":"New York"}'
#PARSE X:
y = json.loads(x)
#the result is a python dictionary:
print(y["age"])


print(' ')
#2
import json
#a python object (dict):
x = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
#convert into JSON
y = json.dumps(x)
#the result is a JSON string:
print(y)


print(' ')
#3
print(json.dumps({"name":"john","age": 30}))
print(json.dumps({"name":"john","age": 30}))
print(json.dumps(["apple", "banana"]))
print(json.dumps(("apple", "banana")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31176))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))
print(' ')










print('===================================')
#python File Handling

#2
f = open("demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()
#open and read the file after the padding:
f = open("demofile2.txt", "r")
print(f.read())

