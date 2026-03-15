from fastapi import FastAPI

app = FastAPI(title="NeuralOps Nucleus")

@app.get("/")
def read_root():
    return {"status": "online", "message": "Nucleus AI Brain is active"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}