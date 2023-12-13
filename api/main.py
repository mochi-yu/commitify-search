from flask import Flask, request, jsonify
from flask_cors import CORS

from models.search import SearchRequestParam

from logic.search import serch_logic

app = Flask(__name__)
CORS(app)

@app.route('/search', methods=['POST'])
def searchHandler():
  param = SearchRequestParam(**request.json)

  return jsonify(serch_logic(param).__dict__), 200

if __name__ == '__main__':
  app.run(debug=False, host='0.0.0.0', port=5000)