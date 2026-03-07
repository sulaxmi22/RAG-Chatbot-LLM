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
            "You are MediChat Pro, an intelligent medical document assistant.\n"
            "Answer only from the provided medical documents.\n\n"
            f"Medical Documents:\n{context}\n\n"
            f"User Question: {question}\n\n"
            "Answer:"
        )
    else:
        prompt = question

    try:
        response = chat_model.invoke(prompt)   # now sending a raw string, not a list of messages
        return response.content
    except Exception as e:
        return f"⚠️ Error from chat model: {str(e)}"
