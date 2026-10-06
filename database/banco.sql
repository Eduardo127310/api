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

    FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
);


INSERT IGNORE INTO usuarios (id, nome, email) VALUES
(1, 'Ana Souza', 'ana@email.com'),
(2, 'Bruno Lima', 'bruno@email.com');


INSERT IGNORE INTO receitas
(id, titulo, descricao, ingredientes, modo_preparo, usuario_id)
VALUES
(1, 'Bolo de Chocolate',
 'Bolo simples de chocolate.',
 'Farinha, açúcar, ovos, leite, chocolate',
 'Misture os ingredientes e asse.',
 1),

(2, 'Lasanha',
 'Lasanha de carne.',
 'Massa, carne moída, molho, queijo',
 'Monte as camadas e leve ao forno.',
 2),

(3, 'Frango Assado',
 'Frango assado com batatas.',
 'Frango, batata, alho, sal',
 'Tempere e asse.',
 1),

(4, 'Bolo de Cenoura',
 'Bolo de cenoura com chocolate.',
 'Cenoura, farinha, açúcar, ovos, chocolate',
 'Misture, asse e coloque a cobertura.',
 1),

(5, 'Macarrão',
 'Macarrão simples.',
 'Macarrão, alho, azeite, sal',
 'Cozinhe e misture os ingredientes.',
 2),

(6, 'Panqueca de Frango',
 'Panqueca recheada com frango.',
 'Farinha, leite, ovos, frango',
 'Prepare a massa, recheie e sirva.',
 2);
