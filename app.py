from flask import Flask, request, jsonify
import requests
import os

# Criando uma instância de Flask
app = Flask(__name__)

# Criando uma rota para o 'home'
@app.route('/')
def home():
	return jsonify({"message": "CONVERSOR DE MOEDAS"})

# Rota para o conversor de moedas
@app.route('/convert')
def convert_currency():
	# Criando os parâmetros na URL para o conversor interpretar
	base = request.args.get('from').upper()
	target = request.args.get('to').upper()
	amount = request.args.get('amount', type=float)

	# Verificando se os parâmetros passados são válidos
	if not base or not target or amount is None:
		return jsonify({"error": "Parâmetros inválidos"}), 400	
	
	# Armazenando a chave da API armazenada em uma variável de ambiente definida na criação do container em uma variável
	api_key = os.environ.get('EXCHANGE_RATE_API_KEY')
	
	# Verificando se a variável de ambiente que armazena a chave da API existe ou tem algum conteúdo
	if api_key is None or api_key == "":
		return jsonify({"error": "Chave de API não configurada. Por favor, defina a variável de ambiente EXCHANGE_RATE_API_KEY."})

	# Tratando possíveis erros em caso de falha de conexão com a API ou outro erro inesperado
	try:
		# Adicionando os parâmetros à URL da API que pega a taxa de câmbio
		api_url = f"https://v6.exchangerate-api.com/v6/{api_key}/pair/{base}/{target}"

		# Fazendo uma requisição GET para a API com os parâmetros necessários para uma taxa de câmbio entre duas moedas, e armazenando a resposta
		response = requests.get(api_url)

		# Verificando o status HTTP resposta 
		response.raise_for_status()

		# Armazenando a resposta JSON da API em um dicionário 
		data = response.json()

		# Retornando um erro caso o resultado da resposta à requisição seja um erro
		if data.get('result') == 'error':
			error_type = data.get('error-type', 'unknown_error')
			return jsonify({"error": f"Erro da API: {error_type}. Verifique as moedas ou a chave da API."}), 400

		# Armazenando o 'convesion_rate'(taxa de câmbio) da resposta em uma variável
		exchange_rate = data.get('conversion_rate')

		# Verificando se a taxa de câmbio foi obtida com sucesso
		if exchange_rate is None:
			return jsonify({"error": "Não foi possível obter a taxa de câmbio da API. Formato de resposta inesperado"}), 500

		# Calculando o valor convertido com base na taxa de câmbio
		converted_amount = round(amount * exchange_rate, 2)

		# Retorna a resposta de sucesso com os dados da conversão em JSON
		# base: moeda base; target: moeda alvo; amount: valor original; exchange_rate: taxa de câmbio (quantas moedas target você receberia por uma moeda base); converted_amount: valor original convertido
		return jsonify({
			"from": base,
            "to": target,
            "amount": amount,
            "converted_amount": converted_amount,
            "exchange_rate": exchange_rate
		})

	except requests.exceptions.RequestException as e:
			return jsonify({"error": "Erro de conexão com a API: {e}"}), 500

	except Exception as e:
		return jsonify({"error": "Ocorreu um erro inesperado"}), 500
		
if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)
