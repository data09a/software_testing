import json

data = {"name":"John", "age":10}

with open("../data/data01.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False)