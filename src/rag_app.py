from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="VisionGenAI", version="0.1.0")


class InferenceRequest(BaseModel):
    image_url: str
    question: str
    prompt_profile: str = "default"


@app.get("/")
def home():
    return {
        "message": "VisionGenAI is running",
        "project": "RAG-enabled visual assistant",
        "status": "ok"
    }


@app.post("/infer")
def infer(req: InferenceRequest):
    # This is a placeholder for full RAG + LLM orchestration.
    # In a production implementation, this would:
    # 1. Fetch the image and metadata
    # 2. Generate embeddings or image features
    # 3. Search the vector store for relevant context
    # 4. Build a grounded prompt using retrieved documents
    # 5. Call the LLM and return a structured result
    return {
        "input": {
            "image_url": req.image_url,
            "question": req.question,
            "prompt_profile": req.prompt_profile,
        },
        "answer": "This endpoint is ready for RAG + LLM integration.",
        "status": "placeholder"
    }
