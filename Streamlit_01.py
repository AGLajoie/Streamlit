# -*- coding: utf-8 -*-
"""
       @@@@@                           
      @%   %@  @      %@@@%%     %@     
     @%       @%     @%    %%   @@      
    @%       @ @    @@         @@       
   @%       @  @   %@         @@        
  @%       @%@%@%@%@%@%@%@%@%@%@%@%@     
  %%     @%    @  %@      %@ @@     
  %@   @%      @  %@%  %@%  %@%      
   %@@@%       %@  %@@@%    %@@@@%    
                
@author: AGL
"""
import streamlit as st
import pandas as pd
import numpy as np

df = pd.read_csv("Streamlit_01.csv")

st.dataframe(df)  # Same as st.write(df)
