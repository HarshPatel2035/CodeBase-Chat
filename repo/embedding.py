from sentence_transformers import SentenceTransformer

def convert_to_embeddings(data):
    model = SentenceTransformer('BAAI/bge-small-en-v1.5')
    dim = model.get_sentence_embedding_dimension()
    print(f"Embedding dimention is {dim}")
    print("Model is converting text into embeddings....")
    embeddings = model.encode(data)
    print(f"{len(embeddings)} Embeddings generated.")
    return embeddings