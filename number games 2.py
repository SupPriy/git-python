import random
fave=31
for i in range (40):
    a=random.randint(30,40);
    if fave==a:
        print 'You win,,YAAAAAAAYYYY!!!!(:'
        break             
    else:
        if a>fave:
            print 'lower'
        else:
            print 'HIGHER'
            print 'no way,try again another day):'
print'Time is up!' 
