num = int(input("Enter ur number : "))
count = 0

for i in range(2, num):

    if (num % i == 0):
        count = count+1

if (count == 0):
    print(f"Ur number {num} is prime")
else:
    print(f"Ur number {num} is not prime")
