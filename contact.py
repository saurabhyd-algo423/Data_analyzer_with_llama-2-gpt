import streamlit as st
from utils.design_utils import create_featurecard,create_specific_feature
from utils.load import load_base64_image

def contact_us(_gettext):
    col1, col2, col3 = st.columns(3)

    #Address
    address_title = _gettext("Address")
    address = _gettext("""Alacrity India Innovation Centre, Ideas to Impacts Building.\n
                \nPallod Farm Lane 3, \n\n Near Vijay Sales, \n\n Baner Road, Pune - 411045""")
    col1.markdown(f"<h3>{address_title}</h3>", unsafe_allow_html=True)
    col1.info(address)

    # Email
    email_title = _gettext("Email")
    email_id = _gettext("info@algoanalytics.com")
    col2.markdown(f"<h3 style='text-align: left;'>{email_title}</h3>", unsafe_allow_html=True)
    col2.warning(email_id)

    # Load base64 images
    twitter_image = load_base64_image("ui_assets/images/twitter_logo.png")
    ig_image = load_base64_image("ui_assets/images/in_logo.png")
    linked_in_image = load_base64_image("ui_assets/images/lk.png")
    fb_image = load_base64_image("ui_assets/images/fb.png")

    # Social Media Links with added space
    twitter_tag = f"<img src='data:image/png;base64,{twitter_image}' width='50' style='margin-right: 10px;'>"
    ig_tag = f"<img src='data:image/png;base64,{ig_image}' width='50' style='margin-right: 10px;'>"
    linked_in_tag = f"<img src='data:image/png;base64,{linked_in_image}' width='50' style='margin-right: 10px;'>"
    fb_tag = f"<img src='data:image/png;base64,{fb_image}' width='50' style='margin-right: 10px;'>"

    social_media_links = f"""
    <div style="text-align: left;">
        <a href="https://twitter.com/AlgoanalyticsIn" target="_blank" rel="noopener noreferrer">{twitter_tag}</a>
        <a href="https://www.linkedin.com/company/algoanalytics/" target="_blank" rel="noopener noreferrer">{linked_in_tag}</a>
        <a href="https://www.facebook.com/Algoanalytics-1861931557423786" target="_blank" rel="noopener noreferrer">{fb_tag}</a>
        <a href="https://instagram.com/algoanalyticsin?igshid=OGQ5ZDc2ODk2ZA==" target="_blank" rel="noopener noreferrer">{ig_tag}</a>
    </div>
    """

    # Social Presence
    sm_title = _gettext("Social Presence")
    col3.markdown(f"<h3 style='text-align: left;'>{sm_title}</h3>", unsafe_allow_html=True)
    col3.markdown(social_media_links, unsafe_allow_html=True)
    st.markdown("")
    st.markdown("")
    st.markdown("")
    st.markdown("")
    st.markdown("")
    st.markdown("")
    st.markdown("")
    st.markdown("")
    st.markdown("")
    st.markdown("")
    st.markdown("")
    st.markdown("")
    st.markdown("")
    st.markdown("")
    st.markdown("")
    