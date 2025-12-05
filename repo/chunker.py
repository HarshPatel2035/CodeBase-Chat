from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import DirectoryLoader,TextLoader
from langchain_core.documents import Document
import os


def chunker(dir_name):
    
    documents = []
        
    for root, _, files in os.walk(dir_name):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                    text = f.read()

                if text.count("�") > 5:
                    print(f"⏩ Skipping corrupted file: {file_path}")
                    continue

                documents.append(Document(
                    page_content = text,
                    metadata = {
                        'source' : file_path
                    }  
                ))

            except Exception as e:
                print(f"⚠️ Could not load file: {file_path} — {e}")
                continue

        print(f"📄 Loaded {len(documents)} text/code files successfully")

    data = documents
    chunk_size = 150
    chunk_overlap = 50
    chunks = []
    
    for file in data:
        content = file.page_content.split('\n')
        lines = len(content)
        j = 0
        i = 0
        while j<lines:
            i += 1
            text = "\n".join(content[j:j+chunk_size])
            start_line = j+1
            finish_line = j+chunk_size
            if finish_line>lines: finish_line = lines
            j+=chunk_size-chunk_overlap
            chunk = Document(
                page_content = text,
                metadata = {"source":file.metadata['source'], "line_start":start_line,"finish_line":finish_line}
            )
            chunks.append(chunk)
        print(f"Chunking file : {file.metadata['source']} ---> {i} chunks")
    print(len(chunks))
    return chunks

