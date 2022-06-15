# TODO
import string
import numbers
a=input()
all = set(string.ascii_letters[::]) #設定set內包含 大小小A-Z 字串的字元
if a in all:  
  print(a+" is an alphabet.")
elif str.isdigit(a) is True:  #str.isdigit(a) 檢視字串str內是否只包含整數 是=TURE
  print(a+" is a number.")
else :
  print(a+" is a symbol.")



"""
_ is an alphabet.
_ is a number.
_ is a symbol.
"""