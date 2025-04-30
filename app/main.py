from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from typing import List

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



## Add multiple quotes 
@app.post("/quotes/bulk", response_model=list[QuoteWithID])
def add_multiple_quotes(quotes_list: List[Quote]):
    global next_id
    added_quotes = []
    for quote in quotes_list:
        if not quote.content.strip():
            continue  # skip empty content
        new_quote = quote.model_dump()
        new_quote["id"] = next_id
        quotes.append(new_quote)
        added_quotes.append(new_quote)
        next_id += 1
    return added_quotes


@app.get("/")
def root():
    return {"message": "Quote Manager API"}


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/quotes", response_model=list[QuoteWithID])
def get_all_quotes():
    return quotes


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
    raise HTTPException(
        status_code=404,
        detail="Quote not found"
    )


@app.put("/quotes/{quote_id}", response_model=QuoteWithID)
def update_quote(quote_id: int, updated_quote: Quote):
    for quote in quotes:
        if quote["id"] == quote_id:
            quote["author"] = updated_quote.author
            quote["content"] = updated_quote.content
            return quote
    raise HTTPException(
        status_code=404,
        detail="Quote not found"
    )


@app.delete("/quotes/{quote_id}")
def delete_quote(quote_id: int):
    for index, quote in enumerate(quotes):
        if quote["id"] == quote_id:
            del quotes[index]
            return {"message": "Quote deleted"}
    raise HTTPException(
        status_code=404,
        detail="Quote not found"
    )


@app.get("/quotes/search", response_model=list[QuoteWithID])
def search_quotes_by_author(author: str = Query(..., min_length=1)):
    matched = [q for q in quotes if author.lower() in q["author"].lower()]
    if not matched:
        raise HTTPException(
            status_code=404,
            detail="No quotes found for this author"
        )
    return matched
