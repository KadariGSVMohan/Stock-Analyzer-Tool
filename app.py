import os
import streamlit as st
import pickle
import time
from dotenv import load_dotenv
from langchain import OpenAI
from langchain.chains import RetrievalQAWithSourcesChain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import UnstructuredURLLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(page_title="News Research Tool", page_icon="📰", layout="wide")

# Title and header
st.markdown("<h1 style='text-align: center;'>📰 News Research Assistant</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: gray;'>Summarize and research news from any URL using AI</h4>", unsafe_allow_html=True)
st.write("---")

# Sidebar input section
st.sidebar.header("🔗 Enter News Article URLs")
urls = []
for i in range(3):
    url = st.sidebar.text_input(f"URL {i + 1}", placeholder="Paste article link here...")
    if url:
        urls.append(url)

process_url_clicked = st.sidebar.button("🚀 Process Articles")

# Placeholder for status updates
status_placeholder = st.empty()
file_path = "faiss_store_openai.pkl"
llm = OpenAI(temperature=0.9, max_tokens=500)

# Processing URLs and building FAISS vector index
if process_url_clicked:
    if len(urls) == 0:
        st.sidebar.warning("Please enter at least one valid URL.")
    else:
        try:
            status_placeholder.info("🔄 Loading data from URLs...")
            loader = UnstructuredURLLoader(urls=urls)
            data = loader.load()

            status_placeholder.info("🔍 Splitting text into chunks...")
            text_splitter = RecursiveCharacterTextSplitter(
                separators=["\n\n", "\n", ".", ","],
                chunk_size=1000
            )
            docs = text_splitter.split_documents(data)

            status_placeholder.info("🧠 Generating embeddings...")
            embeddings = OpenAIEmbeddings()
            vectorstore_openai = FAISS.from_documents(docs, embeddings)
            pkl = vectorstore_openai.serialize_to_bytes()

            with open(file_path, "wb") as f:
                pickle.dump(pkl, f)

            status_placeholder.success("✅ Articles processed and vector store built!")
        except Exception as e:
            status_placeholder.error(f"❌ Error: {e}")

# Question-Answering section
st.write("## 🤖 Ask a Question Based on the Articles")
query = st.text_input("Enter your question here...")

if query:
    if not os.path.exists(file_path):
        st.warning("Please process at least one article first.")
    else:
        with open(file_path, "rb") as f:
            pkl = pickle.load(f)
            vectorstore = FAISS.deserialize_from_bytes(
                embeddings=OpenAIEmbeddings(),
                serialized=pkl,
                allow_dangerous_deserialization=True
            )
            chain = RetrievalQAWithSourcesChain.from_llm(llm=llm, retriever=vectorstore.as_retriever())

            with st.spinner("💬 Generating answer..."):
                result = chain({"question": query}, return_only_outputs=True)

            # Display result
            st.success("✅ Answer generated!")
            st.markdown("### 📌 Answer")
            st.write(result.get("answer", "No answer found."))

            # Display sources
            sources = result.get("sources", "")
            if sources:
                st.markdown("### 📚 Sources")
                for source in sources.split("\n"):
                    st.write(f"- {source}")
