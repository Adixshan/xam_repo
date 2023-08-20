import pandas as pd
import random

outlook=['Sunny','Rainy','Overcast']
temperature=['Hot','Mild','Cool']
humidity=['High','Normal']
windy=['False','True']

data=[]

for _ in range(10):
    row=[
        random.choice(outlook),
        random.choice(temperature),
        random.choice(humidity),
        random.choice(windy),
        random.choice(['yes','no'])
    ]
    data.append(row)


df= pd.DataFrame(data,columns=['Outlook','Temperature','Humidity','Windy','Playtennis'])  
df.to_csv('Play_tennis.csv',index=False)