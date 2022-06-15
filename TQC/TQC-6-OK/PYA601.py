# TODO
a = []
i = 0
#-------------------------------------使用者輸入的12個正整數(範圍1~99)
while i <= 11:  #製作迴圈讓user輸入12次
  n = input()
  if int(n) > 99 or int(n) < 1:   #制訂正整數(範圍1~99)
    break 
  a = a + [n]
  i = i + 1

#-------------------------------------輸出每一個數字欄寬設定為3，每3個一列，靠右對齊
for j in range(0,i):
  print("%3s" %a[j] , end="")
  if (j+1) % 3 == 0:
    print("") 

#-------------------------------------取偶數陣列相加輸出
list_int_a = [int(i) for i in a]  #轉換字串陣列為整數陣列
total = 0
for k in range(0,i,2):
  total += list_int_a[k]
print(total)