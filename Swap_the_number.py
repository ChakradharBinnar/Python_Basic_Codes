# By using Third Variable >>>
a = 10
b = 20
print("Before swapping > ")
print(f" a is > {a}")
print(f" b is > {b}")

print("After swapping > ")
temp = a
a = b
b = temp
print(f" a is > {a}")
print(f" b is > {b}")
print("\n")

# Without using Third Variable >>>

x = 100
y = 200

print("Before swapping > ")
print(f" x is > {x}")
print(f" y is > {y}")

print("After swapping > ")
x = x+y
y = x-y
x = x-y

print(f" x is > {x}")
print(f" y is > {y}")
print("\n")

# Without using Third Variable >>>

a1 = 111
b1 = 222
print("Before swapping > ")
print(f" a1 is > {a1}")
print(f" b1 is > {b1}")

a1, b1 = b1, a1

print("After swapping > ")
print(f" a1 is > {a1}")
print(f" b1 is > {b1}")
