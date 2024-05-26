# enter the size of triangle: 3
# 
# *
# **
# ***
#
# *
# **
# ***
# ****

size_of_triangle = int(input("Enter triangle size: "))
for x in range(0,size_of_triangle):
    for y in range(0,x+1):
        print("*" , end = '')
        if x== y:   
            print(end = '\n')
