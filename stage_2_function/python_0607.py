
# class calculate2:
#   def __init__(self,x,y,fn):
#     self.x = x
#     self.y = y
#     self.fn = fn
        
#   def symbols(self):
#     if fn == 1:
#       total = x + y
#     elif fn == 2:
#       total = x - y
#     elif fn == 3:
#       total = x * y
#     elif fn == 4:
#       total = x / y 
#     return total

# dict={1:"+",2:"-",3:"*",4:"/"}

# x = eval(input("請輸入第一個數字:"))
# fn = eval(input("請輸入運算符號(1.+ 2.- 3.x 4./):"))
# y = eval(input("請輸入第一個數字:")) 

# a = (calculate2(x,y,fn)).symbols()
# print("%d %s %d = %d" %(x,dict[fn],y,a))

# class Calculate:
#   def __init__(self,fn):  #設定符號為預設屬性
#     self.fn=fn  #指定self.fn = fn 的參數設定(目標是讓下面的人都可以使用這個參數)

#   def symbols(self,x,y):  #引用參數 fn 去做 if 的判斷
#     if fn == 1:
#       total = x + y
#     elif fn == 2:
#       total = x - y
#     elif fn == 3:
#       total = x * y
#     elif fn == 4:
#       total = x / y 
#     return total
      
# dict={1:"+",2:"-",3:"*",4:"/"}

# x = eval(input("請輸入第一個數字:"))
# fn = eval(input("請輸入運算符號(1.+ 2.- 3.x 4./):"))
# y = eval(input("請輸入第一個數字:")) 

# a = Calculate(fn)  #指定Calculate(變數)類別為 a
# total = a.symbols(x,y)  # 在a 裡面執行 symbols的方法且填入參數(x,y)  表示方法為a.symbols(x,y)
# print("%d %s %d = %d" %(x,dict[fn],y,total))


# 系統登入頁面
def log_in_sys():
  user_acc = "123"
  user_pwd = "123"
  key_acc = input("請輸入帳號：")
  key_pwd = input("請輸入密碼：")
  i = 1
  while i < 4:  
    if key_acc == user_acc and key_pwd == user_pwd:
      print("帳號密碼正確，歡迎進入本系統。")
      break
    elif i == 3:
      print("錯誤已達3次，請重新執行本程式。")
      exit()
    elif key_acc != user_acc or key_pwd != user_pwd:
      print("輸入錯誤達%d次，剩餘%d次機會，請重新輸入!!" %(i,3-i))
    i += 1
    
log_in_sys()




