import random
x = random.randint(1, 100)
z = 0
while (z < 3):
    y = int(input('guess Number: '))
    if (y == x):
        print('correct number')
    else: print('incorrect Number')
    z+=1