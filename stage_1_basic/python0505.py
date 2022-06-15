"""
  #條件判斷-巢狀if(多條件判斷)
print("目標體重:80kg")
print("理想體重:75kg")
weight = eval(input("請輸入體重:"))

object = 80
ideal = 75
x = object - weight
y = ideal - weight 

if  weight <= object :
  if weight <= ideal:
    print("你已達到理想體重!")
  else:
    print("你已達到目標體重!")
else: 
  print("你還差{:.1f}公斤達到目標體重、{:.1f}公斤達到理想體重".format(x,y))
  

  #for/in迴圈
for key in range(4):
  print("第",key+1,"次")
  
for key in range(4,8):
  print(key) # 4 5 6 7

for key in range(1,18,3):
  print(key) # 1 4 7 10 13 16
  

  #for/else
for key in range(4):
  print(key)
else:
  print("QQQ")
  
x = "hello,world!"
for key in x:
  print(key)

for w in range(4):
  print("第",w+1,"週")
  for d in range(3):
    print(" 第",d+1,"天")

"""


for a in range(1,10):
  for b in range(1,10):
    print(a,"x",b,"=",a*b)