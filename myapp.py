# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 22:01:36 2021

@: asus
"""

import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
st.title('My project')
st.header('prathamesh deore')
df=sns.load_dataset('iris')
st.dataframe(df)
st.bar_chart(df['sepal_length'])



