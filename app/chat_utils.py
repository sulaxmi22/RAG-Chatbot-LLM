# app/chat_utils.py

from euriai.langchain import create_chat_model
from langchain_core.messages import SystemMessage, HumanMessage

def get_chat_model_response(api_key):
    return create_chat_model(
        api_key=api_key,
        model="gpt-4.1-nano",   # adjust if Euri AI uses a different model name
        temperature=0.7
    )

def ask_chat_model(chat_model, question, context=None):
    if context:
        prompt = (
            "You are ResumeMatch Pro, an intelligent resume analysis assistant.\n"
            "Your task is to evaluate resumes against a given job description.\n"
            "Only use the information from the provided resumes.\n\n"
            f"Job Description:\n{question}\n\n"
            f"Uploaded Resumes:\n{context}\n\n"
            "Provide a detailed, structured analysis:\n"
            "Answer:"
        )
    else:
        prompt = (
            "Please provide a job description and at least one resume to analyze."
        )

    try:
        response = chat_model.invoke(prompt)   # now sending a raw string, not a list of messages
        return response.content
    except Exception as e:
        return f"⚠️ Error from chat model: {str(e)}"
