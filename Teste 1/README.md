# Teste 1 - WebScraping

## Dependências utilizadas

Para a implementação da solução deste desafio foram utilizadas as bibliotecas [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/) e [urllib3](https://urllib3.readthedocs.io/en/stable) para a linguagem Python. A biblioteca Beautiful Soup foi utilizada para realizar o parsing do documento HTML da página e navegar facilmente por ela, a fim de obter os links dos arquivos que devem ser recuperados. Já a biblioteca urllib3 é utilizada para disparar requisições HTTP, que são utilizadas tanto para recuperar o HTML da página alvo quanto para baixar os arquivos desejados.

## Instruções de execução

Para executar o script, é necessário ter instalado, em seu computador, um
interpretador Python com suporte ao Python3 e o gerenciador de pacotes
pip. Antes de executar o script, é necessário instalar as dependências mencionadas anteriormente. Para isso, basta executar, em uma linha de comandos aberta no diretório que contém este arquivo, o seguinte comando:

```bash
pip install -r requirements.txt
```

Após instalar as dependências, o script pode ser executado com o seguinte comando:

```bash
python scrapper.py
```

Após uma execução bem sucedida do script, deve ser gerado, no diretório atual, um arquivo .zip com o nome "Anexos - Teste 1". Caso aconteça algum erro durante a execução, uma mensagem é exibida na linha de comando, sinalizando que ocorreu um erro e informando a causa do problema.

**Obs.:** Em alguns ambientes, pode ser que o executável do interpretador
Python3 e/ou do gerenciador de pacotes pip sejam disponibilizado com um nome
diferente. Sendo assim, se algum dos comandos anteriores falhar, basta
substituir o nome "python" por "python3" e/ou "pip" por "pip3".
