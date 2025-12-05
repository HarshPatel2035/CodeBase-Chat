import os
import chromadb
import uuid

class VectorStore():
    def __init__(self,collection_name='coding_files',persistent_directory='../data'):
        self.collection_name = collection_name
        self.persistent_directory = persistent_directory
        self.client = None
        self.collection = None
        self._initialise_store()

    def _initialise_store(self):
        try : 
            os.makedirs(self.persistent_directory,exist_ok=True)
            self.client = chromadb.PersistentClient(path=self.persistent_directory)

            self.collection = self.client.get_or_create_collection(name=self.collection_name,metadata={"description":"Repositery files for RAG Application"})
            print(f"VectorStore Initialised. Collection : {self.collection_name}")
        except Exception as e :
            print(f"Error Initialising store : {e}")

    def add_documents(self,documents,embeddings):
        ids = []
        document_texts = []
        metadatas = []
        embeddings_list = []

        if len(documents) != len(embeddings):
            raise ValueError("Length of documents and embedding must be same")

        for i,(doc,embedding) in enumerate(zip(documents,embeddings)):
            id = f"_{uuid.uuid4().hex[:8]}_{i}"
            ids.append(id)
            metadata = dict(doc.metadata)
            metadata['doc_index'] = i
            metadata['content_length'] = len(doc.page_content)

            metadatas.append(metadata)
            document_texts.append(doc.page_content)
            embeddings_list.append(embedding.tolist())

        try :
            self.collection.add(
                ids=ids,
                embeddings=embeddings_list,
                metadatas=metadatas,
                documents=document_texts,
            )
            print("Documents added successfully to vector store")
        except Exception as e:
            print(f"Error adding documents in vector store : {e}")

