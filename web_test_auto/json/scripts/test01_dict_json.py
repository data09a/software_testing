import json
#
# """1. transfer from python dict to json string """
# data = {"name": "Jack", "age": 18 }
#
# print("Before transfer: ", type(data))
#
# data2 = json.dumps(data)
# print(data2)
# print("After transfer: ", type(data2))


"""2. transfer from json str to python dict"""

data ='{"name": "Jack", "age": 18}'
print("Before transfer: ", type(data))

data2 = json.loads(data)
print(data2)
print("After transfer: ", type(data2))





#
# data = '{"name":"张三", "age":18}'
# # 错误写法，注意：键名必须是双引号
# # data = "{'name':'张三', 'age':18}"
# print("未转换之前类型：", type(data))
# # 转换
# data2 = json.loads(data)
# print(data2)
# print("转换之后类型：", type(data2))