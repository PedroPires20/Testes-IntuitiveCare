# Teste 3 - Banco de Dados

## Tratamento dos dados

## Instruções de execução

Para executar o script, é necessário ter instalado, em seu computador, o
servidor de banco de dados MySQL, versão 8 ou posterior. Inicialmente, é
necessário iniciar a execução de um shell do MySQL no diretório atual (que
contém este arquivo), realizando o login no seu servidor de banco de dados. Isso
é feito invocando o executável do mysql com os comandos necessários para a
autenticação de seu usuário. Também é necessário garantir que a importação de
arquivos locais está habilitada. Geralmente, a invocação do shell do SQL, já com
os parâmetros necessários para executar o script, pode ser feita com o seguinte
comando:

```bash
mysql --local-infile=1 -u {seu usuário} -p 
```

Note que o comando de invocação anterior pode não funcionar e deverá ser
alterado para atender a especificidades de sua instalação do SQL e da
configuração do servidor.

Após a inicialização do shell MySQL, o script desenvolvido para a criação do
banco de dados e importação dos dados pode ser executado com o seguinte comando:

```sql
SOURCE create_and_populate.sql;
```

### Consultas analíticas

Para responder às perguntas feitas no teste, foram desenvolvidas duas consultas
(*queries*) analíticas em SQL. Essas consultas podem ser executadas copiando e
colando o texto das consultas criadas no shell do MySQL e pressionando a tecla
"Enter". Após o processamento da consulta, os resultados produzidos são exibidos
na tela.

Para a primeira pergunta, foi desenvolvida a seguinte *query* analítica do MySQL:

```sql
SELECT RazaoSocial FROM Operadoras JOIN Demonstracoes ON Operadoras.Registro=Demonstracoes.Registro
WHERE `Data` BETWEEN "2021-10-1" AND "2021-12-31"
AND Descricao LIKE "%EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR%"
ORDER BY SaldoFinal DESC
LIMIT 10;
```

Já a segunda pergunta, pode ser respondida executando a seguinte *query*
analítica:

```sql
SELECT RazaoSocial FROM Operadoras JOIN Demonstracoes ON Operadoras.Registro=Demonstracoes.Registro
WHERE `Data` BETWEEN "2021-1-1" AND "2021-12-31"
AND Descricao LIKE "%EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR%"
ORDER BY SaldoFinal DESC
LIMIT 10;
```
