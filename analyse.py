__author__ = 'sabine'

import pandas as pd
import matplotlib.pyplot as plt
import pylab

#from collections import Counter

df_list = pd.read_csv('results_all.csv')
df_list2 = pd.DataFrame(df_list)


#count=[]
# create list with unique codes and count them
#for i in df_list['code']:
#    if i not in count:
#        count.append(i)
#f = Counter(count)

count = df_list['code'].value_counts()
#print count

length = len(set(df_list['code']))
length2 = len(set(df_list['message']))
print length2

#Count = {}
#for i in set(df_list['code']):
#    Count = count

Count = pd.DataFrame(count)
Count.columns = ['occurrence']
Count.index.names = ['index']
print Count.iloc[1]

'''
for i in range(0,10):
    print 'hello', Count['occurrence'][i], df_list[df_list['code'] == 'C0103']['message']


for i in set(df_list['code']):
    print i,df_list[df_list['code'] == i]['message']

#plt.hist(Count)
Count.plot(kind='bar')
#count.hist()
#Count.ylabel('occurence')
#count.xlabel('error')

pylab.show()
'''
#for i in count:
 #   print i, df_list['code'==i]


mean_err = {}

for i in df_list.code:
    mean_err[i] = df_list[df_list['code']==i]['line'].mean()
print mean_err

plt.bar(range(len(mean_err)), mean_err.values(), align='center')
plt.xticks(range(len(mean_err)), mean_err.keys())
pylab.show()





