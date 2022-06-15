# set{}-無序號、無索引、無法重複
#---------------------------------------------------------                            

"""
a = {"apple","banana","cat","dog"}  #大括弧陣列
x = set(("apple","banana","cat","dog","dog")) #2個dog 會自動整合成 1個dog
print(x) #輸出無序

for i in x:
  print(i)
  
print(len(x))


x.add("mouse")  #set用add新增資料
print(x)
x.update(["aBC","bbb","ccc"]) #用update批次新增資料
print(x)

xx = ("bbb" in x)  # in查找陣列內文字
print(xx)

x.remove("apple") #刪除資料
print(x)
x.discard("banana") #刪除資料
print(x)

x.clear()
print(x) #變數還在 但是變成空集合

#del x
#print(x) # 直接刪除變數，不存在


#dictionary字典-json檔案
info = {"name":"hcw","phone":"0988249321","add":"Taipei"}
print(info)

print(info["name"])  #抓字典 不能以數列抓，只能用key值 數列抓只能抓到key

for i in info: #for迴圈為主軸抓key跟value值用法
  print("欄位為:",i) 
  print("資料為:",info[i])  #dictionary 用i抓key  用key抓value
  print("=================")
  
print(info.keys())  # .keys 直接抓key
print(info.values()) #  .values 直接抓value

info.setdefault("gender","male")  # .setdefault 新增資料
print(info)

info2 = {"name":"tony","aaa":"bbb"} # .update 取代+更新
info.update(info2)  
print(info)

info["name"] = "antonio"  # 指定陣列內key值直接修改value
print(info)

del info["gender"]  # del+key值 清除key值and 對應value值
#info['phone'],info['add']………………多筆刪除延伸
print(info)

#info.clear()  # .clear 清除資料
#print(info)

info = {"name":"hcw","phone":"0988249321","add":"Taipei","add":"Taiwan"}  #沒有重複，僅以最後key值的value為主。
print(info)

info3 = info.copy() # .copy 複製dict
print(info3)
info4 = info  #本質與.copy不同， info4 會跟 info 同步變化
print(info4)

info = {"b":"098844897",'c':"qwer","a":"hcw"}
listq = sorted(info)  # sorted 排序key值 #依照ASCII 排序 #短在前,長在後  #同字母依次字母比
print(listq)

for i in listq: #如果是用info 就會變成原本的順序，用listq才是新順序
  print(info[i])
  
"""

