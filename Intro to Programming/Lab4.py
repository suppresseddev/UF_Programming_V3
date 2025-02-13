def fibonacci(n):
    seq = [0, 1]
    result = 0
    if (n == 0) or (n == 1):
        return 0
    for t in range(1,n-1):
        result = seq[t]+seq[t-1]
        seq.append(result)
    return result
def is_prime(n):
    if n <= 1:
        return False
    for i in range(1, n):
        if (n % i == 0):
            if (i == n) or (i == 1):
                continue
            else:
                return False
    return True
debug = True
def print_prime_factors(n):
    if is_prime(n):
        print(f"{n} = {n}")
        return
    prime_factors = []
    for i in range(1, n):
        if is_prime(i):
            if n % i == 0:
                prime_factors.append(i)
    prime_factors.sort()
    # prime_multiples = []
    # for t, factor in enumerate(prime_factors):
    #     for k in prime_factors:
    #         if (k * factor) not in prime_multiples:
    #             prime_multiples.append(k * factor)
    solution = []
    u = n
    for k in prime_factors:
        while u % k == 0:
            solution.append(k)
            u = u // k
    answer = f"{n} = "
    for t in solution:
        answer += str(t) + " * "
    answer = answer[:-3]
    print(answer)