#튜플 (리스트는 가변 튜플은 불변)
t = 12345,54321,'hello'
print(t[0])

u = t,(1,2,3,4,5)

print(u)


#집합

basket={'apple','apple','banana'}
print(basket)

a =set('abracadabra') #{'a', 'r', 'b', 'c', 'd'}

b =set('alacazam') #{a,l,c,z,m}

print(a)
print(b)
print(a-b)
print(a|b)
print(a&b)

tel = {'jack':4098,'sape':4190}
tel['guido'] = 323
print(tel)


# 모듈 import 실습
import fibonacci as fib3
resultList = []
resultList = fib3.fibonacci(1000)
print(resultList)


# import -> 동적 라이브러리 호출(dll)
# include (C, C++) 정적 라이브러리(sll)12



