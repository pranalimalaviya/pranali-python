a = 100
b = 100

print("Before modification:")
print(f"a = {a}, id(a) = {id(a)}")
print(f"b = {b}, id(b) = {id(b)}")
print(f"Do a and b share the same memory? {'Yes' if id(a) == id(b) else 'No'}\n")

a = 200

print("After modification:")
print(f"a = {a}, id(a) = {id(a)}")
print(f"b = {b}, id(b) = {id(b)}")
print(f"Do a and b share the same memory? {'Yes' if id(a) == id(b) else 'No'}")