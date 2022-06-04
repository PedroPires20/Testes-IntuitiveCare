# Teste 4 - API

## Dependências utilizadas

Para a implementação da solução deste desafio foram utilizadas as bibliotecas
[Pandas](https://pandas.pydata.org/) e
[Flask](https://urllib3.readthedocs.io/en/stable) para a linguagem Python. A
biblioteca Pandas foi utilizada para auxiliar na representação e consulta dos
dados tabulares que foram importados a partir do CSV dado na especificação do
desafio. Já a biblioteca Flask foi utilizada para implementar um servidor HTTP
que disponibiliza uma API para realizar buscas textuais nos dados importados.

## Instruções de execução

Para executar o servidor, é necessário ter instalado, em seu computador, um
interpretador Python com suporte ao Python3 e o gerenciador de pacotes pip.
Antes de iniciar o servidor é necessário criar um ambiente virtual python
e instalar as dependências necessárias. Isso pode ser feito com os seguintes
comandos (que devem ser executados a partir do diretório "backend"):

```bash
python -m venv .venv
./.venv/Scripts/activate
pip install -r requirements.txt
```

Após a execução dos comandos anteriores, o servidor pode ser inicializado com
o seguinte comando:

```bash
python server.py
```

**Obs.:** Em alguns ambientes, pode ser que o executável do interpretador Python3 e do
gerenciador de pacotes pip sejam disponibilizado com um nome diferente. Sendo
assim, se algum dos comandos anteriores falhar, basta substituir o nome "python"
por "python3" e/ou "pip" por "pip3".

Após a execução do comando anterior o servidor estará disponível para atender requisições
na porta 5000 no IP dá máquina local (*localhost*).

## Especificação da API

A especificação da API implementada, bem como exemplos de respostas geradas
estão disponíveis no arquivo "Requisições API Teste 4.postman_collection.json",
disponibilizado junto a este documento. O arquivo em questão segue o formato da
aplicação [Postman](https://www.postman.com/) e pode ser melhor visualizado se
importado nessa aplicação.

Em suma, a API implementa utiliza REST e define um *endpoint* "/search", que
permite a realização de consultas sobre os dados. Esse *endpoint* é acessado com
uma requisição do tipo GET e espera dois parâmetros: `type` e `query`. O
parâmetro `type` indica o tipo de busca que se deseja fazer. São suportados três
tipos de busca: por razão social (indicada por `type='c'`), por nome fantasia
(indicada por `type='n'`) e por nome do responsável (indicada por `type='r'`). O
parâmetro `query`, por sua vez, indica o termo de busca, tendo seu valor
associado à string que deseja procurar.

Após realizar a busca pelo termo desejado, o servidor retorna um documento JSON
com alguns dados das empresas encontradas pela busca. Os dados retornados são:
nome fictício, nome fantasia, número de registro na ANS, data de registro na
ANS, nome do responsável, telefone, email, cidade, UF, CEP, número e
complemento. O documento JSON retornado possui uma única chave, de nome
`results`, que contém um array de objetos contendo as informações mencionadas
anteriormente para cada empresa encontrada.
