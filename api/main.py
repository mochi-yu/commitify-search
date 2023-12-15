from flask import Flask, request, jsonify
from flask_cors import CORS
import json

from models.search import SearchRequestParam

from logic.search import serch_logic
from logic.gemini import generate_by_gemini_logic

app = Flask(__name__)
CORS(app)

@app.route('/search', methods=['POST'])
def searchHandler():
  param = SearchRequestParam(**request.json)

  if not param.diff:
    return jsonify({"msg": "request param inviled."}), 400

  return jsonify(serch_logic(param).__dict__), 200

@app.route('/gemini', methods=['POST'])
def generate_by_gemini():
  param = SearchRequestParam(**request.json)

  if not param.diff:
    return jsonify({"msg": "request param inviled."}), 400

  return jsonify(json.loads(generate_by_gemini_logic(param))), 200

if __name__ == '__main__':
  app.run(debug=False, host='0.0.0.0', port=5000)