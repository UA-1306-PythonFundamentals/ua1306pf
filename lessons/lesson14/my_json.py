import json


x = '{ "name":"Liubov", "age":25, "city":"Lviv"}'
print(x)
d = json.loads(x)
print(d)
print(d.get("name"))
# d = json.load(x)

data = None
with open("lessons\\lesson14\\data.json") as f:
    data = json.load(f)
from pprint import pprint
pprint(data)

data["age"] = 55

s_data = json.dumps(data)
print(s_data)

with open("lessons\\lesson14\\data_out.json", "w") as f:
    json.dump(data, f, indent=5)
