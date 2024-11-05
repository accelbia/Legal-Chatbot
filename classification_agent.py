from llama_model import Llama3Model

class ClassificationAgent:
    def __init__(self):
        self.model = Llama3Model()

    def classify_query(self, query):
        classification = self.model.get_response(f"Classify this legal query: {query}")
        return classification
