## 再帰関数の利用

def fact(n):
    if n == 0:
        return 1

    else:
        return n * fact(n-1)

for i in range(0, 21):
    print(str(i)+"! =", fact(i))


##再帰関数は必ず最後に処理が終わるように作る必要がある。そうでないと無限に処理が続くことになってしまうので。






