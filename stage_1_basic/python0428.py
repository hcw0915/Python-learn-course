"""
  #字串取代
name = "qweqweqweqweqweqwe"
print(name.replace("q","A"))

  #字串分割
a = "qaz,123,zxc"
b = a.split(",") #看分隔符號是甚麼就用甚麼符號
print(b)
print(b[2])
print(b[0])

data_origin = "0912569369-John-Taipei-09:02"
data = data_origin.split("-")
print(data)

print("電話:",data[0])
print("姓名:",data[1])
print("縣市:",data[2])
print("登入時間:",data[3])

  #數學運算子
a = 4
b = 6
  
c = a + b
print(c)
d = a - b
print(d) 
e = a * b
print(e) 
f = a / b
print(f) 
g = a // b
print(g) 
h = a ** b
print(h) 
i = a % b
print(i) 

  #指定運算子
a = 5
print(a)
a += 2
print(a)
a -= 4
print(a)
a *= 6
print(a)
a /= 3
print(a)

  #比較運算子
a = 3
b = 5
print( a >= b )
print( a <= b )
print( a == b )
print( a != b )

  #邏輯運算子
a = 10
b = 7
c = 8

print(a<b and b<c) 
print(a<b and b>c and c==a )  
print(a>=b and b>c)  
print(a<b or b>=c and c!=a )  
print(a<b and b>c or c!=a )  
print(a<b or b<c or c==a) 

  #特定運算子
a = 2
b = 4 
c = 2
d = 5
print(a is b)
print(a is c)
print(a is not d)
print(a is not c)

"""
  #實作
print("歡迎來到PY飲料店")
cola = 25
milk_tea = 35
green_tea = 20
print("可樂{:d}元、奶茶{:d}元、綠茶{:d}元".format(cola,milk_tea,green_tea))

  #初始
total = 0
print("目前金額為",total,"元")

  #可樂
num_1 = eval(input("請輸入可樂數量:"))
total += cola * num_1
print("目前金額為",total,"元")

  #奶茶
num_2 = eval(input("請輸入奶茶數量:"))
total += milk_tea * num_2
print("目前金額為",total,"元")

  #綠茶
num_3 = eval(input("請輸入奶茶數量:"))
total += green_tea * num_3 
print("總金額為",total,"元")