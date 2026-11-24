# 🤖 AI PDF Chatbot — RAG Application using Gemini

A **Retrieval-Augmented Generation (RAG)** chatbot that lets you upload any PDF and ask natural language questions about it. The app retrieves the most relevant sections of the document and uses Google's Gemini model to generate accurate, context-grounded answers — reducing hallucination and keeping responses grounded in your actual data.

> 🧩 **Built step by step, from scratch.** This project was built incrementally, one concept at a time (PDF reading → chunking → embeddings → vector search → LLM answer generation), with each step tested independently. The `step1_*.py` to `step8_*.py` files are that exact journey — kept intentionally so anyone can follow the same path.
>
> 👶 **Beginner-friendly by design.** New to RAG or LLM applications? Don't jump straight into `app.py`. Start from `step1_pdf_reader.py` and move forward one file at a time — each script builds on the last and shows exactly one new concept.

---

## ✨ Features

- 📄 **Multi-PDF upload** — process one or several PDFs at once
- ✂️ **Smart chunking** — splits documents into overlapping chunks for better context retention
- 🧠 **Semantic embeddings** — powered by Google's `gemini-embedding-001` model
- ⚡ **Fast vector search** — FAISS (`IndexFlatL2`) for similarity-based retrieval
- 💬 **Context-grounded answers** — powered by `gemini-3.5-flash` with strict "answer only from context" instruction to reduce hallucination
- 🛡️ **Graceful error handling** — warns on scanned/image PDFs, empty extractions, and chunking failures
- 🔑 **Flexible API key input** — set via `.env` file or enter directly in the sidebar
- 🖥️ **Simple Streamlit UI** — upload PDFs on one side, chat on the other

---

## 🏗️ How It Works

```
             ┌─────────────┐
             │   PDF(s)    │
             └──────┬──────┘
                    ▼
          Extract text (PyMuPDF)
                    ▼
       Split into chunks (LangChain)
                    ▼
    Generate embeddings (Gemini API)
                    ▼
      Build FAISS vector index
                    ▼
 ┌──────────────────────────────────┐
 │   User asks a question           │
 └──────────────────┬───────────────┘
                    ▼
       Embed the question (Gemini)
                    ▼
    Retrieve top-k similar chunks (FAISS)
                    ▼
  Generate answer from context (Gemini)
                    ▼
              💬 Final Answer
```

---

## 🛠️ Tech Stack

| Component         | Technology                                                       |
|-------------------|------------------------------------------------------------------|
| UI                | Streamlit                                                        |
| LLM               | Google Gemini (`gemini-3.5-flash`, fallback: `gemini-2.5-flash-lite`) |
| Embeddings        | Google Gemini (`gemini-embedding-001`)                           |
| Vector Search     | FAISS (`IndexFlatL2`)                                            |
| Text Chunking     | LangChain `RecursiveCharacterTextSplitter`                      |
| PDF Parsing       | PyMuPDF (`fitz`)                                                 |
| Config Management | python-dotenv                                                    |

---

## 📁 Project Structure

```
AI-PDF-Assistant/
├── app.py                     # Streamlit app (main entry point)
├── utils/
│   ├── pdf_reader.py          # Extract text from PDFs
│   ├── chunking.py            # Split text into chunks
│   ├── embedding.py           # Generate embeddings via Gemini
│   ├── vector_store.py        # Build FAISS index
│   ├── retriever.py           # Retrieve top-k relevant chunks
│   ├── storage.py             # Save/load FAISS index + chunks
│   └── llm.py                 # Generate final answer via Gemini
├── step1_pdf_reader.py        #
├── step2_chunking.py          #
├── step3_embedding.py         #  Development journey —
├── step4_vector_store.py      #  incremental scripts built
├── step5_retriever.py         #  step by step
├── step6_rag.py               #
├── step7_build_index.py       #
├── step8_chat.py              #
├── requirements.txt
├── .env.example               # Sample env file (no real key)
└── sample.pdf                 # Example PDF for testing
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/ai-pdf-chatbot.git
cd ai-pdf-chatbot
```

### 2. Create a virtual environment

```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS / Linux
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up your API key

Copy `.env.example` to `.env` and add your Gemini API key:

```env
GOOGLE_API_KEY=your_google_gemini_api_key_here
```

> 🔑 Get a **free** API key from [Google AI Studio](https://aistudio.google.com/).
>
> Alternatively, you can skip the `.env` file and enter your API key directly in the **sidebar** when the app starts.

### 5. Run the app

```bash
streamlit run app.py
```

Open [http://localhost:8501](http://localhost:8501) in your browser.

---

## 🖥️ Usage

1. **Upload** one or more text-based PDF files using the left panel.
2. Click **🚀 Process PDFs** to extract text, generate embeddings, and build the knowledge base.
3. Type your question in the **Chat** panel on the right and click **Ask**.
4. The app retrieves the most relevant document sections and generates a grounded answer.

> ⚠️ **Note:** Only text-layer PDFs are supported. Scanned or image-only PDFs cannot be parsed. Use an OCR tool first if needed.

---

## 👶 New to RAG? Learn It Step by Step

Walk through these files in order — each adds exactly one new concept:

| Step | File | What you'll learn |
|------|------|-------------------|
| 1 | `step1_pdf_reader.py` | Extracting raw text from a PDF |
| 2 | `step2_chunking.py` | Splitting long text into overlapping chunks |
| 3 | `step3_embedding.py` | Turning text chunks into vector embeddings |
| 4 | `step4_vector_store.py` | Storing embeddings in a FAISS index |
| 5 | `step5_retriever.py` | Retrieving the most relevant chunks for a query |
| 6 | `step6_rag.py` | Combining retrieval with LLM answer generation |
| 7 | `step7_build_index.py` | Saving the vector store to disk |
| 8 | `step8_chat.py` | Loading the saved index and chatting in a terminal loop |

Run any step directly (requires `.env` with your API key):

```bash
python step1_pdf_reader.py
```

---

## 🧪 Command-Line Alternative

Prefer working from the terminal? Build and query the index without the UI:

```bash
python step7_build_index.py   # Build and save the FAISS index
python step8_chat.py          # Chat with your document in the terminal
```

---

## ⚙️ Environment Variables

| Variable       | Required | Description                                                                 |
|----------------|----------|-----------------------------------------------------------------------------|
| `GOOGLE_API_KEY` | ✅ Yes  | Your Gemini API key from [Google AI Studio](https://aistudio.google.com/)  |
| `GEMINI_MODEL`   | ❌ No   | Override the LLM model (default: `gemini-3.5-flash`)                       |

---

## 🔮 Future Improvements

- [ ] Support for multiple file types (DOCX, TXT, CSV)
- [ ] OCR support for scanned/image PDFs
- [ ] Source citation (show which chunk/page an answer came from)
- [ ] Conversation memory for follow-up questions
- [ ] Deploy on Streamlit Community Cloud

---

## 📄 License

This project is open source and available for learning purposes.
