import streamlit as st

from utils import head, body, key_gender, key_workex

import pickle
model = pickle.load(open('model/model_student_placement_nb.pkl', 'rb'))

gender, workex, etest_p = head()

if st.button('Predict!'):    
    predict = model.predict([[key_gender.index(gender), key_workex.index(workex), etest_p]])[0]

    key_target = ['Not Placed', 'Placed']

    hasil_prediksi = key_target[predict]

    body(hasil_prediksi)
