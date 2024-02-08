from typing import Literal
from collections import deque    

import os
from langchain.chains import RetrievalQA

import streamlit as st
from streamlit_modal import Modal
import requests
from utils.load import load_base64_image
from auth.authenthication import setup_authenticator
from langchain.callbacks import StreamlitCallbackHandler
from streamlit_chat import message
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
from chat.chat_ui_utils import clear_conversation,display_conversation
from chat.chat_history_utils import get_session_chat_history,add_to_session_chat_history
from config.session_config import CONVERSATION_HISTORY_SESSION_STATE, USER_TEXT_SESSION_STATE
from langchain.chat_models import ChatAnyscale
import streamlit as st 
from utils.load import load_base64_image
from utils.load import load_config
from utils.load import displayPDF
import pandas as pd
from utils.load import load_sample_file,get_uploaded_file
from utils.visualise_files import display_file

from model.data_master_app_agents import get_data_agent,get_data_agent2
from sample_questions.sample_questions import sam_ques
from sample_questions.sample_answers import sam_ans
#from langchain.llms import Anyscale 
#ANYSCALE_MODEL_NAME = 'meta-llama/Llama-2-7b-chat-hf'
        
#llama2_llm = Anyscale(model_name = ANYSCALE_MODEL_NAME)

import streamlit as st

# # Check if 'key' already exists in session_state
# # If not, then initialize it
# if 'key' not in st.session_state:
#     st.session_state['key'] = 'value'

# # Session State also supports the attribute based syntax
# if 'key' not in st.session_state:
#     st.session_state.key = 'value'



ANYSCALE_API_KEY=os.getenv('ANYSCALE_API_KEY')
os.environ["ANYSCALE_API_BASE"]='https://api.endpoints.anyscale.com/v1'
os.environ['ANYSCALE_API_KEY']=ANYSCALE_API_KEY
ANYSCALE_MODEL_NAME="meta-llama/Llama-2-7b-chat-hf"

import matplotlib
import matplotlib.pyplot as plt

WIDTH_OF_PLOT = 600

def demo_dashboard(_gettext):
    st.info(_gettext('Welcome, you can ask queries in your natural language from different file formats just as you use code to extract information. In excel, you can analyse each sheets as a dataframe or use whole file as a database. With PDF, DOC and TXT files, you can chat with the data inside. Check the Need Help section below on how to proceed.'))
    st.warning(_gettext('Please only ask to plot graphs in CSV and TSV file type. Check sample questions to get familiar with graph queries.'))

    with st.container():
        file_tab,chatbot,login_tab = st.tabs([_gettext('File Upload'),_gettext('Interactive chatbot'),_gettext('Login')])

        #--------login column------------------------- 
        with login_tab:
            proxy_col1,login_col,proxy_col2 = st.columns((0.5,0.5,0.5))
            with login_col:
                login_heading = _gettext('Login') 
                st.markdown(f"<div class='section-headings'><b>{login_heading}</b></div>", unsafe_allow_html=True)

                #----------Authenticaiton------------------------------
                authenticator = setup_authenticator() 
                name, authentication_status, username = authenticator.login(_gettext('Login'), 'main')
                
                if authentication_status:    
                    authenticator.logout(_gettext('Logout'), 'main')
                    
                # check authentication   
                if authentication_status==False:
                    st.error(_gettext('Username/password is incorrect'))
                if authentication_status is None:
                    st.warning('For credentials, contact Algoanalytics at info@algoanalytics.com')

        
        #--------Document viewer column------------------------- 
        with file_tab:
            file_proxy1,file_col,file_proxy2 = st.columns((0.5,1,0.5))
            with file_col:
                file_tab_heading = _gettext('Select your data files here')
                st.markdown(f"<div class='section-headings'><b>{file_tab_heading}</b></div>", unsafe_allow_html=True)
                st.markdown(f"")
                with st.expander(_gettext("Need help")):
                    st.info(_gettext('1. In the File Upload section, select a file type you want to analyse.\n2. Move forward with either sample file or upload your own.\n4. If you choose EXCEL further choose the type of analysis you want to do and then choose which sheets you want to analyse together. \n4. After above steps you are ready to interact with your data. Move to the Interactive Chatbot section where you can use sample questions to take the demo.\n5. If you want to use your own questions, please login.\n6. For access and additional assistance, please get in touch with us at info@algoanalytics.com'))
                df_c1,df_c2,df_c3 = st.columns((0.5,1,0.5))
                with df_c2:
                    option = st.selectbox(
                    _gettext('File type you would like to analyse'),
                    ('CSV','TSV','EXCEL','TXT','DOC','PDF','JSON','SQLITE_DB'),help=_gettext('Select the file type you want to analyse'))
                if option=='EXCEL':
                    next_step = st.radio(label=_gettext("Choose what to do with your file"),
                            options = ['1.'+_gettext('Analyse multiple sheets together as dataframes (Each multiple file is considered to be a dataframe)'),
                                        '2.'+_gettext('Proceed as a relational database (Each sheet will be converted to a table in SQL database.)'),
                                        #'3.'+_gettext('Cell based analysis(Analyse formula embedded in cell which depends on other cell values. '),
                                        ],   
                            help=_gettext('Select one of the below options to proceed with different types of analysis'),key='excel_radio')
                             
            #--Upload the file or select the the sample files--------
            
            sample_file_col,or_col,upload_col  = st.columns((1,0.1,1))
            with or_col:
                or_text = _gettext('OR')
                st.markdown(f"""
                    <div class='description_v2'>{or_text}</div>
                    """,unsafe_allow_html=True)
            
            file_type_mappings = {'CSV':['csv'],'TSV':['tsv'],'EXCEL':['xls','xlsx'],
                             'TXT':['txt'],'DOC':['doc','docx'],'PDF':['pdf'],'JSON':['json'],'SQLITE_DB':['db']}
            
            sample_file_mappings = {'CSV':['tesla-stock-price.csv'],
                                    'TSV':['tesla-stock-price.tsv'],
                                    'EXCEL':['Tesla_Amazon_stock_price.xlsx'],
                                    'TXT':['Nifty_50_Wikipedia.txt'],
                                    'DOC':['Gold_investment.docx'],
                                    'PDF':['Bill_Paid_Reciept.pdf'],
                                    'JSON':['Quiz.json'],
                                    'SQLITE_DB':['Chinook.db']}
            
            is_it_sample = True 
            with sample_file_col:
                st.info(_gettext('Use the Sample file'))
                sfc1,sample_file_col_,sfc2 = st.columns((0.3,1,0.3))
                with sample_file_col_:
                    sample_files_holder = st.empty()
                    option2 = sample_files_holder.selectbox(_gettext(f'Select sample file'),(sample_file_mappings.get(option)),index=0,
                        help=_gettext('By default a sample file is provided, in case you want to analyse your own file please upload in the right section.'))
                    #if st.session_state.es:
                    if is_it_sample == True and option!='EXCEL':  
                        loaded_file,original_file = load_sample_file(_gettext,file_type=option)
                    
            
            with upload_col:
                st.info(_gettext('Upload your own files'))
                # upload custom file based on selection
                ufc1,upload_file_col_,ufc2 = st.columns((0.3,1,0.3))
                with upload_file_col_:
                    upload_file_holder = st.empty()
                    uploaded_file = upload_file_holder.file_uploader(_gettext("Choose a file"),type=file_type_mappings.get(option),
                        help=_gettext("Here you can upload your own file, the file size limit is kept to 1 MB. Please make sure that the file you upload is of the same file type you choose above."))
                    if uploaded_file is not None:
                        is_it_sample = False
                        st.success('File uploaded!')
                        sample_files_holder.empty()
            
            
            # if file is uploaded select the upload else select sample file 
            if uploaded_file is not None:
                is_it_sample = False
                st.session_state.es = False
                info_c11,info_c21,info_c31 = st.columns((1,0.5,1))
                with info_c21:
                    st.warning(_gettext('Uploaded file selected for analysis'))
                if option=='EXCEL':
                    excel_c11,excel_c21,excel_c31 = st.columns((1,0.5,1))
                    with excel_c21:
                        loaded_file,original_file = get_uploaded_file(_gettext,uploaded_file,file_type = option,next_step=next_step)
                else:
                    loaded_file,original_file = get_uploaded_file(_gettext,uploaded_file,file_type = option, next_step= None)
                _file = loaded_file
                
                if option == 'EXCEL':
                    option_num_selected = original_file[1]
                    if option_num_selected==2:
                        _file = None
                
            else:
                if option=='EXCEL':
                    loaded_file,original_file = load_sample_file(_gettext,file_type=option,next_step=next_step)
                info_c12,info_c22,info_c32 = st.columns((1,0.5,1))
                with info_c22:
                    st.warning(_gettext('Sample file selected for analysis'))
                is_it_sample = True
                _file = loaded_file
                if option == 'EXCEL':
                    option_num_selected = original_file[1]
                    # to display only first sheet selected
                    if option_num_selected==2:
                        _file = None
                    

        #--------Chatbot column-------------------------

        with chatbot:
            cv1,cv2,cv3 = st.columns((1,1,1))
            with cv2:
                with st.expander(_gettext('Need help ?')):
                    st.info(_gettext('1.For demo, select a sample question and press the "Use question" button. \n If you want to ask your own queries, type in text input and then use the "Get answer" button to get the answer."'))
       
            data_viewer_column, chat_column = st.columns((1,0.6))

            with data_viewer_column:
                document_viewer_heading = _gettext('Document Viewer')
                st.markdown(f"<div class='section-headings'><b>{document_viewer_heading}</b></div>", unsafe_allow_html=True)
                st.markdown(f"")
                #if original_file[1] == 1:
                #    original_file = original_file[0]
                display_file(_gettext,original_file,file_type=option)

            with chat_column:
                chat_heading = _gettext('Ask your data queries here')
                st.markdown(f"<div class='section-headings'><b>{chat_heading}</b></div>", unsafe_allow_html=True)
                st.markdown(f"")
                # -----setup chatbot agent----- 
                # language selected by user 
                language_map ={'en':'ENGLISH','ja':'JAPANESE'}
                selected_language = language_map.get(st.session_state.lang,'en')
                #st.write("inside chat")
                #st.write(_file)
                model_selection = st.selectbox(_gettext('Select Model'),(_gettext('gpt-3.5-turbo'),_gettext('Llama-2-7b')),key='model_selected')
                if model_selection == 'gpt-3.5-turbo':
                    if option=='SQLITE_DB':
                        data_agent = get_data_agent(_file=_file, file_type=option, language=selected_language)
                    elif option in ['DOC','TXT','PDF']:
                        data_agent = get_data_agent(_file=_file, file_type=option, language=selected_language)
                    elif option not in ['DOC','TXT','PDF'] and option!='EXCEL':
                        data_agent = get_data_agent(_file=_file.copy(), file_type=option, language=selected_language)
                    elif option == 'EXCEL' and option_num_selected!=2:
                        data_agent = get_data_agent(_file=_file.copy(), file_type=option, language=selected_language)
                    elif option=='EXCEL' and option_num_selected==2:
                        data_agent = get_data_agent(_file = _file, file_type=option, language=selected_language,option_num_selected = 2)
                
                elif model_selection == 'Llama-2-7b':
                    if option in ['DOC','TXT','PDF']:
                        data_agent = get_data_agent2(_file=_file, file_type=option, language=selected_language)
                    elif option not in ['DOC','TXT','PDF'] and option!='EXCEL':
                        data_agent = get_data_agent2(_file=_file.copy(), file_type=option, language=selected_language)
                
                if st.session_state["authentication_status"] == None:
                    st.warning(_gettext('For your own queries, please login for chat functionality'))
                    
                def use_sample_question(selected_question): 
                    st.session_state.text_value = selected_question

                questions = []  
                if is_it_sample:
                    questions = sam_ques(option) 

                selected_question = st.selectbox(_gettext("Choose a sample question"), questions,key='q_select',
                    help=_gettext('Here few sample questions are provided in dropdown you can check that but if you want to ask your own questions, please login.'))
                if is_it_sample:
                    use_question = st.button(label=_gettext('Use question'),on_click=use_sample_question,args=(selected_question,),key='q_button')            
                # model_selection = st.selectbox(_gettext('Select Model'),(_gettext('gpt-3.5-turbo'),_gettext('Llama-2-7b')),key='model_selected')
                if not is_it_sample:
                    use_question = True
                with st.form(key='my_form',clear_on_submit=False):
                    input_text = st.text_input(_gettext('Chat with our LLM-Powered Agent'), value="", key='text_value')
                    submit = st.form_submit_button(label=_gettext('Get Answer'))

                clear_conversation(_gettext)

                input_text = st.session_state.text_value
                if (input_text and submit) or use_question:
                    #print('inside chat')
                    # get the entire chat history of the session
                    chat_history_payload = get_session_chat_history()
                    # add user input to chat history
                    #print(get_session_chat_history())
                    add_to_session_chat_history(chat_text= input_text,response_by='human')
                    
                    # get the entire chat history of the session
                    if is_it_sample and use_question:
                        #print('inside sample chat')
                        ans = sam_ans(input_text, option)
                        if '#' in ans:
                            ans, plot_path = ans.split('#')
                            st.image(plot_path, width=WIDTH_OF_PLOT)
                        response = {'message':ans}
                        # add llm response to session chat history
                        add_to_session_chat_history(chat_text= response['message'],response_by='ai')
                        

                    else:
                        print('inside sample chat')
                        if st.session_state['authentication_status']==True:
                            # get the llm response 
                            with st.spinner(_gettext('Generating your answer ✨')):
                                try:
                                    # response = {'message':_gettext('this is ai message place holder')} # for testing frontend ui
                                    # actual agent respone 
                                    if option in ['PDF','TXT','DOC']:
                                        if model_selection == 'gpt-3.5-turbo':
                                            vectordb = data_agent # data_agent as a proxy
                                            qa = ConversationalRetrievalChain.from_llm(
                                                ChatOpenAI(temperature=0, model_name='gpt-3.5-turbo'),
                                                retriever=vectordb.as_retriever(search_kwargs={'k': 6}),
                                                return_source_documents=True,
                                                verbose=False,
                                                )
                                            result = qa({"question": input_text, "chat_history": []})
                                            response = {'message':result['answer']}
                                        elif model_selection=='Llama-2-7b':
                                            # if 'key' not in st.session_state:
                                            #     st.session_state['key'] = 'value'
                                            print('1')
                                            vectordb = data_agent # data_agent as a proxy
                                            print('2')
                                            # Query against your own data
                                            # qa = ConversationalRetrievalChain.from_llm(llm = ChatAnyscale(temperature=0, model_name="meta-llama/Llama-2-7b-chat-hf"), retriever =vectordb.as_retriever(), return_source_documents=True)
                                            qa = ConversationalRetrievalChain.from_llm(
                                                ChatAnyscale(temperature=0, model_name=ANYSCALE_MODEL_NAME, ANYSCALE_API_KEY='esecret_yc3i77j2j72f2v78s3bdd6ab6g'),
                                                retriever=vectordb.as_retriever(search_kwargs={'k': 6}),
                                                return_source_documents=True,
                                                verbose=False,
                                                )
                                            print('3')
                                            result = qa({"question": input_text, "chat_history": []})
                                            print('4')
                                            response = {'message':result['answer']}

                                    elif (option in ['CSV','TSV']) or (option=='EXCEL' and option_num_selected==1):
                                        assistant_response = data_agent.chat(input_text, output_type='text')
                                        print('Output : ',assistant_response, type(assistant_response))
                                        if assistant_response is None:
                                            assistant_response = _gettext('This query does not require answer')
                                        if 'temp_chart.png' in os.listdir():
                                            assistant_response = _gettext('This query requires above plot')
                                            st.image('temp_chart.png', width=WIDTH_OF_PLOT)
                                            os.remove('temp_chart.png')

                                        response = {'message':assistant_response}
                                    #elif option=='EXCEL' and option_num_selected==1:
                                    #    assistant_response = data_agent.chat(input_text)
                                    #    response = {'message':assistant_response}    
                                    else:
                                        assistant_response = data_agent.run(input_text)
                                        response = {'message':assistant_response}
                                    add_to_session_chat_history(chat_text= response['message'],response_by='ai')
                                except Exception as e :
                                    print("Error : ", e)
                                    response = {'message':_gettext('Something went wrong! Not able to find anything. Please ask another question.')}
                                    add_to_session_chat_history(chat_text= response['message'],response_by='ai')
                            
                    # Display the entire conversation on the frontend
                    display_conversation(st.session_state.conversation_history)
    st.markdown(
    """<style>
        div[class*="Selectbox"] > label > div[data-testid="stMarkdownContainer"] > p {
            font-size:18px;
            font-weight:bold;
        }
    </style>
    """, unsafe_allow_html=True)

    st.markdown(
    """<style>
        div[class*="stFileUploader"] > label > div[data-testid="stMarkdownContainer"] > p {
            font-size:18px;
            font-weight:bold;
        }
    </style>
    """, unsafe_allow_html=True)
    st.markdown(
        """<style>
            div[class*="stRadio"] > label > div[data-testid="stMarkdownContainer"] > p {
                font-weight: bold;
                font-size:18px;
            }
        </style>
        """, unsafe_allow_html=True)
    st.markdown(
        """<style>
            div[class*="stTextInput"] > label > div[data-testid="stMarkdownContainer"] > p {
                font-weight: bold;
                font-size:18px;
            }
        </style>
        """, unsafe_allow_html=True)

    button_style = """
        <style>
            div.stButton > button:first-child {
                display: inline-block;
                padding: 10px 20px;
                margin: 10px 0;
                
                background-color: #0a4e8d; /* Green background */
                color: white; /* White text */
                border: none;
                cursor: pointer;
                font-size: 18px;
                transition: background-color 0.3s, box-shadow 0.3s;
            }
            div.stButton > button:first-child:hover {
                
                background-color: #00008b; /* Darker green on hover */
                box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
            }
        </style>
        """
    st.markdown(button_style, unsafe_allow_html=True)
    
def exists_in_q(q, to_check):
    pointer = -1
    for ind, val in enumerate(q):
        if val[0] == to_check[0] and val[1] == to_check[1] and val[2]==to_check[2]:
            return ind
    else:
        return pointer