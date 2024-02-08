import streamlit as st

def sam_ans(que, file_type):
    ans = None
    lang = st.session_state.lang
    if file_type=='CSV':
        if lang=='en':
            with open('./sample_questions/csv.txt', 'r') as f:
                questions = list(f.readlines())
            with open('./sample_questions/answers/csv.txt', 'r') as f:
                answers = list(f.readlines())
        else:
            with open('./sample_questions/csv_ja.txt', 'r', encoding="utf8") as f:
                questions = list(f.readlines())
            with open('./sample_questions/answers/csv_ja.txt', 'r', encoding="utf8") as f:
                answers = list(f.readlines())
    elif file_type=='TSV':
        if lang=='en':
            with open('./sample_questions/tsv.txt', 'r') as f:
                questions = list(f.readlines())
            with open('./sample_questions/answers/tsv.txt', 'r') as f:
                answers = list(f.readlines())
        else:
            with open('./sample_questions/tsv_ja.txt', 'r', encoding="utf8") as f:
                questions = list(f.readlines())
            with open('./sample_questions/answers/tsv_ja.txt', 'r', encoding="utf8") as f:
                answers = list(f.readlines())
    elif file_type=='EXCEL':
        if lang=='en':
            with open('./sample_questions/excel.txt', 'r') as f:
                questions = list(f.readlines())
            with open('./sample_questions/answers/excel.txt', 'r') as f:
                answers = list(f.readlines())
        else:
            with open('./sample_questions/excel_ja.txt', 'r', encoding="utf8") as f:
                questions = list(f.readlines())
            with open('./sample_questions/answers/excel_ja.txt', 'r', encoding="utf8") as f:
                answers = list(f.readlines())
    elif file_type=='TXT':
        if lang=='en':
            with open('./sample_questions/text.txt', 'r') as f:
                questions = list(f.readlines())
            with open('./sample_questions/answers/text.txt', 'r') as f:
                answers = list(f.readlines())
        else:
            with open('./sample_questions/text.txt_ja', 'r', encoding="utf8") as f:
                questions = list(f.readlines())
            with open('./sample_questions/answers/text_ja.txt', 'r', encoding="utf8") as f:
                answers = list(f.readlines())
    elif file_type=='DOC':
        if lang=='en':
            with open('./sample_questions/docs.txt', 'r') as f:
                questions = list(f.readlines())
            with open('./sample_questions/answers/docs.txt', 'r') as f:
                answers = list(f.readlines())
        else:
            with open('./sample_questions/docs_ja.txt', 'r', encoding="utf8") as f:
                questions = list(f.readlines())
            with open('./sample_questions/answers/docs_ja.txt', 'r', encoding="utf8") as f:
                answers = list(f.readlines())
    elif file_type=='PDF':
        if lang=='en':
            with open('./sample_questions/pdf.txt', 'r') as f:
                questions = list(f.readlines())
            with open('./sample_questions/answers/pdf.txt', 'r') as f:
                answers = list(f.readlines())
        else:
            with open('./sample_questions/pdf_ja.txt', 'r', encoding="utf8") as f:
                questions = list(f.readlines())
            with open('./sample_questions/answers/pdf_ja.txt', 'r', encoding="utf8") as f:
                answers = list(f.readlines())
    elif file_type=='JSON':
        if lang=='en':
            with open('./sample_questions/json.txt', 'r') as f:
                questions = list(f.readlines())
            with open('./sample_questions/answers/json.txt', 'r') as f:
                answers = list(f.readlines())
        else:
            with open('./sample_questions/json_ja.txt', 'r', encoding="utf8") as f:
                questions = list(f.readlines())
            with open('./sample_questions/answers/json_ja.txt', 'r', encoding="utf8") as f:
                answers = list(f.readlines())
    elif file_type=='SQLITE_DB':
        if lang=='en':
            with open('./sample_questions/sqlite.txt', 'r') as f:
                questions = list(f.readlines())
            with open('./sample_questions/answers/sqlite.txt', 'r') as f:
                answers = list(f.readlines())
        else:
            with open('./sample_questions/sqlite_ja.txt', 'r', encoding="utf8") as f:
                questions = list(f.readlines())
            with open('./sample_questions/answers/sqlite_ja.txt', 'r', encoding="utf8") as f:
                answers = list(f.readlines())
    if que in questions:
        index = questions.index(que)
        ans = answers[index]
        if 'Line chart of values in open column?' in que:
            ans = ans + '#' + './sample_questions/answers/line_chart_csv.png'
        elif que=='with month name on x-axis and in serial number, make a chart of histogram of average open values per month with gap in each bar':
            ans = ans + '#' + './sample_questions/answers/histogram_chart_csv.png'
    else:
        ans = 'Something went wrong! Not able to find anything. Please ask another question.'
    return ans


