##1からnまで足し合わせた値を返す関数を定義する

def addup(n):
    a = 0
    for i in range(1, n+1):
        a += i# a = a + iでも良い
    return a
    
print(addup(10))


