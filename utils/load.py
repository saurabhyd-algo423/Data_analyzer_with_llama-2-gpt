from typing import Any, Dict
from pathlib import Path
import json
import base64
import os
import yaml
import shutil
from yaml.loader import SafeLoader
from .file_type_specific import excel_df_reader, json_dict_loader
from langchain.document_loaders import PyPDFLoader
from langchain.document_loaders import Docx2txtLoader
from langchain.document_loaders import TextLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain.vectorstores import Chroma
from langchain.utilities import SQLDatabase

import streamlit as st
import toml

import pandas as pd 




#@st.cache(allow_output_mutation=True, ttl=300)
def get_project_root() -> str:
    """Returns project root path.

    Returns
    -------
    str
        Project root path.
    """
    return str(Path(__file__).parent.parent)

def load_auth_config(auth_config: str) -> Dict[Any, Any]:
    """Loads auth configuration file.

    Parameters
    ----------
    auth_config : str
        Filename of auth configuration file.

    Returns
    -------
    dict
        auth configuration file.
    """   
    file_path = Path(get_project_root()) / f"config/{auth_config}"
    with file_path.open() as file:
        config = yaml.load(file, Loader=SafeLoader)
    return config

def load_config(
    config_streamlit_filename: str) -> Dict[Any, Any]:
    """Loads configuration files.

    Parameters
    ----------
    config_streamlit_filename : str
        Filename of lib configuration file.

    Returns
    -------
    dict
        Lib configuration file.
    """
    config_streamlit = toml.load(Path(get_project_root()) / f"config/{config_streamlit_filename}")
    return dict(config_streamlit)

# get key metrics data
def get_key_metrics_data(news_for):
    file_path_stats_valuation = f"data/stats_valuation_data/{news_for}.json"
    with open(file_path_stats_valuation, "r") as json_file:
        key_metrics_data = json.load(json_file)
    return key_metrics_data


# if __name__ == '__main__':
#     print(load_config("config_streamlit.toml"))

# load lottie files
@st.cache_resource 
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)
    
@st.cache_resource    
def load_base64_image(image_path):
    with open(image_path, "rb") as img_file:
            base64_image = base64.b64encode(img_file.read()).decode()
            
    return base64_image


@st.cache_data
def displayPDF(file,width=700,height=750):
    # Opening file from file path
    with open(file, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')

    # Embedding PDF in HTML
    pdf_display = F'<embed src="data:application/pdf;base64,{base64_pdf}" width=100% height="{height}" type="application/pdf">'
    #pdf_display = F'<div><iframe src="data:application/pdf;base64,{base64_pdf}" type="application/pdf" width: 100%;></iframe></div>'

    # Displaying File
    st.markdown(pdf_display, unsafe_allow_html=True)
    

def write_binary(uploaded_file):
    try:
        shutil.rmtree('./temp_data')
    except:
        pass
    if not os.path.exists('temp_data'):
        os.mkdir('temp_data')

    with open(os.path.join("temp_data",uploaded_file.name),"wb") as f:
        f.write(uploaded_file.getbuffer())

def load_sample_file(_gettext,file_type,next_step = None):
    sample_file = None
    path_ = None
    if file_type=='CSV':

        sample_file = pd.read_csv('./sample_datasets/tesla-stock-price.csv',sep=',')
        path_ = sample_file
    
    elif file_type=='TSV':
        sample_file = pd.read_csv('./sample_datasets/tesla-stock-price.tsv',sep='\t')
        path_ = sample_file

    elif file_type=='EXCEL':
        # excel_df_reader returns a list of dataframes and option selected
        # in case option selected is 2, list of dataframes will be None
        sample_file, option_num_selected  = excel_df_reader(_gettext,file_path = './sample_datasets/Tesla_Amazon_stock_price.xlsx',next_step=next_step)
        if option_num_selected==1:
            path_ = (sample_file,1)
        elif option_num_selected==2:
            path_ = (None,2) 



    elif file_type=='SQLITE_DB':
        sample_file = SQLDatabase.from_uri("sqlite:///./sample_datasets/chinook.db")
        path_ = sample_file
    
    elif file_type in ['PDF','DOC','TXT']:
        documents = []
        try:
            if file_type == 'PDF':
                pdf_path = "./sample_datasets/Bill_Paid_Reciept.pdf"
                loader = PyPDFLoader(pdf_path)
                documents.extend(loader.load())
                vectordb = Chroma.from_documents(documents, embedding=OpenAIEmbeddings(), persist_directory="./embeddings/pdf_embeddings")
                vectordb.persist()  
                path_ = pdf_path
            elif file_type == 'DOC':
                doc_path = "./sample_datasets/Gold_investment.docx"
                loader = Docx2txtLoader(doc_path)
                documents.extend(loader.load())
                vectordb = Chroma.from_documents(documents, embedding=OpenAIEmbeddings(), persist_directory="./embeddings/doc_embeddings")
                vectordb.persist()
                path_ = documents 
            elif file_type == 'TXT':
                text_path = "./sample_datasets/Nifty_50_Wikipedia.txt"
                loader = TextLoader(text_path)
                documents.extend(loader.load())
                vectordb = Chroma.from_documents(documents, embedding=OpenAIEmbeddings(), persist_directory="./embeddings/txt_embeddings")
                vectordb.persist() 
                path_ = documents

            sample_file = vectordb
        except:
            st.write(_gettext('File format is incorrect.'))

    
    elif file_type=='JSON':
        path = './sample_datasets/Quiz.json'
        sample_file,path_ = json_dict_loader(_gettext, path)
        
    return (sample_file,path_) # in case of csv it will be a dataframe


def get_uploaded_file(_gettext,uploaded_file,file_type,next_step):
    #file = None
    if file_type=='CSV':
        to_return = pd.read_csv(uploaded_file,sep=',')
        path_ = to_return
    
    elif file_type=='TSV':
        to_return = pd.read_csv(uploaded_file,sep='\t')
        path_ = to_return
    
    elif file_type=='EXCEL':
        write_binary(uploaded_file)
        filename = uploaded_file.name
        to_return, option_num_selected = excel_df_reader(_gettext,file_path="./temp_data/" + filename,next_step = next_step)
        #to_return, path_ = load_sample_file(_gettext,file_type='EXCEL', excel_file_path = "./temp_data/" + filename)
        if option_num_selected==1:
            path_ = (to_return,1)
        elif option_num_selected==2:
            path_ = (None,2) 

    elif file_type=='SQLITE_DB':
        write_binary(uploaded_file)
        filename = uploaded_file.name
        to_return = SQLDatabase.from_uri("sqlite:///./temp_data/" + filename)
        path_ = to_return
    
    elif file_type in ['PDF','DOC','TXT']:
        write_binary(uploaded_file)
        filename = uploaded_file.name 
        documents = []
        if filename.endswith(".pdf"):
            pdf_path = "./temp_data/" + filename
            loader = PyPDFLoader(pdf_path)
            documents.extend(loader.load())
            vectordb = Chroma.from_documents(documents, embedding=OpenAIEmbeddings())
            #vectordb.persist()  
            path_ = pdf_path
        elif filename.endswith('.docx') or filename.endswith('.doc'):
            doc_path = "./temp_data/" + filename
            loader = TextLoader(doc_path)
            documents.extend(loader.load())
            vectordb = Chroma.from_documents(documents, embedding=OpenAIEmbeddings())
            #vectordb.persist() 
            path_ = pdf_path
        elif filename.endswith('.txt'):
            text_path = "./temp_data/" + filename
            loader = TextLoader(text_path)
            documents.extend(loader.load())
            vectordb = Chroma.from_documents(documents, embedding=OpenAIEmbeddings())
            #vectordb.persist() 
            path_ = pdf_path

        to_return=vectordb
    
    elif file_type=='JSON':
        write_binary(uploaded_file)
        with open(os.path.join("temp_data",uploaded_file.name),"wb") as f:
            f.write(uploaded_file.getbuffer())
        path_ = './temp_data/'+uploaded_file.name

        to_return = json_dict_loader(_gettext, path)
        
    return to_return, path_

@st.cache_data
def custom_footer(_gettext):
    st.markdown("---")
    view_info = _gettext('For the best experience, use a competible browser and view at 1280x720 resolution.')
    rights_info = _gettext('2023 AlgoAnalytics, All rights reserved.')
    About = _gettext(' About ')
    Services = _gettext(' Services ')
    Contact = _gettext(' Contact ')
    st.markdown(f"""
    <style>
        body {{
             /* Ensure the body is relatively positioned */
            margin-bottom: 0px; /* Adjust this value to match the desired footer height */
        }}
        .footer-container {{
            position: absolute;
            bottom: 0;
            width: 100%;
            margin-bottom: 10px; /* Adjust this value to move the footer up */
            background-color: #f9f9f9;
            color: #6c757d;
            font-family: 'Arial', sans-serif;
            padding: 20px 20px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            font-size: 11px;
            border-bottom: 1px solid #d3d3d3;
        }}


        .footer-main-content {{
            display: flex;
            align-items: center;
            gap: 10px; /* Maintain a small gap between items */
        }}

        .footer-logo {{
            font-weight: bold;
            color: #007bff; /* Brand color for the logo */
            font-size: 14px; /* Increase font size for the logo */
        }}

        .footer-link {{
            color: #007bff;
            text-decoration: none;
            transition: color 0.2s ease-in-out;
        }}

        .footer-link:hover {{
            text-decoration: underline;
            color: #0056b3; /* A shade darker on hover for contrast */
        }}

        .footer-link.active {{
            color: #0056b3; /* Highlight color for active link */
        }}

        .footer-instruction {{
        padding: 5px 10px;
        background: linear-gradient(135deg, #e9ecef, #cfd9e1);
        color: #495057;
        font-size: 12px;
        margin: 0;
        border: 1px solid #cfd9e1;
        border-radius: 5px;
        text-align: center;
        box-shadow: 0 1px 2px rgba(0, 0, 0, 0.05);
        line-height: 1.5;
        font-weight: bold;
        display: inline-block; /* Make it inline-block */
        width: auto; /* Let it adjust to the content width */
    }}





        /* Responsive adjustments for smaller screens */
        @media (max-width: 576px) {{
            .footer-container {{
                flex-direction: column; /* Stack elements vertically */
                gap: 5px; /* Space between stacked elements */
            }}

            .footer-main-content {{
                flex-direction: column;
                align-items: center;
            }}

            .footer-instruction {{
                order: 1; /* Instruction part comes first */
                width: 100%; /* Full width for visibility */
                margin: 8px 0; /* Increased margin for visual separation */
            }}

            .footer-logo, .footer-link {{
                font-size: 11px; /* Slightly smaller font size on mobile */
            }}
        }}
    </style>

    <div class="footer-container">
        <div class="footer-main-content">
            <div class="footer-logo">AlgoAnalytics</div>
            <a href="https://www.algoanalytics.com/about" target="_blank" class="footer-link">{About}</a>
            <a href="https://www.algoanalytics.com/services" target="_blank" class="footer-link">{Services}</a>
            <a href="https://www.algoanalytics.com/contact" target="_blank" class="footer-link active">{Contact}</a>
        </div>
        <div class="footer-instruction">
            {view_info}
        </div>
        <div>
            &copy; {rights_info}
        </div>
    </div>




    """,unsafe_allow_html=True)

