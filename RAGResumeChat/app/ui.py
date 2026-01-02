import streamlit as st

def display_chat_interface():
    return st.file_uploader("Upload a PDF", type=["pdf"], 
                            accept_multiple_files=True, 
                            help="Upload one or more PDF files to chat with their content.")