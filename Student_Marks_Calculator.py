name=input("student name: ")
mark1=int(input("Mark1: "))
mark2=int(input("Mark2: "))
mark3=int(input("Mark3: "))

total=mark1+mark2+mark3

average=total/3

if(average>=50):
    print("Pass")
else:
    print("Fail")