
def myinfo():
  print(1)

print(7)
print("name=",__name__)

if __name__ == "__main__":
  print(2)
  print(3)

#在別的檔案被引用的時候 __name__就不會等於__main__ 而是page_1
#所以設如果__name__ == __main__成立，代表不被引用，而是在自己原本檔案執行
#再原本檔案執行是可以印出來 if 裡面的東西