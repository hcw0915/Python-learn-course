#匿名函數 lambda(臨時的小函式)

# price = lambda people:people*4
# data = price(2)
# print(data)

# num = lambda people,abc:(people*4)+abc
# data = num(3,2)
# print(data)

# def cul(people):
#   total = lambda price:price*people
#   return total
# print(cul(3)(100))  
# cul(people)(price)
# 因為是兩個變數，所以不是(3,100) 先執行cul(3) 再執行lambda裡的price變數


# 類別
class cul_ticket :
  def __init__(any,order,price,people):  #self=類別變數
    any.order=order  #存入類別變數
    any.price=price
    any.people=people
  
  def calculate(cool,x):  #可自訂類別變數名稱
    data = cool.price * cool.people   
    print("訂購人 %s，共買了 %d 張票，總共 %d 元 %d" %(cool.order,cool.people,data,x))
    
  
total = cul_ticket("Antonio",100,7) 
total.calculate(123)   #cul_ticket("Antonio",100,7).calculate() 也可以
total2 = cul_ticket("Lin",200,3)
total2.calculate(213)

print(total.order)  #呼叫物件方法
total.order = "LIN" #設定物件變數
print(total.order)  #呼叫物件方法

total.calculate(123)  #人名已改變   #訂購人 LIN，共買了 7 張票，總共 700 元 123


#TypeError: cul_ticket.calculate() missing 1 required positional argument: 'x'
#因為原本的total2.calculate()沒打變數所以有跳出來

      
    