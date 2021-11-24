###  等差数列で解く

def addup_other(n):
    a = (1 + n)*(n/2)
    return int(a)#割り切れない場合があるので、整数型にして返す

print(addup_other(10))

#addup_other(n)は同じ答えを出すが、計算が一回で済むので圧倒的に効率が良い. 
#効率の良いアルゴリズムを使うのが大事