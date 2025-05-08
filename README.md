## ITC Financial Report AI Assistant
This project is an AI-powered assistant that allows users to query ITC Limited’s financial reports using natural language. It uses PDF scraping, sentence embeddings, FAISS vector search, and a language model to retrieve and answer questions based on the financial data.

## 📁 Project Structure:
ITC assignment/

│

├── app.py                 # Streamlit app

├── query_llm.py          # Code to load FAISS index and query with LLM

├── pdf_scraper.py        # Extracts text, chunks it, and creates FAISS index

├── itc_financial_report.pdf  # PDF file containing ITC report

├── faiss.idx             # Saved FAISS index (auto-generated)

├── texts.npy             # Saved text chunks (auto-generated)

├── metas.npy             # Saved metadata (auto-generated)

└── README.md             # You are here!

### 🧰 Setup Instructions
## 1. 📦 Install Required Libraries
Use a virtual environment and install the required packages:

```pip install streamlit sentence-transformers faiss-cpu numpy pymupdf```

## 2. 📄 Add the Financial Report PDF
Ensure the file itc_financial_report.pdf is in the project root folder. This is the document from which data is extracted.

## 3. 🧠 Run the PDF Scraper Script
This script extracts text from the PDF, chunks it, generates embeddings, and creates the FAISS index:

```python pdf_scraper.py```

It will create the following files:

faiss.idx — FAISS vector index

texts.npy — Embedded text chunks

metas.npy — Metadata with page numbers

## 4. 🚀 Run the Streamlit App
Once the index is created, run the app:

```streamlit run app.py```

## 💬 LLM Integration
In query_llm.py, the loaded FAISS index is used to find relevant document chunks based on user queries. You can integrate OpenAI, Anthropic, or other LLM APIs to generate answers using the retrieved context.

