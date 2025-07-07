## 📄 Document Analyzer Tool

> 📈 AI-powered research assistant to analyze and summarize **online documents or news articles from URLs** using LangChain, OpenAI, and FAISS — with an interactive Streamlit UI.
### 🚀 Features
* 🔗 Accepts up to 3 document or article URLs
* ✂️ Automatically splits long content into manageable chunks
* 🧠 Generates embeddings using OpenAI's model
* 🔍 Answers your questions with source references
* 💬 Clean, centered, interactive Streamlit UI
### 🖥️ Demo

![Document Analyzer Tool UI Screenshot](screenshot.png)

### 🧩 Tech Stack

* **Streamlit** – Frontend app UI
* **LangChain** – LLM orchestration
* **OpenAI** – For language model and embeddings
* **FAISS** – Vector database for semantic search
* **Unstructured** – URL content extraction

### ⚙️ Setup Instructions

1. **Clone the Repository**

```bash
git clone https://github.com/gsvmohsan/Document-Analyzer-Tool.git
cd document-analyzer-tool
```

2. **Create Virtual Environment (optional but recommended)**

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

3. **Install Required Packages**

```bash
pip install -r requirements.txt
```

Or manually install:

```bash
pip install streamlit langchain openai faiss-cpu tiktoken "unstructured[all-docs]" python-dotenv
```

4. **Set Up Environment Variables**

Create a `.env` file in the root directory:

```env
OPENAI_API_KEY=your_openai_api_key
```

5. **Run the Streamlit App**

```bash
streamlit run app.py
```


📁 File Structure
bash
document-analyzer-tool/
│
├── app.py                  # Main Streamlit application
├── faiss_store_openai.pkl  # Pickle file for saved FAISS index
├── .env                    # API key environment variables
├── requirements.txt        # Python dependencies
└── README.md               # Project overview and setup


### ✅ Sample Use Cases

* Analyze and compare financial or political news articles
* Quickly extract insights from multiple sources
* Summarize documents and ask AI-driven questions about their content

### 🙌 Credits

* Built with ❤️ using [LangChain](https://www.langchain.com/), [OpenAI](https://openai.com/), and [Streamlit](https://streamlit.io/)
* Powered by [`unstructured`](https://github.com/Unstructured-IO/unstructured) for robust content extraction
