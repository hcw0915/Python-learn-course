# TODO

#1.輸出a-b之間的4、9的倍數
#2.每列10數、寬4 左齊
#3.倍數個數、倍數總和

a = eval(input())
b = eval(input())
count = sum = 0 #給予預設值
for i in range(a,b+1): #從a~b之間檢查每個數字
  if i % 4 == 0 or i % 9 == 0 : #檢查
    count += 1  #符合的個數+1
    sum += i  #符合的數字累加
    print("%-4d" %i,end="") #每個結果依序同一欄輸出寬4
    if count % 10 == 0:  #當個數達10個則print("")-換行 不能用 count == 10
      print("")
print("\n%d\n%d" %(count,sum))