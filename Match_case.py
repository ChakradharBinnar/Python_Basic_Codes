num = int(input("Enter ur Password : "))

match num:
    case 123:
        print("Opps...! Enter correct password")

    case 121:
        print("Welcome mr. Chakradhar")

    case _:
        print("invalid password")
