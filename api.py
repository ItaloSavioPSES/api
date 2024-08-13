from flask import Flask, jsonify, request

app = Flask(__name__)

afazeres = [
    {"id": 1, "atividade": "Estudar python", "horario": "das 8h ate 17h"},
    {"id": 2, "atividade": "arrumar a casa", "esposa": "Se diverti, conversar, assistir filminho"},
    {'id': 3, "atividade": "ajudar a esposa", "ação": "amar ela"}
]

@app.route('/afazeres', methods=['GET'])
def resultado():
    return jsonify(afazeres)    
@app.route('/afazeres/<int:id>', methods=['GET'])
def obter_id(id):
    for afazer in afazeres:
        if afazer.get('id') == id:
            return jsonify(afazer)
        
app.run(port=5000,host='localhost',debug=True)