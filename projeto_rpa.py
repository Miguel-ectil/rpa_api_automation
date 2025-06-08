import requests


API_KEY = 'SUA_CHAVE_API_AQUI'
CIDADE = 'Guarulhos'
EMAIL_DESTINO = 'seudominio@gmail.com'
EMAIL_ORIGEM = 'seudominio@gmail.com'
EMAIL_SENHA = 'SUA_SENHA_DE_APP'

# === ETAPA 1: Coleta de Dados via API ===
url = f'https://api.openweathermap.org/data/2.5/weather?q={CIDADE}&appid={API_KEY}&units=metric&lang=pt_br'
response = requests.get(url)
data = response.json()

temperatura = data['main']['temp']
descricao = data['weather'][0]['description']
umidade = data['main']['humidity']
