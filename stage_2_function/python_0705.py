from urllib.request import DataHandler
import pymysql
conn = pymysql.connect(host='localhost',user='root',passwd='',db='python',charset='utf8')
cur = conn.cursor() 
print("====================================")
print("MySQL-DataBase Connection-Successful")
print("====================================")

def login_interface():
  print("管理者登入系統")
  print("*------------*")
  print("1.登入")
  print("2.註冊帳號")
  print("3.結束程式")

def login_list():
  while True:
    login_interface()
    num = eval(input("請輸入你要執行的動作:"))
    if   num == 1 : login_check()
    elif num == 2 : staff_data_register()
    elif num == 3 : break

def Operating_interface():
  print("請選擇以下動作")
  print("*------------*")
  print("1.查詢所有員工的資料")
  print("2.查詢員工的資料")
  print("3.修改員工資料")
  print("4.刪除員工帳號")
  print("5.離開")

def Operating_list():
  while True:
    Operating_interface()
    a = eval(input("請輸入你要執行的動作:"))
    if a == 1:
      sql.query_all() 
      anykey()
    elif a == 2:
      acc = input("請輸入帳號:")
      if acc == "" : print("你輸入為空值，請重新執行。")
      sql.query_one(acc)
      anykey()
    elif a == 3:
      staff_data_update()
      anykey()
    elif a == 4:
      staff_data_delete()
      anykey()
    elif a == 5:
      print("已離開本系統，返回登入頁面")
      anykey()
      break


def login_check():  # 還要再修正登入系統
  while True: 
    # 檢查帳號空值與否
    acc = input("請輸入帳號:")
    if acc == "" : print("你輸入為空值，請重新執行。")
    data = sql.query(acc) 
    # 檢查資料庫內是否存有帳號資料
    if data == None: 
      print("此帳號不存在!")
      anykey()
      break
    # 檢查密碼
    staff_pwd = data[2] 
    pwd = input("請輸入密碼:")
    if pwd == "" : print("你輸入為空值，請重新執行。")
    if staff_pwd == pwd :
      print("登入成功")
      Operating_list()
      break
    else:
      print("密碼錯誤")
      anykey()
      break

def staff_data_register(): # 帳號註冊系統
  while True:
    name = input("請輸入姓名:")
    if name == "" :
      print("姓名不能為空")
      continue

    acc = input("請輸入帳號:")
    if acc == "" : print("你輸入為空值，請重新執行。")

    data,acc = sql.query_check_include_del(acc)
    if not data == None:  # 如果data不存在，data == None，代表沒找到，可以新增；若data已存在，data != None，顯示帳號已存在，無法新增。
      print("此帳號已存在!")
      anykey()
      break

    pwd = input("請輸入密碼:")
    sql_insert = "INSERT INTO staff_info(sf_name,sf_account,sf_pwd,create_user,update_user)VALUES('"+name+"','"+acc+"','"+pwd+"','"+name+"','"+name+"')" 
    #print(sql_insert)
    cur.execute(sql_insert)
    conn.commit() 
    print("使用者 %s :帳號已註冊成功，可以重新登入已進入系統" % acc)
    break

def staff_data_update():  # 可以調整修改內容 不僅限於使用者姓名。
  while True:
    acc = input("請輸入要修改資料的帳號:")
    if acc == "":
      break

    data,acc = sql.query_check_include_del(acc)
    # 查詢需更改的帳號是否存在
    if(data == None):
      print("此帳號不存在!")
      break
    print(data)

    option = eval(input("1.姓名\n2.帳號\n3.密碼\n請輸入你要修改的項目:"))
    if option == 1 : 
      new_name = input("請輸入新的姓名:")
      sql.update_acc(new_name,acc)
    elif option == 2 : 
      new_acc = input("請輸入新的帳號:")
      sql.update_acc(new_acc,acc)
    elif option == 3 : 
      new_pwd = input("請輸入新的密碼:")
      sql.update_acc(new_pwd,acc)

    print("修改完成")
    anykey()
    break

def staff_data_delete():  # 刪除有兩種 ->   修正狀態碼 0->1  / 直接完整刪掉(不留歷史資料)
  while True:
    acc = input("請輸入要刪除的帳號:")
    if acc == "":
      print("你輸入的是空值")
      break
    # 先查詢帳號存在與否
    data = sql.query_check_include_del(acc)
    if data == None:
      print(" %s ，此帳號不存在!" % acc)
      continue
    # 依照重複輸入帳號去做比對，完備刪除程序。
    acc_delete = input("如確認刪除請再次輸入此帳號:")
    if acc_delete == data[1]: # 用acc_delete 比對 先前的data[1](帳號名稱)
      # 讓SQL自行尋找要刪除的帳號
      sql.delete(acc)
      break



def anykey():
  input("(輸入隨意鍵回到登入頁面...)")
  print("===========================")

class SQL_Grammar:
  # 只能self 超級重要!!
  def query(self,acc): # 查詢帳號資料-OK
    query = "SELECT sf_name,sf_account,sf_pwd FROM staff_info WHERE sf_account='"+ acc +"' AND sf_del = '0'"
    cur.execute(query) # 資料庫執行抓資料存在cur裡  # sql 裡面抓變數用"+變數+"
    data = cur.fetchone() # print(staff_acc) # 總共抓了 名字、帳號、密碼三個欄位
    return data

  def query_one(self,acc): # 查詢特定員工資料-OK
    sql = " SELECT * FROM staff_info WHERE sf_account='"+ acc +"' " 
    cur.execute(sql) # 資料庫執行抓資料存在cur裡  # sql 裡面抓變數用"+變數+"
    data = cur.fetchone() # print(staff_acc) # 總共抓了 名字、帳號、密碼三個欄位
    print("員工資料表:")
    print(data)
    return data

  def query_all(self): # 查詢全部員工資料-OK
    sql = "SELECT sf_pk,sf_name,sf_account,sf_pwd,sf_level,sf_del FROM staff_info WHERE sf_del = 0 "
    cur.execute(sql)
    data = cur.fetchall()
    print("員工資料表:(編號、姓名、帳號、密碼、員工等級、狀態碼)")
    for i in data:
      print(i)
    return data

  def query_check_include_del(self,acc):  # 查詢帳號存在與否(包含del=1/0)-ok
    sql = " SELECT * FROM staff_info WHERE sf_account = '"+ acc +"' "
    cur.execute(sql)
    data = cur.fetchone()
    return data,acc

  def update_acc(self,newacc,acc):
    sql = " UPDATE staff_info SET sf_account='"+ newacc +"' WHERE sf_account='"+ acc +"' "
    cur.execute(sql) 
    conn.commit()
  
  def update_name(self,new_name,acc):
    sql = " UPDATE staff_info SET sf_name='"+ new_name +"' WHERE sf_account='"+ acc +"' "
    cur.execute(sql) 
    conn.commit()
  
  def update_pwd(self,new_pwd,acc):
    sql = " UPDATE staff_info SET sf_pwd='"+ new_pwd +"' WHERE sf_account='"+ acc +"' "
    cur.execute(sql) 
    conn.commit()

  def delete(self,acc): # 刪除資料(直接刪除)-OK
    sql = "DELETE FROM staff_info WHERE sf_account = '" + acc +"' "
    cur.execute(sql)
    conn.commit() # commit 確認提交(用於資料庫"更新")

sql = SQL_Grammar()

# # 建議用class 去存SQL語法資料 各種語法彙整 確認利用種況
 


# login_interface()
# Operating_interface()


login_list()


cur.close()   # 關閉資料庫
conn.close()  # 關閉連線
print("資料庫關閉成功") # 確認有完成關閉

