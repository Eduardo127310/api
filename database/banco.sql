-- Apaga e recria o banco para incluir a coluna "senha" do Projeto 2
DROP DATABASE IF EXISTS api_receitas;

CREATE DATABASE api_receitas
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

USE api_receitas;


CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(150) NOT NULL UNIQUE,
    senha VARCHAR(255) NOT NULL  -- guarda o HASH da senha, nunca a senha pura
);


CREATE TABLE receitas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(150) NOT NULL,
    descricao VARCHAR(255) NOT NULL,
    ingredientes TEXT NOT NULL,
    modo_preparo TEXT NOT NULL,
    usuario_id INT NOT NULL,

    FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
);


-- Senha dos dois usuários: 123456
-- (hash gerado com generate_password_hash, do Werkzeug, que já vem com o Flask)
INSERT INTO usuarios (id, nome, email, senha) VALUES
(1, 'Ana Souza', 'ana@email.com',
 'pbkdf2:sha256:1000000$PWptX0Mg1WLqoZjD$ba8488f0eb44db8e5d649b10f98353b8f47b1b64a00e98651c744f8046c919e4'),
(2, 'Bruno Lima', 'bruno@email.com',
 'pbkdf2:sha256:1000000$GmXsGz4FRr28zj3b$41c1de77315c8b18eaf60a3c007b0e7f03410ca569a063c02076e6fbc9c196e5');


INSERT INTO receitas
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
