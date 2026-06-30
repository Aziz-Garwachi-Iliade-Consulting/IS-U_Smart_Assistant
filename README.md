# 🤖 IS-U Smart Assistant

> Enterprise AI Assistant for SAP IS-U powered by **Llama 3**, **RAG**, and **Document Intelligence**.

---

## 📖 Overview

IS-U Smart Assistant is an intelligent enterprise assistant designed to simplify the validation and analysis of SAP IS-U business documents.

The assistant is capable of understanding multiple document formats (XML, PDF, DOCX, XLSX, CSV, JSON...), extracting business information, validating data against SAP IS-U, and providing intelligent recommendations using a local Large Language Model (LLM).

This project is developed as part of an internship at **Iliade Consulting**.

---

## 🎯 Objectives

The main objectives of this project are:

- Analyze C15 XML subscription flows
- Read enterprise documents
- Validate SAP IS-U business objects
- Detect business inconsistencies
- Answer user questions using AI
- Reduce manual verification time
- Provide intelligent recommendations

---

## ✨ Features

### 📄 Document Analysis

- XML
- PDF
- DOCX
- XLSX
- CSV
- JSON

---

### 🧠 Artificial Intelligence

- Local LLM (Llama 3)
- Retrieval-Augmented Generation (RAG)
- Semantic Search
- Intelligent Question Answering

---

### ⚡ SAP Integration

- Business Partner validation
- Installation validation
- Contract validation
- Point of Delivery (PDL) validation
- Business rule verification

---

### 💬 Chat Interface

- Natural language conversations
- Enterprise knowledge assistant
- Context-aware responses

---

## 🏗️ Project Architecture

```
IS-U_Smart_Assistant
│
├── chatbot/
├── documents/
├── llm/
├── rag/
├── sap/
├── ui/
├── utils/
│
├── data/
│   ├── uploads/
│   ├── processed/
│   └── chroma_db/
│
├── knowledge/
│
├── tests/
│
├── app.py
├── README.md
├── requirements.txt
└── .gitignore
```

---

## 🛠️ Technologies

| Category | Technologies |
|-----------|--------------|
| Language | Python 3.12 |
| LLM | Llama 3 (8B) |
| AI Runtime | Ollama |
| RAG | LlamaIndex |
| Vector Database | ChromaDB |
| Web Interface | Streamlit |
| XML Parsing | lxml |
| PDF | PyMuPDF |
| Office Documents | python-docx / openpyxl |
| Data Analysis | Pandas |
| Version Control | Git + GitHub |

---

## 🚀 Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/IS-U_Smart_Assistant.git
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate it

Windows

```powershell
.\.venv\Scripts\Activate.ps1
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🚀 Running the application

```bash
streamlit run app.py
```

---

## 📅 Roadmap

- [x] Project initialization
- [x] Development planning
- [x] Architecture design
- [ ] Chat interface
- [ ] Llama 3 integration
- [ ] XML analysis
- [ ] Multi-document support
- [ ] RAG implementation
- [ ] SAP connector
- [ ] Intelligent recommendations
- [ ] Production release (v1.0)

---

## 👨‍💻 Author

**Med Aziz Garwachi**

Software Engineering Student

Intern at **Iliade Consulting**

---

## 📄 License

This project is developed for educational and internship purposes.