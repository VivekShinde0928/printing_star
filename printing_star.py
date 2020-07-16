x = int(input('Enter your number :'))
y = int(input('Enter 1 or 0 :'))
if y == 1:
    print('*' * x)
    while True:
        x = x - 1
        print('*' * x)
        if x == 0:
            break
elif y == 0:
    z=0
    while True:
        z=z+1
        print('*'*z)
        if z==x:
            break
else:
    print("\noops! something went wrong")
