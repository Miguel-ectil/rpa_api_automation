import requests
import sqlite3
import re
import yagmail
import datetime

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

# === ETAPA 2: Armazenamento no Banco de Dados ===
conn = sqlite3.connect('projeto_rpa.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS dados_climaticos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cidade TEXT,
    temperatura REAL,
    descricao TEXT,
    umidade INTEGER,
    data_hora TEXT
)
''')

data_hora = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
cursor.execute('''
INSERT INTO dados_climaticos (cidade, temperatura, descricao, umidade, data_hora)
VALUES (?, ?, ?, ?, ?)
''', (CIDADE, temperatura, descricao, umidade, data_hora))
conn.commit()


