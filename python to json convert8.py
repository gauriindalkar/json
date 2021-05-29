import json
keys=["name","degignation","age","salary"]
a=["neelam","programer","24","2400"]
empy1={}
empy2={}
empy3={}
empy4={}
dict={}
for i in range(len(keys)):
    empy1[keys[i]]=a[i]
dict["employee1"]=empy1
# print(empy1)
b=["komal","trainer","24","20000"]
for i in range(len(keys)):
    empy2[keys[i]]=b[i]
dict["employee2"]=empy2
# print(empy2)
c=["anuradha","HR","25","40000"]
for i in range(len(keys)):
    empy3[keys[i]]=c[i]
dict["employee3"]=empy3
# print(empy3)
d=["Abhishek","manager","29","63000"]    
for i in range(len(keys)):
    empy4[keys[i]]=d[i]
dict["employee4"]=empy4
# print(empy4)
out_file = open("file.json", "w")
json.dump(dict, out_file, indent = 6)
out_file.close() 