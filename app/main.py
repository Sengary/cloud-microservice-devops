from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
import random

# Fast API Variable
app = FastAPI()


# Quote schema
class Quote(BaseModel):
    author: str
    content: str


class QuoteWithID(Quote):
    id: int


# In-memory DB with auto-incrementing ID
quotes = []
next_id = 1


@app.get("/")
def root():
    return {"message": "Quote Manager API"}


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/quotes", response_model=list[QuoteWithID])
def get_all_quotes():
    return quotes

# Add quote code


@app.post("/quotes", response_model=QuoteWithID)
def add_quote(quote: Quote):
    global next_id
    if not quote.content.strip():
        raise HTTPException(
            status_code=400,
            detail="Quote content cannot be empty."
        )

    new_quote = quote.model_dump()
    new_quote["id"] = next_id
    quotes.append(new_quote)
    next_id += 1
    return new_quote


@app.get("/quotes/{quote_id}", response_model=QuoteWithID)
def get_quote_by_id(quote_id: int):
    for quote in quotes:
        if quote["id"] == quote_id:
            return quote
    raise HTTPException(status_code=404, detail="Quote not found")


@app.put("/quotes/{quote_id}", response_model=QuoteWithID)
def update_quote(quote_id: int, updated_quote: Quote):
    for quote in quotes:
        if quote["id"] == quote_id:
            quote["author"] = updated_quote.author
            quote["content"] = updated_quote.content
            return quote
    raise HTTPException(status_code=404, detail="Quote not found")

@app.get("/quotes/search", response_model=list[QuoteWithID])
def search_quotes(author: str = Query(None), content: str = Query(None)):
    results = quotes

    if author:
        results = [q for q in results if author.lower() in q["author"].lower()]
    if content:
        results = [q for q in results if content.lower() in q["content"].lower()]

    if not results:
        raise HTTPException(status_code=404, detail="No matching quotes found.")
    return results
    
@app.get("/quotes/random", response_model=QuoteWithID)
def get_random_quote():
    if not quotes:
        raise HTTPException(status_code=404, detail="No quotes available.")
    return random.choice(quotes)


@app.get("/quotes/count")
def get_quote_count():
    return {"count": len(quotes)}


# Added by Abdulrahman Sharqawi – validation improvement

# Delete quote


@app.delete("/quotes/{quote_id}")
def delete_quote(quote_id: int):
    for index, quote in enumerate(quotes):
        if quote["id"] == quote_id:
            del quotes[index]
            return {"message": "Quote deleted"}
    raise HTTPException(status_code=404, detail="Quote not found")
