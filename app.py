from flask import Flask, request, jsonify
from controllers.code_review_controller import analisar_com_codigo
from dotenv import load_dotenv
from flask_cors import CORS

load_dotenv()

app = Flask(__name__)
CORS(app)

@app.route('/api/analisar', methods=['POST'])
def analisar():
    dados = request.get_json()
    codigo = dados.get('codigo')
    descricao = dados.get('descricao', "")

    if not codigo:
        return jsonify({"erro": "Nenhum código foi enviado."}), 400

    try:
        relatorio = analisar_com_codigo(codigo, descricao)
        return jsonify({"relatorio": relatorio})
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
