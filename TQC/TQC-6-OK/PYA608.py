# TODO
# 1.建立2個空矩陣  n = [(x,x,x),(x,x,x),(x,x,x)] ,  a =[]
# 2.將值依序丟入矩陣中，丟滿一個再丟第二個
# 3.找尋輸入的最大值跟最小值
# 4.從最大、最小值反查矩陣位置  用最大、最小值去除陣列 Row 跟 Col數   3*3 的 商(//) 跟 餘數(%)
n=[[],[],[]]
a=[]
for i in range(0,3): 
  for j in range(0,3):
    num = eval(input())
    a += [num]
    n[i].append(num)

MAX = max(a)
MIN = min(a)
M = a.index(MAX)
N = a.index(MIN)

print("Index of the largest number %d is: (%d, %d)" %( MAX , M // 3 , M % 3))
print("Index of the smallest number %d is: (%d, %d)" %( MIN , N // 3 , N % 3))
"""
Index of the largest number _ is: (_, _)
Index of the smallest number _ is: (_, _)
"""