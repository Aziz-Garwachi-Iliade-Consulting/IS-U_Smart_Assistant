# IS-U Smart Assistant

An intelligent assistant for SAP IS-U, powered by LLaMA and Retrieval-Augmented Generation (RAG).

## Project Structure

```
IS-U_Smart_Assistant/
├── app.py                  # Main application entry point
├── chatbot/                # Chatbot logic and prompt templates
├── documents/              # Document readers (XML, PDF, DOCX, Excel, CSV, JSON)
├── llm/                    # LLaMA client and LLM integration
├── rag/                    # RAG pipeline (indexing, retrieval, vector store)
├── sap/                    # SAP IS-U connectivity and queries
├── ui/                     # Streamlit user interface
├── knowledge/              # Business rules, documentation, SAP help
├── data/                   # Uploads, processed files, ChromaDB storage
├── tests/                  # Unit and integration tests
└── utils/                  # Configuration and logging utilities
```

## Getting Started

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the application:**
   ```bash
   streamlit run app.py
   ```

## License

Internal use only — Iliade Consulting.
