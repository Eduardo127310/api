# API de Receitas

O projeto é uma **API de receitas** desenvolvida com **Python, Flask e MySQL**, seguindo uma estrutura simplificada de **MVC (Model-View-Controller)**.

O sistema consulta dados já cadastrados no banco de dados e retorna as informações em **JSON**, além de possuir páginas **HTML** para visualização dos dados.

## Tecnologias utilizadas

- Python
- Flask
- MySQL
- HTML
- JavaScript
- `fetch`
- SQL

## Como executar o projeto

### 1. Pré-requisitos

É necessário ter instalado:

- Python
- MySQL
- MySQL Workbench

### 2. Configurar o banco de dados

Execute o arquivo `banco.sql` no **MySQL Workbench** para criar e configurar o banco de dados.

### 3. Configurar o acesso ao banco

Configure o **usuário e a senha do MySQL** no arquivo:

```text
database.py
```

### 4. Instalar as dependências

No terminal, execute:

```bash
pip install -r requirements.txt
```

### 5. Iniciar o projeto

Execute:

```bash
python app.py
```

Após iniciar, o sistema estará disponível em:

[http://127.0.0.1:5000](http://