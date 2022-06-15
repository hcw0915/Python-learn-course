# from page_1 import myinfo

# print(4)
# myinfo() 
# print(5)

# Page_1--------------
# def myinfo():
#   print(1)

# print(7)                    # 沒有再if裡面 依然可以被執行
# print("name=",__name__)     # 沒有再if裡面 依然可以被執行

# if __name__ == "__main__":
#   print(2)
#   print(3)
# 在別的檔案被引用的時候 __name__就不會等於__main__ 而是page_1
# 所以設如果__name__ == __main__成立，代表不被引用，而是在自己原本檔案執行
# 再原本檔案執行是可以印出來 if 裡面的東西
# __name__ 被命令列執行的時候顯示出來的值 會是 __main__
# --------------------

"""
7 name=page1 4 1 5
"""

# myinfo()
# print(6)
  
"""
1 6
已經不執行page_1裡的其他步驟
所以先回到檔案執行myinfo() 也就是 1
再執行print(6)
https://dotblogs.com.tw/YiruAtStudio/2021/01/25/215512
"""


# import datetime
# update_time = datetime.datetime.now()

# if update_time.strftime("%p") == "PM":
#   time = "晚上"
# else:
#   time = "早上"
  
# print("現在時刻:"+update_time.strftime("%Y{a} %m{b}%d{c} {d} %I{e}%M{f} %p").format(a="年",b="月",c="日",d=time,e="點",f="分"))

# print(update_time.strftime("%I"))

# # https://dotblogs.com.tw/YiruAtStudio/2021/01/27/190736


import page_2

x=dir(page_2)
print(x)