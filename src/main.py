from fastapi import FastAPI
from src.db.database import engine
from src.routes.login import router



app = FastAPI(
    title="RAG API",
    description="Retrieval Augmented Generation API",
    version="1.0.0",
)



@app.get("/")
def root():
    return {
        "message": "RAG API is running"
    }

app.include_router(router)

with engine.connect() as connection:
    print("Connection successful!")

