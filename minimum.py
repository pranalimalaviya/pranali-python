a = 15
b = 25
c = 85

if a < b:
    if a < c:
        minimum = a
    else:
            minimum = c
else:
     if b < c:
        minimum = b
     else:
        minimum = c
    
print("The minimum number is", minimum)