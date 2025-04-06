# RAG-implementation


Here's a demo of how this works
https://youtu.be/4Mw9OyBW_Fk?feature=shared

---

```markdown
# Retrieval-Augmented Generation (RAG) Implementation

This repository presents a complete implementation of a **Retrieval-Augmented Generation (RAG)** pipeline, a powerful method that combines retrieval of external knowledge with the generative capabilities of large language models (LLMs). This allows the model to generate grounded, fact-based answers even when the base LLM has limited contextual memory or out-of-date information.

## 🔍 What is RAG?

**RAG** (Retrieval-Augmented Generation) is a hybrid approach that improves the quality and accuracy of LLM responses by fetching relevant external documents at runtime. Instead of relying solely on the model’s training data, it:

1. **Retrieves**: Fetches relevant chunks from a knowledge base.
2. **Augments**: Passes these chunks along with the user query to the LLM.
3. **Generates**: Produces responses grounded in the retrieved context.

This makes RAG particularly useful for domain-specific Q&A systems, internal knowledge bases, technical documentation bots, and more.

---

## 🧠 How the Code Works

The implementation is broken into modular components that mimic the standard RAG workflow. Here's a breakdown of what happens when you run `main.py`:

### 1. **Document Preprocessing**
- Input: Files inside the `data/` folder.
- The `preprocessing.py` script reads these files and splits them into manageable **chunks** based on a specified `chunk_size`.
- These chunks are preprocessed (e.g., cleaned, normalized) before embedding.

### 2. **Embedding Generation**
- Embeddings are generated for each text chunk using a language model (like Sentence Transformers or OpenAI embeddings, configurable in `rag_config.yaml`).
- The embeddings capture semantic meaning of the text for similarity comparison.

### 3. **Vector Store Setup**
- The `vector_store.py` module stores the embeddings into a vector database (like FAISS, Chroma, or any in-memory vector store).
- This enables fast similarity search during retrieval.

### 4. **Retriever Module**
- Given a query, the `retriever.py` finds the most relevant document chunks by comparing query embeddings with stored vectors.
- Top-k matches are retrieved (k is configurable in the YAML file).

### 5. **Generator Module**
- The `generator/` module takes in:
  - The user query.
  - The retrieved document chunks.
- These are passed to a language model (LLM) which synthesizes a final answer using both the query and context.

### 6. **End-to-End Orchestration**
- `main.py` ties everything together:
  - Loads config from `rag_config.yaml`.
  - Loads and preprocesses documents.
  - Builds the vector store.
  - Takes user query input.
  - Retrieves relevant chunks.
  - Generates and displays the answer.

---

## ✨ Features

- Modular and easy to extend.
- Uses external documents as dynamic knowledge base.
- Logs everything in `rag_pipeline.log`.
- Simple config with `rag_config.yaml`.

---

## ⚙️ Installation

```bash
git clone https://github.com/Abilaashab/RAG-implementation.git
cd RAG-implementation
python3 -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

---

## 🔧 Configuration

Edit `rag_config.yaml` to control:

- Embedding model type
- Chunk size
- Number of top documents to retrieve
- Generator model (LLM)
- Vector store backend

---

## 🚀 Usage

1. Put your documents inside the `data/` folder.
2. Open your terminal and run:

```bash
python main.py
```

3. Enter your query when prompted.
4. The model will retrieve context, generate an answer, and show the result.

---

## 📁 Project Structure

```
.
├── data/                # Input documents
├── generator/           # Generation logic using LLM
├── preprocessing.py     # Document chunking and cleaning
├── retriever.py         # Similarity search
├── vector_store.py      # Vector storage and retrieval
├── main.py              # Entry point of the pipeline
├── rag_config.yaml      # Configurations for the RAG pipeline
├── requirements.txt     # Python dependencies
├── rag_pipeline.log     # Execution logs
```

---

