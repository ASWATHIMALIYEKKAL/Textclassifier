import pandas as pd
import streamlit as st
bbc_text = pd.read_csv('bbc-text.txt')
bbc_text=bbc_text.rename(columns = {'text': 'News_Headline'}, inplace = False)
bbc_text.head()
