#函式實作1-計算機
"""
# 加
def add(x,y):
  total = x + y
  return total
# 減
def min(x,y):
  total = x - y
  return total
# 乘  
def mult(x,y):
  total = x * y
  return total
# 除
def div(x,y):
  total = x / y
  return total

#綜合
def calculate(x,choose,y):
  if choose == 1: 
    total = add(x,y)
    z =str(x)+"+"+str(y)+"="+str(total)
  elif choose == 2: 
    total = min(x,y)
    z =str(x)+"-"+str(y)+"="+str(total)
  elif choose == 3: 
    total = mult(x,y)
    z =str(x)+"*"+str(y)+"="+str(total)
  elif choose == 4: 
    total = div(x,y)
    z =str(x)+"/"+str(y)+"="+str(total)
  return z
 

x = eval(input("請輸入第一個數字:"))
choose = eval(input("請輸入:1.加法2.減法3.乘法4.除法:"))
y = eval(input("請輸入第二個數字:"))
print(calculate(x,choose,y))
    

a = 1 
print(a)  #1

def fun(a):
  print(a)  #!
  a=2
  print(a)  #2
  return a 

print(a)  #2
a = fun(a)
print(a)  #2
fun(a)  #2
"""
  

def a(*name):
  print(name)
  print(name[0])

a("antonio","BOb","tony")  

def b(name):
  print(name)
  print(name[2])
  
namelist = ["antonio","BOb","tony"]
b(namelist)

for i in namelist:
  print(i)

