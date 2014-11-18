__author__ = 'sabine'

import json
from pprint import pprint
import numpy as np
import pandas as pd
import os
import glob
from collections import Counter

'''
#list the files
filelist = os.listdir('test')
print filelist
#read them into pandas
df_list = [pd.read_json(file) for file in filelist]
#concatenate them together
jason_data = pd.concat(df_list)

#with open("landscape-dump/0compute__*.json") as json_file:
#    json_data = json.load(json_file)
#    # pprint(json_data)
'''

path ='test'
allFiles = glob.glob(path + "/*.json")
print allFiles

count =[]
dfs = []
message = []
for files in allFiles:
     with open(files) as json_file:
         json_data = json.load(json_file)

         message.append( (json_data['name'], json_data['messages']['code'],json_data['messages']['message'], json_data['messages']['source'], json_data['messages']['location']['line'], json_data['messages']['location']['path']) )
df = pd.DataFrame(message)
df.columns = ['user','code','message','source','line','path']
print df.info()

df.to_csv('results_2_users.csv', index=False)

'''
for files in allFiles:
    dfs.append(pd.read_json(files)
df = pd.concat(dfs, ignore_index=True)
print df.info()



messages = []
for m in json_data['messages']:
    messages.append( (m['code'],m['message'], m['source'], m['location']['function'], m['location']['line'], m['location']['module'], m['location']['path']) )
print messages

#df = pd.read_json("landscape-dump/mindriot101__staralt.json")
#df.info()
#print df

#df = df.drop(['commit_hash', 'config', 'name', 'owner', 'started'], axis=1)
#df.info()
#print df

#df_2 = pd.DataFrame(data=df)
#print df_2

#df = DataFrame(data=d, index=index)

df = pd.DataFrame(messages)
df.columns = ['code','message','source','function','line','module','path']
print df

'''
