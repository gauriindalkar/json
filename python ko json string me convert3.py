import json
print(json.dumps({"name":"gauri","age":"18"}))
print(json.dumps(["gauri","18"]))
print(json.dumps(("gauri","18")))
print(json.dumps((13,22)))
print(json.dumps((10.5)))
print(json.dumps(True))
print(json.dumps(False))
# print(json.dumps(None))