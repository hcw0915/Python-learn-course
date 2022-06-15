# 1.直接互乘對方分母
# 2.相加
# 3.找分子跟分母最大公因數
# 4.再整除

def compute(c,d): #此函數再取兩變數最大公因數
  list = []
  for i in range(2,c+1):
    if c % i == 0 and d % i == 0:
      list += [i]
  return max(list)

x,y = eval(input())
m,n = eval(input())
# x/y m/n
#結果=x*n+m*y/n*y 取分子=x*n+m*y 分母=n*y  
up = x*n+m*y  # 分子
down = n*y  #分母
e = compute(up,down)  #指定compute()函數給e

print("%d/%d + %d/%d = %d/%d" %(x,y,m,n,up/e,down/e)) #最末兩個變數要除上最大公因數e，方得最簡分數

