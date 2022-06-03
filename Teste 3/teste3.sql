CREATE DATABASE Teste3DB;

USE Teste3DB;

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

CREATE TABLE Despesas (
		Registro INT,
        `Data` DATE,
        CDContaContabil INT,
        Descricao VARCHAR(400),
        SaldoFinal DECIMAL(20, 2)
);

LOAD DATA LOCAL INFILE "./Relatorio_cadop teste 3.csv"  
INTO TABLE Operadoras
CHARACTER SET latin1
FIELDS TERMINATED BY ';' ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 3 ROWS
(Registro, CNPJ, RazaoSocial, NomeFantasia, Modalidade, Logradouro, Numero, Complemento, Bairro, Cidade, UF, CEP, DDD, Telefone, Fax, Email, Representante, CargoRepresentante, @date_var)
SET DataRegistro=str_to_date(@date_var, "%d/%m/%Y");

LOAD DATA LOCAL INFILE "./data/1T2020.csv"  
INTO TABLE Despesas
CHARACTER SET latin1
FIELDS TERMINATED BY ';' ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS
(@date_var, Registro, CDContaContabil, Descricao, @saldo_var)
SET `Data`=str_to_date(@date_Var, "%d/%m/%Y"), SaldoFinal=REPLACE(@saldo_var, ",", ".");

LOAD DATA LOCAL INFILE "./data/2T2020.csv"  
INTO TABLE Despesas
CHARACTER SET latin1
FIELDS TERMINATED BY ';' ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS
(@date_var, Registro, CDContaContabil, Descricao, @saldo_var)
SET `Data`=str_to_date(@date_Var, "%d/%m/%Y"), SaldoFinal=REPLACE(@saldo_var, ",", ".");

LOAD DATA LOCAL INFILE "./data/3T2020.csv"  
INTO TABLE Despesas
CHARACTER SET latin1
FIELDS TERMINATED BY ';' ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS
(@date_var, Registro, CDContaContabil, Descricao, @saldo_var)
SET `Data`=str_to_date(@date_Var, "%d/%m/%Y"), SaldoFinal=REPLACE(@saldo_var, ",", ".");

LOAD DATA LOCAL INFILE "./data/4T2020.csv"  
INTO TABLE Despesas
CHARACTER SET latin1
FIELDS TERMINATED BY ';' ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS
(@date_var, Registro, CDContaContabil, Descricao, @saldo_var)
SET `Data`=str_to_date(@date_Var, "%d/%m/%Y"), SaldoFinal=REPLACE(@saldo_var, ",", ".");

LOAD DATA LOCAL INFILE "./data/1T2021.csv"  
INTO TABLE Despesas
CHARACTER SET latin1
FIELDS TERMINATED BY ';' ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS
(@date_var, Registro, CDContaContabil, Descricao, @saldo_var)
SET `Data`=str_to_date(@date_Var, "%d/%m/%Y"), SaldoFinal=REPLACE(@saldo_var, ",", ".");

LOAD DATA LOCAL INFILE "./data/2T2021.csv"  
INTO TABLE Despesas
CHARACTER SET latin1
FIELDS TERMINATED BY ';' ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS
(@date_var, Registro, CDContaContabil, Descricao, @saldo_var)
SET `Data`=str_to_date(@date_Var, "%d/%m/%Y"), SaldoFinal=REPLACE(@saldo_var, ",", ".");

LOAD DATA LOCAL INFILE "./data/3T2021.csv"  
INTO TABLE Despesas
CHARACTER SET latin1
FIELDS TERMINATED BY ';' ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS
(@date_var, Registro, CDContaContabil, Descricao, @saldo_var)
SET `Data`=str_to_date(@date_Var, "%d/%m/%Y"), SaldoFinal=REPLACE(@saldo_var, ",", ".");

LOAD DATA LOCAL INFILE "./data/4T2021.csv"  
INTO TABLE Despesas
FIELDS TERMINATED BY ';' ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS
(`Data`, Registro, CDContaContabil, Descricao, @discard, @saldo_var)
SET SaldoFinal=REPLACE(@saldo_var, ",", ".");
