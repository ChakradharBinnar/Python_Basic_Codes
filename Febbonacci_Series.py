num = int(input("Enter ur number : "))
a = int(0)
b = int(1)
for i in range(0, num):
    print(a, end=" ")
    c = a+b
    a = b
    b = c
