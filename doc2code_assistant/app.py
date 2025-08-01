import streamlit as st
from llama_index.core import (
    VectorStoreIndex,
    SimpleDirectoryReader,
    StorageContext,
    load_index_from_storage,
)
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
import os

os.environ["OPENAI_API_KEY"] = ""  # 🔒 Evita uso accidental de OpenAI

PERSIST_DIR = "./my_index"

import subprocess

def detectar_uso_gpu():
    try:
        result = subprocess.check_output(["nvidia-smi", "--query-compute-apps=pid,process_name,used_gpu_memory", "--format=csv,noheader,nounits"])
        result = result.decode("utf-8").strip().split("\n")
        for line in result:
            if "ollama" in line.lower():
                pid, proc, mem = line.split(",")
                return f"✅ GPU in use by Ollama (PID {pid.strip()}, {mem.strip()} MiB)"
        return "⚠️ Ollama is not currently using the GPU."
    except Exception as e:
        return f"❌ GPU usage could not be verified: {e}"


@st.cache_resource
def load_or_create_index():
    #llm = Ollama(model="phi3:mini")
    llm = Ollama(model="codellama:7b")
    embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")

    if os.path.exists(PERSIST_DIR):
        storage_context = StorageContext.from_defaults(persist_dir=PERSIST_DIR)
        index = load_index_from_storage(storage_context, llm=llm, embed_model=embed_model)
    else:
        documents = SimpleDirectoryReader(input_dir="docs",recursive=True).load_data()
        index = VectorStoreIndex.from_documents(
            documents, llm=llm, embed_model=embed_model
        )
        index.storage_context.persist(persist_dir=PERSIST_DIR)

    return index, llm

# Mostrar estado de la GPU
estado_gpu = detectar_uso_gpu()
st.info(f"🖥️ GPU State: {estado_gpu}")

st.set_page_config(page_title="Documentation Based Assistant", layout="centered")
st.title("📚 Documentation Based Assistant")
st.write("Ask questions about your locally uploaded documentation.")

# Cargar o crear el índice
index, llm = load_or_create_index()
query_engine = index.as_query_engine(llm=llm)

# Interfaz
question = st.text_input("🔍 Ask your question about the documentation:")

if question:
    with st.spinner("Thinking..."):
        answer = query_engine.query(question)
        st.markdown("### 🧠 Answer:")
        st.write(answer.response)

def main():
    import streamlit.web.bootstrap
    streamlit.web.bootstrap.run("doc2code_assistant/app.py", "", [], [])
