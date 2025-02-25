from math import log
#Decimal to Binary
def bin(n):
    if n == 0:
        return ''
    g_d = round(log(n, 2)) + 1
    r = n
    result = ""
    for d in range(g_d, -1, -1):
        k = r // (2 ** d)
        if k == 0:
            result += "0"
        if k == 1:
            result += "1"
            r = r - (2 ** d)
    return(str(int(result)))
#Capitalize (but not really)
def capitalize(t):
    t_words = t.split(' ')
    new_t = ""
    invalid = ['o', 'u', 's', 'n', 'd']
    for word in t_words:
        if word[0].lower() in invalid:
            new_t += f"{word.lower()} "
        else:
            new_t += f"{word.capitalize()} "
    return new_t[:-1]
#List Partioning
def partition(t, segsize):
    g = t.copy()
    k = []
    #expected length
    el = (len(t) // segsize)
    for i in range(el):
        k.append(g[(i*segsize):((i+1)*segsize)])
    for seg in k:
        for v in range(0, segsize):
            g.pop(0)
    if g != []:
        k.append(g)
    return(k)
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(partition(nums, 3))