# TODO
def compute(num):
  n = [0,1] #先賦予 n[0]跟n[1]值 避免計算錯誤
  for i in range(0,num): #i從0開始到num
    q = n[-1]+n[-2] #q 為列表末兩位相加的結果 也可以用 n[i]+n[i+1] 從前面後面的區別而已
    n += [q]  #將新得出的q值 新增置n表中
    print(n[i],end=" ") #列印n列表 從i=0開始
    
num = eval(input())
compute(num)

# i=1,q=n[0]+n[1]=0+1=1  q=1 n=[0,1,1]
# i=2,q=n[1]+n[2]=1+1=2  q=2 n=[0,1,1,2]
# i=3,q=n[2]+n[3]=1+2=3  q=3 n=[0,1,1,2,3]