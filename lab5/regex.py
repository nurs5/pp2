from re import *
text=input()
pattern=r'ab*'
print(*findall(pattern,text))   
#exer 1

from re import *
text1=input()
pattern1=r'ab{2,3}'
print(*findall(pattern1,text1))
#exer 2

from re import *
text2=input()
pattern2=r'[a-z]+_[a-z]+'
print(*findall(pattern2,text2))  
#exer 3

from re import *
text3=input()
pattern3=r'[A-Z][a-z]+'
print(*findall(pattern3,text3))

#exer 4

from re import * 
text4=input()
result=[]
for i in text:
    if match(r'a.*b$', i):
        result.append(i)
print(*result)     

#exer 5

from re import *
text = input()
pattern, pattern1 = r'[,. ]', r':'
print(sub(pattern, pattern1, text))  
##exer 6

from re import *
snake_string = input().split('_')
print((snake_string[0] + ''.join(x.title() for x in snake_string[1:])))   

#exer 7

from re import *
text = input()
pattern = r'[A-Z][^A-Z]*'
print(*findall(pattern, text))   

#exer 8

from re import *
text = input()
pattern = r"(?<!^)(?=[A-Z])"
print(sub(pattern, ' ', text))   

#exer 9


from re import *
string = input()
snake_case_string = sub('([A-Z])', r'_\1', string).lower()
if snake_case_string[0] == '_':
    snake_case_string = snake_case_string[1:]
print(snake_case_string)   
 
#exer 10
