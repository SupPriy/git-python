fave=234
for i in range (40):
     guess=int(raw_input('What is my favorite number?!Hint hint,it is between 1-1000'))
     if fave==guess:
        print 'You win,,YAAAAAAAYYYY!!!!(:'
        break             
     else:
        if guess>fave:
            print 'lower'
        else:
            print 'HIGHER'
            print 'no way,try again another day):'
print'Time is up!' 
  
