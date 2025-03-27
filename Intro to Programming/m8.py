def flatten(l):
    rep = False
    new_l = []
    for x in l:
        if type(x) != list:
            new_l.append(x)
            continue
        else:
            rep = True
            for sub_l in x:
                new_l.append(sub_l)
    if rep:
        return flatten(new_l)
    else:
        return new_l
def mystery1(n):
    idk = [1, 2, 3, 4, 5]
    for i in range(n, 0, -1):
        new_idk = [0,0,0,0,0]
        new_idk[0] = idk[1]
        new_idk[1] = idk[2]
        new_idk[2] = idk[3]
        new_idk[3] = idk[4]
        new_idk[4] = idk[0] - idk[2] + idk[4]
        idk = new_idk.copy()
    return idk[0]
def mystery2(n, total = 0):
    if n == 0:
        return total
    else:
        digit = n % 10
        new_n = n // 10
        return mystery2(new_n, total+digit)
def collatz_sequence(n, result = ""):
    if n == 1:
        print (result + "1 ")
        return
    if n % 2 == 0:
        return collatz_sequence(n // 2, result+str(n)+" ")
    else:
        return collatz_sequence((3 * n) + 1, result+str(n)+" ")