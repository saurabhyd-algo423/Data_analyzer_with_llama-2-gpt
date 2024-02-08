
import streamlit as st
#from utils.load import load_lottiefile
from utils.design_utils import create_featurecard,create_specific_feature
from utils.load import load_base64_image





def hompage_content(_gettext):
    #-------App name-----------------------
    with st.container():
            
        base64_image= load_base64_image("ui_assets/images/481921111_blur.png")    
        background_image = f"data:image/png;base64,{base64_image}"
        
        col1,col2,col3 = st.columns((1,3,1))
        with col2:
            pass
        
        app_name = _gettext("Interactive Data Analyser")
        tag_line = _gettext("Analyze your data in a live interactive manner")
        features = [_gettext('Ask queries to your CSV, TSV, EXCEL files in natural language.'),
                    _gettext('Plot graphs from data. '),
                    _gettext('Analyse textual data in different formats such as PDFs, TXT and DOC files.'),
                    _gettext('Work with multiple sheets in excel. Analyse it as dataframes or use it as a database.'),
                    _gettext('No need to write SQL queries, just upload your sqlite database file and chat naturally.')]
        #description = _gettext("With this interactive analyser, you can analyse different kinds of files such as CSV, TSV, EXCEL, SQL, PDF, DOC, TEXT, JSON. Plot graphs in CSV, write SQL queries in natural language, chat with your data are the key features.")
        st.markdown(
                f"""
                <div class="background1">
                <div class="title">{app_name}</div>
                <div class="subtitle">{tag_line}</div>
                </div>
                                <style>
                    .background1{{
                        background-image: url({background_image});

                        background-position: cover;
                        
                        height: 50vh;
                        display: flex;
                        flex-direction: column;
                        justify-content: center;
                        align-items: center; 
                         
                     }} 
                <style>  
                """,unsafe_allow_html=True)
        
    #----------High Level description of the app --------------------
    with st.container():
        col1, col2, col3 = st.columns((1,1.9,1))
        with col2:
             
            general_question = _gettext("Tired of writing code to analyze data files?")
            #general_description =_gettext("Meet our LLM-powered chatbot! Get quick answers about your data files, Just upload your format, and our AI interprets and responds accurately")
            st.markdown(f"""
                        <div class='appDescriptioncontainer'>
                            <div class =textHeading>
                                {general_question}
                            </div>
                            <br>
                            <br>
                            <div class=>
                                <ul>
                                    <li class='description_v2'>{features[0]}</li>
                                    <li class='description_v2'>{features[1]}</li>
                                    <li class='description_v2'>{features[2]}</li>
                                    <li class='description_v2'>{features[3]}</li>
                                    <li class='description_v2'>{features[4]}</li>
                                </ul>
                            </div>
                
                            
                        </div>
                        
                        
                        
                        """,unsafe_allow_html=True)
            
            #-------Add Illustrations----------
            #insurance_illustration_base64 = load_base64_image('./ui_assets/images/home_page-small.PNG')
            #travel_illustration = f"data:image/jpeg;base64,{travel_illustration_base64}"
            
            #insurance_illustration_tag = f'<img src="data:image/jpeg;base64,{insurance_illustration_base64}" width="400" align="center">'
            # Display the image using st.markdown()
            #st.markdown(insurance_illustration_tag, unsafe_allow_html=True)
            
        st.divider()

   #------------Explicit Feature Description----------------------
    feature1 = _gettext('Intelligent Data Processing')
    description1 = _gettext("Say goodbye to writing complex data processing and analysis code! Our state-of-the-art analyzer chatbot adeptly deciphers queries and seamlessly conducts data processing. Thanks to its natural language query capability, you can now wave goodbye to concerns over syntax errors and the tiresome quest for online solutions.")
    image_path1='./ui_assets/images/document_scan_image_small.jpg'           
    create_specific_feature(feature1, description1,lottie_image=False,image_path=image_path1,image_present=True)
    
    feature2 = _gettext('Precise Responses')
    description2 = _gettext("No need for extensive explanations. Our chatbot delivers responses with utmost precision and clarity, skillfully distilling intricate information into easily digestible summaries. It not only furnishes swift and precise answers but also trims down the time invested in exploratory data analysis.")
    image_path2='./ui_assets/images/document_summary_small.jpg'           
    create_specific_feature(feature2, description2,lottie_image=False,image_path=image_path2,image_present=True,image_right_side=False)
    
    feature3 = _gettext('Contextually Aware')
    description3 = _gettext("Our chatbot possesses the intelligence to discern questions that diverge from context or demand additional information. It actively partakes in interactive dialogues, skillfully directing users to furnish the essential particulars for precise responses. This guarantees that each interaction bears fruit and carries substantial meaning.")
    image_path3='./ui_assets/images/contexually aware.png'           
    create_specific_feature(feature3, description3,lottie_image=False,image_path=image_path3,image_present=True)
    
    #st.divider()
    
    #-----------contact us section-------------------------
    '''
    with st.container():
        
        st.markdown(f"""
                    <div class='appDescriptioncontainer'>
                    <h4 style="text-align:center;
                                color: #635F5F;
                                font-size:30px;
                                font-weight:normal
                                ">
                        {_gettext("For more information please contact us at")} 
                        <a href="mailto:info@algoanalytics.com" style="color: #789be6;">info@algoanalytics.com</a>
                        </h4>
                        
                    </div>
                    
                    """,unsafe_allow_html=True)
    '''
            
        

