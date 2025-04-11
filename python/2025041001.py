def standard_arg(arg):
    print(arg)
    
def pos_only_arg(arg,/):
    print(arg)

def kwd_only_arg(*,arg):
    print(arg)
    
standard_arg("standard_arg(arg)")
standard_arg(arg = "standard_arg(arg)")

pos_only_arg("pos_only_arg(arg)")
#pos_only_arg(arg = "pos_only_arg(arg)")

#kwd_only_arg("kwd_only_arg(arg)")
kwd_only_arg(arg = "kwd_only_arg(arg)")


print("===========")

print(list(range(3,6)))

args = [3,6]
print(list(range(*args))) #언패킹

print("===========")

#람다
foo = lambda a,b:a+b
print(foo(1,2))

def make_incrementor(n):
    return lambda x: x+n

f = make_incrementor(0)
print(f(10))


print("===========")

l = [1,4,3,2]
l.sort()
print(l)


print("===========")

#큐 알고리즘
from collections import deque #collections패키지 안에 있는 deque클래스 사용
queue = deque(["A","B","C"])
queue.append("D")
queue.append("F")
print(queue.popleft())
print(queue.popleft())
print(queue.popleft())


squares = []
for x in range(10):
    squares.append(x**2)
    
print(*squares)



squares = list(map(lambda x:x ** 2,range(10)))
print(*squares)

vec = [-4, -2, 0, 2 ,4]

print([x * 2 for x in vec])






