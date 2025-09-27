from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS 
import utils

app = Flask(__name__)
CORS(app)

# Load the coach agent
utils.load_saved_artifacts()


@app.route('/')
def home():
    return send_from_directory('../Client', 'coach.html')


@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    speech = data.get("speech")

    if not speech:
        return jsonify({"error": "Speech must be provided"}), 400

    result = utils.analyze(speech)
    return jsonify({"Impact analysis": result})


if __name__ == '__main__':
    app.run(debug=True)
