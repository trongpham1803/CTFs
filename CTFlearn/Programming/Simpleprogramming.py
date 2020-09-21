


Count = 0
with open("data.dat","r") as f:
    # Read lines from file and decode Hex
    ls = f.readlines()
    for l in ls:
        Count_0 =l.count("0")
        Count_1 = l.count("1")
        if Count_0 % 3 == 0:
            Count = Count + 1
        elif Count_1 % 2 == 0:
            Count = Count + 1
print(Count)


        

