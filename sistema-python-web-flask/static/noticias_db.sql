CREATE DATABASE noticias_db;

USE noticias_db;

CREATE TABLE noticias (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(255),
    conteudo TEXT,
    data_publicacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);