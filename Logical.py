val1 = input("Enter first boolean value (True/False): ")
val2 = input("Enter second boolean value (True/False): ")

bool1 = val1.lower() == "true"
bool2 = val2.lower() == "true"

print("\nResults:")
print("AND (bool1 and bool2):", bool1 and bool2)
print("OR (bool1 or bool2):", bool1 or bool2)
print("NOT (not bool1):", not bool1)
print("NOT (not bool2):", not bool2)