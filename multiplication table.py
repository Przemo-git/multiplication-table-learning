import random

while True:
    x=random.randint(1,10)
    y=random.randint(1,10)
    while True:
        z=input('Count this please: %d*%d'%(x,y))
        if z.isdecimal():
            z=int(z)
            break
    if z==x*y:
        print('   ')
        print('OK')
        print('   ')
    else:
        print('   ')
        print('Wrong, wrong, wrong one more time wrong!!!')
        print('It is:',x*y)
        print('   ')
