from typing import Union
from fastapi import FastAPI
from agents.connectors.google_feeds import GoogleNews
from agents.application.executor import Executor
from agents.polymarket.gamma import GammaMarketClient as Gamma
from agents.polymarket.polymarket import Polymarket
from py_clob_client.order_builder.constants import BUY
from agents.db.sqlite_db import SQLiteDB
import ast

app = FastAPI()
gn = GoogleNews()
gamma = Gamma()
polymarket = Polymarket()
db = SQLiteDB()

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

def alert(q: str = None, email: str = None):
    if q is None or email is None:
        return {"response": "invalid data"}
    documents = gn.fetch_search_documents(q)
    results = []
    for x in documents:
        results.append({"content": x.page_content, "id": x.id})
    
    


@app.get("/current/markets")
def current_markets():
    # polymarket.get_all_markets()
    markets = gamma.get_current_markets()
    market = markets[0]
    m = polymarket.get_market("44549619870282609065128487805032844507655355600285498718196203751201617089156")

    test_size = 0.1
    test_side = BUY
    test_price = float(ast.literal_eval(m["outcome_prices"])[0])
    print(test_price)
    order = polymarket.execute_market_order_token("44549619870282609065128487805032844507655355600285498718196203751201617089156", test_size)
    print(order)

    return gamma.get_current_markets()

# post new prompt
