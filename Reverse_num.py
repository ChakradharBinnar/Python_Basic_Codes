num = int(123)
rev = int(0)
while (num > 0):
    rem = num % 10
    rev = (rev*10)+rem
    num = num//10

print("Reverse num is >>> ", rev)
