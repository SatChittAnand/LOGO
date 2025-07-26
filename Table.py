a = int(input("Enter any value: "))

def maketable(a):
    for i in range(1,11):
        print(a,'X' , i , "=" , a*(i))
maketable(a)
Greet = input("Thank You!")

class ZeroDenominatorError(Exception):
    try:
        a=10
        b=0
        if(b==0):
            raise ZeroDivisionError()
        c = a/b
    except ZeroDivisionError:
        print('zero division error occured')

z = ZeroDenominatorError()


