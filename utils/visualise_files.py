import streamlit as st 
import base64

from utils.load import displayPDF,load_base64_image

def display_file(_gettext,file,file_type):
    
    #file_type_mappings = {'CSV':['csv'],'TSV':['tsv'],'EXCEL':['xls','xlsx'],
    #                         'TXT':['txt'],'DOC':['doc'],'PDF':['pdf'],'JSON':['json']}
    
    if file_type in ['CSV','TSV']:
        st.dataframe(file)
    elif file_type=='EXCEL':
        option_num_selected = file[1]
        if option_num_selected==1:
            file_ = file[0]
            sheet_options = [i+1 for i in range(len(file_))]
            sheet_to_vizualize = st.selectbox(_gettext('Which sheet number you would like to see ? '), sheet_options, 
                help=_gettext("Choose the sheet number you want to see as a tabular format."))
            st.dataframe(file_[sheet_to_vizualize-1])
        elif option_num_selected==2:
            st.text(_gettext("Using excel as a database now. Therefore nothing to display."))
    elif file_type=='SQLITE_DB':
        st.text(_gettext("Using SQLITE database currently."))

    
    elif file_type in ['PDF']:
        #document = file[1]
        #st.text(document[0].page_content)
        height=1000
        with open(file, "rb") as f:
            base64_pdf = base64.b64encode(f.read()).decode('utf-8')

        # Embedding PDF in HTML
        pdf_display = F'<embed src="data:application/pdf;base64,{base64_pdf}" width=100% height="{height}" type="application/pdf">'
        #pdf_display = F'<div><iframe src="data:application/pdf;base64,{base64_pdf}" type="application/pdf" width: 100%;></iframe></div>'

        # Displaying File
        st.markdown(pdf_display, unsafe_allow_html=True)

    elif file_type in ['DOC','TXT']:
        document = file[0]
        st.text(document.page_content)
    
    elif file_type=='JSON':
        st.json(file)
    
# def display_file(_gettext, file, file_type):
#     if file is not None:
#         if file_type in ['CSV', 'TSV']:
#             st.dataframe(file)
#         elif file_type == 'EXCEL':
#             option_num_selected = file[1]
#             if option_num_selected == 1:
#                 file_ = file[0]
#                 sheet_options = [i + 1 for i in range(len(file_))]
#                 sheet_to_visualize = st.selectbox(_gettext('Which sheet number you would like to see ? '), sheet_options,
#                                                   help=_gettext("Choose the sheet number you want to see as a tabular format."))
#                 st.dataframe(file_[sheet_to_visualize - 1])
#             elif option_num_selected == 2:
#                 st.text(_gettext("Using excel as a database now. Therefore nothing to display."))
#         elif file_type == 'SQLITE_DB':
#             st.text(_gettext("Using SQLITE database currently."))
#         elif file_type in ['PDF']:
#             height = 1000
#             with open(file, "rb") as f:
#                 base64_pdf = base64.b64encode(f.read()).decode('utf-8')

#             # Embedding PDF in HTML
#             pdf_display = F'<embed src="data:application/pdf;base64,{base64_pdf}" width=100% height="{height}" type="application/pdf">'
#             st.markdown(pdf_display, unsafe_allow_html=True)
#         elif file_type in ['DOC', 'TXT']:
#             document = file[0]
#             st.text(document.page_content)
#     else:
#         st.text("File is None")

def show_data_resources(_gettext):
    
    col1, col2, col3 = st.columns((1.5,1.5,0.8))
    
    with col1:
        st.info(_gettext('Travel Document : Chennai Tour Guide '))
        pdf_file_path = "data/sample_data_ui/Chennai-Ebrochure-sample.pdf"
        displayPDF(pdf_file_path)
        
        
    with col2:
        st.info(_gettext('SQL Database: Hotels Information'))
        conn = st.experimental_connection(
        "local_db",
        type="sql",
        url="sqlite:///data/sharks.db"
            )
        
        
        #st.write('Hotels data')
        #col_names = "'hotel_id', 'name', 'city', 'hotel_type', 'hotel_star_rating', 'uniq_id', 'crawl_timestamp', 'pageurl', 'name', 'hotel_id', 'area', 'city', 'address', 'lat', 'long', 'amenities', 'hotel_star_rating', 'hotel_type', 'review_count', 'average_rating', 'photo_count', 'cleanliness', 'facilities', 'location', 'staff', 'wifi', 'comfort', 'value_for_money', 'extra_adult_rate', 'extra_child_rate'"
        #query1 = f"select {col_names} from hotel_info limit 20"
        query1 = "select name as hotel_name,city,hotel_type,hotel_star_rating,\
            value_for_money,average_rating,cleanliness\
        from hotel_info limit 20"
        df1 = conn.query(query1)
        st.dataframe(df1)
        
        
        # flights 
        query2 = "select * from "
        
        

        
    with col3:
        st.info(_gettext('Web search : Google search API'))
        
        # serpapi
        
        serp_base64 = load_base64_image('data/sample_data_ui/serpapi-logo.png')
        serp_tag = f'<img src="data:image/png;base64,{serp_base64}" width=100%>'
        # Display the image using st.markdown()
        st.markdown(serp_tag, unsafe_allow_html=True)
        
        
        websearch_base64 = load_base64_image('data/sample_data_ui/search_image.jpg')          
        websearch_tag = f'<img src="data:image/jpeg;base64,{websearch_base64}" width=100%>'
        # Display the image using st.markdown()
        st.markdown(websearch_tag, unsafe_allow_html=True)
