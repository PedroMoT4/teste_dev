import psycopg2
import pandas as pd

#Variaveis de ambiente
DB_HOST = "localhost"
DB_NAME = "teste_dev"
DB_USER = "postgres"
DB_PASSWORD = "houer_test_dev"

#Funcao para se conectar ao bd
def conectar_db():
	return psycopg2.connect(
		host=DB_HOST,
		database=DB_NAME,
		user=DB_USER,
		password=DB_PASSWORD
	)

#Funcao para criar a tabela de forma dinamica
def create_table(nome_tabela, lista_colunas):

	#Gerando o nome das colunas da tabela
	colunas_com_tipos = ", ".join([f'{col} TEXT' for col in lista_colunas])

	#Query de criacao da tabela
	create_table_query = f"""
	CREATE TABLE IF NOT EXISTS {nome_tabela} (
		id SERIAL PRIMARY KEY,
		{colunas_com_tipos}
	);
	"""

	#Conectar ao banco de dados
	conn = conectar_db()
	cursor = conn.cursor()

	try:
		cursor.execute(create_table_query)
		conn.commit()
		print(f"Tabela {nome_tabela} criada ou ja existente")
	except Exception as e:
		print(f"Erro ao criar a tabela: {e}")
		conn.rollback()
	finally:
		cursor.close()
		conn.close()

#Funcao para inserir os valores na tabela
def inserir_dados(data, lista_colunas, nome_tabela):
	conn = conectar_db()
	cursor = conn.cursor()

	#Gerando os placeholders '%s' e a lista de colunas de forma dinamica
	placeholders = ', '.join(['%s'] * len(lista_colunas))
	colunas = ', '.join(lista_colunas)
      
	#Query de insercao
	query_inserir = f"""
	INSERT INTO escolas_teste_dev ({colunas})
    VALUES ({placeholders});
	"""

	try:
		cursor.executemany(query_inserir, data)
		conn.commit()
		print("Dados inseridos na tabela com sucesso")
	except Exception as e:
		print(f"Erro ao inserir os valores: {e}")
		conn.rollback()
	finally:
		cursor.close()
		conn.close()


#Funcao principal
def main():
	#Path do arquivo csv
	path = 'escolas122022.csv' # Importante deixar o arquivo no mesmo diretorio do arquivo db.py

	#Utilizando o encoding 'cp860' para o carregamento sem erros
	escolas = pd.read_csv(path, sep =';', encoding='cp860')

	#Nome das colunas e valores
	lista_colunas = list(escolas.columns)
	valores = escolas.values.tolist()

	#Nome da tabela no banco de dados
	nome_tabela = 'escolas_teste_dev'

	#Criar a tabela no bd
	create_table(nome_tabela, lista_colunas)

	#Inserir os valores na tabela
	inserir_dados(valores, lista_colunas, nome_tabela)

#Execucao da funcao principal
if __name__ == '__main__':
	main()