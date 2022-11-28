def loadFile(x):
    with open(x, "r") as f:
        t1 = []
        t2 = []
        for i in f:
            t1.append(i.split(sep=","))
        for i in range(len(t1)):
            t2.append([])
            for j in range(len(t1[i])):
                if i == 0 or j == len(t1[i]) - 1:
                    t2[i].append(t1[i][j].strip())
                else:
                    t2[i].append(float(t1[i][j].strip()))
        return t2

#print(loadFile("/home/alis/PycharmProjects/pd6/data/iris.csv")[1][:-1])