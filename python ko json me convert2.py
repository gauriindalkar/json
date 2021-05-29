import json
a={"name":"David","class":"I","age": "6"}
file = open("file2.json", "w")
b=json.dumps(a)
json.dump(a,file, indent = 6)
file.close() 