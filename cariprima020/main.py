#mencari bilangan prima dari angka 0 sampai 20
i = 0
while(i < 20):
    j = 2
    while(j <= i/j):
        if not(i%j):break
        j  = j + 1
    if ((j > i/j) and i !=0): print(i, "adalah bilangan prima")
    i +=1