from retriever import Retriever
from generator.generator import generator
from generator.prompt_templates import create_prompt

class RAGPipeline:
    def __init__(self, retriever_model="sentence-transformers/all-MiniLM-L6-v2", generator_model="gemini-1.5-flash"):
        self.retriever = Retriever(retriever_model)
        self.generator = generator(generator_model)


    def run(self, query:str, file_path:str, top_k=2) -> str:
        """Returns the response based on query and content of given file using llm.

        Args:
            query (_type_): User's actual query.
            file_path (_type_): Path of the file or document used to retrieve content related to the query.
            top_k (int, optional): Number of top matched content of document with query to return. Defaults to 4.

        Returns:
            str: Response from the generator. 
        """
       
        self.retriever.index_documents(file_path)
        context = self.retriever.search(query, top_k)
        prompt = create_prompt(query, context)
        return self.generator.generate(prompt)