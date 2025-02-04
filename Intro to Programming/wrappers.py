def candytotal():
    budget = int(input("How much money do you have: "))
    candy = budget // 4
    wrappers = candy
    k = 0
    while wrappers >= 3:
        extra_candy = wrappers // 3
        wrappers = (wrappers % 3) + extra_candy
        candy += extra_candy
    print(f"You can purchase {candy} candy bars!")
candytotal()