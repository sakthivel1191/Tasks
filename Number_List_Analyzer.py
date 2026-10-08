num=[1,2,3,4,5]
for i in num:
    print(i)
max=num[0]
min=num[0]
total=0
for n in num:
    if(n>max):
        max=n
    elif(n<min):
        min=n

    total=total+n

print("Largest Number",max)
print("Smallest Number",min)
print("Total",total)

