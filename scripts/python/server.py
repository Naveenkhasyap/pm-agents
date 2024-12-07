from typing import Union
from fastapi import FastAPI
from agents.connectors.google_feeds import GoogleNews
from agents.application.executor import Executor

app = FastAPI()
gn = GoogleNews()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/trades/{trade_id}")
def read_trade(trade_id: int, q: Union[str, None] = None):
    return {"trade_id": trade_id, "q": q}


@app.get("/markets/{market_id}")
def read_market(market_id: int, q: Union[str, None] = None):
    return {"market_id": market_id, "q": q}

@app.get("/predict/market")
def read_market(q: str = None):
    documents = gn.fetch_search_documents(q)
    executor = Executor()
    response = executor.get_polymarket_news_llm(q, documents)
    return response


# post new prompt
