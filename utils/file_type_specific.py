import streamlit as st
import json
from langchain.tools.json.tool import JsonSpec
from langchain.agents.agent_toolkits import JsonToolkit
import sqlite3
import os
import pandas as pd

def checkbox_container(data,_gettext):
    sheets = data.sheet_names
    st.write(_gettext('Which sheets would you like to analyse(In case you do not choose any, by default first sheet will be automatically selected)'))
    if 'dummy_data' not in st.session_state.keys():
        dummy_data = sheets
        st.session_state['dummy_data'] = dummy_data
    else:
        dummy_data = st.session_state['dummy_data']

    
    for i in sheets:
        st.checkbox(i, key='dynamic_checkbox_' + i)

def get_selected_checkboxes():
    return [i.replace('dynamic_checkbox_','') for i in st.session_state.keys() if i.startswith('dynamic_checkbox_') and st.session_state[i]]

def excel_df_reader(_gettext,file_path,next_step):
    print('inside excel sample')
    # for excel file only input is output of pd.ExcelFile

    option_num_selected=1
    if '1' in next_step:
        file_ = pd.ExcelFile(file_path)
        sheets = file_.sheet_names
        checkbox_container(file_,_gettext)
        st.write(_gettext('You selected:'))
        sheets_selected = get_selected_checkboxes()
        st.write(sheets_selected)
        dataframes = [file_.parse(sheet) for sheet in sheets_selected]
        if not dataframes:
            # Default selection : Always select sheet one if user does not select any 
            dataframes = [file_.parse(sheets[0])]

    elif '2' in next_step:
        if os.path.isfile('sqlite_db.db'):
            #print('File exists')
            try:
                os.remove('sqlite_db.db')
            except:
                pass
        con=sqlite3.connect('sqlite_db'+".db")
        wb=pd.ExcelFile(file_path)
        for sheet in wb.sheet_names:
                df=pd.read_excel(file_path,sheet_name=sheet)
                df.to_sql(sheet,con, index=False,if_exists="replace")
        con.commit()
        con.close()
        dataframes = None 
        option_num_selected = 2
    elif '3' in next_step:
        pass 
    return (dataframes,option_num_selected)



def json_dict_loader(_gettext,path):
    try:
        with open(path, 'r') as f:
            data = json.load(f)
    except Exception as e:
        st.write(_gettext("Error while checking the file. Please try again."),e)
        return  
    try:
        json_spec = JsonSpec(dict_=data, max_value_length=4000)
    except:
        st.error(_gettext("The format is wrong(Should be a dictionary type)"))
        return 
    json_toolkit = JsonToolkit(spec=json_spec)
    return (json_toolkit,data)