import requests
import sqlite3
import re
import yagmail
import datetime

# === CONFIGURAÇÕES ===
EMAIL_ORIGEM = 'ectilmiguelmiguelectil@gmail.com'
EMAIL_SENHA = 'vhhf nnuq fpss bkrs'
EMAIL_DESTINO = 'miguel.ectil@aluno.faculdadeimpacta.com.br'

# === ETAPA 1: Coleta de Dados via API ===
url = 'https://api.adviceslip.com/advice'
print("Requisitando conselho da API...")
response = requests.get(url)
data = response.json()

# Pegando o conselho
conselho = data['slip']['advice']
print("Conselho coletado:", conselho)

# === ETAPA 2: Armazenamento no Banco de Dados ===
conn = sqlite3.connect('projeto_rpa.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS conselhos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    conselho TEXT,
    data_hora TEXT
)
''')

data_hora = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
cursor.execute('''
INSERT INTO conselhos (conselho, data_hora)
VALUES (?, ?)
''', (conselho, data_hora))
conn.commit()

# === ETAPA 3: Processamento com Regex ===
match = re.findall(r'vida|tempo|felicidade|sabedoria|trabalho|amor', conselho.lower())
padrao = ', '.join(match) if match else 'Nenhum padrão identificado'

cursor.execute('''
CREATE TABLE IF NOT EXISTS conselhos_processados (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    conselho_original TEXT,
    padrao_encontrado TEXT,
    data_hora TEXT
)
''')

cursor.execute('''
INSERT INTO conselhos_processados (conselho_original, padrao_encontrado, data_hora)
VALUES (?, ?, ?)
''', (conselho, padrao, data_hora))
conn.commit()
conn.close()

# === ETAPA 4: Envio de E-mail ===
yag = yagmail.SMTP(user=EMAIL_ORIGEM, password=EMAIL_SENHA)

conteudo = f"""
Relatório RPA - Conselho Aleatório

Conselho: {conselho}
Padrões Identificados: {padrao}
Data/Hora da coleta: {data_hora}
"""

yag.send(
    to=EMAIL_DESTINO,
    subject='[RPA] Relatório Automatizado de Conselho Aleatório',
    contents=conteudo
)

print("✅ E-mail enviado com sucesso!")
