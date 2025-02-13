def sum(*args):
    sum = 0.0
    for arg in args:
        sum += float(arg)
    return sum
def print_range(start, stop):
    seq = ""
    for i in range(start, stop+1):
        seq += (str(i))
        if i != (stop):
            seq += (","+" ")
    print(seq)
def sum_of_digits(num:int):
    digits = list(str(num))
    sum = 0
    for digit in digits:
        sum += int(digit)
    return sum