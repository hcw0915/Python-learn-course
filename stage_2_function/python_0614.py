# import page_2
# # import xxx "as" x (縮短模板名稱)
# # https://dotblogs.com.tw/YiruAtStudio/2021/01/27/205625
# # a = p2.dbname("aaa")
# """ Pqge_2

# def call_name(name):
#   print("hi"+name)
#   return True

# dbname = "payment"

# shop = {"thing":"pen","prict":30,"num":5} #1x3

# https://dotblogs.com.tw/YiruAtStudio/2021/01/27/205625
# """

# a = page_2.call_name("aaa")
# print(a)  # hi aaa    True
# b = page_2.dbname
# print(b)  # payment
# c = page_2.shop["thing"]
# print(c)  # pen

# # 翻譯: page_2 的 shop 裡面 key 為 thing 對應的值
# # 要匯入特定模板/功能/變數  from XXX import AAA
# # https://dotblogs.com.tw/YiruAtStudio/2021/01/27/212012

# d = dir(page_2)  # 查詢 page2裡面所有的函示、變數等可引用的資料
# print(d)
# # https: // dotblogs.com.tw/YiruAtStudio/2021/01/27/211235

import datetime


class Info:
  def __init__(self, name, phone_num, address, birthday, gender):
    self.name = name
    self.phone_num = phone_num
    self.address = address
    self.birthday = birthday
    self.gender = gender
    self.time = datetime.datetime.now()

  def age_cal(self):
    self.age = int(self.time.strftime("%Y")) - int(self.birthday[0:4])
    return "年齡:"+str(self.age)

  def gender_check(self):
    if self.gender == "1":
      return "性別:男"
    elif self.gender == "2":
      return "性別:女"
      
  def profile(self):
    print("姓名:",self.name)
    print("電話:", self.phone_num)  
    print("住址:", self.address)    
    print("生日:", self.birthday)     
   
def inputinfo():
  name = input("請輸入姓名:")
  phone_num = input("請輸入電話:")
  address = input("請輸入住址:")
  birthday= input("請輸入生日:")
  gender = input("請輸入性別:")

    
  user_info = Info(name,phone_num,address,birthday,gender)
  user_info.profile()
  print(user_info.age_cal())
  print(user_info.gender_check())


# Tony = Info("Tony", "0912345678", "新北市", 1992, 1)
# print(Tony.age_cal())
# print(Tony.gender_check())

# Sandy = Info("Sandy", "0912394985", "台南市", 2000, 2)
# print(Sandy.age_cal())
# print(Sandy.gender_check())

while (True):
  x = inputinfo()
  q = input("請問是否結束程式:")
  if q == "Y":
    break
  else : 
    print("請重新輸入~")
