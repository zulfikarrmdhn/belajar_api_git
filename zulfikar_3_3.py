from flask import Flask, request, jsonify

import re

app = Flask(__name__)

def _remove_punct(s):
    return re.sub(r"[^\w\d\s]+", "",s)

@app.route("/nama/v1", methods=['GET']) 
def json_response():
    name_input = request.args.get('name')

    if name_input == "jokowi":
        json_response = {"nama": "ya ndak tau kok tanya saya"}
    else:
        json_response = {"nama": f"nama beliau adalah {name_input}"}

    return jsonify(json_response)

@app.route("/telor/v1", methods=['POST']) 
def get_text():
    s = request.get_json()
    s = s['text']

    total_char = len(s)

    s = s.lower()
    s = _remove_punct(s)

    list_s = s.split()
    
    total_telor = list_s.count("telor")

    return_text = {
        "total_char":f"Jumlah karakter dari input string adalah {total_char}",
        "total_telor":f"Jumlah kata 'telor' adalah {total_telor}"
    }

    return jsonify(return_text)

if __name__ == "__main__":
    app.run(port=2212, debug=True)