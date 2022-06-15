# TODO

def compute(x,y):
  n = []  # 先建立空的list
  for i in range(2,x+1):  #設定i值位於2~x之間(x,y有誰大誰小問題)，但是隨便指定其中一個都符合篩選條件
    if x % i == 0 and y % i ==0:  # 判斷可以同時被 X 跟 y 整除的 i 值
      n += [i]  #將篩選出的 i 值丟到n的集合(n列表內的就是x,y的公因數)
  return max(n) #回傳 n列表中的最大值

x,y = eval(input())
print(compute(x,y))