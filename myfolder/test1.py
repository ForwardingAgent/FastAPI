import json

with open(r"/Users/nikolas/Downloads/data.json", encoding='UTF-8') as file:
    data = json.load(file)
    lst = []
    for i in data:
        if type(i) is str:
            i += '!'
            lst.append(i)
        elif type(i) is None:
            continue
        elif type(i) is int:
            i += 1
            lst.append(i)
        elif type(i) is bool:
            i = not i
            lst.append(i)
        elif type(i) is list:
            i *= 2
            lst.append(i)
        elif type(i) is dict:
            i.update({"newkey": None})
            lst.append(i)

updated_data.json = json.dump(lst)
print(updated_data.json)

My_first_website