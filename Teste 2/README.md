# Teste 2 - Transformação de dados

## Dependências utilizadas

Para a implementação da solução deste desafio foram utilizadas as bibliotecas
[Pandas](https://pandas.pydata.org/),
[PyPDF2](https://urllib3.readthedocs.io/en/stable) e
[Camelot](https://camelot-py.readthedocs.io/en/master/) para a linguagem Python.
A biblioteca Pandas foi utilizada para auxiliar na representação e tratamento
dos dados tabulares que foram extraídos do PDF de entrada. A biblioteca PyPDF2,
por sua vez, foi utilizada para realizar um pré-processamento básico no PDF,
obtendo, por exemplo, o número total de páginas no documento. Por fim, a
biblioteca Camelot foi utilizada para realizar a extração dos dados tabulares de
cada página do PDF para um Dataframe do Pandas.

## Instruções de execução

Para executar o script, é necessário ter instalado, em seu computador, um
interpretador Python com suporte ao Python3, o gerenciador de pacotes pip além
do interpretador GhostScript (para a linguagem PostScript) e da biblioteca
Tkinter, sendo, estes últimos, dependências requeridas pela biblioteca Camelot.
Antes de executar o script, é necessário instalar as dependências mencionadas
anteriormente.

Inicialmente, é necessário instalar o interpretador GhostScript
e a biblioteca Tkinter. Em um ambiente Linux Ubuntu, isso pode ser
feito executando o seguinte comando:

```bash
sudo apt install ghostscript python3-tk
```

Em um ambiente MacOS, o gerenciador de pacotes Brew pode ser utilizado para realizar
a instalação utilizando o seguinte comando:

```bash
sudo brew install ghostscript tcl-tk
```

Em ambientes Windows, é necessário baixar o GohstScript a partir desse
[link](https://www.ghostscript.com/index.html) e realizar a instalação seguindo
as instruções do executável obtido. Você deve também garantir que o diretório do
GhostScript foi adicionado à variável de ambiente PATH. A biblioteca Tkinter já
vem instalada por padrão com o Python 3 no Windows e, portanto, não é necessário
nenhuma instalação adicional deve ser necessária.

Em seguida, é necessário instalar as bibliotecas do Python utilizadas pelo
script. Para isso, basta executar o seguinte comando em uma linha de comandos
no diretório atual:

```bash
pip install -r requirements.txt
```

Após instalar as dependências, o script pode ser executado com o seguinte comando:

```bash
python pdf_processor.py
```

Durante a execução, o script gerará alguns feedbacks na tela, informando, por
exemplo, qual a etapa atual do processamento (processando PDF, gerando CSV,
etc.) e qual a página sendo processada. Após uma execução bem sucedida do
script, um arquivo ".zip" é gerado na pasta atual. Esse arquivo contém o arquivo
".csv" da tabela extraída a partir do PDF.

**Obs.:** Em alguns ambientes, pode ser que o executável do interpretador
Python3 e/ou do gerenciador de pacotes pip sejam disponibilizado com um nome
diferente. Sendo assim, se algum dos comandos anteriores falhar, basta
substituir o nome "python" por "python3" e/ou "pip" por "pip3".
