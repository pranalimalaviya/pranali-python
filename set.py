myset = {1, 2, 3, 4, 5}
myset.add(6)
print(myset)
myset.remove(3)
print(myset)

is_present = 2 in myset
print(is_present)

#que=2
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

result = set_a.union(set_b)
print(result)
result = set_a & set_b
print(result)
result = set_a.difference(set_b)
print(result)

#que=3
student = {"Name": "Alice", "Age": "20", "Grade": "A"}
print(student["Age"])
student["city"] = "Delhi"
print(student)
student.update({"Age" : "21"})
print(student)
student.pop("Grade")
print(student)

#que=4
keys = ['id', 'name', 'email']
values = [101, 'Bob', 'bob@example.com']
result = dict(zip(keys, values))
print(result)

#que=5
s = '123'
num = int(s)
print(num)
lst = [1, 2, 3]
tup = tuple(lst)
print(tup)
tup = (4, 5, 6)
lst = list(tup)
print(lst)
pairs = [(1, 'A'), (2, 'B')]
result = dict(pairs)
print(result)

#que=6
lst = [10, 20, 30, 40]
del lst[2]
print(lst)