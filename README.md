# Teste dev_junior
## Carregamento de Arquivos CSV no Banco de Dados SQL utilizando PostgreSQL e Python

Este projeto conecta-se a um banco de dados PostgreSQL, cria uma tabela de forma dinâmica e insere dados a partir do arquivo `escolas122022.csv`. Ele utiliza a biblioteca `psycopg2` para a conexão com o banco de dados e o `pandas` para manipulação do arquivo CSV.

## Pré-requisitos

Certifique-se de ter o Python 3.x instalado em seu sistema. Você também precisará de um servidor PostgreSQL em execução e acessível localmente.

Neste caso a configuração do Banco de Dados foi feita utilizando o `pgAdmin 4`.

### 1. Instalar dependências

As bibliotecas necessárias para executar o código são:

- `psycopg2`: Biblioteca para conectar ao PostgreSQL.
- `pandas`: Biblioteca para manipulação e leitura do CSV.

Você pode instalá-las diretamente com o comando abaixo:

```bash
pip install psycopg2 
pip install pandas
```

Em caso de incompatibilidade com a biblioteca `psycopg2` recomendo a utilização da biblioteca `psycopg2-binary`.

# Formatação  da tabela
Para simplificação do carregamento optei por formatar as colunas da tabela no `pgAdmin 4`
