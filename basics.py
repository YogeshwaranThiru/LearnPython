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