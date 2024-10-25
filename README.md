# Teste dev_junior
## Carregamento de Arquivos CSV no Banco de Dados SQL utilizando PostgreSQL e Python

Este projeto conecta-se a um banco de dados PostgreSQL, cria uma tabela de forma dinâmica e insere dados a partir do arquivo `escolas122022.csv`. Ele utiliza a biblioteca `psycopg2` para a conexão com o banco de dados e o `pandas` para manipulação do arquivo `escolas122022.csv`.

## Funcionalidades

1. **Leitura de Dados**: Lê dados do arquivo `escolas122022.csv` usando `pandas`.
2. **Conexão ao Banco de Dados**: Estabelece uma conexão com um banco PostgreSQL local ou remoto.
3. **Criação Dinâmica de Tabela**: Cria uma tabela com colunas adaptadas ao arquivo `escolas122022.csv` importado.
4. **Inserção de Dados**: Insere todos os dados do `escolas122022.csv` na tabela recém-criada no banco.

## Pré-requisitos

- **Python 3.x**: O projeto requer Python na versão 3.x.
- **PostgreSQL**: O banco de dados PostgreSQL deve estar instalado e ativo no ambiente local ou acessível via rede.
- **Bibliotecas Python**:
  - `psycopg2`: Para conexão e interação com o PostgreSQL.
  - `pandas`: Para manipulação e leitura do arquivo CSV.

## Banco de Dados

As variáveis para conexão com o Banco de Dados se encontram no arquivo `db.py`

1. **Clone o repositório** (ou faça o download do código):

    ```bash
    git clone https://github.com/PedroMoT4/teste_dev.git
    ```

2. **Instale as dependências** usando `pip`:

    ```bash
    pip install psycopg2
    pip install pandas
    ```

3. **Configuração do PostgreSQL**: Certifique-se de que o PostgreSQL está ativo e que o banco de dados `teste_dev` foi criado com o comando:

    ```sql
    CREATE DATABASE teste_dev;
    ```

4. **Posicione o arquivo CSV**: Coloque o arquivo `escolas122022.csv` no mesmo diretório onde está o arquivo `db.py`. Isso garante que o script possa localizá-lo sem modificações adicionais no código.

## Como Executar

Para rodar o programa, execute o arquivo `db.py` com o seguinte comando:

```bash
python ./db.py
