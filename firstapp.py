
import pandas as pd
import streamlit as st


data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}

st.title(" Your First Streamlit App")
st.title("Displaying Data in a Table")


data = pd.DataFrame(data)   
st.write(data)



print("UMesh")



    