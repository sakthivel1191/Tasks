import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("employees.csv")

print("Employees Data")
print(df)

average_salary=df["salary"].mean()

highest_salary=df["salary"].max()

print("\nAverage Salary",average_salary)
print("Highest Salary",highest_salary)

plt.bar(df["name"],df["salary"])

plt.title("Employee Salary Chart")
plt.xlabel("Employee")
plt.ylabel("Salary")

plt.show()
