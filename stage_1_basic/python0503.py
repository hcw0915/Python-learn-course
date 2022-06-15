"""
  #判斷條件式-1.單條件成立、執行
switch = 1 
if (switch > 0):
  print("switch ON !")
else:
  print("switch OFF !")


  #判斷條件式-2.實作1-簡易意願判別
choose = input("你想不想開燈呢?(y/n)")
trans = choose.lower()
if trans == "y" :
  print("那就開燈吧!!")
else :
  print("還是關燈好了!!")


  #判斷條件式-2.實作2-性別判別
name = input("請輸入姓名:")
num = input("請輸入身份證字號:")
gender = num[1] #判別第二碼 1/2
if gender == "1":
  print("{:s}，先生你好!".format(name))
else:
  print("{:s}，小姐你好!".format(name))

  #判斷條件式-2.實作3-成績判別
score = eval(input("請輸入成績:"))
if score >= 90 and score <= 100 :
  print("非常好")
elif score >= 70 and score < 90 :
  print("還不錯")
elif score >= 60 and score < 70 :
  print("勉強及格")
elif score >= 0 and score < 60 :
  print("不及格")
else :
  print("超出範圍")
  

  #判斷條件式-2.實作4-帳號登入判別
from sys import exit

user_acc = input("請輸入帳號:")
user_pwd = input("請輸入密碼:")
acc = "ABC123"
pwd = "123abc"

if (user_acc == acc) and (user_pwd == pwd):
  print("成功登入")
elif (user_acc == acc) and (user_pwd != pwd):
  print("密碼輸入錯誤")
  exit()
elif (user_acc != acc) and (user_pwd == pwd):
  print("帳號輸入錯誤")
  exit()
elif (user_acc == "") or (user_pwd == ""):
  print("您的帳號、密碼是空值")
  exit()
else:
  print("登入失敗")
  exit()
  
print(123)

""" 
  #綜合測試
from sys import exit

user_acc = input("請輸入帳號:")
user_pwd = input("請輸入密碼:")
acc = "ABC123"
pwd = "123abc"
if (user_acc == acc) and (user_pwd == pwd):
  print("成功登入")
elif (user_acc == acc) and (user_pwd != pwd):
  print("密碼輸入錯誤")
  exit()
elif (user_acc != acc) and (user_pwd == pwd):
  print("帳號輸入錯誤")
  exit()
elif (user_acc == "") or (user_pwd == ""):
  print("輸入錯誤，系統回覆為空值!")
  exit()
else:
  print("登入失敗")
  exit()
  
print("請選擇你想要執行的程式(請輸入1-4):\n1.BMI計算\n2.溫度換算\n3.公里/英哩轉換\n4.結帳系統")
choose = eval(input())

if choose == 1 :
  print("歡迎來到PY健康中心")
  name = input("請輸入姓名:")
  weight = eval(input("請輸入體重(kg):"))
  height = eval(input("請輸入身高(cm):")) / 100
  bmi = weight / pow(height,2) #bmi = weight / (height ** 2)
  print("{:s},你好,你的BMI為{:.1f}(kg/cm2)".format(name,bmi))
  
elif choose == 2 :
  print("歡迎來到PY溫度計")
  print("請輸入你要傳換的溫度單位(1/2):\n1.華式\n2.攝氏")
  option = eval(input())
  if option == 1:
    cel = input("請輸入攝氏溫度:")
    fah = ( float(cel) * 9 / 5 ) + 32
    print("現在溫度為華氏{:.2f}度。".format(fah))
  elif option == 2:
    fah_2 = input("請輸入華氏溫度:")
    cel_2 = ( float(fah_2) - 32 ) * 5 / 9
    print("現在溫度為攝氏{:.2f}度。".format(cel_2))
  elif option == "":
    print("輸入錯誤，系統回覆為空值!")
  else:
    print("輸入錯誤!")
    exit()
  
elif choose == 3 :
  print("歡迎來到PY公/英哩傳換器")
  print("請輸入你要兌換的長度單位(1/2):\n1.公里\n2.英哩")
  print("(目前公里/英哩為 1 km:0.6 miles)")
  num = eval(input())
  
  if num == 1:
    km = eval(input("請輸入公里數:")) 
    miles = km * 0.62
    print("{:.2f}公里為{:.2f}英哩。".format(km,miles))
  elif num == 2:
    miles = eval(input("請輸入英哩數:")) 
    km = miles / 0.6
    print("{:.2f}英哩為{:.2f}公里。".format(miles,km))
  elif num == "":
    print("輸入錯誤，系統回覆為空值!")
  else:
    print("輸入錯誤!")
    exit()
  
elif choose == 4 :
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
  exit()
  
elif choose == "" :
  print("輸入錯誤，系統回覆為空值!")
  exit()
else:
  print("輸入錯誤")
  exit()
