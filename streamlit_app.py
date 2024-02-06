import streamlit as st
import pandas as pd
dict={
    'mass' :[9,8,6,7,5],
    'velocity' :[12,13,14,15,16]
}
df=pd.DataFrame(dict)
st.table(df)
st.title('Mass velocity Table')
st.write('roshan')
