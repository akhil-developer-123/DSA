Python 3.11.4 (v3.11.4:d2340ef257, Jun  6 2023, 19:15:51) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> print("hello world!")
hello world!
>>> 1 + 2
3
>>> 4 + 5
9
>>> 5 - 3
2
>>> 5 * 2
10
>>> 5 // 2
2
>>> from math import floor, ceil
>>> floor(2.9)
2
>>> floor(2.1)
2
>>> ceil(2.9)
3
>>> ceil(2.1)
3
>>> 5 / 2
2.5
>>> type(2.5)
<class 'float'>
>>> type(2)
<class 'int'>
>>> type("this is akhil")
<class 'str'>
>>> [1,2,3, "string1", "string2", "hi", 2.5, 9.8]
[1, 2, 3, 'string1', 'string2', 'hi', 2.5, 9.8]
>>> x = 10
>>> x
10
>>> x = 100
>>> x
100
>>> x = 1200
x
1200
y = "this is a string"
y
'this is a string'
a = [1,2,3, "string1", "string2", "hi", 2.5, 9.8]
a[0]
1
a[1]
2
a[2]
3
a[5]
'hi'
len(a)
8
a[2] = 4
a
[1, 2, 4, 'string1', 'string2', 'hi', 2.5, 9.8]
a.append(100)
a
[1, 2, 4, 'string1', 'string2', 'hi', 2.5, 9.8, 100]
a.pop()
100
a.insert(0, 10)
a
[10, 1, 2, 4, 'string1', 'string2', 'hi', 2.5, 9.8]
a.insert(2, 6)
a
[10, 1, 6, 2, 4, 'string1', 'string2', 'hi', 2.5, 9.8]
a.pop(8)
2.5
a
[10, 1, 6, 2, 4, 'string1', 'string2', 'hi', 9.8]
dir(a)
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
a.count(9.8)
1
a.append(9.8)
a
[10, 1, 6, 2, 4, 'string1', 'string2', 'hi', 9.8, 9.8]
a.count(9.8)
2
2 + 3
5
[1,2,3] + [4,5,6]
[1, 2, 3, 4, 5, 6]
a = [1,2,3]
b = [4,5,6]
a + b
[1, 2, 3, 4, 5, 6]
a
[1, 2, 3]
b
[4, 5, 6]
c = a + b
c
[1, 2, 3, 4, 5, 6]
a.extend([4,5,6,7,8])
a
[1, 2, 3, 4, 5, 6, 7, 8]
a.index(4)
3
a = [1,2,3,4,5,5,4,4,8]
a.index(4)
3
a.index(5)
4
b = a[::-1]
b
[8, 4, 4, 5, 5, 4, 3, 2, 1]
a
[1, 2, 3, 4, 5, 5, 4, 4, 8]
a.reverse()
a
[8, 4, 4, 5, 5, 4, 3, 2, 1]
a.sort()
a
[1, 2, 3, 4, 4, 4, 5, 5, 8]
a.sort(reverse=True)
a
[8, 5, 5, 4, 4, 4, 3, 2, 1]
a.remove(5)
a
[8, 5, 4, 4, 4, 3, 2, 1]
a.append(5)
a
[8, 5, 4, 4, 4, 3, 2, 1, 5]
a.remove(5)
a
[8, 4, 4, 4, 3, 2, 1, 5]
b = a.copy()
b
[8, 4, 4, 4, 3, 2, 1, 5]
a
[8, 4, 4, 4, 3, 2, 1, 5]
a[0] = 1
a
[1, 4, 4, 4, 3, 2, 1, 5]
b
[8, 4, 4, 4, 3, 2, 1, 5]
a = [1,2,3]
x,y,z = a
x
1
y
2
z
3
x,y = a
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    x,y = a
ValueError: too many values to unpack (expected 2)
x,y,z,w = a
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    x,y,z,w = a
ValueError: not enough values to unpack (expected 4, got 3)
a
[1, 2, 3]
a.clear()
a
[]
a = [1,2,3]
a = (1,2,3)
a
(1, 2, 3)
a[0]
1
a[1]
2
a[2]
3
a[0] = 100
Traceback (most recent call last):
  File "<pyshell#98>", line 1, in <module>
    a[0] = 100
TypeError: 'tuple' object does not support item assignment
a.count(1)
1
a.count(2)
1
b = (4,5,6)
a
(1, 2, 3)
b
(4, 5, 6)
a  + b
(1, 2, 3, 4, 5, 6)
a
(1, 2, 3)
b
(4, 5, 6)
c = a + b
c
(1, 2, 3, 4, 5, 6)
(1,2,3, 'hi', 'bye')
(1, 2, 3, 'hi', 'bye')
type(a)
<class 'tuple'>
a = [1,2,3]
type(a)
<class 'list'>
a = 10.4
int(a)
10
int(10.9)
10
a = "103"
type(a)
<class 'str'>
b = int(a)
b
103
type(b)
<class 'int'>
a = "10.890"
int(a)
Traceback (most recent call last):
  File "<pyshell#122>", line 1, in <module>
    int(a)
ValueError: invalid literal for int() with base 10: '10.890'
float(a)
10.89
b = float(a)
b
10.89
c = int(b)
c
10
b = str(10.890)
b
'10.89'
"hello hi
SyntaxError: incomplete input
int("hello")
Traceback (most recent call last):
  File "<pyshell#131>", line 1, in <module>
    int("hello")
ValueError: invalid literal for int() with base 10: 'hello'
a = [1,2,3]
type(a)
<class 'list'>
b = tuple(a)
b
(1, 2, 3)
type(b)
<class 'tuple'>
a = (1,2,3)
b = list(a)
b
[1, 2, 3]
type(b)
<class 'list'>
a = [1,2,3, [4,5,6], [7,8,9], [1,2]]
a[0]
1
a[3]
[4, 5, 6]
a[3][0]
4
a[3][2]
6
a[4][2]
9
a[5][1]
2
a = [ 1,2,3, [4,5,[6,[7,8]]]
      ]
a
[1, 2, 3, [4, 5, [6, [7, 8]]]]
a[3][2][1]
[7, 8]
a[3][2][1][1]
8
len(a)
4
# unordered, unique elements
a = { 1 2, 3, 4 }
SyntaxError: invalid syntax. Perhaps you forgot a comma?
a = {1,2,3,4}
a
{1, 2, 3, 4}
type(a)
<class 'set'>
a[0]
Traceback (most recent call last):
  File "<pyshell#159>", line 1, in <module>
    a[0]
TypeError: 'set' object is not subscriptable
a.add(10)
a.add(11)
a.add(0)
a
{0, 1, 2, 3, 4, 10, 11}
a.add(200)
a
{0, 1, 2, 3, 4, 200, 10, 11}
a.add(200)
a
{0, 1, 2, 3, 4, 200, 10, 11}
dir(a)
['__and__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']
s1 = {1,2,3}
s2 = {1,2,3,4,5}
s1 = {1,2,3,7,8}
s1
{1, 2, 3, 7, 8}
s2
{1, 2, 3, 4, 5}
1,2,3,7,8,4,5
(1, 2, 3, 7, 8, 4, 5)
s3 = s1.union(s2)
s3
{1, 2, 3, 4, 5, 7, 8}
s1
{1, 2, 3, 7, 8}
s2
{1, 2, 3, 4, 5}
s1.intersection(s2)
{1, 2, 3}
s1
{1, 2, 3, 7, 8}
s2
{1, 2, 3, 4, 5}
# s1 - s2 = s1 - (s1 intersection s2)
s1.difference(s2)
{8, 7}
s1
{1, 2, 3, 7, 8}
s2
{1, 2, 3, 4, 5}
s1.remove(1)
s1
{2, 3, 7, 8}
s1.add(1)
s1
{1, 2, 3, 7, 8}
s1.discard(1)
s1
{2, 3, 7, 8}
s1.discard(100)
s1.remove(100)
Traceback (most recent call last):
  File "<pyshell#193>", line 1, in <module>
    s1.remove(100)
KeyError: 100
s1.update({10,12})
s1
{2, 3, 7, 8, 10, 12}
s1
{2, 3, 7, 8, 10, 12}
s2
{1, 2, 3, 4, 5}
s1.isdisjoint(s2)
False
s2 = {100,20}
s1
{2, 3, 7, 8, 10, 12}
s2
{100, 20}
s1.isdisjoint(s2)
True
s1.issubset(s2)
False
s1.issuperset(s2)
False
s1
{2, 3, 7, 8, 10, 12}
s1.pop()
2
s1
{3, 7, 8, 10, 12}
s1.pop()
3
s1
{7, 8, 10, 12}
s1.pop()
7
# key: value
nameToPhoneMap = { "akhil": "phoneNumber", "tamzi": "tamzi phone", "asif": "asif phone"  }
nameToPhoneMap["akhil"]
'phoneNumber'
nameToPhoneMap["tamzi"]
'tamzi phone'
nameToPhoneMap["jon"]
Traceback (most recent call last):
  File "<pyshell#215>", line 1, in <module>
    nameToPhoneMap["jon"]
KeyError: 'jon'
nameToPhoneMap.get("akhil")
'phoneNumber'
nameToPhoneMap.get("jon", "default number")
'default number'
nameToPhoneMap.get("james", "default number")
'default number'
nameToPhoneMap.get("james") == None
True
dir(nameToPhoneMap)
['__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__ior__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__ror__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
nameToPhoneMap.items()
dict_items([('akhil', 'phoneNumber'), ('tamzi', 'tamzi phone'), ('asif', 'asif phone')])
nameToPhoneMap.keys()
dict_keys(['akhil', 'tamzi', 'asif'])
nameToPhoneMap.values()
dict_values(['phoneNumber', 'tamzi phone', 'asif phone'])
nameToPhoneMap.update({"akhil": "phoneNumber1"})
nameToPhoneMap
{'akhil': 'phoneNumber1', 'tamzi': 'tamzi phone', 'asif': 'asif phone'}
nameToPhoneMap.update({"jon": "jon number"})
nameToPhoneMap
{'akhil': 'phoneNumber1', 'tamzi': 'tamzi phone', 'asif': 'asif phone', 'jon': 'jon number'}
nameToPhoneMap.pop()
Traceback (most recent call last):
  File "<pyshell#228>", line 1, in <module>
    nameToPhoneMap.pop()
TypeError: pop expected at least 1 argument, got 0
nameToPhoneMap.pop("akhil")
'phoneNumber1'
nameToPhoneMap
{'tamzi': 'tamzi phone', 'asif': 'asif phone', 'jon': 'jon number'}
nameToPhoneMap.pop("james")
Traceback (most recent call last):
  File "<pyshell#231>", line 1, in <module>
    nameToPhoneMap.pop("james")
KeyError: 'james'
nameToPhoneMap.popitem()
('jon', 'jon number')
nameToPhoneMap
{'tamzi': 'tamzi phone', 'asif': 'asif phone'}
nameToPhoneMap.popitem()
('asif', 'asif phone')
nameToPhoneMap
{'tamzi': 'tamzi phone'}
nameToPhoneMap.setdefault('akhil', 'akhil phone')
'akhil phone'
nameToPhoneMap
{'tamzi': 'tamzi phone', 'akhil': 'akhil phone'}
nameToPhoneMap.setdefault('akhil', 'akhil phone1')
'akhil phone'
nameToPhoneMap
{'tamzi': 'tamzi phone', 'akhil': 'akhil phone'}
nameToPhoneMap.fromkeys(['person1', 'person2', 'person3'], 'common phone number')
{'person1': 'common phone number', 'person2': 'common phone number', 'person3': 'common phone number'}
True
True
False
False
4 > 5
False
5 < 6
True
4 > 5 and 5 < 6
False
# and # truth table
# operand1 and operand2
# True and True => True
# True and False => False
# False and True => False
# False and False => False
# op1 and op2 and op3 => op4 and op3
True and True
True
False and False
False
True and False
False
False and True
False
# or
# True and True => True
# True and False => true
# False and True => True

True or True
True
True or False
True
False or True
True
False or False
False
# in => iteration
fruits = ["apple", "banana", "grapes"]
"grapes" in fruits
True
"pineapple" in fruits
False
"apple"=="grapes" or "banana" == "grapes" or "grapes" == "grapes"
True
for fruit in fruits:
    print(fruit)

    
apple
banana
grapes
list(range(0, 10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in range(0, 10):
    print(i)

    
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
for i in range(0, 10, 2):
    print(i)

    
0
2
4
6
8
for i in range(10):
    print(i)

    
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
# print numbers between 10 to 100
for i in range(11, 20):
    print(i)

    
11
12
13
14
15
16
17
18
19
number = 10
while number < 15:
    print(number)
    number += 1

    
10
11
12
13
14
number = 10
if number < 10:
    print("number is less than 10")
else:
    print("number is not less than 10")

    
number is not less than 10
if number < 10:
    print("number is less than 10")
elif number > 10:
    print("number is greater than 10")
else:
    print("number is equal to 10")

    
number is equal to 10
if number < 10:
    print("number is less than 10")
elif number > 10:
    print("number is greater than 10")
else:
    print("number is equal to 10")
else:
    
SyntaxError: invalid syntax
if number < 10:
    print("number is less than 10")
elif number > 10:
    print("number is greater than 10")
else:
    print("number is equal to 10")
else:
    
SyntaxError: invalid syntax
if number < 10:
    print("number is less than 10")
elif number > 10:
    print("number is greater than 10")

    

