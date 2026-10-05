O projeto é uma API de receitas desenvolvida com Python, Flask e MySQL, seguindo uma estrutura simplificada de MVC. O sistema apenas consulta dados já cadastrados no banco e retorna informações em JSON, além de possuir páginas HTML para visualização.
Para executar, é necessário instalar Python e MySQL, executar o arquivo banco.sql no MySQL Workbench, configurar usuário e senha em database.py, instalar as dependências com pip install -r requirements.txt e iniciar com python app.py. Depois, o sistema fica disponível em http://127.0.0.1:5000.
As principais funcionalidades são:
- listar receitas com paginação de 5 itens;
- pesquisar receitas por título, ingredientes ou descrição;
- pesquisar usuários pelo nome;
- consultar uma receita específica;
- visualizar o perfil do usuário, com nome, e-mail e suas receitas;
- retornar os dados através de diferentes rotas da API em JSON.
A estrutura segue o MVC: os Models fazem as consultas SQL, os Controllers recebem as requisições e retornam JSON, e as Views são os arquivos HTML. O Flask controla as rotas, enquanto o JavaScript utiliza fetch para buscar os dados da API.
No banco, receitas são relacionadas aos usuários através de uma chave estrangeira. As consultas utilizam recursos como LIKE para pesquisa, JOIN para relacionar receitas e autores, LIMIT e OFFSET para paginação e COUNT para calcular o número de páginas.
O projeto atende aos principais requisitos: busca com parâmetro String, paginação, busca de usuários, conteúdo associado ao usuário, MVC, front-end consumindo a API e banco MySQL.