num1 = int(input("Enter ur first number : "))
num2 = int(input("Enter ur secound number : "))

operation = input("Choose ur operation : ")

match (operation):

    case "+":
        print(f"Your addition is > {num1+num2}")
    case "-":
        print(f"Your substraction is > {num1-num2}")
    case "*":
        print(f"Your Multiplication is > {num1*num2}")
    case "/":
        print(f"Your Division is > {num1/num2}")
    case _:
        print("Plzz enter valid input...!")
