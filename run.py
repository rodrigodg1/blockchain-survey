# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd

df = pd.read_csv("blockchain_data_privacy_SCHOLAR.csv",sep=",")


#df_2015 = df['Year']==2015
#df_2015 = df[df_2015]

#only_title = df['Title'].to_frame()

only_title_after = df.drop_duplicates('Title')