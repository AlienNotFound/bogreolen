# syntax=docker/dockerfile:1
FROM python:3.10-alpine

WORKDIR /code

COPY backend/requirements.txt .
RUN pip install -r requirements.txt
COPY . .

ENV FLASK_ENV=development
ENV FLASK_APP=app
ENV FLASK_RUN_HOST=0.0.0.0
RUN apk add --no-cache gcc musl-dev linux-headers mysql-client

EXPOSE 5000
CMD ["python", "-m", "backend.app", "--host=0.0.0.0", "--port=5000"]