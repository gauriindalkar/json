import json
d={'4': 5,'6': 7,'1': 3,'2': 4}
print("original string:")
print(d)
print("json data:")
print(json.dumps(d,sort_keys=True,indent=4))

