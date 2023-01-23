i = 1
x = int(input("Enter the number: "))
for _ in range(2, x):
    if x % _ == 0:
        i += _
if x == i:
    print("It is a perfect number")
else:
    print("Not so perfect lol")