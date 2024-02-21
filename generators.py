n=int(input())
num_sq=(i**2 for i in range(1,n+1))
print(*num_sq) #ex1
n=int(input())
even_num=(i for i in range(n+1)  if i%2==0)
print(*even_num,sep=',') #ex2
num=int(input())
numbers=(i for i in range(num+1) if (i%3==0 and i%4==0))
print(*numbers) #ex3
def squares(a,b):
    for i in range(a,b+1):
        yield i**2

a=int(input())
b=int(input())
print(*squares(a,b))   #ex4
number=int(input())
print(*(i for i in range(number,0,-1))) 
#ex5