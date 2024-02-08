import os
from dotenv import load_dotenv
import openai
import streamlit as st

import pinecone
from llama_index import GPTVectorStoreIndex, SimpleDirectoryReader, QuestionAnswerPrompt, StorageContext
from llama_index.vector_stores import PineconeVectorStore


load_dotenv()


#-----environment initalisation-----------

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
os.environ['OPENAI_API_KEY'] = OPENAI_API_KEY
Pinecone_API_KEY = os.getenv('Pinecone_API_KEY')
Pinecone_ENVIRONMENT = os.getenv('Pinecone_ENVIRONMENT')

openai.api_key= OPENAI_API_KEY

@st.cache_resource
def document_reader(directory_path: str):
    return SimpleDirectoryReader(directory_path).load_data()


def create_pinecone_index():

    # Initialize Pinecone 
    pinecone.init(api_key=Pinecone_API_KEY, environment=Pinecone_ENVIRONMENT)
    print('pinecone initalised')

    # Create the index if not already created. (It expires after 7 days usage)
    # You can create index online or offline once it is created need not to run another time
    if not pinecone.Index("test-12"):
        pinecone.create_index("test-12", dimension=1536, metric="euclidean", pod_type="p1")
        print('No index foudn, creating new index')
    else:
        print('Index already exists')


    # construct vector store and customize storage context
    storage_context = StorageContext.from_defaults(
        vector_store = PineconeVectorStore(pinecone.Index("test-12"))
    )
    print('storage context created!')

    # Load documents and build index
    index = GPTVectorStoreIndex.from_documents(document_reader('data'), storage_context=storage_context)
    
    return index

#import streamlit as st
@st.cache_resource
def setup_insurance_agent():
    #st.write('inside setup')
    index = create_pinecone_index()
    print('created index succesfully!')
    QA_PROMPT_TMPL = (
        "We have provided context information below. \n"
        "---------------------\n"
        "{context_str}"
        "\n---------------------\n"
        "Given this information,  with no previous knowledge, please answer the question only from context: {query_str}\n"
    )

    # Create wrapper for QA prompt
    QA_PROMPT = QuestionAnswerPrompt(QA_PROMPT_TMPL)

    query_engine = index.as_query_engine(
        text_qa_template=QA_PROMPT
    )
    
    print('created query engine!')

    return query_engine


if __name__ == "__main__":
    
    
    insurance_agent = setup_insurance_agent()
    #General greetings
    response = insurance_agent.query("Good morning !")
    print(response)
    # response = insurance_agent.query("How are you doing?")
    # print(response)

    # #in context
    # response = insurance_agent.query("How is IDV determined?")
    # print(response)

    # response = insurance_agent.query("How to address any grievance?")
    # print(response)

    # response = insurance_agent.query('What is personal accident cover for owner driver?')
    # print(response)

    # #out of context
    # response = insurance_agent.query("What is quantum mechanics?")
    # print(response)

    # response = insurance_agent.query("How many players play football?")
    # print(response)
