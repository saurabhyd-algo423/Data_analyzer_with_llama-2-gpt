import base64
import os 
import streamlit as st
from streamlit_option_menu import option_menu
import webbrowser
from utils.load import custom_footer
from homepage_content import homepage_content,homepage_vf,homepage_content_v2
from dashboard import demo_dashboard
from contact import contact_us
import os


#ANYSCALE_API_KEY = 'esecret_bg4uq3xfw5aziblg8dftl6bq7m'
#os.environ['ANYSCALE_API_BASE'] = "https://api.endpoints.anyscale.com/v1"
#os.environ['ANYSCALE_API_KEY'] = ANYSCALE_API_KEY


if "lang" not in st.session_state:
    st.session_state.lang = "en"

if "excel_sample" not in st.session_state:
    st.session_state.es = True

# TRANSLATE
#=============================================================================================================
import gettext
_gettext = gettext.gettext


try:
  localizator = gettext.translation('base', localedir='locales', languages=[st.session_state.lang])
  localizator.install()
  _gettext = localizator.gettext 
except Exception as e:
  print('inside exception')
  print(e)
#=============================================================================================================


#Page Configuraion
st.set_page_config(page_title="Interactive Data Analyser",
                   page_icon="ui_assets/images/algo-logo.png",
                   layout="wide",
                   )

with open('css/style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# ----------Website Header section------------------------

# divide navbar in three sectins
brand_logo, demo_button_section,view_all_button,language_option  = st.columns((2,2,0.7,0.5))#((2.3,2.2,0.5))


# ---------------------language section----------------------------------------- 
with language_option:
    # this is center the drop down widget
    st.markdown(
        """
        <style>
            
            div[data-testid="column"]:nth-of-type(3)
            {
                text-align: end;
                align-items: center;
                background-color": #E1EDFA
            } 
        </style>
        """,unsafe_allow_html=True
        )
    
    col1, col2 = st.columns((0.2,0.8))
    with col2:
        
        option = st.selectbox(label = "Language Selector", options = ("en","ja"), label_visibility = "collapsed", key = "lang")
    
    
    #=============================================================================================================   

#----------------------Brand Logo and App Name-----------------------------------  
with brand_logo:

    with open("ui_assets/images/algo-logo.png", "rb") as img_file:
        brand_image = base64.b64encode(img_file.read()).decode()
        
    # image_tag = f'<img src="data:image/png;base64,{brand_image}" width="100">'
    # # Display the image using st.markdown()
    # st.markdown(image_tag, unsafe_allow_html=True)
    app_name1 = _gettext("Interactive Data Analyser")
    st.markdown(f'''
    <div class='brand_logo_namestyle'>
        <a href = "https://onestop.ai/">
        <img src="data:image/png;base64,{brand_image}" width="70">
        </a>
        <div style="flex: 1; text-align: start; padding-left:5vw;">
        <h4 class='app-name'>{app_name1}</h4>
        </div>
        
    </div>''', unsafe_allow_html=True)
with view_all_button:
    
    st.markdown(
    """
    <style>
        div[data-testid="column"]:nth-of-type(1)
        {
            align-items: center
        } 

        div[data-testid="column"]:nth-of-type(2)
        {
            
            text-align: start;
        } 
        div[data-testid="column"]:nth-of-type(3)
        {
            text-align: center;
            
        } 
    </style>
    """,unsafe_allow_html=True
    )
    # url = "https://apps.onestop.ai/llm-dashboard/"
    # st.button('View All apps',on_click=on_click_js,args=(url,))
    
    def create_link(url, label, hover_color="#263557"):  # You can change the hover color here
        # HTML and CSS to style the link as a button, including hover effect
        button_html = f"""
        <style>
        .custom-button {{
            color: white; 
            background-color: #799BE6; 
            border: none; 
            border-radius: 4px; 
            padding: 5px 10px; 
            text-align: center; 
            text-decoration: none; 
            display: inline-block; 
            font-size: 16px; 
            margin: 4px 2px; 
            cursor: pointer;
            transition: background-color 0.3s;  /* Smooth transition for background color change */
        }}
        .custom-button:hover {{
            background-color: {hover_color};  /* Change hover background color */
        }}
        </style>
        <a href="{url}" target="_blank">
        <button class="custom-button">{label}</button></a>
        """

        st.markdown(button_html, unsafe_allow_html=True)

    # Usage
    button_name = _gettext("LLM Dashboard")
    create_link("https://apps.onestop.ai/llm-dashboard/", button_name)
    
#----------------------Navbar buttons section-----------------------------------    
with demo_button_section:
    
    st.markdown(
        """
        <style>
            
            div[data-testid="column"]:nth-of-type(2)
            {
                text-align: end;
                align-items: center;
                background-color": #E1EDFA
            } 
        </style>
        """,unsafe_allow_html=True
        )
    
    if 'option_menu' not in st.session_state:
        st.session_state.option_menu="Overview"

    if st.session_state.get('demo_button', False):
        st.session_state['manual_select'] = 1
        manual_select = st.session_state['manual_select']
    else:
        manual_select = None
        
    selected_tab = option_menu(None, [_gettext("Overview"), _gettext("Demo"),_gettext('Contact us')],#,_gettext('View all apps')], #,_gettext('Login')
        icons=['house-fill', 'arrow-up-circle-fill','telephone-fill'], #'box-arrow-in-right'
        key='option_menu',
        menu_icon="cast", 
        default_index=0, 
        orientation="horizontal",
        manual_select=manual_select,
        
        styles={
                    "container": {"padding": "0.01", "background-color": "#E1EDFA00"},#E1EDFA99
                    #"icon": {"font-size": "20px"}, #"#789BE6"
                    "nav-link": {
                        "font-size": "15px",
                        "color":"grey",
                        "text-align": "center",
                        "margin": "0px",
                        "--hover-color": "#E1EDFA",
                        "--background-color" :"grey"
    
                    },
                    "nav-link-selected": {"background-color": "#789BE600","color":"#789BE6"},
                    
                },
        
        )
    #dashboard_link = st.button("View all apps")
    #if dashboard_link:
    #    url = 'https://apps.onestop.ai/llm-dashboard/'
    #    webbrowser.open_new_tab(url)
#-----------------------Navbar divider line---------------------------------   
st.markdown(
    """
    <style>
    .horizontal-line {
        height: 1px;
        width: calc(100% + 3rem); /* Adjusted width to account for the left and right padding in your main layout */
        margin-left: -1.5rem; /* Adjusted negative margin to counteract the left padding in your main layout */
        background-color: #D3D3D3;
        box-shadow: 0px 1px 2px 0px rgba(0,0,0,0.2);
        margin-top: 0;
        padding: 0;
        border: none;
    }
    </style>
    <hr class="horizontal-line">
    """,
    unsafe_allow_html=True
)

#------Home page ------------------------------
if st.session_state.option_menu in ["Overview","概要"]: #==_gettext("Home")
    
    homepage_content_v2(_gettext)#homepage_vf(_gettext)#homepage_content(_gettext)
    
#---------Dashboard-----------------------------
elif st.session_state.option_menu in ["Demo","デモ"]: # ==_gettext('Demo Dashboard')
    
    # Readjusting the styling for demo dashboard containers to get displayed as expected
    st.markdown(
    """
    <style>
        div[data-testid="column"]:nth-of-type(1)
        {
            align-items: center
        } 

        div[data-testid="column"]:nth-of-type(2)
        {
            
            text-align: start;
        } 
        div[data-testid="column"]:nth-of-type(3)
        {
            text-align: center;
            
        } 
    </style>
    """,unsafe_allow_html=True
    )
    
    # demo dashboard
    #st.write('Inside dashboard')
    demo_dashboard(_gettext)

elif st.session_state.option_menu in ["Contact us","お問い合わせ"]:
    contact_us(_gettext)

#elif st.session_state.option_menu in ["View all apps","すべてのアプリを表示"]: #==_gettext("Home")
#    
#    url = 'https://apps.onestop.ai/llm-dashboard/'


#    webbrowser.open_new_tab(url)



st.markdown('')
st.markdown('')
custom_footer(_gettext)

hide_streamlit_style = """
            <style>
            
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

