import random

A = [random.randint(1,10) for x in range(0,10)]
print(A)

count = 1

for i in A:
    print(count,i)
    count +=1

for num, list in enumerate(A,1):
    print(num,list)

