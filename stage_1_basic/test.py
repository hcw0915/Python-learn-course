"""
輸入加油的公升數

未滿20公升會出現提示訊息，"再加?公升，就滿20公升可以選擇贈品"
1.繼續加 2.不加油
1.繼續加時詢問→還要加多少公升

滿20公升會提醒，可以選擇贈品


L = 20
x = 0
while (1):
    x += int(input("請輸入加油數量: "))
    if (x<20):
        print("您目前已加油 ",x,"公升")
        print("您還差",L-x,"公升，就滿20公升可以兌換贈品~")
        if (input("請問是否要繼續加油: 1.繼續加、2.不加油: ")=="1"):
            continue
        else:
            break
    else:
        print("您目前已加油",x,"公升")
        print("您已加滿20公升，可兌換贈品~")
        break
print("謝謝您的使用~")


user_acc = 123
user_pwd = 321

while True:
  acc = eval(input("請輸入帳號"))
  pwd = eval(input("請輸入密碼"))
  if (user_acc == acc) and (user_pwd == pwd):
    print("登入成功")
    break
  else:
    print("帳號或密碼輸入錯誤",i,"次，剩餘",3-i,"次機會")
    for i in range(1,4,1):
      if i == 3:
        print("帳號已鎖定，請洽管理員。")
      break
    continue

"""
#AB遊戲、10次機會 猜到 數字順序

import random
ans = random.sample(range(1,10),4)
print(ans)

A = B = N =0
while A != 4:
  A = B = N =0
  num = list(input("請輸入四位數字"))
  for i in num:
    if int(num[N]) == ans[N]:
      A = A + 1
    elif int(i) in ans :
      B = B + 1
    N = N + 1
  output = ','.join(num).replace(',','')    # 四個數字都判斷後，使用 join 將串列合併成字串
  print(f'{output}: {A}A{B}B')
print(A,B)