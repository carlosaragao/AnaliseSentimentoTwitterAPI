from analisador import Analisador
from flask import Flask, request
from flask_cors import CORS, cross_origin 

app = Flask(__name__) # Inicializa a aplicação
cors = CORS(app)

@app.route('/analisar', methods=['POST'])
def analisar():
  body = request.get_json()

  if ('nome_perfil_usuario' not in body):
    return { 'Erro': 'É necessário informar um nome de perfil de usuário!' }

  analisador = Analisador()

  return analisador.analisar(body['nome_perfil_usuario'])

if __name__ == '__main__':
  app.run(debug=True) #executa a aplicação