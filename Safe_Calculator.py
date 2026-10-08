try:
    num1=int(input("Enter Number1:"))
    num2=int(input("Enter Number2:"))

    result=num1/num2
    print("Result:",result)

except Exception as e:
    print(e,"\nDont Divisible by zero")
    print(e,"\nEnter Number only")