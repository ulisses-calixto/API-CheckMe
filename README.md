# API-CheckMe
API de checagem de dados de usuário

# Como rodar a API localmente?
1. Clonagem do repositório.
   git bash
   git clone https://github.com/ulisses-calixto/API-CheckMe

# 2. Execução do terminal para abertura no VS Code.
  API-CheckMe -> Botão direito do mouse -> Abrir no terminal.
Em seguida, digite o código:
   code .
Para abrir no VS Code.

# 3. Instalação das dependências.
Abra o terminal Bash. Após isso, escreva ou copie o comando:
   pip install -r requirements.txt

# 4.Inicie a API
No terminal Bash, escreva ou copie o comando:
   uvicorn app.main:app --reload
Para iniciar o servidor localmente.

# 5. Acesse no navegador os links.
👉🏼http://127.0.0.1:8000/health
👉🏼 http://127.0.0.1:8000/me

# Link da API rodando no Render
🔗https://api-checkme.onrender.com/health
🔗https://api-checkme.onrender.com/me
