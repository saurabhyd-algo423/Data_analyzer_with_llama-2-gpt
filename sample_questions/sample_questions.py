import streamlit as st
def sam_ques(file_type):
    lang = st.session_state.lang 
    if file_type=='CSV':
        if lang=='en':
            with open('./sample_questions/csv.txt', 'r') as f:
                questions = list(f.readlines())
        else:
            with open('./sample_questions/csv_ja.txt', 'r', encoding="utf8") as f:
                questions = list(f.readlines())
    elif file_type=='TSV':
        if lang=='en':
            with open('./sample_questions/tsv.txt', 'r') as f:
                questions = list(f.readlines())
        else:
            with open('./sample_questions/tsv_ja.txt', 'r', encoding="utf8") as f:
                questions = list(f.readlines())
    elif file_type=='EXCEL':
        if lang=='en':
            with open('./sample_questions/excel.txt', 'r') as f:
                questions = list(f.readlines())
        else:
            with open('./sample_questions/excel_ja.txt', 'r', encoding="utf8") as f:
                questions = list(f.readlines())
    elif file_type=='TXT':
        if lang=='en':
            with open('./sample_questions/text.txt', 'r') as f:
                questions = list(f.readlines())
        else:
            with open('./sample_questions/text_ja.txt', 'r', encoding="utf8") as f:
                questions = list(f.readlines())
    elif file_type=='DOC':
        if lang=='en':
            with open('./sample_questions/docs.txt', 'r') as f:
                questions = list(f.readlines())
        else:
            with open('./sample_questions/docs_ja.txt', 'r', encoding="utf8") as f:
                questions = list(f.readlines())
    elif file_type=='PDF':
        if lang=='en':
            with open('./sample_questions/pdf.txt', 'r') as f:
                questions = list(f.readlines())
        else:
            with open('./sample_questions/pdf_ja.txt', 'r', encoding="utf8") as f:
                questions = list(f.readlines())
    elif file_type=='JSON':
        if lang=='en':
            with open('./sample_questions/json.txt', 'r') as f:
                questions = list(f.readlines())
        else:
            with open('./sample_questions/json_ja.txt', 'r', encoding="utf8") as f:
                questions = list(f.readlines())

    elif file_type=='SQLITE_DB':
        if lang=='en':
            with open('./sample_questions/sqlite.txt', 'r') as f:
                questions = list(f.readlines())
        else:
            with open('./sample_questions/sqlite_ja.txt', 'r', encoding="utf8") as f:
                questions = list(f.readlines())

    return questions

