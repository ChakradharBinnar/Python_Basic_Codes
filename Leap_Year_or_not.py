year = int(input("Enter ur year : "))
if (((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0)):
    print("Ur year is Leap")

else:
    print("ur year is not leap")
