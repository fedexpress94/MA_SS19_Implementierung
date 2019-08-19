import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

list = []

with open('../Excel_Dateien/190817_Geometrie.csv') as file:
    file.readline() # skip the first line
    for line in file:
        list.append(line.strip().split(";"))
print(list)




for i in range(0, len(list)):
   for j in range(1, len(list[i])):
        if list[i][j] == "y": 
            print("Yes")
        else:
            print("No")
    



