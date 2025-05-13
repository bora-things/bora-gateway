FROM python:3.12.6-slim

ARG BACKEND_URL
ARG FRONTEND_URL

ENV BACKEND_URL=$BACKEND_URL
ENV FRONTEND_URL=$FRONTEND_URL

WORKDIR /app

COPY pyproject.toml poetry.lock* ./

RUN pip install --no-cache-dir .

COPY . .

EXPOSE 8083

CMD ["uvicorn", "bora_gateway.main:app", "--host", "0.0.0.0", "--port", "8083"]