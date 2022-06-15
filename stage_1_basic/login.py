from sys import exit

user_acc = 123
user_pwd = 321

for i in range(1,4,1):
  acc = eval(input("請輸入帳號"))
  pwd = eval(input("請輸入密碼"))
  if (user_acc == acc) and (user_pwd == pwd) :
    print("帳號輸入正確，登入成功\n")
    break
  else:
    print("帳號或密碼輸入錯誤",i,"次，剩餘",3-i,"次機會")
    if i == 3:
      print("帳號已鎖定，請洽管理員。")
      exit()
      
print("請選擇你想要執行的程式(請輸入1-4):\n1.BMI計算\n2.溫度換算\n3.公里/英哩轉換\n4.結帳系統\n5.九九乘法表\n6.小遊戲-PY升職記\n7.")
choose = eval(input())