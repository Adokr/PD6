from sys import argv
from iris_analysis.io.load import loadFile
from iris_analysis.io.save import saveFile
from iris_analysis.calculate import newMedian, newMean, newStdev

def runAnalysis(x, y):
    t1 = list(map(list, zip(*(loadFile(x)))))
    wynik = [["function", "median", "mean", "stdev"]]
    for i in range(len(t1) - 1):
        wynik.append([])
        wynik[i+1].append(t1[i][0])
        wynik[i+1].append(round(newMedian(t1[i][1:]), 2))
        wynik[i+1].append(round(newMean(t1[i][1:]), 2))
        wynik[i+1].append(round(newStdev(t1[i][1:]), 2))
    saveFile(wynik, y)

runAnalysis(argv[1], argv[2])
