# CodeBase-Chat
AI-powered codebase understanding using RAG, local embeddings, and Chroma vector search. Automatically clones, filters, chunks, and indexes GitHub repos with metadata for precise source citations.


---

## 🧱 Tech Stack

- Python
- LangChain
- Groq LLaMA 3.3 API (70B Versatile)
- FAISS Vector Store
- Chroma DB Experimental Support
- Git + Local Repo Indexing
- Custom Chunker with file/line metadata


## Architecture Diagram


## 🧬 Architecture Diagram

```
+-----------------+
|  User Question  |
+-----------------+
          |
          v
+-----------------+        +---------------------+
| Query Embedding | -----> | Semantic Search     |
| via BGE / E5    |        | in Vector DB (Faiss)|
+-----------------+        +---------------------+
                                   |
                                   v
                         +---------------------+
                         | Top Ranked Code     |
                         | Chunks w/ Metadata  |
                         +---------------------+
                                   |
                                   v
+-------------------------+
| LLM (LLaMA 3.3 70B)     |
| Answer Synthesis        |
| (Context Grounded)      |
+-------------------------+
          |
          v
+---------------------------------------------+
| Final Answer with Filepaths + Line Numbers  |
+---------------------------------------------+
```


---

## 🔍 Supported File Types
`.py`, `.js`, `.ts`, `.md`, `.txt`, `.yml`, `.csv`, `.json`, `.rs`, `.go`

---

## 📊 Current Status
- RAG System: ✔ 93/100 retrieval accuracy benchmark  
- UI & Deployment: 🚧 (Coming soon)

---

## 📌 Coming Next
- Hybrid search (keyword + embeddings)
- Better code structure understanding with Tree-sitter
- Code snippet highlighting in UI
- React Frontend + FastAPI Backend deployment

---

## 🧑‍💻 Usage

🚧 Detailed usage steps coming after frontend integration…

---

## 🧪 Evaluation Results

Custom test benchmark on LangChain repo:  
**93% precision, grounded answers, minimal hallucination**

![score](https://img.shields.io/badge/RAG%20Score-93%2F100-brightgreen)

---

## 📎 License
MIT License

---

## 🌟 Support
If you like this project, please ⭐ the repo!  
Your feedback will power the next version of Codebase Chat!

