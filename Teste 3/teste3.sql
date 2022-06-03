-- Criando um banco de dados para os dados do teste e selecionando esse banco
-- para a realização das operações seguintes
CREATE DATABASE Teste3DB;

USE Teste3DB;

-- Criando uma tabela para armazenar os dados das operadoras, contidos no
-- arquivo "Relatorio_cadop teste 3.csv", que será importado em sequência
CREATE TABLE Operadoras (
	Registro INT UNIQUE PRIMARY KEY,
    CNPJ CHAR(14),
    RazaoSocial VARCHAR(200),
    NomeFantasia VARCHAR(150),
    Modalidade VARCHAR(40),
    Logradouro VARCHAR(100),
    Numero VARCHAR(20),
    Complemento VARCHAR(40),
    Bairro VARCHAR(80),
    Cidade VARCHAR(60),
    UF CHAR(2),
    CEP CHAR(8),
    DDD CHAR(2),
    Telefone VARCHAR(20),
    Fax VARCHAR(20),
    Email VARCHAR(320),
    Representante VARCHAR(200),
    CargoRepresentante VARCHAR(100),
    DataRegistro DATE
);

-- Criando uma tabela para armazenar os dados das demonstrações contábeis das
-- operadoras nos anos de 2020 e 2021, que estão contidos nos arquivos ".csv" no
-- diretório "data", separados por trimestre.
CREATE TABLE Demonstracoes (
		Registro INT,
        `Data` DATE,
        CDContaContabil INT,
        Descricao VARCHAR(400),
        SaldoFinal DECIMAL(20, 2)
);

-- Importando os dados das operadoras:
LOAD DATA LOCAL INFILE "./Relatorio_cadop teste 3.csv"  
INTO TABLE Operadoras
CHARACTER SET latin1
FIELDS TERMINATED BY ';' ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 3 ROWS
(Registro, CNPJ, RazaoSocial, NomeFantasia, Modalidade, Logradouro, Numero, Complemento, Bairro, Cidade, UF, CEP, DDD, Telefone, Fax, Email, Representante, CargoRepresentante, @date_var)
SET DataRegistro=str_to_date(@date_var, "%d/%m/%Y");

-- Importando os dados dos demonstrativos financeiros:
LOAD DATA LOCAL INFILE "./data/1T2020.csv"  
INTO TABLE Demonstracoes
CHARACTER SET latin1
FIELDS TERMINATED BY ';' ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS
(@date_var, Registro, CDContaContabil, Descricao, @saldo_var)
SET `Data`=str_to_date(@date_Var, "%d/%m/%Y"), SaldoFinal=REPLACE(@saldo_var, ",", ".");

LOAD DATA LOCAL INFILE "./data/2T2020.csv"  
INTO TABLE Demonstracoes
CHARACTER SET latin1
FIELDS TERMINATED BY ';' ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS
(@date_var, Registro, CDContaContabil, Descricao, @saldo_var)
SET `Data`=str_to_date(@date_Var, "%d/%m/%Y"), SaldoFinal=REPLACE(@saldo_var, ",", ".");

LOAD DATA LOCAL INFILE "./data/3T2020.csv"  
INTO TABLE Demonstracoes
CHARACTER SET latin1
FIELDS TERMINATED BY ';' ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS
(@date_var, Registro, CDContaContabil, Descricao, @saldo_var)
SET `Data`=str_to_date(@date_Var, "%d/%m/%Y"), SaldoFinal=REPLACE(@saldo_var, ",", ".");

LOAD DATA LOCAL INFILE "./data/4T2020.csv"  
INTO TABLE Demonstracoes
CHARACTER SET latin1
FIELDS TERMINATED BY ';' ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS
(@date_var, Registro, CDContaContabil, Descricao, @saldo_var)
SET `Data`=str_to_date(@date_Var, "%d/%m/%Y"), SaldoFinal=REPLACE(@saldo_var, ",", ".");

LOAD DATA LOCAL INFILE "./data/1T2021.csv"  
INTO TABLE Demonstracoes
CHARACTER SET latin1
FIELDS TERMINATED BY ';' ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS
(@date_var, Registro, CDContaContabil, Descricao, @saldo_var)
SET `Data`=str_to_date(@date_Var, "%d/%m/%Y"), SaldoFinal=REPLACE(@saldo_var, ",", ".");

LOAD DATA LOCAL INFILE "./data/2T2021.csv"  
INTO TABLE Demonstracoes
CHARACTER SET latin1
FIELDS TERMINATED BY ';' ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS
(@date_var, Registro, CDContaContabil, Descricao, @saldo_var)
SET `Data`=str_to_date(@date_Var, "%d/%m/%Y"), SaldoFinal=REPLACE(@saldo_var, ",", ".");

LOAD DATA LOCAL INFILE "./data/3T2021.csv"  
INTO TABLE Demonstracoes
CHARACTER SET latin1
FIELDS TERMINATED BY ';' ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS
(@date_var, Registro, CDContaContabil, Descricao, @saldo_var)
SET `Data`=str_to_date(@date_Var, "%d/%m/%Y"), SaldoFinal=REPLACE(@saldo_var, ",", ".");

-- O CSV Seguinte (do quarto trimestre de 2021), possui uma coluna a mais, com o
-- saldo inicial, que foi descartada para manter a conformidade com os dados
-- importados dos CSVs de anos anteriores e com o formato definido para a tabela
-- "Demonstracoes"
LOAD DATA LOCAL INFILE "./data/4T2021.csv"  
INTO TABLE Demonstracoes
FIELDS TERMINATED BY ';' ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS
(`Data`, Registro, CDContaContabil, Descricao, @discard, @saldo_var)
SET SaldoFinal=REPLACE(@saldo_var, ",", ".");

-- Consulta para a primeira pergunta:
SELECT RazaoSocial FROM Operadoras JOIN Demonstracoes ON Operadoras.Registro=Demonstracoes.Registro
WHERE `Data` BETWEEN "2021-10-1" AND "2021-12-31"
AND Descricao LIKE "%EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR%"
ORDER BY SaldoFinal DESC
LIMIT 10;

-- Consulta para a segunda pergunta:
SELECT RazaoSocial FROM Operadoras JOIN Demonstracoes ON Operadoras.Registro=Demonstracoes.Registro
WHERE `Data` BETWEEN "2021-1-1" AND "2021-12-31"
AND Descricao LIKE "%EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR%"
ORDER BY SaldoFinal DESC
LIMIT 10;
