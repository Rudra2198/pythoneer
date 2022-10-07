import numpy as np
from scipy import stats

def statcalc(arr1):
    sum = 0
    for i in arr1:
        sum += i

    mean = sum / a

    arr = np.array(list(arr1))
    mode = stats.mode(list(arr))
    median = np.median(list(arr1))

    print("The mean is " + str(mean) + ", the median is " + str(median) + ", and the mode is " + str(mode[0]))


a = int(input("Enter capacity of array : "))

arr1 = []

for i in range(a):
    arr1.append(int(input("Enter " + str(i) + " value : ")))

statcalc(list(arr1))


