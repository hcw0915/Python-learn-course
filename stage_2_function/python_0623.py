import json
file = open("test0623.json",encoding="utf8")

file_array = json.load(file)
# file_array = [{"id": "1","city": "台北"},{"id": "2","city": "高雄"}]

for key in file_array:
  print("id:",key["id"])
  print("city:",key["city"])

file.close()



# 老師好 我遇到一個問題
# "C:\.....python-yiru\stage_2_function\test0623.json"
# 執行檔(py)放在 stage_2 這個資料夾裡面
# json 也放在 stage_2 不能執行
# 但是往上放在更上層就可以執行