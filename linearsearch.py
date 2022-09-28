def search(arr, x):
    for i in range(len(arr)):

        if arr[i] == x:
            print(i)
            return i

    return -1

array = [10,20,30,40,50,60,70,80,90,100,110,120,130]

target = 60

search(array,target)


