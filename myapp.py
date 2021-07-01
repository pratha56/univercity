# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 22:01:36 2021

@author: asus
"""

import streamlit as st
import pandas as pd
import numpy as np
df=pd.read_csv(r'C:\Users\asus\Desktop\my desk\data science\hirearchical clustering\Universities.csv')
st.title('My project')
st.header('prathamesh deore')
st.dataframe(df)
st.bar_chart(df['SAT'])


