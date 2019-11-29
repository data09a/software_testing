
import yaml

data = {'search_data': {'search_test_002': {'expect': {'value': '你好'}, 'value': 'hello'}, 'search_test_001': {'expect': [4, 5, 6], 'value': 456}}}

with open("./hello.yaml", "w") as f:
    yaml.dump(data, f, encoding='utf-8', allow_unicode=True)