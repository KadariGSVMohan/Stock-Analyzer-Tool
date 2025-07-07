---
## 📰 News Research Tool
> 📈 AI-powered research assistant to analyze and summarize online news articles from URLs using LangChain, OpenAI, and FAISS — with an interactive Streamlit UI.
---

### 🚀 Features
* 🔗 Accepts up to 3 news URLs
* ✂️ Auto splits long content into manageable chunks
* 🧠 Generates embeddings using OpenAI's model
* 🔍 Answers your questions with sources from the articles
* 💬 Clean, centered, interactive Streamlit UI
---

### 🖥️ Demo
![News Research Tool UI Screenshot](screenshot.png)
---

### 🧩 Tech Stack
* **Streamlit** – Frontend app UI
* **LangChain** – LLM orchestration
* **OpenAI** – For language model and embeddings
* **FAISS** – Vector database for semantic search
* **Unstructured** – URL content extraction
---
### ⚙️ Setup Instructions
1. **Clone the Repository**
```bash
git clone https://github.com/gsvmohsan/Stock-Analyzer-Tool.git
cd news-research-tool
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
Or, manually install:
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
---
### 📁 File Structure
```bash
news-research-tool/
│
├── app.py               # Main Streamlit application
├── faiss_store_openai.pkl # Pickle file for saved FAISS index
├── .env                 # API key environment variables
├── requirements.txt     # Python dependencies
└── README.md            # Project overview and setup
```
---
### ✅ Sample Use Cases
* Research financial or political news
* Get quick answers from multiple articles
* Compare how different news sources report the same event
---
### ❓ FAQ
**Q: Do I need an OpenAI key?**
Yes, this project uses OpenAI for embeddings and answers.
**Q: What if I don’t want to use OpenAI?**
You can swap out `OpenAIEmbeddings` with a local embedding model like HuggingFace + Chroma DB.
---
### 🙌 Credits

* Built with ❤️ using [LangChain](https://www.langchain.com/), [OpenAI](https://openai.com/), and [Streamlit](https://streamlit.io/)
* `unstructured` for robust article content loading
---
