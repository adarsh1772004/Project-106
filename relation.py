import csv
import pandas as pd
import plotly.express as px
import math
import numpy as np
f=open("Student Marks.csv")
reader=csv.reader(f)
data=list(reader)
data.pop(0)
add=0
MarksInPercentage=[]
DaysPresent=[]
for i in range(len(data)):
    MarksInPercentage.append(float(data[i][1]))
    DaysPresent.append(float(data[i][2]))
dict={'x':DaysPresent,'y':MarksInPercentage}
c=np.corrcoef(dict['x'],dict['y'])
print (c)