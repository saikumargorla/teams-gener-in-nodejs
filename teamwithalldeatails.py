import json
import random
import os

open("E://saikumar/pyth2.txt","a")
os.remove("E://saikumar/pyth2.txt")
f = open("bk2.json","r") 
contents = f.read()     #reads entire file into a single string
data = json.loads(contents)
students = data["students"]#get list, process with for loop
a = []
for i in range(0,len(students)):
    a.append(students[i])
random.shuffle(a)
json.dumps(a)
n = len(a)
print("the total members:%d" %(n))
cnt = 1
while True:
    try:
        m = input("how many members for a team :")
        if m <= 0 or m > n:
            raise exception
    except(NameError,TypeError,SyntaxError) or exception:
        print("invalid input ")
        print("the total members are:%d" %(n))
        continue
    else:
        break
for i in range(0,n,m):
    print("the %d team" %(cnt))
    b = a[i:i+m]
    c = json.dumps(b)
    print c
    with open("E://saikumar/pyth2.txt","a") as f:
        f.write("the %d team" %(cnt))
        f.write("\n" + c + "\n")    
    cnt += 1
    

