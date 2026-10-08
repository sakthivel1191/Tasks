import numpy as np
marks=np.array([89,56,78,90,34,67,86,50,93,81])

Mean=np.mean(marks)
maximum=np.max(marks)
minimum=np.min(marks)

print("Marks:",marks)
print("Mean:",Mean)
print("Maximum Mark:",maximum)
print("Mimimum Mark:",minimum)
print("Marks Greater than 80:",marks[marks>80])

