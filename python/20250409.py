for n in range(2,10):
    for x in range(2,n):
        if n % x == 0:
            print(n,'equals',x,'*',n//x)
            break
        
        else:
            print(n,'is a prime number')
            
           
           
print("==============") 


#피보나치 수열
def fib(n):
    a,b = 0,1
    while a<n:
        print(a,end=' ')
        a,b = b, a+b
        
    print()
    
f = fib

f(100)


def ask_ok(prompt, retries = 4, reminder = "Please try again"):
    while True:
        ok = input(prompt)
        if ok in ('yes'):
            return True
        if ok in ('no'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)
        
ask_ok("입력:",3,"다시 입력 해주세요")


def f(a,L=None):
    if L is None:
        L = []
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))

