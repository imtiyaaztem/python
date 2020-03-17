strfname = input("please enter first name\n")
strsname = input("please enter surname\n")
intmark = int(input("enter your mark\n"))
if (intmark>79) and (intmark<101):
    print("Student name", strfname, "Surname", strsname, "Grade A-Outstanding")
elif (intmark>=60) and (intmark<79):
    print("Student name", strfname, "Surname", strsname, "Grade B-Satisfactory")
elif (intmark>=50) and (intmark<59):
    print("Student name", strfname, "Surname", strsname, "Grade C-Pass")
elif (intmark>0) and (intmark<49):
    print("Student name", strfname, "Surname", strsname, "Grade D-Fail")


