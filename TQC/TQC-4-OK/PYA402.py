# TODO

a = []
while True:
  x = input()
  a = a + [x] #建立輸入值的list
  
  if "9999" in a:
    break

list_a = [int(i) for i in a]  #list內字串轉數值
re_list = sorted(list_a)  #反轉數列

print(re_list)
if 9999 in re_list: #避免9999是最小值的處理
  re_list.remove(9999)
  
print(re_list[0])