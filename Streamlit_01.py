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
import streamlit as st
from streamlit_gsheets import GSheetsConnection

url = "https://docs.google.com/spreadsheets/d/1Z2n8Hl8M_TzJx1-hun4FXbGJjvcupC6q89ijQbLmYgA/edit?usp=sharing"

conn = st.experimental_connection("gsheets", type=GSheetsConnection)

data = conn.read(spreadsheet=url, usecols=[0, 1])
st.dataframe(data)
