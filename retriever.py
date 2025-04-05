from sentence_transformers import SentenceTransformer
from vector_store import VectorStore
from preprocessing import read_pdf, preprocess_text

class Retriever:
    def __init__(self, model_name = "paraphrase-MiniLM-L6-v2", dim= 384):
        """
        paraphrase-MiniLM-L6-v2 model for embedding
        dim = 384 dimension for vector store
        """
        self.model = SentenceTransformer(model_name)
        self.vector_store = VectorStore(dim)
    
    def index_documents(self, file_path:str):
        raw_text = read_pdf(file_path)
        preprocessed_text = preprocess_text(raw_text)
        chunks = self.split_into_chunks(preprocessed_text)
        embeddings = self.model.encode(chunks)
        self.vector_store.add_vectors(embeddings, chunks)

    def split_into_chunks(self, text:str, chunk_size= 100) -> list[str]:
        return [text[i:i+chunk_size] for i in range(0,len(text), chunk_size)]
    
    def search(self, query:str, top_k = 4) -> list[str]:
        query_vector = self.model.encode([query])[0]
        return self.vector_store.search(query_vector,top_k)
    
if __name__ == "__main__":
    file = "/Users/abilaasha/Documents/GitHub/Abi Github/RAG implementation/data/Clinical Query Agent FAQ.pdf"
    retriever = Retriever()
    retriever.index_documents(file)

    query = "What is clinical query agent?"
    result = retriever.search(query=query)
    print(result)