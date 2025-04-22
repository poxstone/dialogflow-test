# DIALOG FLOW TEST

## Service account

- Create service account project
- Set PErmissions: Dialogflow API Client
- For local download json key

## Install
```bash
python3 -m virtualenv .venv;
source .venv/bin/activate;
pip install -r requirements.txt;
```
## Run
```bash
export GOOGLE_APPLICATION_CREDENTIALS="${PWD}/credentials.json"
python main.py
```
## Build
```bash
docker build -t dialogflow-test ./;
docker run -p 8080:8080 -v "${PWD}/credentials.json:/app/credentials.json" -e GOOGLE_APPLICATION_CREDENTIALS=/app/credentials.json dialogflow-test;
```

## deploy (gcp)
```bash
# once
gcloud auth configure-docker us-central1-docker.pkg.dev;
# push
docker tag dialogflow-test us-central1-docker.pkg.dev/p4-operations-dev/dialog-flow/dialogflow-test:latest;
docker push us-central1-docker.pkg.dev/p4-operations-dev/dialog-flow/dialogflow-test:latest;
```

## Test
- Browser
```bash
http://localhost:8080/ask
```

- Curl
```bash
HOST="http://localhost:8080";
curl -X POST ${HOST}/ask \
     -H "Content-Type: application/json" \
     -d '{"sesionId":"e4820134-3c81-4112-adea-bf398128bdd7","message": "Hola"}'
```