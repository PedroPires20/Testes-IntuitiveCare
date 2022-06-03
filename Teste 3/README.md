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

Após a inicialização do shell MySQL, o script desenvolvido pode ser executado com o seguinte comando:

```sql
SOURCE teste3.sql;
```
