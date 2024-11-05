# llama_model.py
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

class Llama3Model:
    def __init__(self):
        self.model_name = "llama-3"  # Replace with actual model path or identifier for fine-tuning
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        self.model = AutoModelForCausalLM.from_pretrained(self.model_name)

    def get_response(self, input_text):
        inputs = self.tokenizer(input_text, return_tensors="pt")
        with torch.no_grad():  # Disable gradient calculations
            outputs = self.model.generate(inputs["input_ids"], max_length=150)
        response = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return response
