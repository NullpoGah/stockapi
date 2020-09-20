FROM tiangolo/uvicorn-gunicorn:python3.8

RUN pip install --no-cache-dir fastapi yfinance numpy fuzzywuzzy[speedup]

COPY ./app /app