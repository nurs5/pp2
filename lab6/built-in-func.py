import math
import random
list=[]
num=int(input())
for i in range(num):
    i=int(input())
    list.append(i)
result=math.prod(list)
print(result) #ex1

s=str(input())
upperc=[]
lowerc=[]
for i in range(len(s)):
    if s[i].isupper():
        upperc.append(i)
    else:
        lowerc.append(i)
print(len(upperc),len(lowerc))  #ex2

s=input()
left=0
right=len(s)-1
flag=True
while left<right:
    if s[left]!=s[right]:
        flag=False
        break
    left+=1
    right-=1
if flag:
    print("palindrome")
else:
    print("not palindrome")   #ex3 

import time
a,b=int(input()),int(input())
time.sleep(b/1000)
print("Square root of", a, "after", b, "miliseconds is", math.sqrt(a))  #ex4

def a(number):
    return True if number > 0 else False
n=int(input())
x = tuple(a(random.randint(-100, 100)) for i in range(n))
p = all(x)
for i in x:
    print(i, end=' ')
print()
print(p)   #ex5
