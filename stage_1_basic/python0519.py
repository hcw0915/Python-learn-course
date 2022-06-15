"""
code = 87
print("-----終極密碼猜數字遊戲-----")

while True:
  x = eval(input("請輸入數字0~100:"))
  if x == code: 
    print("猜中了!!")
    break
  elif x > code and x < 100:
    print("猜小一點")
  elif x < code and x >= 0:
    print("猜大一點")
  else:
    print("輸入錯誤，請重新輸入")
"""    
"""
                              # list有序號、可重複、可不同型別、可更改list內資料


member_id = [ "001" , 100 , "003" ]
print(member_id)
print(member_id[2])

std_id = list(("A001","A002","A003"))
print(std_id)
print(std_id[2])
q = std_id[0] = "QAQ"
print(q)
print(std_id[0])
print(std_id)

std_id.append("DDD") # append:新增
print(std_id)

std_id.insert(0,"insert") # insert:插入
print(std_id)

del std_id[2] # del:刪除
print(std_id)

std_id.clear() # .clear:全部刪除
print(std_id) # 剩 [ ] 空集合

for i in member_id:
  print(i) #不需要member_id[i]



m1 = [ "001" , 100 , "003" ]
print(len(m1))

                              # tuple元組-有序號、可重複、不可更改元組內資料   

a = ("apple","banana","cat","dog","dog")
print(a)
x = tuple(("apple","banana","cat","dog","dog"))
print(x)

#c=x[3]="QQQ"
#print(c) 
#錯誤代碼  不可更改元組內資料

for i in a :
  print(i)

print(len(x))

#del x[0]  #不可刪除元組內
print(x)

#del x  #可刪除變數X
#print(x)

"""

                              # set{}-無序號、無索引、無法重複
a = {"apple","banana","cat","dog"}  #大括弧陣列
x = set(("apple","banana","cat","dog","dog")) #2個dog 會自動整合成 1個dog
print(x) #輸出無序

for i in x:
  print(i)
  
print(len(x))

#set用add新增資料
x.add("mouse")
print(x)