from fastapi import FastAPI, HTTPException
import yfinance as yf
import numpy as np
import datetime

from disintegration2 import ticker_comparison

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "hello"}

@app.get("/API/shares/{stock_id}")
def read_stock(stock_id):
    stock = yf.Ticker(stock_id)
    # print(stock)
    try:
        data = stock.history()
        last_close_price = np.around((data.tail(1)['Close'].iloc[0]) + np.random.uniform(0,5), decimals=2)
    except IndexError:
        try:
            stock_id = ticker_comparison(stock_id)
            if(stock_id):
                stock = yf.Ticker(stock_id)
                data = stock.history()
                last_close_price = np.around((data.tail(1)['Close'].iloc[0]) + np.random.uniform(0,5), decimals=2)
            else:
                return HTTPException(status_code=404, detail="Item not found")
        except IndexError:
            return HTTPException(status_code=404, detail="Item not found")
    time = datetime.datetime.now().astimezone().replace(microsecond=0).isoformat()
    # TODO: rename stock_id key to the Title
    return{"stock_id": stock_id, "Price": last_close_price, "Time": time}