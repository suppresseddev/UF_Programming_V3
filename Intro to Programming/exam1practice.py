def fourbonacci(n):
    seq = [1, 4, 7, 8]

    skipseq = [1, 2, 3, 4]
    if n in skipseq:
        return(seq[skipseq.index(n)])

    for i in range(4,(n+2)):
        seq.append(4*seq[i-4] + 3*seq[i-3] + 2*seq[i-2] + 1*seq[i-1])
    return(seq[n-1])
def odd_squares(n):
    seq = range(1, (n*2), 2)
    for i in seq:
        print(i ** 2)
def diamond(h):
    seq = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    middle = (h // 2) + 1
    t = 0
    k = middle
    if h == 1:
        print(1)
        return
    while h > 0:
        bar = seq[:(t+1)]
        space = " "*(k-1)
        pillar = ""
        for i in bar:
            pillar = pillar + str(i)
        print(space+pillar)
        if h > middle:
            t = t+2
            k = k-1
        if h == middle:
            t = t-2
            k = k+1
        if h < middle:
            t = t-2
            k = k+1
        h = h-1