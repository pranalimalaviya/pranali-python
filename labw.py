while True:
    num = int(input("Enter a number: "))
    if (num == 0):
        print("Stop")
        break
        print(num)
        
for i in range(1, 11):
    print(i ** 2)

i = 1
while (i <= 50):
    if i % 2 == 0:
        print(i)
    i += 1
    
for i in range(1, 21, 2):
    print(i)
    
for i in range(5, 51, 5):
    print(i)
    
for i in range(10, 0, -1):
    print(i)
    
for i in range(1, 51):
    if (i % 2 == 0) and (i % 3 == 0):
        print(i, "divisable by both 2 and 3")
    elif(i % 2 == 0):
        print(i, "divisable by 2")
    elif(i % 3 == 0):
        print(i, "divisable by 3")
