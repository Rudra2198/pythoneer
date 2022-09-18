n = int(input("Enter height: "))

num = 1

for i in range(0, n):

    num = 1

    for j in range(0, i + 1):
        # printing number
        print(num, end=" ")

        num = num + 1

    print("\r")