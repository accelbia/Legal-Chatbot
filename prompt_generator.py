from llama_model import Llama3Model

class PromptGenerator:
    def __init__(self):
        self.model = Llama3Model()

    def generate_prompt(self, query):
        refined_prompt = self.model.get_response(f"Generate a detailed prompt for this legal question: {query}")
        return refined_prompt
