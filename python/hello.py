print("hello")
a = [1, '1' , "1"] #문자열 배열
a = str(a[0]) + a[1] + a[2]
b = int(a[0]) + int(a[1]) + int(a[2])
print(b)


print(8 / 5) #실수
print(10 / 5) #실수
print(10 // 5) #정수
print(10 * 5)

print("=================")

i = 1
print(i << 1)
print(i << 2)
print(i >> 1)
i = 8
print(i >> 3)

word = "Python"
print(word[0:2])


word = "Python"
print(word[2:5])


print("=================")

#str은 불변
#word[0] = 'J'
word = "Jython"
print(word)

word = 'J' + word[1:]

length = len(word)
print(word)
print(length)


print("=================")

letters = ['a','b','c','d']
letters[2:5] = []
print(letters)

print("=================")

temp = input("입력하세요:")

print(temp)
print(type(temp))


print("=================")

temp = int(input("숫자를 입력하세요:"))

if temp < 0:
    print("음수를 입력 하셨습니다.")
elif temp > 0:
    print("양수를 입력 하셧습니다.")
else:
    print("Zero 를 입력 하셨습니다")
    
    
print("=================")

words = ['cat', 'window', 'defenestrate']

for w in words:
    print(w, len(w))
    

print("=================")
for i in range(5):
    print(i)
