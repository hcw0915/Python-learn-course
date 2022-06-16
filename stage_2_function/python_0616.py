# # 遞迴
# def mycode(n):
#   if (n == 1) : return 1
#   else : return n*mycode(n-1)
  
# print(mycode(1))
# print(mycode(5))    # 120 = 5*4*3*2*1   return 5*mycode(4)  →　5*4*mycode(3) .....

# a = 2
# def fun():
#   a = 5
#   a = a +6
#   print(a) 
  
# fun() # print(a) = 5 + 6 = 11
# print(a) # 1

# b = 3 
# def asd():
#   global b 
#   b = b + 4
#   print(b) 
# asd() # 7 = 3+4 
# print(b)  #3

# class Myname: # 父類別
#   def __init__(self,name):
#     self.name = name
    
#   def printName(self):
#     print("Name =",self.name,"你好!")

# class welcome(Myname):  # 子類別(可以繼承父類別的所有變數跟方法)
#   def __init__(self,name):  # 如果有子類別有init 則不會繼承父類別建構子，但是方法還是會繼承
#     self.name = name
#     super().__init__(name)  # super() 可叫回父類別的建構子
#   def saywelcome(self):
#     print("welcome")

    
# xxx = Myname(input("請輸入名字:"))
# xxx.printName()

# yyy = welcome(input("請輸入名字:"))
# yyy.printName()
# yyy.saywelcome()


class Petinfo():
  def __init__(self,name,age,color):
    self.name = name
    self.age = age
    self.color = color
    
def age_compare():
  age_hub = []
  name_hub = []
  for i in create:
    print("------------")
    print("姓名: %s" %(i.name))
    print("年齡: %s" %(i.age))
    print("毛色: %s" %(i.color))
    age_hub.append(i.age)
    name_hub.append(i.name)
  max_age = max(age_hub)
  min_age = min(age_hub)
  print(" %s 的年齡最大，它 %d 歲" % ( name_hub [ age_hub.index(max_age) ] , max_age ) )
  print(" %s 的年齡最小，它 %d 歲" % ( name_hub [ age_hub.index(min_age) ] , min_age ) )


def create_file(): 
  nums = eval(input("請輸入你要建立檔案的數量:"))
  list_info = []
  for i in range(nums):
    print("--輸入第 %d 隻--" %(i+1))
    name,age,color = input("請輸入名字:"),eval(input("請輸入年齡:")),input("請輸入毛色:")
    a = Petinfo(name,age,color)    
    list_info.append(a)
  return list_info


create = create_file()
age_compare()


