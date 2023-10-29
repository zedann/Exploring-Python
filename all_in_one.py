# n = 5
# print(n)
# n='zedan'
# print(n)
# n=True
# print(n)
# n=None
# print(n)
# n = 'z'
# print(n)

# n,m = 5,5
# if  n > m:
#     print(f"{n} > {m}" )
# elif n < m:
#     print(f"{n} < {m}")
# else:
#     print(f"{n}={m}")

# n,m=10 , 7
# if (n > 5 and m < 10):
#     print("hello")

# n=10
# while n:
#     print(n)
#     n-=1

# for i in range(10,-1,-1):
#     print(i)

# math

# print(5/2)
# print(5//2)
# print(int(-5/2))

# print(-10%3)
# import math
# print(math.fmod(-10,3))

# import math
# print(math.floor(3/2))

# max / min int
# float("inf")
# float("-inf")

# import math
# print(math.pow(2,200) < float("inf"))

# arrays

# arr = [1,2,3]
# print(arr)

# arr.append(4)
# arr.append(5)
# print(arr)
# arr.pop()
# print(arr)
# arr.insert(0,5) #O(n)
# print(arr)

# n = 5
# arr = [0]*n
# print(arr)

# from collections import deque
# arr = [1, 2, 3, 4, 5, 6, 7]
# arr2 = [10, 20, 30, 40]

# for n1, n2 in zip(arr, arr2):
#     print(n1, n2)
# print(arr[1:3]) # exclude 3

# unpacking or destructuring in js

# a,b,c = [1,2,3]
# print(a,b,c)

# for i in range(len(arr)):
#     print(arr[i],end=' ')
# print()

# for n in arr:
#     print(n)

# for i , n in enumerate(arr):
#     print(i , n)

# print(arr)
# arr.reverse()
# print(arr)

# print(arr)
# arr.sort(reverse=True)
# print(arr)
# arr.sort(key=lambda x: x % 2 == 0)
# print(arr)

# arr3 = [[0]*4 for i in range(4)]
# print(arr3)

# print(ord('A'))

# strings = ['ab', 'cd', 'ef']
# print("".join(strings))

# q = deque()
# q.append(1)
# q.append(2)
# q.append(3)
# q.appendleft(5)
# q.appendleft(6)
# q.pop()
# q.popleft()
# print(q)

# myset = set()
# myset.add(1)
# myset.add(2)
# myset.add(3)
# myset.add(3)

# print(myset)
# print(1 in myset)
# myset.remove(3)
# print(3 in myset)
# print(len(myset))

# myset = set([1, 2, 3, 4, 5, 6, 7, 8, 8, 8])
# print(myset)

# myset = set()
# myset = {i for i in range(10)}
# print(myset)

# HashMap Dictunary

# myMap = {}
# myMap['zedan'] = 1
# myMap['zedanmoh'] = 12
# print(myMap)

# Dict comprehension

# myMap = { i:10*i for i in range(3)}
# print(type (myMap))

# myMap = {"zedan": 12, 1: "moro"}
# print(myMap)
# print(myMap["zedan"])

# tuple like arrays but immutable and () not []
# tup = (1, 2, 3)
# can't tup[0]=10
# can read
'''
it can be use as key for hashmap
like pairs 
'''

# myMap = {(1, 2): 2}
# print(myMap[(1, 2)])

'''
why we need tuples then ?
we need tuples because lists can't be keys 
why can't be keys because they are not hashed 
what is this mean ?
it is mean that we cant replace it with hash value so everytime we call the key get this hashed value be the same
'''

# heaps -> minMax heap


# minHeap = []
# heapq.heappush(minHeap, 3)
# heapq.heappush(minHeap, 5)
# heapq.heappush(minHeap, 1)
# heapq.heappush(minHeap, 2)
# print(minHeap[0])

# while len(minHeap):
#     print(minHeap[0])
#     heapq.heappop(minHeap)

# arr = [2,1,8,4,5]
# heapq.heapify(arr)
# while arr:
#     print(heapq.heappop(arr))

# def fuc(n,m):
#     return n * m;

# def outer(a,b):
#     c = "c"
#     def inner():
#         return a + b + c
#     return inner()




import heapq
class MyClass:
    # constructor
    def __init__(self, nums):
        # create member number
        self.nums = nums
        self.size = len(nums)

    def getLength(self):
        return self.size

    def getDoubleLength(self):
        return 2*self.getLength()


nums = [1, 2, 3, 4]
obj = MyClass(nums)
print(obj.getDoubleLength())

class A:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.country = "EGY"
    def getCountry(self):
        return self.country
    
class B(A):
    def __init__(self):
        A.__init__(self)

oB = B("zedan",26)

print(oB)
    
    
oA = A("zedan",21)

print(oA.getCountry())

