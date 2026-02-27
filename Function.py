my_int = 42
my_float = 3.14159
my_string = "Hello, Python!"
my_bool = True
my_list = [1, 2, 3, 4, 5]
my_tuple = (10, 20, 30)
my_dict = {"name": "pranali", "age": 27}

def print_var_details(var, var_name):
    print(f"{var_name}:")
    print(f"  Value: {var}")
    print(f"  Type: {type(var)}")
    print(f"  Memory Address: {id(var)}\n")

print_var_details(my_int, "Integer")
print_var_details(my_float, "Float")
print_var_details(my_string, "String")
print_var_details(my_bool, "Boolean")
print_var_details(my_list, "List")
print_var_details(my_tuple, "Tuple")
print_var_details(my_dict, "Dictionary")