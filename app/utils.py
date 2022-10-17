import streamlit as st

key_gender = ['F', 'M']
key_workex = ['No', 'Yes']


def head():
    st.markdown("""
        <h1 style='text-align: center; margin-bottom: -35px;'>
        Predict Student Placement</h1>
        """, unsafe_allow_html=True)

    st.caption("""
        <p style='text-align: center'>
        using gaussian naive bayes model built with sklearn, data from
        <a href='https://www.kaggle.com/datasets/benroshan/factors-affecting-campus-placement'>
        Campus Recruitment (Kaggle)</a></p>
        """, unsafe_allow_html=True)

    gender = st.selectbox("Gender", key_gender, index=0)
    workex = st.selectbox("Work Experience", key_workex, index=0)
    etest_p = st.number_input("Interview Test Result (per 100)", 0, 100, step=1)

    return gender, workex, etest_p
    
def body(result):
    st.write(result)
    st.markdown('---')
