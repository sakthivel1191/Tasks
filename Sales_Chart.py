import matplotlib.pyplot as plt

months=["January","Februry","march","april","may"]
sales=[15000,9000,4000,12000,21000]

plt.bar(months,sales)

plt.title("5 months of sales values")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.show()