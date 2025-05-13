FROM python:3.12.6-slim

WORKDIR /app

COPY pyproject.toml poetry.lock* ./

RUN pip install --no-cache-dir .

COPY . .

EXPOSE 8080

CMD ["uvicorn", "bora_gateway.main:app", "--host", "0.0.0.0", "--port", "8080"]