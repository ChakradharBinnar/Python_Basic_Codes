num1 = int(156)
num2 = int(122)
num3 = int(155)

if ((num1 > num2) and (num1 > num3)):
    print(f"{num1} is greatest")
elif ((num2 > num1) and (num2 > num3)):
    print(f"{num2} is greatest")
else:
    print(f"{num3} is greatest")
