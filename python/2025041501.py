import numpy as np
print(np.__version__)

print(np.array([[1,2,3],[4,5,6]]))
print(np.array([2,3,4], dtype="float32"))


b = np.array([[ 0, 1, 2, 3],
[ 4, 5, 6, 7],
[ 8, 9, 10, 11]])

print(b)
print(b.ndim)
print(b.shape)
print(b.size)
print(b.dtype)
print(b.itemsize)


#axis = 축
#축은 단지 가장 바깥 리스트에서 안쪽리스트 순으로 0부터 이름을 붙인 것.
sumRow, sumCol, sumAll = np.sum(b,axis=0), np.sum(b,axis=1) , np.sum(b)

print(sumRow)
print(sumCol)
print(sumAll)

b = np.array([[ 0, 1, 2, 3],
[ 4, 5, 6, 7],
[ 8, 9, 10, 11],
[12, 13, 14, 15]])

print(b)
print(np.split(b, 2)) # 2개로 나눠짐 


split1, split2 = np.vsplit(b,2) 
print("axis = 0")
print(split1)
print(split2)

split1, split2 = np.hsplit(b,2) 
#[:,0:2][:,2:3]
print("axis = 1")
print(split1)
print(split2)

stack0 = np.stack((b,b))
#2개를 합침[0:4][0,4], axis = 0 (default)
print(stack0.shape)

stack0 = np.stack((b,b), axis = 1)

print("######## reshape(), resize() ########")
print(b.shape) 
print(b.reshape(2,8)) # -> 바뀐 값을 리턴해줌
#print(b.reshape(3,4)) 에러
print(b.reshape(-1, 8)) # 음수 무시
b.resize(2,8) # resize -> 본인이 바뀜
print(b)




