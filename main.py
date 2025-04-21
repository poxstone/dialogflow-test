from flask import Flask, request, jsonify, render_template
from google.cloud import dialogflow_v2 as dialogflow
import uuid
import os

app = Flask(__name__)

# Ruta a tu archivo de credenciales
os.getenv('GLOBAL_STATE', '200')

# ID del proyecto de tu agente Dialogflow
PROJECT_ID = os.getenv('PROJECT_ID', "chatbot-nkti")
gen_session_id = str(uuid.uuid4())

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.json.get("message", "")
    session_id = request.json.get("sessionId", gen_session_id)
    response_text = detect_intent_text(PROJECT_ID, session_id, user_input, "es")
    print(f'{session_id} -- {response_text}')
    return jsonify({"response": response_text})

def detect_intent_text(project_id, session_id, text, language_code):
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(project_id, session_id)

    text_input = dialogflow.types.TextInput(text=text, language_code=language_code)
    query_input = dialogflow.types.QueryInput(text=text_input)

    response = session_client.detect_intent(
        request={"session": session, "query_input": query_input}
    )

    return response.query_result.fulfillment_text

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")