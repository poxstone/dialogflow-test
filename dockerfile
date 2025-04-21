FROM python:3.10-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir flask google-cloud-dialogflow

ENV GOOGLE_APPLICATION_CREDENTIALS="/app/credentials.json"
ENV PROJECT_ID="chatbot-nkti"

EXPOSE 8080

CMD ["python", "main.py"]