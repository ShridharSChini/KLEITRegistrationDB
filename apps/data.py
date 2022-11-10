import streamlit as st
import numpy as np
import pandas as pd
import mysql.connector as sqlc
from mysql.connector import Error
def app():
    try:
        cnx=sqlc.connect(host="localhost",user="root",password="root",database="sdm")
        Cursor=cnx.cursor()
        if st.checkbox("Student Details"):
            SelectQuery="SELECT * FROM DETAILS"
            Cursor.execute(SelectQuery)
            data=Cursor.fetchall()
            result=pd.DataFrame(data)
            result.columns=['USN','Full Name','Branch','Fees Due','Fees Paid','Date of Payment','Receipt','Admission Sought','Email','Mobile No.','Parents Mob. No.','Postal Address','Admission To','Admission Quota','Category','Prof. Elective-1','Prof. Elective-2','Open Elective-1','Open Elective-2']
            
            # st.write(result['Receipt'])
            # st.write(type(str(result['Receipt'])))
            # result['Receipt'] = str(result['Receipt'])
            # result['Receipt'] =result['Receipt'].apply(result['Receipt'])

            st.markdown(result.to_html(render_links=True,escape=False),unsafe_allow_html=True)
            # result = result.to_html(escape=False)
            # st.write(result,unsafe_allow_html = True) 
            # st.dataframe(result)
            # cnx.commit()
    except Error as e:
        print("Error occured",e)