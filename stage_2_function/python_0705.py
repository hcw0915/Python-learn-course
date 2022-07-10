import pymysql
conn = pymysql.connect(host='localhost',user='root',passwd='',db='python',charset='utf8')
cur = conn.cursor() 
print("MySQL-DataBase Connection-Successful.")

def Managers_login_interface():
  print("管理者登入系統")
  print("*------------*")
  print("1.登入")
  print("2.註冊帳號")
  print("3.結束程式")

def Managers_login_list():
  while True:
    Managers_login_interface()
    num = int(input("請輸入你要執行的動作:"))
    if num == 1:
      print("Success!")
      staff_data_query()
    elif num == 2:
      print("Register")
      staff_data_insert()
    elif num == 3:
      print("Exit!")
      break

def Operating_interface():
  print("請選擇以下動作")
  print("*------------*")
  print("1.查詢所有員工的資料")
  print("11.查詢員工的資料")
  print("2.修改員工資料")
  print("3.刪除員工帳號")
  print("4.離開")
  while True:
    a = input("請輸入你要執行的動作:")
    if a == "1":
      print("你選擇的是查詢所有員工資料")
    elif a == "11":
      print("你選擇的是查詢員工資料")
    elif a == "2":
      print("你選擇的是修改員工資料")
    elif a == "3":
      print("你選擇的是刪除員工帳號")
    elif a == "4":
      print("你已離開本系統，返回登入頁面")
      break

def Operating_list():
  while True:
    Operating_interface()
    item = int(input("請輸入您執行的行動:"))
    if item == 1 :
      print("查詢所有資料")
    elif item == 2 :
      print("更新資料")
    elif item == 3 :
      print("刪除資料")
    elif item == 4 :
      break

def staff_data_query():  # 還要再修正登入系統
  while True: 
    data = sql_check_acc_existed() #不確定指定的data資料跟函數內return的data內容是否一樣 須測試
    if data == None: 
      print("此帳號不存在")
      continue

    staff_pwd = data[2]
    user_pwd = input("請輸入密碼:")
    if user_pwd == "":
      break
    if staff_pwd == user_pwd:
      print("登入成功")
      Operating_list()
      break
    else:
      print("密碼錯誤")
      continue

def staff_data_insert():
  while True:
    name = input("請輸入姓名:")
    if name == "" :
      print("姓名不能為空")
      continue

    acc=input("請輸入帳號")
    if acc == "" :
      print("帳號不能為空")
      continue

    # 確認帳號是否存在
    sql_query_all_acc = " SELECT * FROM staff_info WHERE sf_account = '"+ acc +"' "
    cur.execute(sql_query_all_acc)
    data = cur.fetchone()
    if not data == None:  # 如果data不存在，data == None，代表沒找到，可以新增；若data已存在，data != None，顯示帳號已存在，無法新增。
      print(" %d ，此帳號已存在" %acc)
      continue

    pwd = input("請輸入密碼")
    sql_insert = "INSERT INTO staff_info(sf_name,sf_account,sf_pwd,create_user,update_user)VALUES('"+name+"','"+acc+"','"+pwd+"','"+name+"','"+name+"')" 
    #print(sql_insert)
    cur.execute(sql_insert)
    conn.commit() 
    print("使用者 %d :帳號已註冊成功，可以重新登入已進入系統" %acc)
    break

def staff_data_update():  # 可以調整修改內容 不僅限於使用者姓名。
  while True:
    acc = input("請輸入要修改的帳號:")
    if acc == "":
      break

    sql_query = " SELECT sf_name,sf_account,sf_pwd,sf_del FROM staff_info WHERE sf_account='" + acc + "' "
    cur.execute(sql_query)
    staff_data=cur.fetchone()
    # 查詢需更改的帳號是否存在
    if(staff_data == None):
      print(" %d ，此帳號不存在" %acc)
      continue
    print(staff_data)
    # 主要修改姓名
    newname = input("請輸入新的姓名")
    # sql_3 是更新sf_name的SQL語法
    sql_update = " UPDATE staff_info SET sf_name='"+ newname +"' WHERE sf_account='"+ acc +"' "
    cur.execute(sql_update) 
    conn.commit()

    # 用SQL_query語法查詢是否確實完成修改
    cur.execute(sql_query)
    person=cur.fetchone()
    print(person)
    input("修改成功，請按任意鍵回首頁")
    break

def staff_data_delete():
  while True:
    acc = input("請輸入要刪除的帳號:")
    if acc == "":
      print("你輸入的是空職")
      break
    # 先查詢帳號存在與否
    sql_query = " SELECT sf_name,sf_account,sf_pwd,sf_del FROM staff_info WHERE sf_account='" + acc + "' "
    cur.execute(sql_query)
    data = cur.fetchone()
    if data == None:
      print(" %d ，此帳號不存在" % acc)
      continue
    # 依照重複輸入帳號去做比對，完備刪除程序。
    option = input("如確認刪除請再次輸入此帳號?")
    if option == data[1]: # 用option比對 先前的data[1](帳號名稱)
      # 讓SQL自行尋找要刪除的帳號
      sql_delete="DELETE FROM staff_info WHERE sf_acc = '" +option+"' "
      cur.execute(sql_delete)
      conn.commit() # commit 確認提交(用於資料庫"更新")
      input("刪除成功，請輸入任意鍵回首頁")
      break


def sql_check_acc_existed():
  # 從SQL裡面抓資料
  acc = input("請輸入帳號:")
  if acc == "" : 
    print("你輸入為空值，請重新執行。")

  sql_query = "SELECT sf_name,sf_account,sf_pwd FROM staff_info WHERE sf_account='"+ acc +"' AND sf_del = '0'" 
  cur.execute(sql_query) # 資料庫執行抓資料存在cur裡  # sql 裡面抓變數用"+變數+"
  data = cur.fetchone() # print(staff_acc) # 總共抓了 名字、帳號、密碼三個欄位
  return data

# 建議用class 去存SQL語法資料 各種語法彙整 確認利用種況



# Managers_login_interface()
# Operating_interface()


Managers_login_list()


cur.close()   # 關閉資料庫
conn.close()  # 關閉連線
print("資料庫關閉成功") # 確認有完成關閉
