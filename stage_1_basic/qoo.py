"""
終極密碼
1.題目
2.步驟
3.猜X  顯示目標介於 X-數字之間
4.再次輸入 X


"""

import random

code = random.randint(1,100)
cell = 100  #設定初始上限
floor = 1 #設定初始下限
print(code)


while True:
  print("---------------------")
  print("請輸入密碼:(密碼介於{:d}~{:d}之間)".format(floor,cell))
  ans = int(input())
  if ans == code :
    print("恭喜答對了!")
    break
  elif ans >= code and ans <= 100:
    print("密碼介於{:d}~{:d}".format(floor,ans))
    cell = ans
    continue
  elif ans <= code and ans >= 1:
    print("密碼介於{:d}~{:d}".format(ans,cell))
    floor = ans
    continue
  else:
    print(input("輸入錯誤，請按任意鍵重新作答。"))