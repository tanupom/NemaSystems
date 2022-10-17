import json



#need to import javascript variable into this path
f = "/home/infinitysystem/Downloads/Infinity2.0Django_09042022/Pages/Assay_Profiles.txt"


jsonpath = "/home/infinitysystem/Downloads/Infinity2.0Django_09042022/updated-file.json"

ExampleAssayProfile = {}
with open(f) as file:
 for line in file:
    key = line.split(":")[0]
    value = line.split(":")[1]
    print(key)
    print(value)
    ExampleAssayProfile[str(key)] = str(value)
 
with open(jsonpath, "w") as w:
    json.dump(ExampleAssayProfile, w)