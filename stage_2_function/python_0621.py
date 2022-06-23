# class Petinfo():
#   def __init__(self,name,age,color):
#     self.name = name
#     self.age = age
#     self.color = color
    
# def age_compare():
#   age_hub = []
#   name_hub = []
#   for i in create:
#     print("------------")
#     print("姓名: %s" %(i.name))
#     print("年齡: %s" %(i.age))
#     print("毛色: %s" %(i.color))
#     age_hub.append(i.age)
#     name_hub.append(i.name)
#   max_age = max(age_hub)
#   min_age = min(age_hub)
#   print("%s 的年齡最大，它 %d 歲" % ( name_hub [ age_hub.index(max_age) ] , max_age ) )
#   print("%s 的年齡最小，它 %d 歲" % ( name_hub [ age_hub.index(min_age) ] , min_age ) )


# def create_file(): 
#   list_info = []
#   for i in range(nums):
#     print("--輸入第 %d 隻--" %(i+1))
#     name,age,color = input("請輸入名字:"),eval(input("請輸入年齡:")),input("請輸入毛色:")
#     a = Petinfo(name,age,color)    
#     list_info.append(a) # Line 75、76、77→ list_info.append(Perinfo(input("請輸入名字:"),eval(input("請輸入年齡:")),input("請輸入毛色:")))
#   return list_info

# nums = eval(input("請輸入你要建立檔案的數量:"))
# create = create_file()
# age_compare()

#--------------------------------------------------------------------------------
# import json

# bee = {
#   "company":"台灣養蜂協會",
#   "name":"豬小明",
#   "award":"VIP",
#   "phone":"0912312334",
#   "year":"2022"
# }

# print(bee)  # <class 'dict'>
# json_bee = json.dumps(bee,ensure_ascii=False) # json.dumps把json資料 dict → str
# print(json_bee) # <class 'str'>

# dict_json_bee = json.loads(json_bee)  # json.dumps把json資料 str → dict
# print(dict_json_bee) # <class 'dict'>

#--------------------------------------------------------------------------------
# import json

# person = {
#   "name":"mary",  # 字典
#   "age":50, # int
#   "married":True, # 布林
#   "pet":("mini","lulu"), # tuple
#   "car":None, # 空值
#   "children":[ # 陣列
#     {"name":"ming","age":"23"},
#     {"name":"LEE","age":"23"}
#   ],
# }

# people = json.dumps(person,indent=3)
# print(people)

#--------------------------------------------------------------------------------
"""
實作:'[{"id": "1","city": "台北"},{"id": "2","city": "高雄"}]'
編號:1
城市:台北
編號:2
城市:高雄"
"""

import json

a = '[{"id": "1","city": "台北"},{"id": "2","city": "高雄"}]'
loads_a = json.loads(a)
print(a)
for i in loads_a:
  print("編號:" ,i["id"])
  print("城市:" ,i["city"])