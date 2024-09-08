Session - 1

>>>print('hello world!')
hello world!
>>>print(100)
100
>>>2 + 3
5
>>> 2 * 5
10
>>>4 - 2
2
>>>10 // 3
3
>>>10 / 3
3.3333333333333335
>>>type(5)
<class 'int'>
>>>type(5.23)
<class 'float'>
>>>type('asif is intelligent')
<class 'str'>
>>>x = 10
>>>y = 60
>>>x + y
70
>>>x - y
-50
>>> x// y
0
>>>x / y
0.16666666666666666
>>> type(x)
<class 'int'>
>>> x = ' variabnle string'
>>> type(x)
<class 'str'>
>>> x = 200
>>>x
200
>>> X = 500
>>> print(x, X)
200 500
z
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    z
NameError: name 'z' is not defined
a = 2
b = 3
print(a,b)
2 3
a,b = 4, 5
print(a,b)
4 5
x, y, z = 10, 20, 30
x
10
y
20
z
30
a
4
b
5
a = b = 10
a
10
b
10
[10, 20, 30, 40]
[10, 20, 30, 40]
sampleList = [ 10, 20, 'string', 'bmw', 'porsche', 2.55, 0]
type(sampleList)
<class 'list'>
smallList = [1,2,3]
x,y,z = smallList
x
1
y
2
z
3
x, y = smallList
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    x, y = smallList
ValueError: too many values to unpack (expected 2)
x, y, z, w = smallList
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    x, y, z, w = smallList
ValueError: not enough values to unpack (expected 4, got 3)
print(a,b)
10 10
print('string', 'string2')
string string2
print(x, y, z)
1 2 3
def sampleFunction():
    print('hi hello welcome')
    print('how are you doing')
    print('third step')

    
sampleFunction()
hi hello welcome
how are you doing
third step
sampleFunction()
hi hello welcome
how are you doing
third step
sampleFunction()
hi hello welcome
how are you doing
third step
def sampleFunction(username):
    print('hi ', username)

    
sampleFunction('asif')
hi  asif
sampleFunction('akhil')
hi  akhil
x = '23'
type(x)
<class 'str'>
y = int(x)
y
23
type(y)
<class 'int'>
x = 3.567
type(x)
<class 'float'>
y = int(x)
y
3
type(y)
<class 'int'>
sampleTuple = (1,2,3)
type(sampleTuple)
<class 'tuple'>
smallList
[1, 2, 3]
smallList[0]
1
smallList[2]
3
smallList[1]
2
smallList[0] = 'banana'
smallList[0]
'banana'
smallList
['banana', 2, 3]
sampleTuple[0]
1
sampleTuple[1]
2
sampleTuple[2]
3
sampleTuple[0] = 'banana'
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    sampleTuple[0] = 'banana'
TypeError: 'tuple' object does not support item assignment
sampleTuple2 = ('banana', 'apple')
sampleTuple + sampleTuple2
(1, 2, 3, 'banana', 'apple')
s=sampleTuple + sampleTuple2
s
(1, 2, 3, 'banana', 'apple')
s[0]
1
s[3]
'banana'
s[-1]
'apple'
s[-2]
'banana'
s[-3]
3
s[-4]
2
dir(sampleTuple)
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']
sampleTuple
(1, 2, 3)
sampleTuple.count(1)
1
sampleTuple = (1,1,1,1,1,2,2, 3)
sampleTuple.count(1)
5
sampleTuple.count(3)
1
sampleTuple.count(2)
2
sampleTuple = (1,2,3)
sampleTuple
(1, 2, 3)
sampleTuple.index(3)
2
sampleTuple.index(2)
1
sampleTuple = (1,1,1,1,1,2,2, 3)
sampleTuple.index(1)
0
sampleTuple.index(2)
5
len(sampleTuple)
8
len(2)
Traceback (most recent call last):
  File "<pyshell#112>", line 1, in <module>
    len(2)
TypeError: object of type 'int' has no len()
string to int, float to int
SyntaxError: invalid syntax
sampleTuple
(1, 1, 1, 1, 1, 2, 2, 3)
type(sampleTuple)
<class 'tuple'>
y = list(sampleTuple)
y
[1, 1, 1, 1, 1, 2, 2, 3]
y[0]= 100
y
[100, 1, 1, 1, 1, 2, 2, 3]
y.append(200)
y
[100, 1, 1, 1, 1, 2, 2, 3, 200]
y.append(300)
y
[100, 1, 1, 1, 1, 2, 2, 3, 200, 300]
y.pop()
300
y
[100, 1, 1, 1, 1, 2, 2, 3, 200]
y.pop()
200
y
[100, 1, 1, 1, 1, 2, 2, 3]
y.insert(1, 200)
y
[100, 200, 1, 1, 1, 1, 2, 2, 3]
y.insert(2, 300)
y
[100, 200, 300, 1, 1, 1, 1, 2, 2, 3]
y.pop(2)
300
y
[100, 200, 1, 1, 1, 1, 2, 2, 3]
z = y[::-1]
z
[3, 2, 2, 1, 1, 1, 1, 200, 100]
y
[100, 200, 1, 1, 1, 1, 2, 2, 3]
y.reverse()
y
[3, 2, 2, 1, 1, 1, 1, 200, 100]
dir(y)
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
y.remove(200)
y
[3, 2, 2, 1, 1, 1, 1, 100]
y.remove(0)
Traceback (most recent call last):
  File "<pyshell#142>", line 1, in <module>
    y.remove(0)
ValueError: list.remove(x): x not in list
y.append(200)
y.append(200)
y
[3, 2, 2, 1, 1, 1, 1, 100, 200, 200]
y.remove(200)
y
[3, 2, 2, 1, 1, 1, 1, 100, 200]
y.sort()
y
[1, 1, 1, 1, 2, 2, 3, 100, 200]
y.sort(reverse=True)
y
[200, 100, 3, 2, 2, 1, 1, 1, 1]
dir(y)
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
5//2
2
5/2
2.5
float("2.5")
2.5
y
[200, 100, 3, 2, 2, 1, 1, 1, 1]
z = y + [1,2,3]
z
[200, 100, 3, 2, 2, 1, 1, 1, 1, 1, 2, 3]
y
[200, 100, 3, 2, 2, 1, 1, 1, 1]
y.append(250)
y
[200, 100, 3, 2, 2, 1, 1, 1, 1, 250]
y.extend([300, 400, 500])
y
[200, 100, 3, 2, 2, 1, 1, 1, 1, 250, 300, 400, 500]
y.copy()
[200, 100, 3, 2, 2, 1, 1, 1, 1, 250, 300, 400, 500]
z = y.copy()
z
[200, 100, 3, 2, 2, 1, 1, 1, 1, 250, 300, 400, 500]
z[0] = 500
z
[500, 100, 3, 2, 2, 1, 1, 1, 1, 250, 300, 400, 500]
y
[200, 100, 3, 2, 2, 1, 1, 1, 1, 250, 300, 400, 500]
y = z = [1,2,3]
y
[1, 2, 3]
z
[1, 2, 3]
y[0] = 10
y
[10, 2, 3]
z
[10, 2, 3]
z[2] = 100
>>> z
[10, 2, 100]
>>> y
[10, 2, 100]
>>> y = [1,2,3]
>>> z = [4,5,6]
>>> z = [1,2,3]
>>> y[0] = 100
>>> y
[100, 2, 3]
>>> z
[1, 2, 3]
>>> z = y[0:2]
>>> z
[100, 2]
>>> y[:2]
[100, 2]
>>> y[0:3]
[100, 2, 3]
>>> y[:]
[100, 2, 3]

Session - 2,3

>>> "this is a string"
'this is a string'
>>> x = " this is a string
SyntaxError: incomplete input
>>> x = """ this is a string
... this is line2
... this is line3"""
>>> x
' this is a string\nthis is line2\nthis is line3'
>>> x + "this is string3"
' this is a string\nthis is line2\nthis is line3this is string3'
>>> def greetUser(username):
...     print("hi " + username)
... 
...     
>>> greetUser("asif")
hi asif
>>> def greetUser(username):
...     print("hi " + username + " have a good day")
... 
...     
>>> greetUser("asif")
hi asif have a good day
>>> "hi {username} have a good day. your total shopping bill is {price}".format(username, price)
Traceback (most recent call last):
  File "<pyshell#205>", line 1, in <module>
    "hi {username} have a good day. your total shopping bill is {price}".format(username, price)
NameError: name 'username' is not defined
>>> username = "asif"
>>> price = 100
>>> "hi {username} have a good day. your total shopping bill is {price}".format(username, price)
Traceback (most recent call last):
  File "<pyshell#208>", line 1, in <module>
    "hi {username} have a good day. your total shopping bill is {price}".format(username, price)
KeyError: 'username'
f"hi {username} have a good day. your total shopping bill is {price}"
'hi asif have a good day. your total shopping bill is 100'
true
Traceback (most recent call last):
  File "<pyshell#210>", line 1, in <module>
    true
NameError: name 'true' is not defined. Did you mean: 'True'?
True
True
False
False
10 > 100
False
100 > 10
True
10//2 > 0
True
10>2 and 5>2
True
10>2 and 5<2
False
10<2 and 5>2
False
10<2 and 5<2
False
a = [1,2,3]
or
SyntaxError: incomplete input
10>2 or 5>2
True
10<2 or 5<2
False
10>2 or 5<2
True
10>2 or 5<2 or 10 < 6
True
# and: 1 false => total expression = False
# or: 1 true => total expression = True
# in
fruit = "banana"
fruits = ["apple", "banana", "grapes"]
fruit in fruits
True
fruit2 = "pineapple"
fruit2 in fruits
False
for fruit in fruits:
print("hi")
SyntaxError: expected an indented block after 'for' statement on line 1
for fruit in fruits:
    print("hi")

    
hi
hi
hi
for fruit in fruits:
    print(fruit)

    
apple
banana
grapes
range(10)
range(0, 10)
for number in range(10):
    print(number)

    
0
1
2
3
4
5
6
7
8
9
for number in range(0, 10):
    print(number)

    
0
1
2
3
4
5
6
7
8
9
for number in range(10):
    print(number)

    
0
1
2
3
4
5
6
7
8
9
for idx in range(3):
    print(fruits[idx])

    
apple
banana
grapes
# print idx, fruit for every fruit
for idx in range(3):
    print(idx, fruits[idx])

    
0 apple
1 banana
2 grapes
for idx, fruit in enumerate(fruits):
    print(idx, fruit)

    
0 apple
1 banana
2 grapes
# print numbers from 1 to 100.
# 0 to 100
# using for loop
for number in range(101):
    print(number)

    
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
100
# print numbers from 10 to 15. include 10, 15
# start: inclusive, stop: exclusive
for number in range(10, 16):
    print(number)

    
10
11
12
13
14
15
# print alternate numbers from 10 to 16.
for number in range(10, 16, 1):
    print(number)

    
10
11
12
13
14
15
for number in range(10, 16, 2):
    print(number)

    
10
12
14
for number in range(10, 17, 2):
    print(number)

    
10
12
14
16
# boolean, and, or, for
10 == 12
False
10 == 10
True
2+3 == 5+6
False
2 + 3 == 4 + 1
True
# = assignment, == equality check
number = 5
while number < 5:
    print(number)
    number = number + 1

    
while number < 10:
    print(number)
    number += 1

    
5
6
7
8
9
# print numbers from 0 to 10
number = 0
while number < 11:
    print(number)
    number += 1

    
0
1
2
3
4
5
6
7
8
9
10
number = 0
while number < 11:
    print(number)
    number += 2

    
0
2
4
6
8
10
number = -
SyntaxError: incomplete input
number = 0
while number <= 10:
    print(number)
    number += 1

    
0
1
2
3
4
5
6
7
8
9
10
while True:
    print("hi")

hi
hi
hi
hi
hi
Traceback (most recent call last):
  File "<pyshell#317>", line 2, in <module>
    print("hi")
KeyboardInterrupt
c
fruits
['apple', 'banana', 'grapes']
for idx in range(3):
    print(fruit)

    
grapes
grapes
grapes
for idx in range(3):
    print(fruits[idx])

    
apple
banana
grapes
fruit
'grapes'
n = len(fruits)
n
3
fruits.append('pineapple')
fruits
['apple', 'banana', 'grapes', 'pineapple']
n = len(fruits)
n
4
for idx in range(n):
    print(fruits[idx])

    
apple
banana
grapes
pineapple
# int, float, string, list, tuple
# set
fruits = { "apple", "banana", "grapes" }
fruits[0]
Traceback (most recent call last):
  File "<pyshell#339>", line 1, in <module>
    fruits[0]
TypeError: 'set' object is not subscriptable
fruits.add("apple")
fruits
{'apple', 'grapes', 'banana'}
# set: unique list of elements, unordered
fruits.remove('grapes')
fruits
{'apple', 'banana'}
for fruit in fruits:
    print(fruit)

    
apple
banana
fruits.add('banana2')
fruits.add('dkfdjkfjkdh')
for fruit in fruits:
    print(fruit)

    
apple
banana
dkfdjkfjkdh
banana2
'pineapple' in fruits
False
'banana' in fruits
True
len(fruits)
4
{1,2,3} {4,5,1,2}
SyntaxError: invalid syntax
{1,2,3,4,5}
{1, 2, 3, 4, 5}
{1,2}
{1, 2}
s1 = {1,2,3}
s2 = {4,5,1,2}
s1.union(s2)
{1, 2, 3, 4, 5}
s1.intersection(s2)
{1, 2}
{1,2,"asif", "akhil", "python"}
{1, 2, 'python', 'akhil', 'asif'}
{1,2, [3,4]}
Traceback (most recent call last):
  File "<pyshell#364>", line 1, in <module>
    {1,2, [3,4]}
TypeError: unhashable type: 'list'
type(s1)
<class 'set'>
x = set({1,1,2,2,3,4,5,6,7,8, 'python', 'python'})
x
{1, 2, 3, 4, 'python', 5, 6, 7, 8}
y = list(x)
y
[1, 2, 3, 4, 'python', 5, 6, 7, 8]
z = tuple(x)
z
(1, 2, 3, 4, 'python', 5, 6, 7, 8)
type(z)
<class 'tuple'>
type(y)
<class 'list'>
dir(s1)
['__and__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']
{1,2}.difference({1,2,3,4})
set()
{1,2} - {1,2} = {}
SyntaxError: cannot assign to expression here. Maybe you meant '==' instead of '='?
{1,2,3,4}.difference({1,2})
{3, 4}
s1
{1, 2, 3}
s1.discard(1)
s1
{2, 3}
s1.discard(10)
s1
{2, 3}
s1.remove(10)
Traceback (most recent call last):
  File "<pyshell#383>", line 1, in <module>
    s1.remove(10)
KeyError: 10
s1
{2, 3}
s2 = {3,4}
s1
{2, 3}
s2
{3, 4}
s1.union(s2)
{2, 3, 4}
s1
{2, 3}
s2
{3, 4}
s1.update(s2)
s1
{2, 3, 4}
s2
{3, 4}
# set
# dictionary
# hashmap {key1: value1, key2: value2, ... }
phoneNumberMap = { 'aisf' : 'phnumber', 'akhil': 'akhil number' }
phoneNumberMap['asif']
Traceback (most recent call last):
  File "<pyshell#398>", line 1, in <module>
    phoneNumberMap['asif']
KeyError: 'asif'
phoneNumberMap['aisf']
'phnumber'
phoneNumberMap['akhil']
'akhil number'
phoneNumberMap['tamzi']
Traceback (most recent call last):
  File "<pyshell#401>", line 1, in <module>
    phoneNumberMap['tamzi']
KeyError: 'tamzi'
phoneNumberMap.get('tamzi', 'tamzis number')
'tamzis number'
phoneNumberMap.get('akhil')
'akhil number'
phoneNumberMap.get('tamzi')
phoneNumberMap.get('tamzi') == None
True
phoneNumberMap.put('tamzi', 'tamzi number')
Traceback (most recent call last):
  File "<pyshell#406>", line 1, in <module>
    phoneNumberMap.put('tamzi', 'tamzi number')
AttributeError: 'dict' object has no attribute 'put'
dir(phoneNumberMap)
['__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__ior__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__ror__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
phoneNumberMap.update('tamzi', 'tamzi number')
Traceback (most recent call last):
  File "<pyshell#408>", line 1, in <module>
    phoneNumberMap.update('tamzi', 'tamzi number')
TypeError: update expected at most 1 argument, got 2
phoneNumberMap.update({'tamzi': 'tamzi number'})
phoneNumberMap
{'aisf': 'phnumber', 'akhil': 'akhil number', 'tamzi': 'tamzi number'}
phoneNumberMap.update({'tamzi': 'tamzi number 2'})
phoneNumberMap
{'aisf': 'phnumber', 'akhil': 'akhil number', 'tamzi': 'tamzi number 2'}
phoneNumberMap.keys()
dict_keys(['aisf', 'akhil', 'tamzi'])
phoneNumberMap.values()
dict_values(['phnumber', 'akhil number', 'tamzi number 2'])
phoneNumberMap.items()
dict_items([('aisf', 'phnumber'), ('akhil', 'akhil number'), ('tamzi', 'tamzi number 2')])
for key, value in phoneNumberMap:
    print(key, value)

    
Traceback (most recent call last):
  File "<pyshell#419>", line 1, in <module>
    for key, value in phoneNumberMap:
ValueError: too many values to unpack (expected 2)
x,y,z = [1,2,3]
x
1
y
2
z
3
for item in phoneNumberMap:
    print(item)

    
aisf
akhil
tamzi
for key in phoneNumberMap:
    value = phoneNumberMap.get(key)
    print(key, value)

    
aisf phnumber
akhil akhil number
tamzi tamzi number 2
for item in phoneNumberMap.items():
    print(item)

    
('aisf', 'phnumber')
('akhil', 'akhil number')
('tamzi', 'tamzi number 2')
for item in phoneNumberMap.items():
    key, value = item
    print("for the key", key, "the value is ", value)

    
for the key aisf the value is  phnumber
for the key akhil the value is  akhil number
for the key tamzi the value is  tamzi number 2
for item in phoneNumberMap.items():
    key, value = item
    print(f"for the key {key} the value is {value}")

    
for the key aisf the value is phnumber
for the key akhil the value is akhil number
for the key tamzi the value is tamzi number 2
for value in phoneNumberMap.values():
    print(value)

    
phnumber
akhil number
tamzi number 2
>>> phoneNumberMap
{'aisf': 'phnumber', 'akhil': 'akhil number', 'tamzi': 'tamzi number 2'}
>>> phoneNumberMap.pop('akhil')
'akhil number'
>>> phoneNumberMap
{'aisf': 'phnumber', 'tamzi': 'tamzi number 2'}
>>> phoneNumberMap.popitem()
('tamzi', 'tamzi number 2')
>>> phoneNumberMap
{'aisf': 'phnumber'}
>>> phoneNumberMap.popitem('akhil')
Traceback (most recent call last):
  File "<pyshell#447>", line 1, in <module>
    phoneNumberMap.popitem('akhil')
TypeError: dict.popitem() takes no arguments (1 given)
>>> phoneNumberMap.setdefault('akhil', default='ph')
Traceback (most recent call last):
  File "<pyshell#448>", line 1, in <module>
    phoneNumberMap.setdefault('akhil', default='ph')
TypeError: dict.setdefault() takes no keyword arguments
>>> phoneNumberMap.setdefault('akhil', 'ph')
'ph'
>>> phoneNumberMap
{'aisf': 'phnumber', 'akhil': 'ph'}
>>> phoneNumberMap.setdefault('akhil', 'ph')
'ph'
>>> phoneNumberMap.setdefault('akhil', 'phone')
'ph'
>>> phoneNumberMap
{'aisf': 'phnumber', 'akhil': 'ph'}

On Fri, Sep 6, 2024 at 6:30 PM akhil sirasanagandla <akhil.developer.123@gmail.com> wrote:
Python 3.11.4 (v3.11.4:d2340ef257, Jun  6 2023, 19:15:51) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
print('hello world!')
hello world!
print(100)
100
2 + 3
5
2 * 5
10
4 - 2
2
10 // 3
3
10 / 3
3.3333333333333335
type(5)
<class 'int'>
type(5.23)
<class 'float'>
type('asif is intelligent')
<class 'str'>
x = 10
y = 60
x + y
70
x - y
-50
x // y
0
x / y
0.16666666666666666
type(x)
<class 'int'>
x = ' variabnle string'
type(x)
<class 'str'>
x = 200
x
200
X = 500
print(x, X)
200 500
z
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    z
NameError: name 'z' is not defined
a = 2
b = 3
print(a,b)
2 3
a,b = 4, 5
print(a,b)
4 5
x, y, z = 10, 20, 30
x
10
y
20
z
30
a
4
b
5
a = b = 10
a
10
b
10
[10, 20, 30, 40]
[10, 20, 30, 40]
sampleList = [ 10, 20, 'string', 'bmw', 'porsche', 2.55, 0]
type(sampleList)
<class 'list'>
smallList = [1,2,3]
x,y,z = smallList
x
1
y
2
z
3
x, y = smallList
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    x, y = smallList
ValueError: too many values to unpack (expected 2)
x, y, z, w = smallList
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    x, y, z, w = smallList
ValueError: not enough values to unpack (expected 4, got 3)
print(a,b)
10 10
print('string', 'string2')
string string2
print(x, y, z)
1 2 3
def sampleFunction():
    print('hi hello welcome')
    print('how are you doing')
    print('third step')

    
sampleFunction()
hi hello welcome
how are you doing
third step
sampleFunction()
hi hello welcome
how are you doing
third step
sampleFunction()
hi hello welcome
how are you doing
third step
def sampleFunction(username):
    print('hi ', username)

    
sampleFunction('asif')
hi  asif
sampleFunction('akhil')
hi  akhil
x = '23'
type(x)
<class 'str'>
y = int(x)
y
23
type(y)
<class 'int'>
x = 3.567
type(x)
<class 'float'>
y = int(x)
y
3
type(y)
<class 'int'>
sampleTuple = (1,2,3)
type(sampleTuple)
<class 'tuple'>
smallList
[1, 2, 3]
smallList[0]
1
smallList[2]
3
smallList[1]
2
smallList[0] = 'banana'
smallList[0]
'banana'
smallList
['banana', 2, 3]
sampleTuple[0]
1
sampleTuple[1]
2
sampleTuple[2]
3
sampleTuple[0] = 'banana'
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    sampleTuple[0] = 'banana'
TypeError: 'tuple' object does not support item assignment
sampleTuple2 = ('banana', 'apple')
sampleTuple + sampleTuple2
(1, 2, 3, 'banana', 'apple')
s=sampleTuple + sampleTuple2
s
(1, 2, 3, 'banana', 'apple')
s[0]
1
s[3]
'banana'
s[-1]
'apple'
s[-2]
'banana'
s[-3]
3
s[-4]
2
dir(sampleTuple)
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']
sampleTuple
(1, 2, 3)
sampleTuple.count(1)
1
sampleTuple = (1,1,1,1,1,2,2, 3)
sampleTuple.count(1)
5
sampleTuple.count(3)
1
sampleTuple.count(2)
2
sampleTuple = (1,2,3)
sampleTuple
(1, 2, 3)
sampleTuple.index(3)
2
sampleTuple.index(2)
1
sampleTuple = (1,1,1,1,1,2,2, 3)
sampleTuple.index(1)
0
sampleTuple.index(2)
5
len(sampleTuple)
8
len(2)
Traceback (most recent call last):
  File "<pyshell#112>", line 1, in <module>
    len(2)
TypeError: object of type 'int' has no len()
string to int, float to int
SyntaxError: invalid syntax
sampleTuple
(1, 1, 1, 1, 1, 2, 2, 3)
type(sampleTuple)
<class 'tuple'>
y = list(sampleTuple)
y
[1, 1, 1, 1, 1, 2, 2, 3]
y[0]= 100
y
[100, 1, 1, 1, 1, 2, 2, 3]
y.append(200)
y
[100, 1, 1, 1, 1, 2, 2, 3, 200]
y.append(300)
y
[100, 1, 1, 1, 1, 2, 2, 3, 200, 300]
y.pop()
300
y
[100, 1, 1, 1, 1, 2, 2, 3, 200]
y.pop()
200
y
[100, 1, 1, 1, 1, 2, 2, 3]
y.insert(1, 200)
y
[100, 200, 1, 1, 1, 1, 2, 2, 3]
y.insert(2, 300)
y
[100, 200, 300, 1, 1, 1, 1, 2, 2, 3]
y.pop(2)
300
y
[100, 200, 1, 1, 1, 1, 2, 2, 3]
z = y[::-1]
z
[3, 2, 2, 1, 1, 1, 1, 200, 100]
y
[100, 200, 1, 1, 1, 1, 2, 2, 3]
y.reverse()
y
[3, 2, 2, 1, 1, 1, 1, 200, 100]
dir(y)
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
y.remove(200)
y
[3, 2, 2, 1, 1, 1, 1, 100]
y.remove(0)
Traceback (most recent call last):
  File "<pyshell#142>", line 1, in <module>
    y.remove(0)
ValueError: list.remove(x): x not in list
y.append(200)
y.append(200)
y
[3, 2, 2, 1, 1, 1, 1, 100, 200, 200]
y.remove(200)
y
[3, 2, 2, 1, 1, 1, 1, 100, 200]
y.sort()
y
[1, 1, 1, 1, 2, 2, 3, 100, 200]
y.sort(reverse=True)
y
[200, 100, 3, 2, 2, 1, 1, 1, 1]
