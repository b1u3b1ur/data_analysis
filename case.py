import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv ('StudentsPerformance .csv')
dst = df.info()
a = df.groupby(by='gender')['math score'].value_counts()
b = df.groupby(by='gender')['reading score'].value_counts()
c = df.groupby(by='gender')['writing score'].value_counts()
#hacer la pivot table
#piso = df.pivot_table(columns = 'test preparation course',
#    index = 'gender',
#    values = ['math score','reading score','writing score'],
#    aggfunc = ['min','mean','max'])

piso = df.groupby(by='gender')[['math score','reading score','writing score']].agg(['min','mean'])

p = int(input())
if p == 1:
    print(a,b,c)
    a.plot(kind = 'barh')
    #b.plot(kind = 'bar')
    #c.plot(kind = 'bar')
    plt.show()
elif p == 2:
    print(piso)
    piso.plot(kind = 'barh')
    plt.show()
