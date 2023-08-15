# Establishing Connection
import mysql.connector as h
mycon = h.connect(host='localhost', user='root', passwd='MyPass', database='marksheet')
cursor = mycon.cursor()
row = cursor.execute('select * from PCMCS')
data1 = cursor.fetchall()
row1 = cursor.execute('select * from PCMB')
data = cursor.fetchall()

# Menu
def menu():
    print("1. Add new student")
    print("2. View marks of student")
    print("3. Change marks of student")
    print("4. Check who is topper")
    print("5. Check passed or failed student")
    print("6. Close")


menu()

option = int(input("Enter an option (1 - 6): "))

# Adding new student
if option == 1:
    x = input("Computer Science or Biology: ")
    a = input("Enter student name: ")
    b = int(input("Enter roll number: "))
    c = int(input("Enter marks obtained in physics: "))
    d = int(input("Enter marks obtained in chemistry: "))
    e = int(input("Enter marks obtained in maths: "))
    f = int(input("Enter marks obtained in biology or computer science: "))
    g = input("Enter result PASS or FAIL: ")
    if x == 'Computer Science':
        inputs = (a, b, c, d, e, f, g)
        st = "insert into PCMCS(student_name,roll_no,physics_marks,chemistry_marks,maths_marks,computer_marks,result) values('{}',{},{},{},{},{},'{}')".format(a, b, c, d, e, f, g)
        cursor.execute(st)
        mycon.commit()

    elif x == 'Biology':
        inputs = (a, b, c, d, e, f, g)
        st = "insert into PCMB(student_name,roll_no,physics_marks,chemistry_marks,maths_marks,biology_marks,result) values('{}',{},{},{},{},{},'{}')".format(a, b, c, d, e, f, g)
        cursor.execute(st)
        mycon.commit()

    else:
        print("A mistake has been made! Please enter your choice Computer Science or Biology correctly when asked.")

# Viewing marks of student
elif option == 2:
    x = input("Computer Science or Biology: ")
    if x == 'Computer Science':
        a = input("Enter student name: ")
        st = "select * from pcmcs where student_name='{}'".format(a)
        y = cursor.execute(st)
        row = cursor.fetchall()
        for y in row:
            print(y)

    elif x == 'Biology':
        a = input("Enter student name: ")
        st = "select * from pcmb where student_name='{}'".format(a)
        y = cursor.execute(st)
        row = cursor.fetchall()
        for y in row:
            print(y)

    else:
        print("INVALID CHOICE!")

# Changing marks of student
elif option == 3:
    x = input("Computer Science or Biology: ")
    a = input("Student name correction? (Yes or No): ")
    b = input("Roll number correction? (Yes or No): ")
    c = input("Physics marks correction? (Yes or No): ")
    d = input("Chemistry marks correction? (Yes or No): ")
    e = input("Maths marks correction? (Yes or No): ")
    f = input("Computer Science or Biology marks correction? (Yes or No): ")
    g = input("Result correction? (Yes or No): ")

    # For computer science students
    if x == 'Computer Science':
        # Changing  computer student's name
        if a == 'Yes':
            b1 = input("Enter old name: ")
            b2 = input("Enter new name: ")
            st = "update pcmcs set student_name = '{}' where student_name = '{}'".format(b2, b1)
            cursor.execute(st)
            mycon.commit()

        elif a == 'No':
            pass

        else:
            print("INVALID CHOICE!")

        # Changing Computer student's roll number
        if b == 'Yes':
            b1 = int(input("Enter old roll number: "))
            b2 = int(input("Enter new roll number: "))
            st = "update pcmcs set roll_no = '{}' where roll_no = '{}'".format(b2, b1)
            cursor.execute(st)
            mycon.commit()

        elif b == 'No':
            pass

        else:
            print("INVALID CHOICE!")

        # Changing Computer student's physics mark
        if c == 'Yes':
            b1 = int(input("Enter student's name: "))
            b2 = int(input("Enter new physics mark: "))
            st = "update pcmcs set physics_marks = '{}' where student_name = '{}'".format(b2, b1)
            cursor.execute(st)
            mycon.commit()

        elif c == 'No':
            pass

        else:
            print("INVALID CHOICE!")

        # Changing Computer student's chemistry mark
        if d == 'Yes':
            b1 = int(input("Enter student's name: "))
            b2 = int(input("Enter new chemistry mark: "))
            st = "update pcmcs set chemistry_marks = '{}' where student_name = '{}'".format(b2, b1)
            cursor.execute(st)
            mycon.commit()

        elif d == 'No':
            pass

        else:
            print("INVALID CHOICE!")

        # Changing Computer student's maths mark
        if e == 'Yes':
            b1 = int(input("Enter student's name: "))
            b2 = int(input("Enter new maths mark: "))
            st = "update pcmcs set maths_marks = '{}' where student_name = '{}'".format(b2, b1)
            cursor.execute(st)
            mycon.commit()

        elif e == 'No':
            pass

        else:
            print("INVALID CHOICE!")

        # Changing Computer student's computer science mark
        if f == 'Yes':
            b1 = int(input("Enter student's name: "))
            b2 = int(input("Enter new computer science mark: "))
            st = "update pcmcs set computer_marks = '{}' where student_name = '{}'".format(b2, b1)
            cursor.execute(st)
            mycon.commit()

        elif f == 'No':
            pass

        else:
            print("INVALID CHOICE!")

        # Changing Computer student's result
        if g == 'Yes':
            b1 = int(input("Enter student's name: "))
            b2 = int(input("Enter new result PASS or FAIL: "))
            st = "update pcmcs set result = '{}' where student_name = '{}'".format(b2, b1)
            cursor.execute(st)
            mycon.commit()

        elif g == 'No':
            pass

        else:
            print("INVALID CHOICE!")

    # For Biology students
    if x == 'Biology':
        # Changing biology student's name
        if a == 'Yes':
            b1 = input("Enter old name: ")
            b2 = input("Enter new name: ")
            st = "update pcmb set student_name = '{}' where student_name = '{}'".format(b2, b1)
            cursor.execute(st)
            mycon.commit()

        elif a == 'No':
            pass

        else:
            print("INVALID CHOICE!")

        # Changing biology student's roll number
        if b == 'Yes':
            b1 = int(input("Enter old roll number: "))
            b2 = int(input("Enter new roll number: "))
            st = "update pcmb set roll_no = '{}' where roll_no = '{}'".format(b2, b1)
            cursor.execute(st)
            mycon.commit()

        elif b == 'No':
            pass

        else:
            print("INVALID CHOICE!")

        # Changing biology student's physics mark
        if c == 'Yes':
            b1 = int(input("Enter student's name: "))
            b2 = int(input("Enter new physics mark: "))
            st = "update pcmb set physics_marks = '{}' where student_name = '{}'".format(b2, b1)
            cursor.execute(st)
            mycon.commit()

        elif c == 'No':
            pass

        else:
            print("INVALID CHOICE!")

        # Changing biology student's chemistry mark
        if d == 'Yes':
            b1 = int(input("Enter student's name: "))
            b2 = int(input("Enter new chemistry mark: "))
            st = "update pcmb set chemistry_marks = '{}' where student_name = '{}'".format(b2, b1)
            cursor.execute(st)
            mycon.commit()

        elif d == 'No':
            pass

        else:
            print("INVALID CHOICE!")

        # Changing biology student's maths mark
        if e == 'Yes':
            b1 = int(input("Enter student's name: "))
            b2 = int(input("Enter new maths mark: "))
            st = "update pcmb set maths_marks = '{}' where student_name = '{}'".format(b2, b1)
            cursor.execute(st)
            mycon.commit()

        elif e == 'No':
            pass

        else:
            print("INVALID CHOICE!")

        # Changing biology student's biology mark
        if f == 'Yes':
            b1 = int(input("Enter student's name: "))
            b2 = int(input("Enter new biology mark: "))
            st = "update pcmb set biology_marks = '{}' where student_name = '{}'".format(b2, b1)
            cursor.execute(st)
            mycon.commit()

        elif f == 'No':
            pass

        else:
            print("INVALID CHOICE!")

        # Changing biology student's result
        if g == 'Yes':
            b1 = int(input("Enter student's name: "))
            b2 = int(input("Enter new result PASS or FAIL: "))
            st = "update pcmb set result = '{}' where student_name = '{}'".format(b2, b1)
            cursor.execute(st)
            mycon.commit()

        elif g == 'No':
            pass

        else:
            print("INVALID CHOICE!")

# Checking topper
elif option == 4:
    a = input("Computer Science or Biology: ")

    # Finding Computer Science topper for each subject
    if a == 'Computer Science':
        q = input('SELECT ONE SUBJECT FROM: Physics, Chemistry, Maths, Computer Science: ')

        # Physics Topper
        if q == 'Physics':
            st = 'select student_name from pcmcs order by physics_marks desc'
            y = cursor.execute(st)
            row = cursor.fetchall()
            count = 0
            for y in row:
                if count < 1:
                    print("Highest mark scored by:", y)
                    count += 1

                elif count == 1:
                    print("Other students:")
                    print(y)
                    count += 1

                else:
                    print(y)

        # Chemistry Topper
        elif q == 'Chemistry':
            st = 'select student_name from pcmcs order by chemistry_marks desc'
            y = cursor.execute(st)
            row = cursor.fetchall()
            count = 0
            for y in row:
                if count < 1:
                    print("Highest mark scored by:", y)
                    count += 1

                elif count == 1:
                    print("Other students:")
                    print(y)
                    count += 1

                else:
                    print(y)

        # Maths Topper
        elif q == 'Maths':
            st = 'select student_name from pcmcs order by maths_marks desc'
            y = cursor.execute(st)
            row = cursor.fetchall()
            count = 0
            for y in row:
                if count < 1:
                    print("Highest mark scored by:", y)
                    count += 1

                elif count == 1:
                    print("Other students:")
                    print(y)
                    count += 1

                else:
                    print(y)

        # Computer Science Topper
        elif q == 'Computer Science':
            st = 'select student_name from pcmcs order by computer_marks desc'
            y = cursor.execute(st)
            row = cursor.fetchall()
            count = 0
            for y in row:
                if count < 1:
                    print("Highest mark scored by:", y)
                    count += 1

                elif count == 1:
                    print("Other students:")
                    print(y)
                    count += 1

                else:
                    print(y)

        else:
            print('INVALID CHOICE!')

    # Finding Biology topper for each subject
    elif a == 'Biology':
        q = input('SELECT ONE SUBJECT FROM: Physics, Chemistry, Maths, Biology: ')

        # Physics Topper
        if q == 'Physics':
            st = 'select student_name from pcmb order by physics_marks desc'
            y = cursor.execute(st)
            row = cursor.fetchall()
            count = 0
            for y in row:
                if count < 1:
                    print("Highest mark scored by:", y)
                    count += 1

                elif count == 1:
                    print("Other students:")
                    print(y)
                    count += 1

                else:
                    print(y)

        # Chemistry Topper
        elif q == 'Chemistry':
            st = 'select student_name from pcmb order by chemistry_marks desc'
            y = cursor.execute(st)
            row = cursor.fetchall()
            count = 0
            for y in row:
                if count < 1:
                    print("Highest mark scored by:", y)
                    count += 1

                elif count == 1:
                    print("Other students:")
                    print(y)
                    count += 1

                else:
                    print(y)

        # Maths Topper
        elif q == 'Maths':
            st = 'select student_name from pcmb order by maths_marks desc'
            y = cursor.execute(st)
            row = cursor.fetchall()
            count = 0
            for y in row:
                if count < 1:
                    print("Highest mark scored by:", y)
                    count += 1

                elif count == 1:
                    print("Other students:")
                    print(y)
                    count += 1

                else:
                    print(y)

        # Biology Topper
        elif q == 'Biology':
            st = 'select student_name from pcmb order by biology_marks desc'
            y = cursor.execute(st)
            row = cursor.fetchall()
            count = 0
            for y in row:
                if count < 1:
                    print("Highest mark scored by:", y)
                    count += 1

                elif count == 1:
                    print("Other students:")
                    print(y)
                    count += 1

                else:
                    print(y)

        else:
            print('INVALID CHOICE!')

    else:
        print('INVALID CHOICE!')

# Checking passed or failed student
elif option == 5:
    a = input('Computer Science or Biology: ')

    # For Computer Science
    if a == 'Computer Science':
        b = input('Enter - PASSED for Passed Students names or Enter - FAILED for Failed Students names: ')

        # Students who passed
        if b == 'PASSED':
            st = 'select student_name from pcmcs where result="PASS"'
            y = cursor.execute(st)
            row = cursor.fetchall()
            for y in row:
                print(y)

        # Students who failed
        elif b == 'FAILED':
            st = 'select student_name from pcmcs where result="FAIL"'
            y = cursor.execute(st)
            row = cursor.fetchall()
            for y in row:
                print(y)

        else:
            print('INVALID CHOICE!')

    # For Biology
    elif a == 'Biology':
        b = input('Enter - PASSED for Passed Students names or Enter - FAILED for Failed Students names: ')

        # Students who passed
        if b == 'PASSED':
            st = 'select student_name from pcmb where result="PASS"'
            y = cursor.execute(st)
            row = cursor.fetchall()
            for y in row:
                print(y)

        # Students who failed
        elif b == 'FAILED':
            st = 'select student_name from pcmb where result="FAIL"'
            y = cursor.execute(st)
            row = cursor.fetchall()
            for y in row:
                print(y)

        else:
            print('INVALID CHOICE!')

    else:
        print('INVALID CHOICE!')

# Closing
elif option == 6:
    mycon.close()

else:
    print('INVALID CHOICE!')

