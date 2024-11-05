from llama_model import Llama3Model

class QueryRewriter:
    def __init__(self):
        self.model = Llama3Model()

    def rewrite_query(self, query):
        rewritten_query = self.model.get_response(f"Rewrite this legal query for clarity: {query}")
        return rewritten_query
