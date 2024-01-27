with open("time.txt", "r") as f:
    times = f.readlines()
    times = [float(i) for i in times]
    print(sum(times)/len(times))