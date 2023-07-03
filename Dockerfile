From python:3.10

RUN mkdir /fastapi_app

WORKDIR /fastappi_app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD uvicorn web_service_fastapi:app --host 0.0.0.0 --port 80
