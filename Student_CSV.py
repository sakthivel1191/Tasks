import pandas as pd 
with open("Students.csv","w") as s:
    s.write("name,age,mark\n")
    s.write("sakthi,23,65\n")
    s.write("sarmi,23,98\n")
    s.write("vel,20,85\n")
    s.write("mukil,27,77\n")
    s.write("priya,27,75\n")
    s.write("Sakthivel,18,50\n")


data=pd.read_csv("Students.csv")
print("First 5 Row")
print(data.head())

average =data["mark"].mean()

print("Average Mark:",average)
print("students who scored above 80 marks")
print(data[data["mark"]>80])