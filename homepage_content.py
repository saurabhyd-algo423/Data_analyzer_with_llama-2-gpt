import base64
import streamlit as st
#from utils.load import load_lottiefile
from utils.design_utils import create_featurecard,create_specific_feature
from utils.load import load_base64_image
import streamlit.components.v1 as components

def image_to_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

@st.cache_data(experimental_allow_widgets=True)
def homepage_content(_gettext):
    # Display Header using Streamlit Markdown with HTML styling
    main_heading_text =_gettext('Analyze your data in a live interactive manner')
    description_text = _gettext('Ask your queries from different types of data files and visualize the data.')

    st.markdown(f"""
        <style>
            body {{
                font-family: 'Poppins', sans-serif;
                margin: 0;
                padding: 0;
                box-sizing: border-box;
                color: #333;
                background-color: #ffffff;
            }}
            .hero-text {{
                text-align: center;
            }}
            .hero-text h1 {{
                font-size: 2rem;
                color: #0a4e8d; /* Adjust color */
                font-weight: 600;
                margin-bottom: 0.2rem;
                text-shadow: 2px 2px 8px #c2c2c2; /* Subtle text shadow */
            }}
            .hero-text p {{
                font-size: 1.2rem;
                color: #333333;2/* Adjust color */
                margin: 0.5rem 0;
                line-height: 1.4;
            }}
        </style>
        <body>
        <div class="hero-text">
            <h1>{main_heading_text}</h1>
            <br>
            <p>{description_text}</p>
            <br>
        </div>
        </body>
    """, unsafe_allow_html=True)
  
    #-----------------------------------------------

    # Create three columns: Left for Info, Middle for Upload and View, Right for Insights
    left_col,button_col, right_col= st.columns([4,1,4])
    with button_col:

        # View Demo Button
        button_style = """
        <style>
            div.stButton > button:first-child {
                display: inline-block;
                padding: 10px 20px;
                margin: 10px 0;
                border-radius: 25px;
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
        button_name = _gettext('Try Demo')
        st.button(button_name,key ='demo_button')

    #f1_image_load = load_base64_image("ui_assets/images/contexually aware.png")
    #image1_base64 = f"data:image/jpeg;base64,{f1_image_load}"
    feature1_heading = _gettext("Your Personal AI data analyser")
    feature1_description = _gettext("Say goodbye to writing complex data processing and analysis code! Our state-of-the-art analyzer chatbot adeptly deciphers queries and seamlessly conducts data processing.")#" Thanks to its natural language query capability, you can now wave goodbye to concerns over syntax errors and the tiresome quest for online solutions.")
    
    #f2_image_load = load_base64_image("ui_assets/images/document_summary.jpg")
    #image2_base64 = f"data:image/jpeg;base64,{f2_image_load}"
    feature2_heading = _gettext("Some feature highlights")
    feature2_description = _gettext("Ask queries to your CSV, TSV, EXCEL files in natural language and plot graphs. Analyse textual data in different formats such as PDFs, TXT and DOC files. Work with multiple sheets in excel.")#" No need to write SQL queries, just upload your sqlite database file and chat naturally.")
    
    #f3_image_load = load_base64_image("ui_assets/images/3156627.jpg")
    #image3_base64 = f"data:image/jpeg;base64,{f3_image_load}"
    feature3_heading = _gettext("Less time for your EDA")
    feature3_description = _gettext("No need for extensive explanations. Our chatbot delivers responses with precision and clarity, skillfully distilling intricate information into easily digestible summaries.")#" It not only furnishes swift and precise answers but also trims down the time invested in exploratory data analysis.")
    
    # Base64 encoding of images
    image1_base64 = image_to_base64("ui_assets/images/contexually aware.png")
    image2_base64 = image_to_base64("ui_assets/images/document_summary.jpg")
    image3_base64 = image_to_base64("ui_assets/images/3156627.jpg")
    
    st.markdown(f"""
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');
            body, html {{
                margin: 0;
                padding: 0;
                font-family: 'Poppins', sans-serif;
                color: #333;
                line-height: 1.6;
            }}
            .features-container {{
                display: flex;
    justify-content: center; 
    flex-wrap: wrap;
    margin-top: 10px;
                gap:15px;
            }}
            .features-container .card {{
                  flex-grow: 0; /* Prevents cards from growing */
    flex-shrink: 0; /* Prevents cards from shrinking */
    flex-basis: 25%; /* Base width of the cards */
    margin: 5px; /* Reduced margin */
    padding: 20px; /* Adjust padding if needed */
                background: linear-gradient(135deg, #ffffff 0%, #e6e9f0 100%);
                border-radius: 20px;
                
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                transition: transform 0.3s ease, box-shadow 0.3s ease;
                border: none;
            }}
            .card:hover {{
                transform: translateY(-10px);
                box-shadow: 0 12px 20px rgba(0, 0, 0, 0.2);
            }}
            .card img {{
                max-width: 100%;
                max-height: 300px;
                border-radius: 10px;
                transition: transform 0.3s ease-in-out;
            }}
            .card img:hover {{
                transform: scale(1.05);
            }}
            .card h3 {{
                margin-top: 15px;
                font-weight: 600;
                color: #2c3e50;
            }}
            .card p {{
                font-weight: 300;
                line-height: 1.7;
            }}
            @media (max-width: 768px) {{
                .features-container .card {{
                    max-width: 40%; /* Adjust for smaller screens */
                }}
            }}
            @media (max-width: 480px) {{
                .features-container .card {{
                    max-width: 80%; /* Full width on very small screens */
                }}
            }}
        </style>
    </head>
    <body>
        <div class="features-container">
            <div class="card">
                <img src="data:image/jpeg;base64,{image1_base64}" alt="Effortless Feedback Import">
                <h3>{feature1_heading}</h3>
                <p>{feature1_description}</p>
            </div>
            <div class="card">
                <img src="data:image/jpeg;base64,{image2_base64}" alt="Sentiment Analysis">
                <h3>{feature2_heading}</h3>
                <p>{feature2_description}</p>
            </div>
            <div class="card">
                <img src="data:image/jpeg;base64,{image3_base64}" alt="Actionable Insights">
                <h3>{feature3_heading}</h3>
                <p>{feature3_description}</p>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('')
    st.markdown('')
    st.markdown('')
    st.markdown('')
    st.markdown('')
    st.markdown('')
    st.markdown('')
    st.markdown('')


def homepage_content_v2(_gettext):
    # Base64 encoding of images
    image1_base64 = image_to_base64("ui_assets/images/contexually aware.png")
    image2_base64 = image_to_base64("ui_assets/images/document_summary.jpg")
    image3_base64 = image_to_base64("ui_assets/images/3156627.jpg")

    #title = _gettext("AlgoAnalytics brings you AlgoMed!")
    #sub = _gettext("A Healthcare Chat Assistant for all your medical questions!")
    title =_gettext('Analyze your data in a live interactive manner')
    sub = _gettext('Ask your queries from different types of data files and visualize the data.')
    subhead = _gettext("Powered by Large Language Models (LLM)")
   
    feature1_heading = _gettext("Your Personal AI data analyser")
    feature1_description = _gettext("Say goodbye to writing complex data processing and analysis code! Our state-of-the-art analyzer chatbot adeptly deciphers queries and seamlessly conducts data processing.")#" Thanks to its natural language query capability, you can now wave goodbye to concerns over syntax errors and the tiresome quest for online solutions.")
    
    feature2_heading = _gettext("Some feature highlights")
    feature2_description = _gettext("Ask queries to your CSV, TSV, EXCEL files in natural language and plot graphs. Analyse textual data in different formats such as PDFs, TXT and DOC files. Work with multiple sheets in excel.")#" No need to write SQL queries, just upload your sqlite database file and chat naturally.")
    
    feature3_heading = _gettext("Less time for your EDA")
    feature3_description = _gettext("No need for extensive explanations. Our chatbot delivers responses with precision and clarity, skillfully distilling intricate information into easily digestible summaries.")#" It not only furnishes swift and precise answers but also trims down the time invested in exploratory data analysis.")
    
 
    # Define the HTML content with Base64 encoded images
    main_heading_text =_gettext('Analyze your data in a live interactive manner')
    description_text = _gettext('Ask your queries from different types of data files and visualize the data.')

    st.markdown(f"""
        <style>
            body {{
                font-family: 'Poppins', sans-serif;
                margin: 0;
                padding: 0;
                box-sizing: border-box;
                color: #333;
                background-color: #ffffff;
            }}
            .hero-text {{
                text-align: center;
            }}
            .hero-text h1 {{
                font-size: 2rem;
                color: #0a4e8d; /* Adjust color */
                font-weight: 600;
                margin-bottom: 0.2rem;
                text-shadow: 2px 2px 8px #c2c2c2; /* Subtle text shadow */
            }}
            .hero-text p {{
                font-size: 1.2rem;
                color: #333333;2/* Adjust color */
                margin: 0.5rem 0;
                line-height: 1.4;
            }}
        </style>
        <body>
        <div class="hero-text">
            <h1>{main_heading_text}</h1>
            <br>
            <p>{description_text}</p>
            <br>
        </div>
        </body>
    """, unsafe_allow_html=True)
    
    html_content_2 = f"""<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Healthcare Chatbot</title>
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');
            body, html {{
                margin: 0;
                padding: 0;
                font-family: 'Poppins', sans-serif;
                color: #333;
            }}
            .main-container {{
    margin-top: 10px; /* Reduced from auto */
    margin-bottom: 10px; /* Reduced from auto */
                width: 85%;
                margin: auto;
                overflow: hidden;
                display: flex;
                flex-direction: column;
                align-items: center;
            }}
            .app-header {{
                text-align: center;
                padding: 0;
                animation: fadeIn 1s ease;
                margin-top:0;
                margin-bottom: 0;
            }}
            .app-header h1 {{
                font-weight: 600;
                color: #4682B4;
                text-shadow: 0px 2px 4px rgba(0,0,0,0.2);
                padding-bottom: 0; /* Reduce or remove padding */
                margin-top: 0;
                margin-bottom: 0;
            }}
            .app-header p {{
                font-weight: 300;
                color: #555;
                margin-top: 0;
                margin-bottom:0;
            }}
            
            .card {{
                background: linear-gradient(135deg, #ffffff 0%, #e6e9f0 100%);
                border-radius: 20px;
                margin: 0px ;
                padding: 10px;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                transition: transform 0.3s ease, box-shadow 0.3s ease;
                border: none;
            }}
            .card:hover {{
                transform: translateY(-10px);
                box-shadow: 0 12px 20px rgba(0, 0, 0, 0.2);
            }}
            .card img {{
                max-width: 100%;
                max-height: 300px;
                border-radius: 10px;
                transition: transform 0.3s ease-in-out;
            }}
            .card img:hover {{
                transform: scale(1.05);
            }}
            .card h3 {{
                margin-top: 15px;
                font-weight: 600;
                color: #2c3e50;
            }}
            .card p {{
                font-weight: 300;
                line-height: 1.7;
            }}
            .contact {{
                background: rgba(255, 255, 255, 0.9);
                text-align: center;
                padding: 20px;
                border-radius: 20px;
                margin-top: 30px;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
                transition: all 0.3s ease-in-out;
            }}
            .contact a {{
                color: #ea4c89;
                text-decoration: none;
                font-weight: 600;
                transition: color 0.3s ease;
            }}
            .contact a:hover {{
                color: #3498db;
            }}
            footer {{
                text-align: center;
                padding: 20px 0;
                background: #222;
                color: #fff;
                font-weight: 300;
            }}
            @keyframes fadeIn {{
                from {{ opacity: 0; }}
                to {{ opacity: 1; }}
            }}
            .features-container {{
                display: flex;
                justify-content: space-around;
                flex-wrap: wrap;
                margin-top: 10px;
            }}
            .features-container .card {{
                max-width: 30%;
                margin: 5px;
                flex: 1;
            }}
            .hero {{
                background-size: cover; /* or try 'contain' depending on the image */
                position: relative;
                height: 100px;  /* Adjust this value based on your design needs */
                width: 100%;
                display: flex;
                justify-content: center;
                align-items: center;
                text-align: center;
            }}
            .hero-bg {{
                width: 100%;
                height: auto; /* Adjust this as needed */
                position: absolute;
                top: 0;
                left: 0;
                background-size: cover;
                background-position: center;
                background-repeat: no-repeat;
                z-index: -1; /* Ensure it stays behind the content */
            }}
            .hero-content {{
                position: relative;
                z-index: 2; /* To ensure content appears above the overlay */
            }}
            .hero-cta {{
                display: inline-block;
                background-color: #ea4c89;
                color: white;
                padding: 10px 20px;
                border-radius: 5px;
                text-decoration: none;
                transition: background-color 0.3s;
            }}
            .hero-cta:hover {{
                background-color: #3498db;
            }}
            @media (max-width: 768px) {{
                .features-container .card {{
                    max-width: 45%; /* Adjust for smaller screens */
                }}
            }}
            @media (max-width: 480px) {{
                .features-container .card {{
                    max-width: 90%; /* Full width on very small screens */
                }}
            }}
        </style>
    </head>
    <body>
        <div class="main-container">
        
            <!-- Features Section with Base64 Images -->
            <div class="features-container">
                <div class="card">
                    <img src="data:image/jpeg;base64,{image1_base64}" alt={feature1_heading}>
                    <h3>{feature1_heading}</h3>
                    <p>{feature1_description}</p>
                </div>
                <div class="card">
                
                    <img src="data:image/jpeg;base64,{image2_base64}" alt={feature2_heading}>
                    <h3>{feature2_heading}</h3>
                    <p>{feature2_description}</p>
                </div>
                <div class="card">
                    <img src="data:image/jpeg;base64,{image3_base64}" alt={feature3_heading}>
                    <h3>{feature3_heading}</h3>
                    <p>{feature3_description}</p>
                </div>
            </div>
            <br/>
            <br/>
            <br/>
            <br/>
            <br/>
            <br/>
            <br/>
            <br/>
        </div>
    </body>
    </html>"""
    
    # Display HTML content using components.html
    #components.html(html_content_1, scrolling=False)
    left_col,button_col, right_col= st.columns([4,0.72,4])
    with button_col:
        button_style = """
    <style>
        div.stButton > button:first-child {
            display: inline-block;
            padding: 10px 20px;
            margin: 2px 0;
            border-radius: 25px;
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

        button_name = _gettext('Try Demo')
        st.button(button_name,key ='demo_button')
    components.html(html_content_2, height=1000, scrolling=True)
    


def homepage_vf(_gettext):
    # Base64 encoding of images
    image1_base64 = image_to_base64("ui_assets/images/contexually aware.png")
    image2_base64 = image_to_base64("ui_assets/images/document_summary.jpg")
    image3_base64 = image_to_base64("ui_assets/images/3156627.jpg")

    #title = _gettext("AlgoAnalytics brings you AlgoMed!")
    #sub = _gettext("A Healthcare Chat Assistant for all your medical questions!")
    title =_gettext('Analyze your data in a live interactive manner')
    sub = _gettext('Ask your queries from different types of data files and visualize the data.')
    subhead = _gettext("Powered by Large Language Models (LLM)")
   
    feature1_heading = _gettext("Your Personal AI data analyser")
    feature1_description = _gettext("Say goodbye to writing complex data processing and analysis code! Our state-of-the-art analyzer chatbot adeptly deciphers queries and seamlessly conducts data processing.")#" Thanks to its natural language query capability, you can now wave goodbye to concerns over syntax errors and the tiresome quest for online solutions.")
    
    feature2_heading = _gettext("Some feature highlights")
    feature2_description = _gettext("Ask queries to your CSV, TSV, EXCEL files in natural language and plot graphs. Analyse textual data in different formats such as PDFs, TXT and DOC files. Work with multiple sheets in excel.")#" No need to write SQL queries, just upload your sqlite database file and chat naturally.")
    
    feature3_heading = _gettext("Less time for your EDA")
    feature3_description = _gettext("No need for extensive explanations. Our chatbot delivers responses with precision and clarity, skillfully distilling intricate information into easily digestible summaries.")#" It not only furnishes swift and precise answers but also trims down the time invested in exploratory data analysis.")
    
 
    # Define the HTML content with Base64 encoded images
    html_content_1 = f"""<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Healthcare Chatbot </title>
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');
            body, html {{
                margin: 0;
                padding: 0;
                font-family: 'Poppins', sans-serif;
                color: #333;
            }}
            .main-container {{
    margin-top: 10px; /* Reduced from auto */
    margin-bottom: 10px; /* Reduced from auto */
                width: 85%;
                margin: auto;
                overflow: hidden;
                display: flex;
                flex-direction: column;
                align-items: center;
            }}
            .app-header {{
                text-align: center;
                padding: 0;
                animation: fadeIn 1s ease;
                margin-top:0;
                margin-bottom: 0;
            }}
            .app-header h1 {{
                font-weight: 600;
                color: #4682B4;
                text-shadow: 0px 2px 4px rgba(0,0,0,0.2);
                padding-bottom: 0; /* Reduce or remove padding */
                margin-top: 0;
                margin-bottom: 0;
            }}
            .app-header p {{
                font-weight: 300;
                color: #555;
                margin-top: 0;
                margin-bottom:0;
            }}
            
            .card {{
                background: linear-gradient(135deg, #ffffff 0%, #e6e9f0 100%);
                border-radius: 20px;
                margin: 0px ;
                padding: 10px;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                transition: transform 0.3s ease, box-shadow 0.3s ease;
                border: none;
            }}
            .card:hover {{
                transform: translateY(-10px);
                box-shadow: 0 12px 20px rgba(0, 0, 0, 0.2);
            }}
            .card img {{
                max-width: 100%;
                max-height: 300px;
                border-radius: 10px;
                transition: transform 0.3s ease-in-out;
            }}
            .card img:hover {{
                transform: scale(1.05);
            }}
            .card h3 {{
                margin-top: 15px;
                font-weight: 600;
                color: #2c3e50;
            }}
            .card p {{
                font-weight: 300;
                line-height: 1.7;
            }}
            .contact {{
                background: rgba(255, 255, 255, 0.9);
                text-align: center;
                padding: 20px;
                border-radius: 20px;
                margin-top: 30px;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
                transition: all 0.3s ease-in-out;
            }}
            .contact a {{
                color: #ea4c89;
                text-decoration: none;
                font-weight: 600;
                transition: color 0.3s ease;
            }}
            .contact a:hover {{
                color: #3498db;
            }}
            footer {{
                text-align: center;
                padding: 20px 0;
                background: #222;
                color: #fff;
                font-weight: 300;
            }}
            @keyframes fadeIn {{
                from {{ opacity: 0; }}
                to {{ opacity: 1; }}
            }}
            .features-container {{
                display: flex;
                justify-content: space-around;
                flex-wrap: wrap;
                margin-top: 10px;
            }}
            .features-container .card {{
                max-width: 30%;
                margin: 5px;
                flex: 1;
            }}
            .hero {{
                background-size: cover; /* or try 'contain' depending on the image */
                position: relative;
                height: 100px;  /* Adjust this value based on your design needs */
                width: 100%;
                display: flex;
                justify-content: center;
                align-items: center;
                text-align: center;
            }}
            .hero-bg {{
                width: 100%;
                height: auto; /* Adjust this as needed */
                position: absolute;
                top: 0;
                left: 0;
                background-size: cover;
                background-position: center;
                background-repeat: no-repeat;
                z-index: -1; /* Ensure it stays behind the content */
            }}
            .hero-content {{
                position: relative;
                z-index: 2; /* To ensure content appears above the overlay */
            }}
            .hero-cta {{
                display: inline-block;
                background-color: #ea4c89;
                color: white;
                padding: 10px 20px;
                border-radius: 5px;
                text-decoration: none;
                transition: background-color 0.3s;
            }}
            .hero-cta:hover {{
                background-color: #3498db;
            }}
            @media (max-width: 768px) {{
                .features-container .card {{
                    max-width: 45%; /* Adjust for smaller screens */
                }}
            }}
            @media (max-width: 480px) {{
                .features-container .card {{
                    max-width: 90%; /* Full width on very small screens */
                }}
            }}
        </style>
    </head>
    <body>
        <div class="main-container">
            <!-- App Name and Tagline -->
            <div class="app-header">
                <h1 >{title}</h1>
                <h2 style = "margin-top: 0;">{sub}</h2>
                
            </div>
           
        </div>
    </body>
    </html>"""
    
    html_content_2 = f"""<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Healthcare Chatbot</title>
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');
            body, html {{
                margin: 0;
                padding: 0;
                font-family: 'Poppins', sans-serif;
                color: #333;
            }}
            .main-container {{
    margin-top: 10px; /* Reduced from auto */
    margin-bottom: 10px; /* Reduced from auto */
                width: 85%;
                margin: auto;
                overflow: hidden;
                display: flex;
                flex-direction: column;
                align-items: center;
            }}
            .app-header {{
                text-align: center;
                padding: 0;
                animation: fadeIn 1s ease;
                margin-top:0;
                margin-bottom: 0;
            }}
            .app-header h1 {{
                font-weight: 600;
                color: #4682B4;
                text-shadow: 0px 2px 4px rgba(0,0,0,0.2);
                padding-bottom: 0; /* Reduce or remove padding */
                margin-top: 0;
                margin-bottom: 0;
            }}
            .app-header p {{
                font-weight: 300;
                color: #555;
                margin-top: 0;
                margin-bottom:0;
            }}
            
            .card {{
                background: linear-gradient(135deg, #ffffff 0%, #e6e9f0 100%);
                border-radius: 20px;
                margin: 0px ;
                padding: 10px;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                transition: transform 0.3s ease, box-shadow 0.3s ease;
                border: none;
            }}
            .card:hover {{
                transform: translateY(-10px);
                box-shadow: 0 12px 20px rgba(0, 0, 0, 0.2);
            }}
            .card img {{
                max-width: 100%;
                max-height: 300px;
                border-radius: 10px;
                transition: transform 0.3s ease-in-out;
            }}
            .card img:hover {{
                transform: scale(1.05);
            }}
            .card h3 {{
                margin-top: 15px;
                font-weight: 600;
                color: #2c3e50;
            }}
            .card p {{
                font-weight: 300;
                line-height: 1.7;
            }}
            .contact {{
                background: rgba(255, 255, 255, 0.9);
                text-align: center;
                padding: 20px;
                border-radius: 20px;
                margin-top: 30px;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
                transition: all 0.3s ease-in-out;
            }}
            .contact a {{
                color: #ea4c89;
                text-decoration: none;
                font-weight: 600;
                transition: color 0.3s ease;
            }}
            .contact a:hover {{
                color: #3498db;
            }}
            footer {{
                text-align: center;
                padding: 20px 0;
                background: #222;
                color: #fff;
                font-weight: 300;
            }}
            @keyframes fadeIn {{
                from {{ opacity: 0; }}
                to {{ opacity: 1; }}
            }}
            .features-container {{
                display: flex;
                justify-content: space-around;
                flex-wrap: wrap;
                margin-top: 10px;
            }}
            .features-container .card {{
                max-width: 30%;
                margin: 5px;
                flex: 1;
            }}
            .hero {{
                background-size: cover; /* or try 'contain' depending on the image */
                position: relative;
                height: 100px;  /* Adjust this value based on your design needs */
                width: 100%;
                display: flex;
                justify-content: center;
                align-items: center;
                text-align: center;
            }}
            .hero-bg {{
                width: 100%;
                height: auto; /* Adjust this as needed */
                position: absolute;
                top: 0;
                left: 0;
                background-size: cover;
                background-position: center;
                background-repeat: no-repeat;
                z-index: -1; /* Ensure it stays behind the content */
            }}
            .hero-content {{
                position: relative;
                z-index: 2; /* To ensure content appears above the overlay */
            }}
            .hero-cta {{
                display: inline-block;
                background-color: #ea4c89;
                color: white;
                padding: 10px 20px;
                border-radius: 5px;
                text-decoration: none;
                transition: background-color 0.3s;
            }}
            .hero-cta:hover {{
                background-color: #3498db;
            }}
            @media (max-width: 768px) {{
                .features-container .card {{
                    max-width: 45%; /* Adjust for smaller screens */
                }}
            }}
            @media (max-width: 480px) {{
                .features-container .card {{
                    max-width: 90%; /* Full width on very small screens */
                }}
            }}
        </style>
    </head>
    <body>
        <div class="main-container">
        
            <!-- Features Section with Base64 Images -->
            <div class="features-container">
                <div class="card">
                    <img src="data:image/jpeg;base64,{image1_base64}" alt={feature1_heading}>
                    <h3>{feature1_heading}</h3>
                    <p>{feature1_description}</p>
                </div>
                <div class="card">
                
                    <img src="data:image/jpeg;base64,{image2_base64}" alt={feature2_heading}>
                    <h3>{feature2_heading}</h3>
                    <p>{feature2_description}</p>
                </div>
                <div class="card">
                    <img src="data:image/jpeg;base64,{image3_base64}" alt={feature3_heading}>
                    <h3>{feature3_heading}</h3>
                    <p>{feature3_description}</p>
                </div>
            </div>
            <br/>
            <br/>
            <br/>
            <br/>
            <br/>
            <br/>
            <br/>
            <br/>
        </div>
    </body>
    </html>"""
    
    # Display HTML content using components.html
    components.html(html_content_1, scrolling=False)
    left_col,button_col, right_col= st.columns([4,0.72,4])
    with button_col:
        button_style = """
    <style>
        div.stButton > button:first-child {
            display: inline-block;
            padding: 10px 20px;
            margin: 2px 0;
            border-radius: 25px;
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

        button_name = _gettext('Try Demo')
        st.button(button_name,key ='demo_button')
    components.html(html_content_2, height=1000, scrolling=True)
