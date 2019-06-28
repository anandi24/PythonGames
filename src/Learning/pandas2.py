import pandas as pd

sal = pd.read_csv('Salaries.csv')

year = sal.groupby('yearID')
salPerYear = (group.sort_values(by='salary', ascending = False)[:1] for k, group in year)

topSal = pd.DataFrame()

for line in salPerYear:
    topSal = topSal.append(line)

ts = topSal[['yearID','salary']].set_index('yearID')

#print(ts)
ts.plot

#print(sal.ix[3:8,'yearID':'playerID'])

#print(sal.ix[[3,4,5,6,7],['yearID','playerID','salary']])

print(sal[(sal.salary > 20000000) & (sal.yearID>2000)])