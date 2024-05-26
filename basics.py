print("hello world")


# addition of numbers
a = 1
b = 2
c = a + b
print(c)

# float datatype
a = 1.0
b = 2.0
c= a + b
print(c)

# string data type
left_string = "foo"
right_string = "bar"
print(left_string + right_string)


##### logical operators #####  
# "and" operator 
if True and True:   
    print("both true")
if True and False:
    print("this will not work")

# "or" operator
if True or True:
    print("both true")
if True or False:
    print("one of them is true")

## Data structures
# list 
print("--list--")
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)
print("Length of list is: " + str(len(thislist)))
print("3rd element from start: ", thislist[2])
print("2rd element from end: ", thislist[-2])

sorting_test_list = [423, 1, 334,234 ,435]
print("sorting list: ", str(sorting_test_list))
sorting_test_list.sort()
print("sorting list: ", str(sorting_test_list))

## type()
print("--type--")
a = 1
b = "stirng"
c = 2.0
d = True
e = []
f = {
    "name": "Yogu",
    "height": 6
}
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))


# for loops
print('--for--')
for fruit in thislist:
    print("the fruit is " + fruit)

print('looping a string')
for x in "yogeshwaram":
    print(x)

print("--append to list --")
thislist.append("kiwi")
print(thislist)


print("--loop with range--")
for x in range(0,5):
    print("for loop with range: " + str(x))

for x in range(7,9):
    print("for loop with range: " + str(x))


# string
print('--string--')
print('firstline with end', end='')
print('second line without end')
print('thrid line')


# range funciton and list comprephension
print('--range funciton and list comprephension--')
# range func returns and iterable
# can print using 
print("range(5) using list comprehension")
print([x for x in range(5)])

print("range(13,20)) using list comprehension")
print([x for x in range(13, 20)])

print("range(13,40,3)) using list comprehension")
print([x for x in range(13, 40, 3)])

print("range(13,5,-1)) using list comprehension")
print([x for x in range(13, 5, -1)])

print("range(40,3,-3)) using list comprehension")
print([x for x in range(40, 3, -3)])


# list comprehension

print("[x for x in range(200) if (x%5 and x%3) == 0]")
print([x for x in range(200) if x%5 ==0 and x%3 == 0])
