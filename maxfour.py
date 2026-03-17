a = 15
b = 45
c = 85
d = 32

if a > b:
    if a > c:
        if a > d:
            maximum = a
        else:
            maximum = d
    else:
        if b > c:
            if b > d:
             maximum = b
        else:
            maximum = d
else:
        if c > d:
            maximum = c
        else:
            maximum = d   
print("The four numbers are:", a, b, c, d)
print("The maximum number is:", maximum)   