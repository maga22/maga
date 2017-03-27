import json
with open('data.json','rt',encoding='utf-8') as f:
    js = f.read()
dictionary = json.loads(js)
print(dictionary["Вирус"]["Имя"])
dictionary["Вирус"]["Имя"] = "Мага"
print(dictionary["Вирус"]["Имя"])
js2 = json.dumps(dictionary)
with open("data.json","wt",encoding='utf-8') as f:
    f.write(js2)
