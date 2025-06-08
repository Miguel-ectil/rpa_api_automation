# 📊 RPA API Automation

Automação com Python para coleta, armazenamento, processamento e envio automatizado de dados obtidos via API pública.  
Este projeto foi desenvolvido como avaliação final da disciplina de Robotic Process Automation (RPA).

## 👤 Autor

- **Nome:** Miguel Ectil  
- **Data:** Junho de 2025

---

## 🎯 Objetivo

Criar um sistema automatizado que integra:
1. Requisição a uma API pública
2. Armazenamento em banco de dados SQLite
3. Processamento de dados com expressões regulares
4. Geração e envio de relatório automatizado por e-mail

---

## 🔌 API Utilizada

- **API:** [Advice Slip API](https://api.adviceslip.com/advice)
- **Justificativa:** A API é gratuita, pública e não requer autenticação, facilitando a integração e permitindo foco na lógica de automação.

---

## 🛠️ Tecnologias e Bibliotecas

- Python 3.x
- [requests](https://pypi.org/project/requests/) – para requisição à API
- [sqlite3](https://docs.python.org/3/library/sqlite3.html) – para banco de dados local
- [re](https://docs.python.org/3/library/re.html) – para expressões regulares
- [yagmail](https://pypi.org/project/yagmail/) – para envio de e-mails automatizado

---

## 🚀 Execução

1. Baixe o projeto de repositório
``` bash
git clone https://github.com/Miguel-ectil/rpa_api_automation.git
```

2. Instale os pacotes necessários (em um ambiente virtual recomendado):
```bash
pip install requests yagmail
```
3. Edite o arquivo projeto_rpa.py com:

- Seu e-mail Gmail

- Senha de app gerada

- E-mail de destino (pode ser o mesmo)

```bash
  python projeto_rpa.py
```

## 📧 Exemplo de Conteúdo do E-mail

Relatório RPA - Conselho Aleatório

Conselho: True happiness always resides in the quest.
Padrões Identificados: Nenhum padrão identificado
Data/Hora da coleta: 2025-06-07 23:48:01