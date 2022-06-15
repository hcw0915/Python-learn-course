"""
num_1 = eval(input("請輸入數字:"))
op = input("請輸入運算符號:")
num_2 = eval(input("請輸入數字:"))

if op == "+":
  print(num_1+num_2)
elif op == "-":
  print(num_1-num_2)
elif op == "*":
  print(num_1*num_2)
elif op == "/":
  print(num_1/num_2)
else:
  print("輸入錯誤")
  
"""


#AB遊戲、10次機會 猜到 數字順序

import random
ans = random.sample(range(1,10),4)
print(ans)

a = b = n = 0
while a != 4:
  a = b = n = 0
  user = list(input('輸入四個數字：'))  # 讓使用者輸入數字，並透過 list 轉換成串列
  for i in user:                     # 使用 for 迴圈，將使用者輸入的數字一一取出
    if int(user[n]) == ans[n]:    # 因為使用者輸入的是「字串」，透過 int 轉換成數字，和答案串列互相比較
      a += 1                         # 如果位置和內容都相同，就將 a 增加 1
    else:
      if int(i) in ans:           # 如果位置不同，但答案裡有包含使用者輸入的數字
        b += 1                       # 就將 b 增加 1
    n += 1                           # 因為輸入的每個數字都要判斷，將 n 增加 1
  output = ','.join(user).replace(',','')    # 四個數字都判斷後，使用 join 將串列合併成字串
  print(f'{output}: {a}A{b}B')
print('答對了！')    




