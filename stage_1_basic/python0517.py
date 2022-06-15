"""
  # while迴圈條件式
a = 10
while a <= 100:
  print(a)
  a += 10
  
  # while迴圈條件式-無窮迴圈
while True:
  print("無窮")

  # while迴圈條件式-while/if混合
a = 10
while a <= 100:
  print(a)
  if a == 50:
    break #continue
  a += 10
print("STOP")

  #while迴圈條件式-else
a = 10
while (a <= 100):
  print(a)
  print("目前為{:d}".format(a))
  a = a + 10
else:
  print("終於到100了。")
  
"""

"""
輸入加油的公升數

未滿20公升會出現提示訊息，"再加?公升，就滿20公升可以選擇贈品"
1.繼續加 2.不加油
1.繼續加時詢問→還要加多少公升

滿20公升會提醒，可以選擇贈品

oil = eval(input("請輸入加油的公升數:"))

while oil < 20:
  x = 20 - oil
  print("再加{:d}公升，就滿20公升可以選擇贈品!".format(x))
  choose = eval(input("請問是否繼續加?1.繼續加 2.不加油"))
  if choose == 1:
    oil = oil + eval(input("請問還要加多少?"))
    continue
  else:
    break
if oil >= 20:
  print("已滿20公升，可以選擇贈品!")

"""
from sys import exit

user_acc = 123
user_pwd = 321

for i in range(1,4,1):
  acc = eval(input("請輸入帳號"))
  pwd = eval(input("請輸入密碼"))
  if (user_acc == acc) and (user_pwd == pwd) :
    print("帳號輸入正確，登入成功")
    break
  else:
    print("帳號或密碼輸入錯誤",i,"次，剩餘",3-i,"次機會")
    if i == 3:
      print("帳號已鎖定，請洽管理員。")
      exit()
  
print("請選擇你想要執行的程式(請輸入1-4):\n1.BMI計算\n2.溫度換算\n3.公里/英哩轉換\n4.結帳系統\n5.九九乘法表\n6.小遊戲-PY升職記\n7.")
choose = eval(input())