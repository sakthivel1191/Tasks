def Calculate_total(price,quantity):
    return price*quantity

pname=input("Price Name: ")
price=float(input("Price: "))
quantity=int(input("Quantity: "))

total=Calculate_total(price,quantity)
print("Shopping Bill")
print("Product Name",pname)
print("Quantity",quantity)
print("Final Amount",total)