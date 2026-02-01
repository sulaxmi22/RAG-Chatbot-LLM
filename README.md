
https://github.com/user-attachments/assets/6834c855-5aa4-4fe6-8c86-d138ad43a594



# 🤖 AI Resume Analyzer Assistant

**Stop guessing. Start hiring smarter.**

Your AI-powered assistant that **reads, understands, and evaluates resumes in seconds** matching candidates to job descriptions with precision. Built for **candidates applying for jobs, recruiters, HR teams, and hiring managers** who want speed, accuracy, and actionable insights.

---

## 🤖 Key Features

- **Resume Parsing** – Effortlessly extract text from multiple PDFs.  
- **AI Job Matching** – GPT-based assistant analyzes resumes against any job description.  
- **Semantic Search** – FAISS-powered search retrieves relevant resume sections instantly.  
- **Interactive Chat Interface** – Ask questions, get structured, human-readable insights.  
- **Skill & Keyword Highlighting** – Instantly see if candidates have the skills you need.  
- **Document & Session Management** – Keep multiple resumes and chat history organized.  

---

## 🤖 Tech Stack

- **Frontend**: Streamlit – real-time, interactive chat interface  
- **AI & NLP**: GPT-4.1-nano (via EuriAI), LangChain, Sentence Transformers  
- **Vector Database**: FAISS – semantic, lightning-fast document search  
- **PDF Processing**: `pypdf`, `fpdf`  
- **Custom Modules**: Resume analysis, vectorstore management, chat interface  

---

## 🤖 Quick Start

1. Upload one or more resumes (PDF).
2. Click Process Documents to extract and vectorize content.
3. Enter a job description or query in the chat.
4. Receive structured AI insights, highlighting skills, experience, and match scores.

```bash
git clone <repo-url>
cd rag-chatbot-llm
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
pip install -r requirements.txt
pip install langchain==1.1.0
streamlit run main.py


