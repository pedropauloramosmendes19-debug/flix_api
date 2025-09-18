Flix API
Uma API RESTful desenvolvida com Django e Django REST Framework para gerenciar um catálogo de filmes, atores e suas avaliações.

✨ Funcionalidades Principais
Gerenciamento de Filmes: CRUD completo (Criar, Ler, Atualizar, Deletar) para filmes.

Gerenciamento de Atores: CRUD completo para atores.

Sistema de Avaliações (Reviews): Permite que filmes recebam múltiplas avaliações.

Endpoint de Estatísticas: Uma rota que consolida dados como o número total de filmes, o número de avaliações e a média geral de estrelas.

Comandos Customizados: Inclui comandos de gerenciamento para tarefas de automação, como popular o banco de dados com atores a partir de um arquivo CSV.

💻 Tecnologias Utilizadas
Backend: Python, Django

API: Django REST Framework

Banco de Dados: PostgreSQL (configurado para produção, SQLite para desenvolvimento)

Qualidade de Código: Flake8

🚀 Instalação e Configuração
Siga os passos abaixo para configurar e executar o projeto em seu ambiente local.

Pré-requisitos
Git

Python 3.10+

Um gerenciador de pacotes Python (pip)

Passos
1. Clone o repositório:

Bash

git clone https://github.com/pedropauloramosmendes19-debug/flix_api.git
cd flix_api
2. Crie e ative um ambiente virtual (venv):

Bash

# Para Windows
python -m venv venv
.\venv\Scripts\activate

# Para Linux/macOS
python3 -m venv venv
source venv/bin/activate
3. Instale as dependências do projeto:

Bash

pip install -r requirements.txt
4. Configure as variáveis de ambiente:
Crie um arquivo chamado .env na raiz do projeto, copiando o exemplo .env.example (se existir) ou usando a estrutura abaixo. Este arquivo guardará suas credenciais e configurações sensíveis.

Ini, TOML

# Exemplo de arquivo .env
SECRET_KEY='sua-chave-secreta-super-forte-aqui'
DEBUG=True

# Configuração do Banco de Dados (Opcional, para usar PostgreSQL)
DB_NAME='flix_db'
DB_USER='postgres'
DB_PASSWORD='your_db_password'
DB_HOST='localhost'
DB_PORT='5432'
5. Aplique as migrações do banco de dados:
Este comando criará as tabelas no banco de dados com base nos models do Django.

Bash

python manage.py migrate
6. (Opcional) Popule o banco de dados com dados iniciais:
O projeto inclui um comando para importar atores de um arquivo CSV. Coloque o arquivo actors.csv na raiz do projeto e execute:

Bash

python manage.py import_actors --file_name=actors.csv
▶️ Executando o Projeto
Após a instalação, inicie o servidor de desenvolvimento do Django:

Bash

python manage.py runserver
A aplicação estará disponível em http://127.0.0.1:8000/.


👨‍💻 Autor
Feito com ❤️ por Pedro, futuro dev backend😁
