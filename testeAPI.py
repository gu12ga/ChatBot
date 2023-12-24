import requests
import json

# Substitua 'sua_chave_de_api' pela sua chave de API
api_key = 'sua_chave_de_api'

# URL da API do ChatGPT (consulte a documentação para a URL correta)
api_url = 'https://api.openai.com/v1/engines/davinci/completions'

# Texto da sua consulta
prompt = 'Translate the following English text to French: "{}"'

# Faça a solicitação à API
response = requests.post(api_url, headers={'Authorization': f'Bearer {api_key}'}, json={'prompt': prompt})

# Analise a resposta JSON
if response.status_code == 200:
    data = json.loads(response.text)
    completions = data['choices'][0]['text']
    print(completions)
else:
    print('Erro ao fazer a solicitação à API:', response.status_code, response.text)