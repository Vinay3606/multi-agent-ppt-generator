# 🤖 Multi-Agent AI PPT Generator

An AI-powered Multi-Agent system that generates editable PowerPoint presentations using company documents and user requirements.

---


## 🚀 Features

- 📄 Upload Company PDF
- 📊 Upload PPT Template
- 🔍 RAG-based Information Retrieval
- 🧠 FAISS Vector Search
- ✍️ AI Content Generation
- 🛡️ Content Validation
- 📑 Editable PPT Generation
- 🌐 Streamlit Web Interface

---


## ⚙️ How It Works

```text
📄 Company PDF + 📊 PPT Template + 💬 User Prompt
                        ↓
                  🤖 Document Agent
                        ↓
                  🧠 RAG + FAISS
                        ↓
              ✍️ Content Generator Agent
                        ↓
                 🛡️ Validation Agent
                        ↓
                 📊 PPT Generator Agent
                        ↓
              ⬇️ Editable PPT Output

```

🛠️ Tech Stack

```text
Python
Streamlit
FAISS
Sentence Transformers
Hugging Face
PyPDF
python-pptx
Scikit-learn
```

📁 Project Structure


```text
multi-agent-ppt-generator/
│
├── agents/
│   ├── document_agent.py
│   ├── content_generator.py
│   ├── validation_agent.py
│   ├── ppt_generator.py
│   ├── supervisor.py
│   └── vector_store.py
│
├── streamlit_ui.py
├── requirements.txt
└── README.md

```

💻 Installation


git clone https://github.com/Vinay3606/multi-agent-ppt-generator.git
cd multi-agent-ppt-generator

python -m venv multienv
multienv\Scripts\activate

pip install -r requirements.txt


▶️ Run

streamlit run streamlit_ui.py


👨‍💻 Author

Vinay Choudhary

🔗 LinkedIn: https://www.linkedin.com/in/vinay-choudhary-3a6286288
💻 GitHub: https://github.com/Vinay3606
