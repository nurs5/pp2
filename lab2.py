#booleans
print(10>9)
#True            #ex1

print(10==9)
#False           #ex2

print(10<9)
#False           #ex3

print(bool("abc"))
#True            #ex4

print(bool(0))
#False           #ex5

#operators
print(10*5)    #ex1

print(10/2)    #ex2

fruits=["apple", "banana"]
if "apple" in fruits:
   print("Yes, apple is a fruit!")   #ex3

if 5!=10:
   print("5 and 10 is not equal")    #ex4

if 5==10 or 4==4:
   print("At least one of the statements is true")  #ex5
#dictionaries
   car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(car.get("model"))    #ex1

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
car["year"] = 2020     #ex2

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
car["color"] = "red"    #ex3

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
car.pop("model")    #ex4

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
car.clear()    #ex5
#sets
fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
    print("Yes, apple is a fruit!")   #ex1

fruits = {"apple", "banana", "cherry"}
fruits.add("orange")    #ex2

fruits = {"apple", "banana", "cherry"}
more_fruits = {"orange", "mango", "grapes"}
fruits.update(more_fruits)     #ex3

fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")   #ex4

fruits = {"apple", "banana", "cherry"}
fruits.descard("banana")    #ex5
#if else
a = 50 
b = 10
if a > b:
  print("Hello world")   #ex1

a=50
b=10
if a!=b:
    print("Hello World")    #ex2

a=50
b=10
if a==b:
    print("Yes")
else:
    print("No")    #ex3

a=50
b=10
if a==b:
    print("1")
elif(a>b):
    print("2")
else:
    print("3")   #ex4

if a==b and c==d:
    print("Hello")   #ex5

if a==b or c==d:
    print("Hello") #ex6

if 5>2:
    print("YES")  #ex7

a=2
b=5
print("YES") if a==b else print("NO")   #ex8

a=2
b=50
c=2
if a==c or b==c:
    print("YES")   #ex9
#for loops
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)     #ex1

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x=="banana":
        continue
    print(x)    #ex2

for x in range(6):
    print(x)     #ex3

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x=="banana":
        break
    print(x)     #ex4
    #tuples
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)     #ex1

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x=="banana":
        continue
    print(x)    #ex2

for x in range(6):
    print(x)     #ex3

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x=="banana":
        break
    print(x)     #ex4
#while loops
    i=1
while i<6:
    print(i)
    i+=1    #ex1

i=1
while i<6:
    if i==3:
        break
    i+=1     #ex2

i=0
while i<6:
    i+=1
    if i==3:
        continue
    print(i)     #ex3

i=1
while i<6:
    print(i)
    i+=1
else:
    print("i is no longer less than 6")   #ex4
#lists
    fruits=["apple", "banana", "cherry"]
print(fruits[1])    #ex1

fruits = ["apple","banana", "cherry"]
fruits[0]="kiwi"    #ex2

fruits=["apple","banana","cherry"]
fruits.append("orange")   #ex3

fruits=["apple","banana","cherry"]
fruits.insert(1,"lemon")    #ex4

fruits=["apple","banana","cherry"]
frutis.remove("banana")   #ex5

fruits=["apple","banana","cherry"]
print(fruits[-1])        #ex6

fruits=["apple","banana","cherry","orange","kiwi","melon","mango"]
print(frutis[2:5])     #ex7

fruits=["apple","banana","cherry"]
print(len(fruits))    #ex8
#operators
print(10*5)    #ex1

print(10/2)    #ex2

fruits=["apple", "banana"]
if "apple" in fruits:
   print("Yes, apple is a fruit!")   #ex3

if 5!=10:
   print("5 and 10 is not equal")    #ex4

if 5==10 or 4==4:
   print("At least one of the statements is true")  #ex5
