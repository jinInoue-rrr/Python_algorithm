###九九の計算2

for i in range(1, 10):
    k = ""#空の文字列kを作成
    
    for j in range(1, 10):

        k = k + "{}×{}={:2d} ".format(j, i, i * j)

    print(k)


