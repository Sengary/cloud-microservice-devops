from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# In-memory quote DB
quotes = []

class Quote(BaseModel):
    author: str
    content: str

@app.get("/")
def root():
    return {"message": "Quote Manager API"}

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/quotes")
def get_quotes():
    return quotes

@app.post("/quotes")
def add_quote(quote: Quote):
    if not quote.content.strip():
        raise HTTPException(status_code=400, detail="Quote content cannot be empty.")
    quotes.append(quote)
    return {"message": "Quote added successfully."}
