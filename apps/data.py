import streamlit as st
import numpy as np
import pandas as pd
import mysql.connector as sqlc
from mysql.connector import Error


def app():
    try:
        branch_li = ['Select your branch','CSE - Computer Science and Engineering','ECE - Electronics and Communication Engineering',
        'EEE - Electrical and Electronics Engineering','CIV - Civil Engineering','MEC - Mechanical Engineering',
        'MCA - Master of Computer Application']

        branch = st.selectbox('Branch:',branch_li)

        cnx=sqlc.connect(host="localhost",user="root",password="root",database="sdm")
        Cursor=cnx.cursor()
        if(branch=='CSE - Computer Science and Engineering'):
            SelectQuery="SELECT * FROM CSE"
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
            CountQuery="SELECT COUNT(*) FROM CSE"
            Cursor.execute(CountQuery)
            for row in Cursor:
                st.write("Total Count:",row[0])
            PaidQuery="SELECT SUM(FEES_PAID) FROM CSE"
            Cursor.execute(PaidQuery)
            for row in Cursor:
                st.write("Total Fees Paid:",row[0])
            PendingQuery="SELECT SUM(FEES_PENDING) FROM CSE"
            Cursor.execute(PendingQuery)
            for row in Cursor:
                st.write("Total Fees Pending:",row[0])
        elif(branch=='ECE - Electronics and Communication Engineering'):
            SelectQuery="SELECT * FROM ECE"
            Cursor.execute(SelectQuery)
            data=Cursor.fetchall()
            result=pd.DataFrame(data)
            result.columns=['USN','Full Name','Branch','Fees Due','Fees Paid','Date of Payment','Receipt','Admission Sought','Email','Mobile No.','Parents Mob. No.','Postal Address','Admission To','Admission Quota','Category','Prof. Elective-1','Prof. Elective-2','Open Elective-1','Open Elective-2']
            st.markdown(result.to_html(render_links=True,escape=False),unsafe_allow_html=True)
            CountQuery="SELECT COUNT(*) FROM ECE"
            Cursor.execute(CountQuery)
            for row in Cursor:
                st.write("Total Count:",row[0])
            PaidQuery="SELECT SUM(FEES_PAID) FROM ECE"
            Cursor.execute(PaidQuery)
            for row in Cursor:
                st.write("Total Fees Paid:",row[0])
            PendingQuery="SELECT SUM(FEES_PENDING) FROM ECE"
            Cursor.execute(PendingQuery)
            for row in Cursor:
                st.write("Total Fees Pending:",row[0])
        elif(branch=='EEE - Electrical and Electronics Engineering'):
            SelectQuery="SELECT * FROM EEE"
            Cursor.execute(SelectQuery)
            data=Cursor.fetchall()
            result=pd.DataFrame(data)
            result.columns=['USN','Full Name','Branch','Fees Due','Fees Paid','Date of Payment','Receipt','Admission Sought','Email','Mobile No.','Parents Mob. No.','Postal Address','Admission To','Admission Quota','Category','Prof. Elective-1','Prof. Elective-2','Open Elective-1','Open Elective-2']
            st.markdown(result.to_html(render_links=True,escape=False),unsafe_allow_html=True)
            CountQuery="SELECT COUNT(*) FROM EEE"
            Cursor.execute(CountQuery)
            for row in Cursor:
                st.write("Total Count:",row[0])
            PaidQuery="SELECT SUM(FEES_PAID) FROM EEE"
            Cursor.execute(PaidQuery)
            for row in Cursor:
                st.write("Total Fees Paid:",row[0])
            PendingQuery="SELECT SUM(FEES_PENDING) FROM EEE"
            Cursor.execute(PendingQuery)
            for row in Cursor:
                st.write("Total Fees Pending:",row[0])
        elif(branch=='CIV - Civil Engineering'):
            SelectQuery="SELECT * FROM CIV"
            Cursor.execute(SelectQuery)
            data=Cursor.fetchall()
            result=pd.DataFrame(data)
            result.columns=['USN','Full Name','Branch','Fees Due','Fees Paid','Date of Payment','Receipt','Admission Sought','Email','Mobile No.','Parents Mob. No.','Postal Address','Admission To','Admission Quota','Category','Prof. Elective-1','Prof. Elective-2','Open Elective-1','Open Elective-2']
            st.markdown(result.to_html(render_links=True,escape=False),unsafe_allow_html=True)
            CountQuery="SELECT COUNT(*) FROM CIV"
            Cursor.execute(CountQuery)
            for row in Cursor:
                st.write("Total Count:",row[0])
            PaidQuery="SELECT SUM(FEES_PAID) FROM CIV"
            Cursor.execute(PaidQuery)
            for row in Cursor:
                st.write("Total Fees Paid:",row[0])
            PendingQuery="SELECT SUM(FEES_PENDING) FROM CIV"
            Cursor.execute(PendingQuery)
            for row in Cursor:
                st.write("Total Fees Pending:",row[0])
        elif(branch=='MEC - Mechanical Engineering'):
            SelectQuery="SELECT * FROM MECH"
            Cursor.execute(SelectQuery)
            data=Cursor.fetchall()
            result=pd.DataFrame(data)
            result.columns=['USN','Full Name','Branch','Fees Due','Fees Paid','Date of Payment','Receipt','Admission Sought','Email','Mobile No.','Parents Mob. No.','Postal Address','Admission To','Admission Quota','Category','Prof. Elective-1','Prof. Elective-2','Open Elective-1','Open Elective-2']
            st.markdown(result.to_html(render_links=True,escape=False),unsafe_allow_html=True)
            CountQuery="SELECT COUNT(*) FROM MECH"
            Cursor.execute(CountQuery)
            for row in Cursor:
                st.write("Total Count:",row[0])
            PaidQuery="SELECT SUM(FEES_PAID) FROM MECH"
            Cursor.execute(PaidQuery)
            for row in Cursor:
                st.write("Total Fees Paid:",row[0])
            PendingQuery="SELECT SUM(FEES_PENDING) FROM MECH"
            Cursor.execute(PendingQuery)
            for row in Cursor:
                st.write("Total Fees Pending:",row[0])
    except Error as e:
        print("Error occured",e)