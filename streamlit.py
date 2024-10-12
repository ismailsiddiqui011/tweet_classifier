import streamlit as st
import numpy as np
import os
from utils import predict
st.title('Tweet Classifier')
st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQejMAWRzRClrWFA8hZbje7x3ErUgJs-YEf3gB328187vSlMbAJbrQGiAMTxEOjQwykXXA&usqp=CAU', width = 300)

try:
    tweet = st.text_input('Enter tweet...')
    result = predict(tweet)
    st.markdown(f'Emotion: {result[0]}')
    st.markdown(f'Product: {result[1]}')
except:
  pass