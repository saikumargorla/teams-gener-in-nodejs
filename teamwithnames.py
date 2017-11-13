import json
import random
import os

open("E://saikumar/pyth2.txt","a")
os.remove("E://saikumar/pyth2.txt")
f = open("bk2.json","r") 
contents = f.read()     #reads entire file into a single string
students_d = json.loads(contents)
students = students_d["students"]#get list, process with for loop
temp = []
for student in students:
    g = student["Name"]
    temp.append(g)
    random.shuffle(temp)
h = []
h = ",".join(temp)
print h
cnt = 1
n = len(temp)
print("the total members:%d" %(n))
while True:
    try:
        m = input("how many members for a team :")
        if m <= 0 or m > n:
            raise exception
    except(NameError,TypeError,SyntaxError) or exception:
        print("invalid input")
        continue
    else:
        break
for i in range(0,n,m):
    print("the %d team" %(cnt))
    b = ",".join(temp[i:i+m])
    print b
    with open("E://saikumar/pyth2.txt","a") as f:
        f.write("the %d team" %(cnt))
        f.write("\n" + b + "\n")
    cnt+=1
    
