"""
  # Excercise_1 攝氏/華氏溫度轉換
cel = input("請輸入攝氏溫度:")
fah = ( float(cel) * 9 / 5 ) + 32
print("現在溫度為華氏",fah,"度。")

fah_2 = input("請輸入華氏溫度:")
cel_2 = ( float(fah_2) - 32 ) * 5 / 9
print("現在溫度為攝氏",cel_2,"度。")


  # Excercise_2 .format()用法
  # {:s}字串,{:d}整數,{:f}浮點數,{:.1f}位數,{:%}百分比
name = "John"
age = "20"
print("Hi,{:s}. I'm{:s} years old".format(name,age))

num = 26.66667
print("Num = {:.2f}".format(num))
print("Num = {:%}".format(num))

  # Excercise_3 eval()轉型可計算數值(可不用int,float)
num = eval(input())
price = eval(input())
total = num * price
print(total,"元")


  # Excercise_4 eval()、format()應用
a = 6 ** 3
b = pow(6,4) #power 表指數次方
print(a,b)

name = input("請輸入姓名:")
weight = eval(input("請輸入體重(kg):"))
height = eval(input("請輸入身高(cm):")) / 100
bmi = weight / pow(height,2) #bmi = weight / (height ** 2)
print("{:s},你好,你的BMI為{:.1f}".format(name,bmi))

  # Excercise_5 字串抓取[:]應用
num = input("請輸入身份證字號(10碼):")
gender = int(num[1])
print("身分證號碼第二位=",num[1])
if gender == 1:
  print("性別=男生")
else:
  print("性別=女生") 
  
a = "hello,world"
print(a[2:5])

  # Excercise_6 大小寫轉換(.upper/.lower)  
alphabet = input("請輸入驗證碼(不限大小寫):")
print("你輸入的驗證碼(小寫)=",alphabet.lower())
print("你輸入的驗證碼(大寫)=",alphabet.upper()) 
"""

   # Excercise_7 字串長度計算(length)
a = "qwekjclknsckwjeio"
print(len(a))