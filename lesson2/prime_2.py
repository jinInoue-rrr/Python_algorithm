##エラストテネスの篩

p = [True] * 100#要素のTrueを100こ出力
p[0] = False
p[1] = False
n = 2

def hyou():#数の一覧を出力する関数を定義する
    s = ""#空の文字列を定義
    for i in range(100):
        if p[i] == True:
            s += "{:2d},".format(i)#iの値を文字列としてsに加える
        else:
            s += "/,"#Falseは素数じゃないので斜線をひく
        if i%10 == 9:
            s += "¥n"##改行コードを加える
    print(s)#for loopが終わってから最後に出力する

def furui():
    global n#nをグローバル変数として定義する
    for i in range(n+n, 100, n):#n+nから99までnずつ増える
        p[i] = False
    print(n, "の倍数をふるい落としました")
    hyou()
    while n < 100:#次に篩い落とす数の倍数を決める
        n = n + 1
        if p[n] == True:
            break

hyou()
while n < 10:
    input("Enterキーを押してください")
    furui()



