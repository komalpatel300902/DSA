def cbroot(N):   
    num = 2
    while True:
        if N < num**3:
            return num -1
        num+=1

print(cbroot(90))