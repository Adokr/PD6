def saveFile(x, file):
    with open(file, "w") as f:
        for i in range(len(x)):
            for j in range(len(x[i])):
                if j == len(x[i]) - 1:
                    f.write(f"{x[i][j]}")
                else:
                    f.write(f"{x[i][j]}, ")
            f.write("\n")