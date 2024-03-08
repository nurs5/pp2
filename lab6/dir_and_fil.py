import os
import string
 
path = "../"
dir_list = os.listdir(path)
 print("Files and directories in '", path, "' :")
 print(dir_list)    #ex1

print('Exist:', os.access("../", os.F_OK))
print('Readable:', os.access("../", os.R_OK))
print('Writable:', os.access("../", os.W_OK))
print('Executable:', os.access("../", os.X_OK)) #ex2 

path = r"pp2\dates"
print(os.path.exists(path))
print(os.path.basename(path))
print(os.path.dirname(path))   #ex3 

def line(anyfile):
        with open(anyfile) as f:
                for i, l in enumerate(f):
                        pass
        return i + 1
print("Number of lines:",line("sampl.text"))  #ex4 

items = ["My", "name", "is","Nursultan"]
file = open('sampl_list.txt','w')
for i in items:
	file.write(i+"\n")
file.close()     #ex5  

if not os.path.exists("letters"):
   os.makedirs("letters")
for letter in string.ascii_uppercase:
   with open(letter + ".txt", "w") as f:
       f.writelines(letter)   #ex6  

with open("sampl_list.txt") as g:
    with open("B.txt", "w") as g1:
        for i in g:
            g1.write(i)    #ex7   

if os.path.exists("delete.txt"):
  os.remove("delete.txt")
else:
  print("The file does not exist")  #ex8 



