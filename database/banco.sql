CREATE DATABASE IF NOT EXISTS api_receitas
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

USE api_receitas;


CREATE TABLE IF NOT EXISTS usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(150) NOT NULL UNIQUE
);


CREATE TABLE IF NOT EXISTS receitas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(150) NOT NULL,
    descricao VARCHAR(255) NOT NULL,
    ingredientes TEXT NOT NULL,
    modo_preparo TEXT NOT NULL,
    usuario_id INT NOT NULL,

    CONSTRAINT fk_receita_usuario
        FOREIGN KEY (usuario_id)
        REFERENCES usuarios(id)
);


INSERT IGNORE INTO usuarios (id, nome, email) VALUES
(1, 'Ana Souza', 'ana@email.com'),
(2, 'Bruno Lima', 'bruno@email.com'),
(3, 'Carlos Silva', 'carlos@email.com'),
(4, 'Daniela Rocha', 'daniela@email.com');


INSERT IGNORE INTO receitas
(id, titulo, descricao, ingredientes, modo_preparo, usuario_id)
VALUES

(
    1, 'Bolo de Chocolate',
    'Bolo simples e fofinho de chocolate.',
    'Farinha, açúcar, ovos, leite, chocolate em pó',
    'Misture os ingredientes e asse por aproximadamente 40 minutos.',
    1
),

(
    2, 'Lasanha à Bolonhesa',
    'Lasanha tradicional com carne moída.',
    'Massa de lasanha, carne moída, molho de tomate, queijo',
    'Monte as camadas e leve ao forno.',
    2
),

(
    3, 'Frango Assado',
    'Frango assado simples com batatas.',
    'Frango, batata, alho, sal, azeite',
    'Tempere o frango e asse junto com as batatas.',
    3
),

(
    4, 'Bolo de Cenoura',
    'Bolo de cenoura com cobertura de chocolate.',
    'Cenoura, farinha, açúcar, ovos, óleo, chocolate',
    'Bata os ingredientes, asse e coloque a cobertura.',
    1
),

(
    5, 'Macarrão ao Alho e Óleo',
    'Macarrão rápido e simples.',
    'Macarrão, alho, azeite, sal',
    'Cozinhe o macarrão e misture com alho dourado no azeite.',
    4
),

(
    6, 'Panqueca de Frango',
    'Panqueca recheada com frango desfiado.',
    'Farinha, leite, ovos, frango, molho de tomate',
    'Prepare a massa, recheie e cubra com molho.',
    3
),

(
    7, 'Arroz de Forno',
    'Arroz de forno com queijo e presunto.',
    'Arroz, queijo, presunto, milho, molho de tomate',
    'Misture tudo e leve ao forno.',
    2
),

(
    8, 'Torta de Frango',
    'Torta salgada de liquidificador.',
    'Farinha, leite, ovos, óleo, frango',
    'Bata a massa, coloque o recheio e asse.',
    3
),

(
    9, 'Pão de Queijo',
    'Pão de queijo mineiro simples.',
    'Polvilho, queijo, ovos, leite, óleo',
    'Misture os ingredientes, faça bolinhas e asse.',
    4
),

(
    10, 'Brigadeiro',
    'Doce brasileiro tradicional.',
    'Leite condensado, chocolate em pó, manteiga',
    'Cozinhe em fogo baixo até desgrudar da panela.',
    1
),

(
    11, 'Salada de Frango',
    'Salada leve com frango grelhado.',
    'Frango, alface, tomate, cenoura, azeite',
    'Grelhe o frango e misture aos vegetais.',
    3
),

(
    12, 'Bolo de Banana',
    'Bolo caseiro simples de banana.',
    'Banana, farinha, açúcar, ovos, canela',
    'Misture os ingredientes e asse.',
    2
);
