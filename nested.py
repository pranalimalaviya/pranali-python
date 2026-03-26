text = "PYTHON"
vowel = "aeiouAEIOU"

for char in text:
    if char in vowel:
        continue
    print(char,end=" ")
    
n = int(input("Enter a number: "))

for i in range(1, 11):
    print(n, "x", i, "=", n * i)
    
for i in range(1, 6):
    for j in range(1, i+1):
        print(j, end=" ")
    print()
    
for i in range(5, 0, -1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()
    
for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()
    
for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()
    