from itertools import combinations
import math

listCat = []
with open('../01_Test_Excel/190819_3Categories.csv') as file:
    file.readline() # skip the first line
    for line in file:
        listCat.append(line.strip().split(";"))



listComb = combinations([listCat[0], listCat[1], listCat[2]], 2)
listUebergabe = []
for i in list(listComb):
    listUebergabe.append(i)
    
print(listUebergabe)



class ListAnalysis():
    def __init__(self, listA):
        self.listA = listA
        
    def __len__(self):
        return len(self.listA)
        

    def calcSim(self):
        bothAB = 0
        onlyA  = 0
        onlyB  = 0
    
        for i in range(0, len(self.listA)):
            for j in range(1, len(self.listA[i][0])):
                if self.listA[i][0][j] =="y" and self.listA[i][1][j] == "y":
                    bothAB = bothAB + 1
                elif self.listA[i][0][j] == "y" and self.listA[i][1][j] == "n":
                    onlyA = onlyA + 1
                elif self.listA[i][0][j] == "n" and self.listA[i][1][j] == "y":
                    onlyB = onlyB + 1
            similarityEuclid = (bothAB)/(math.sqrt((onlyA +bothAB)*(onlyB + bothAB)))
            print(similarityEuclid)

test = ListAnalysis(listUebergabe)
test.calcSim()





