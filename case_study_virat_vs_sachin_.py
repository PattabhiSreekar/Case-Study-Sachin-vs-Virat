# -*- coding: utf-8 -*-
"""Case Study - Virat vs Sachin .ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RDS6HQRNH_q1WStwcafmmh543pvmJZMA
"""

import warnings
warnings.filterwarnings('ignore')

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

#to display all rows columns
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.expand_frame_repr', False)
pd.set_option('max_colwidth', -1)

df = pd.read_csv('ODI_data.csv')

df.head(2)

len(df), len(df.columns)

# Runs per innings
# SR
# 100's
# 50's
# Team contribution

df['Innings Runs Scored Num'].unique()

df = df[df['Innings Runs Scored Num'] != '-']

df['Innings Runs Scored Num'].unique()

df = df.dropna(subset = ['Innings Runs Scored Num'])

df['Innings Runs Scored Num'].unique()

df.head(1)

# convert to datetime
df['Innings Date'] = pd.to_datetime(df['Innings Date'])

df['year'] = df['Innings Date'].dt.year

df.tail(1)

df['Innings Runs Scored Num'] = df['Innings Runs Scored Num'].astype('int')

df['Innings Balls Faced'] = df['Innings Balls Faced'].astype('int')

df['Innings Not Out Flag'] = df['Innings Not Out Flag'].astype('int')





# Sachin 1994 - 2004
# Virat 2009 - 2019

sachin_df = df[(df.year >= 1994) & (df.year <= 2004)]

kohli_df = df[(df.year >= 2009) & (df.year <= 2019)]

sachin_df.head(2)

kohli_df.head(2)

# Runs per innings = Total Runs/Total Innings
# SR = 100*(Total Runs/Total Balls)
# 100's = sum(100's)
# 50's = sum(50's)
# Team contribution = Player Runs/Team Runs (ex: Virat 50/ Team Ind 150 => 50/150 : 33%)

# df.dtypes

# sachin_df.to_csv('sachin_data.csv')

# what is the total runs scored by sachin in these time frames?

# sachin_df.head(20)

# SR Tendulkar
sdf = sachin_df[sachin_df['Innings Player'] == 'SR Tendulkar']

sdf.head()

sum(sdf['Innings Runs Scored Num'])

kdf = kohli_df[kohli_df['Innings Player'] == 'V Kohli']

# kohli_df['Innings Player'].unique()

kdf.head()

sum(kdf['Innings Runs Scored Num'])

len(kdf), len(sdf)

# RPI - Sachin, Virat
sum(kdf['Innings Runs Scored Num'])/len(kdf), sum(sdf['Innings Runs Scored Num'])/len(sdf)

# SR
100*sum(kdf['Innings Runs Scored Num'])/sum(kdf['Innings Balls Faced']), 100*sum(sdf['Innings Runs Scored Num'])/sum(sdf['Innings Balls Faced'])

# 100's
sum(kdf["100's"]), sum(sdf["100's"])

# 50's
sum(kdf["50's"]), sum(sdf["50's"])

# Team Contribution - Runs score by each player, Runs by team
sum(kdf['Innings Runs Scored Num']), sum(sdf['Innings Runs Scored Num'])

# 1994 - 2004 = All players
sum(sachin_df[sachin_df.Country == 'India']['Innings Runs Scored Num'])

# 2009 - 2019 = All players
sum(kohli_df[kohli_df.Country == 'India']['Innings Runs Scored Num'])

100*sum(kdf['Innings Runs Scored Num'])/sum(kohli_df[kohli_df.Country == 'India']['Innings Runs Scored Num'])

100*sum(sdf['Innings Runs Scored Num'])/sum(sachin_df[sachin_df.Country == 'India']['Innings Runs Scored Num'])

"""### Visualizations:"""

sachin_df.groupby(['Innings Player'])['Innings Runs Scored Num'].sum().sort_values(ascending = False).head(10)

sachin_df.groupby(['Innings Player'])['Innings Runs Scored Num'].sum().sort_values(ascending = False).head(10).plot(kind = 'barh')
plt.show()

kohli_df.groupby(['Innings Player'])['Innings Runs Scored Num'].sum().sort_values(ascending = False).head(10)

kohli_df.groupby(['Innings Player'])['Innings Runs Scored Num'].sum().sort_values(ascending = False).head(10).plot(kind = 'barh')
plt.show()

sdf.head(1)

sdf.groupby(['year'])['Innings Runs Scored Num'].sum().plot(kind = 'bar')

kdf.groupby(['year'])['Innings Runs Scored Num'].sum().plot(kind = 'bar')

"""### Normalization:"""

# RPI - Sachin, Virat
sum(kdf['Innings Runs Scored Num'])/len(kdf), sum(sdf['Innings Runs Scored Num'])/len(sdf)

# Kohli_df = player runs with Kohli
# player runs excluding Kohli => not_kohli = kohli_df[kohli_df.player_name != 'V Kohli']

# RPI - Sachin, Virat
sum(kohli_df['Innings Runs Scored Num'])/len(kohli_df)

kohli_df.head(1)

non_kohli_df = kohli_df[kohli_df['Innings Player'] != 'V Kohli']

non_sachin_df = sachin_df[sachin_df['Innings Player'] != 'SR Tendulkar']

# Avg = 25 runs
# Kohli = 50

(sum(kdf['Innings Runs Scored Num'])/len(kdf))/(sum(non_kohli_df['Innings Runs Scored Num'])/len(non_kohli_df))

(sum(sdf['Innings Runs Scored Num'])/len(sdf))/(sum(non_sachin_df['Innings Runs Scored Num'])/len(non_sachin_df))

# kohli => other
# SR = V = 93, Other = 80, V/other, S/others
# 100s - Number of matches to score a 100
# 50s - Number of matches to score a 50
# Team contribution - V_cont/O_cont

200/40, 200/37

"""### Strike Rate:"""

# sr of sachin
sum(sdf['Innings Runs Scored Num'])/sum(sdf['Innings Balls Faced'])

# sr of sachin's peers
sum(non_sachin_df['Innings Runs Scored Num'])/sum(non_sachin_df['Innings Balls Faced'])

# sr of kohli
sum(kdf['Innings Runs Scored Num'])/sum(kdf['Innings Balls Faced'])

# sr of kohli's peers
sum(non_kohli_df['Innings Runs Scored Num'])/sum(non_kohli_df['Innings Balls Faced'])

# normalized sachin's value
sachin_sr = sum(sdf['Innings Runs Scored Num'])/sum(sdf['Innings Balls Faced'])
sachin_peer_sr = sum(non_sachin_df['Innings Runs Scored Num'])/sum(non_sachin_df['Innings Balls Faced'])
sachin_sr/sachin_peer_sr

# normalized kohli's value
kohli_sr = sum(kdf['Innings Runs Scored Num'])/sum(kdf['Innings Balls Faced'])
kohli_peer_sr = sum(non_kohli_df['Innings Runs Scored Num'])/sum(non_kohli_df['Innings Balls Faced'])
kohli_sr/kohli_peer_sr

"""### 100's: Number of matches to score a 100"""

# sachin matches per 100
len(sdf)/sum(sdf["100's"])

# sachin peers - matches per 100
len(non_sachin_df)/sum(non_sachin_df["100's"])

# kohli matches per 100
len(kdf)/sum(kdf["100's"])

# kohli peers - matches per 100
len(non_kohli_df)/sum(non_kohli_df["100's"])

# normalized sachin value
sachin_mper_100 = len(sdf)/sum(sdf["100's"])
sachin_peers_mper_100 = len(non_sachin_df)/sum(non_sachin_df["100's"])
sachin_mper_100/sachin_peers_mper_100

# normalized virat value
kohli_mper_100 = len(kdf)/sum(kdf["100's"])
kohli_peers_mper_100 = len(non_kohli_df)/sum(non_kohli_df["100's"])
kohli_mper_100/kohli_peers_mper_100

"""### 50's: Number of matches to score a 50"""

# sachin matches per 100
len(sdf)/sum(sdf["50's"])

# sachin peers - matches per 100
len(non_sachin_df)/sum(non_sachin_df["50's"])

# kohli matches per 100
len(kdf)/sum(kdf["50's"])

# kohli peers - matches per 100
len(non_kohli_df)/sum(non_kohli_df["50's"])

# normalized sachin value
sachin_mper_50 = len(sdf)/sum(sdf["50's"])
sachin_peers_mper_50 = len(non_sachin_df)/sum(non_sachin_df["50's"])
sachin_mper_50/sachin_peers_mper_50

# normalized virat value
kohli_mper_50 = len(kdf)/sum(kdf["50's"])
kohli_peers_mper_50 = len(non_kohli_df)/sum(non_kohli_df["50's"])
kohli_mper_50/kohli_peers_mper_50

"""### Team Contribution: Here we are already comparing with peers, hence no need of a normalization"""

# % of team runs by sachin
100*sum(sdf['Innings Runs Scored Num'])/(sum(non_sachin_df[non_sachin_df.Country == 'India']['Innings Runs Scored Num'])+sum(sdf['Innings Runs Scored Num']))

# % of team runs by kohli
100*sum(kdf['Innings Runs Scored Num'])/(sum(non_kohli_df[non_kohli_df.Country == 'India']['Innings Runs Scored Num'])+sum(kdf['Innings Runs Scored Num']))