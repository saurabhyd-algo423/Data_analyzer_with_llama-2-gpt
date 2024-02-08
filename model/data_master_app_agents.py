import pandas as pd 
import streamlit as st 
#from langchain_experimental.agents.agent_toolkits.pandas.base import create_pandas_dataframe_agent
from langchain.agents import create_json_agent
from auth.authenthication import setup_authenticator
from langchain.llms import OpenAI
from dotenv import load_dotenv
# from secret_key import key


from langchain.llms import OpenAI
from langchain.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain
from langchain.tools import Tool
from langchain.agents import load_tools
from langchain.agents.agent_toolkits import JsonToolkit
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma

import openai
import os

from pandasai import PandasAI
from pandasai.llm.openai import OpenAI as oai
from pandasai.middlewares.streamlit import StreamlitMiddleware
from pandasai import SmartDatalake
from langchain.chat_models import ChatAnyscale

#from langchain.llms import Anyscale
#from model.insurance_faq_llama_agent import setup_insurance_agent


# Initialize environment variables
load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
openai.api_key = OPENAI_API_KEY
#ANYSCALE_MODEL_NAME = 'meta-llama/Llama-2-7b-chat-hf'

ANYSCALE_API_KEY=os.getenv('ANYSCALE_API_KEY')
os.environ["ANYSCALE_API_BASE"]='https://api.endpoints.anyscale.com/v1'
os.environ['ANYSCALE_API_KEY']=ANYSCALE_API_KEY
#ANYSCALE_MODEL_NAME="codellama/CodeLlama-34b-Instruct-hf"
ANYSCALE_MODEL_NAME="meta-llama/Llama-2-7b-chat-hf"

def get_data_agent(_file,file_type,language,option_num_selected = None):
    prompt_prefix = f"""Use only {language} language to reply"""
    agent = None
    if file_type in ['CSV','TSV']:
        llm = oai()
        #ANYSCALE_MODEL_NAME = 'meta-llama/Llama-2-7b-chat-hf'
        
        #llama2_llm = Anyscale(model_name = ANYSCALE_MODEL_NAME)
        agent = SmartDatalake([_file], config={"llm": llm})
        #agent = create_pandas_dataframe_agent(
            #           OpenAI(temperature=0), 
            #            _file, 
            #            verbose=True,
            #            prefix=prompt_prefix,
            #            max_iterations=4
            #            )
        

    elif file_type=='EXCEL':
        print('dd1')
        if option_num_selected == 2:
            db = SQLDatabase.from_uri("sqlite:///./sqlite_db.db")
            llm = OpenAI(temperature=0, verbose=True)
            agent = SQLDatabaseChain.from_llm(llm, db, verbose=True)
        else:
            llm = oai()
            agent = SmartDatalake(_file, config={"llm": llm})


    elif file_type =='SQLITE_DB':
        llm = OpenAI(temperature=0, verbose=True)
        #ANYSCALE_MODEL_NAME = 'meta-llama/Llama-2-7b-chat-hf'
        
        #llama2_llm = Anyscale(model_name = ANYSCALE_MODEL_NAME)
        agent = SQLDatabaseChain.from_llm(llm, _file, verbose=True)

    elif file_type in ['PDF','TXT','DOC']:
        #st.write(_file)
        '''
        st.write('check_py')

        result = qa({"question": "what is the amount mentioned", "chat_history": []})
        st.write(result["answer"])
        '''
        #st.write("sssssssssssssssssssssssssssssss",type(qa))
        agent = _file # vectordb
        
    
    elif file_type=='JSON':
        #st.write(_file)
        agent = create_json_agent(
                        llm=OpenAI(temperature=0),
                        prefix=prompt_prefix,
                        toolkit=_file,
                        verbose=True,
                        max_iterations=4
                        )
        
    return agent


def get_data_agent2(_file,file_type,language,option_num_selected = None):
    prompt_prefix = f"""Use only {language} language to reply"""
    agent = None
    if file_type in ['CSV','TSV']:
        llm = oai()
        # llm  = ChatAnyscale(model_name=ANYSCALE_MODEL_NAME,temperature=0.0)
        #ANYSCALE_MODEL_NAME = 'meta-llama/Llama-2-7b-chat-hf'
        
        #llama2_llm = Anyscale(model_name = ANYSCALE_MODEL_NAME)
        agent = SmartDatalake([_file], config={"llm": llm})
        #agent = create_pandas_dataframe_agent(
            #           OpenAI(temperature=0), 
            #            _file, 
            #            verbose=True,
            #            prefix=prompt_prefix,
            #            max_iterations=4
            #            )
        

    elif file_type=='EXCEL':
        print('dd1')
        if option_num_selected == 2:
            db = SQLDatabase.from_uri("sqlite:///./sqlite_db.db")
            llm = ChatAnyscale(model_name=ANYSCALE_MODEL_NAME,temperature=0.0, verbose=True)
            agent = SQLDatabaseChain.from_llm(llm, db, verbose=True)
        else:
            llm = oai()
            agent = SmartDatalake(_file, config={"llm": llm})


    elif file_type =='SQLITE_DB':
        llm = ChatAnyscale(model_name=ANYSCALE_MODEL_NAME,temperature=0.0, verbose=True)
        #ANYSCALE_MODEL_NAME = 'meta-llama/Llama-2-7b-chat-hf'
        
        #llama2_llm = Anyscale(model_name = ANYSCALE_MODEL_NAME)
        agent = SQLDatabaseChain.from_llm(llm, _file, verbose=True)

    elif file_type in ['PDF','TXT','DOC']:
        #st.write(_file)
        '''
        st.write('check_py')

        result = qa({"question": "what is the amount mentioned", "chat_history": []})
        st.write(result["answer"])
        '''
        #st.write("sssssssssssssssssssssssssssssss",type(qa))
        agent = _file # vectordb
        
    
    elif file_type=='JSON':
        #st.write(_file)
        agent = create_json_agent(
                        llm=ChatAnyscale(model_name=ANYSCALE_MODEL_NAME,temperature=0.0),
                        prefix=prompt_prefix,
                        toolkit=_file,
                        verbose=True,
                        max_iterations=4
                        )
        
    return agent