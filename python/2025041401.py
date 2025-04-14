import sys
print(dir(sys))

#10 * (1/0) 에러
# 4 + spam * 3 에러


while True: 
    try:
        x = int(input("Please enter a number:"))
        break
    except ValueError:
        print("Oops ! That was no valid number. Try again...")
        
 
  
        
class B(Exception):
    pass
class C(B):
    pass
class D(C):
    pass


for cls in [B,C,D]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")
        
        
        
def divide(x,y):
    try:
        result = x/y
    except ZeroDivisionError:
        print("division by zero")
    else:
        print("result is", result)
    finally:
        print("executiong finally clause")
        
divide(2,1)
divide(2,0)


def divide(x,y):
    while True:
        try:
            x = int(input("Please enter first number: "))
            y =  int(input("Please enter first number: "))
            result = x/y
        except ZeroDivisionError:
            print("division by zero")
        else:
            print("result is",result)
        finally:
            print("executing finally clause")