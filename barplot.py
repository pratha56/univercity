# -*- coding: utf-8 -*-
"""
Created on Thu May 27 21:02:46 2021

@author: asus
"""

import pandas as pd
import numpy as np
import streamlit as st 


st.title('plot graph')
st.subheader('information')
bar=np.arange(1,100)
st.bar_chart(bar)





  