import streamlit as st

from config.session_config import CONVERSATION_HISTORY_SESSION_STATE


user_emoji = "🙋‍♂️" #config_data["emojis"]["user_emoji"]
chatbot_emoji = "🤖" #config_data["emojis"]["chatbot_emoji"]


user_message_style = """
    background-color: #D5F5E3;
    padding: 10px;
    border-radius: 5px;
    margin-bottom: 10px;
    display: flex;
    align-items: right;
    justify-content: flex-end;
    font-size: 18px; 
    color: black;
"""

chatbot_message_style = """
    background-color: #E5E8E8;
    padding: 10px;
    border-radius: 5px;
    margin-bottom: 10px;
    display: flex;
    align-items: left;
    font-size: 18px; 
    color: black;
    justify-content: flex-start;
"""


def clear_conversation(_gettext):
    #st.session_state.text_value = ''
    """Clear the conversation history."""
    if (
        st.button("🧹 " + _gettext("Clear conversation"), use_container_width=True)
        or "conversation_history" not in st.session_state
    ):
        st.session_state[CONVERSATION_HISTORY_SESSION_STATE]= []
        st.session_state.total_cost = 0




def display_conversation(conversation_history:list):
    """Display the conversation history in reverse chronology."""

    for idx, item in enumerate(reversed(conversation_history)):
        # Display the messages on the frontend
        
        message = item.data["content"]
        
        if item.type == "ai":
            # display ai message
            st.markdown(
                        f'<div style="{chatbot_message_style}">{chatbot_emoji} {message}</div>',
                        unsafe_allow_html=True
                            )
            
        elif item.type == "human":
    
            st.markdown(
                        f'<div style="{user_message_style}">{user_emoji} {message}</div>',
                        unsafe_allow_html=True
                            )
        
        
        
           