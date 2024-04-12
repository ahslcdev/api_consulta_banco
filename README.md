# API Consulta Banco

Este projeto foi desenvolvido para a vaga de estágiario de devops da empresa RevGás.

- O sistema possuí a área administrativa, onde é possível realizar as operações de CRUD no model BANCO. Ademais, é possível realizar o import do xls que foi fornecido no e-mail através desta url: http://localhost:8000/admin/core/bank/import/ , basta informar o xls e prosseguir com a operação. Esta operação pode ser realizada também através da API, o qual foi disponibilizado um endpoint apenas para esta tarefa.

- Além da área administrativa, possui também a área do usuário normal, onde é possível ver os bancos cadastrados.
- Ambas as áreas necessitam de login.
- A documentação da API encontra-se na url: http://localhost:8000/doc/swagger-ui/ .
- No mais, este projeto foi desenvolvido utilizando o framework Django e foi utilizado o MySQL para persistência de dados.

## Instalação

Siga estas etapas para instalar e configurar o projeto:

1. Clone este repositório:

    ```
    git clone https://github.com/ahslcdev/api_consulta_banco
    ```

2. Acesse o diretório do projeto:

    ```
    cd api_consulta_banco
    ```

3. Instale as dependências:

    ```
    pip install -r requirements.txt
    ```

4. Execute as migrações do banco de dados:

    ```
    python manage.py migrate
    ```

5. Crie um superusuário:

    ```
    python manage.py createsuperuser
    ```

## Uso

Para iniciar o servidor de desenvolvimento, execute o seguinte comando:
    
    ```
    python manage.py runserver
    ```

Acesse o projeto em seu navegador em `http://localhost:8000`.

Para as variavéis de ambiente, segue o exemplo:

    ```
    DB_ALIAS='default'
    DB_ENGINE='django.db.backends.mysql'
    DB_USER=database_user
    DB_PASSWORD=user_database_password
    DB_HOST=localhost
    DB_NAME='database_name'
    DB_PORT=port_mysql

    DEBUG=True
    SECRET_KEY='my_secret_key'
    ALLOWED_HOSTS="*"
    ```

    