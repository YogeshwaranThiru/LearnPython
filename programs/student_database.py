# list
# add
# update
# remove
# end
# student (rollno, name)


students = {} # key is roll no
while True:
    print("Options:")
    print("1] List")
    print("2] Add")
    print("3] Update")
    print("4] Remove")
    print("5] End")

    user_choice = int(input("Please select: "))

    if user_choice == 1:
        for key in students:
            student = students[key]
            print(f"Rollno: {student['rollno']}")
            print(f"Name: {student['name']}")
    elif user_choice == 2:
        rollno = input("please enter rollno: ")
        name = input("please enter name: ")
        student_to_add = {
            "rollno": rollno,
            "name": name
        }
        students[rollno] = student_to_add
    elif user_choice == 3:
        rollno = input("please enter rollno: ")
        name = input("please enter name: ")
        student_to_add = {
            "rollno": rollno,
            "name": name
        }
        students[rollno] = student_to_add
    elif user_choice == 4:
        rollno = input("please enter rollno: ")
        students.pop(rollno)
    elif user_choice == 5:
        break