###平均値を求める2

score = [70, 98, 92, 88, 64]
total = 0
for i in score:
    total = total + i
average = total / 5
print("合計点", total)
print("平均点", average)

#配列のindexではなく、配列の中身をそのまま指定してる
#なぜかこのコードが最初実行できなかったけど、ターミナルでpythonが対話モードになってたらしく、
#>> exit()
#で抜けられた。めでたし。


