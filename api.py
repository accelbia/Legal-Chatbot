from fastapi import FastAPI
from prompt_generator import PromptGenerator
from classification_agent import ClassificationAgent
from query_rewriter import QueryRewriter
from vector_database import VectorDatabase

app = FastAPI()

query_rewriter = QueryRewriter()
classification_agent = ClassificationAgent()
prompt_generator = PromptGenerator()
vector_db = VectorDatabase()

@app.post("/ask/")
async def ask_question(query: str):
    # Step 1: Rewrite the query
    rewritten_query = query_rewriter.rewrite_query(query)
    
    # Step 2: Classify the query
    classification = classification_agent.classify_query(rewritten_query)
    
    # Step 3: Generate the prompt
    prompt = prompt_generator.generate_prompt(rewritten_query)
    
    # Step 4: Store in Vector Database (simulation)
    vector_db.store_embedding(rewritten_query, prompt)
    
    # Step 5: Retrieve similar documents (simulated)
    similar_docs = vector_db.get_similar(rewritten_query)
    
    return {
        "classification": classification,
        "prompt": prompt,
        "similar_docs": similar_docs
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
