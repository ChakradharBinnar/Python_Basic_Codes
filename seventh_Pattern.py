for i in range(0, 4):
    for j in range(3, i, -1):
        print(" ", end="")
    for k in range(i+1):
        print(" *", end="")
    print()
