user_input = input("Enter a boolean value (True/False): ")

bool_value = user_input.strip().lower() == "true"

int_value = int(bool_value)
str_value = str(bool_value)

print("\nBoolean value:", bool_value)
print("Converted to integer:", int_value)
print("Converted to string:", str_value)