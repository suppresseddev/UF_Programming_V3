def numberpile():
    height = int(input("Height: "))
    for i in range(1, height+1):
        pattern = " "*(height-i)
        for j in range(1, i+1):
            pattern = pattern + str(j)
        print(pattern)
numberpile()