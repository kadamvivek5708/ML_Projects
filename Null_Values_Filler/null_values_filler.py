import streamlit as st
import pandas as pd
import numpy as np

st.title('Fill Null Values')
filee = st.file_uploader('Choose a file')

if filee is not None:
  file = pd.read_csv(filee)
  st.dataframe(file)
   
  option = st.selectbox(
       'Fill with',
       ('Mean', 'Min', 'Max'))
  

  if(st.button('Generate')):
      
      if(option == 'Mean'):
        for col in file.columns:
          file[col].fillna((file[col].mean()), inplace=True)

      if(option == 'Min'):
        for col in file.columns:
          file[col].fillna((file[col].min()), inplace=True)

      if(option == 'Max'):
        for col in file.columns:
          file[col].fillna((file[col].max()), inplace=True)

      st.dataframe(file)