import mysql.connector

class BaseRepository:
    def __init__(self, connection):
        self.connection = connection

    def insert(self, table, data):
        cursor = self.connection.cursor()
        try:
            columns = ', '.join(data.keys())
            values = ', '.join(['%s'] * len(data))
            sql_insert = f"INSERT INTO {table} ({columns}) VALUES ({values})"
            cursor.execute(sql_insert, list(data.values()))
            self.connection.commit()
            return cursor.lastrowid  # Retorna o ID do último registro inserido
        except mysql.connector.Error as e:
            print(f"Erro ao inserir dados em {table}: {e}")
        finally:
            cursor.close()

    def update(self, table, data, where_clause, where_params):
        cursor = self.connection.cursor()
        try:
            # Certifique-se de que o número de colunas corresponde ao número de valores
            if len(data.keys()) != len(data.values()):
                raise ValueError("Número de colunas não corresponde ao número de valores.")

            set_clause = ', '.join([f"{key} = %s" for key in data.keys()])
            sql_update = f"UPDATE {table} SET {set_clause} WHERE {where_clause}"
            
            # Verifique o número de parâmetros
            params = list(data.values()) + list(where_params.values())
            if sql_update.count("%s") != len(params):
                raise ValueError("Número de placeholders na consulta não corresponde ao número de valores.")

            # Executar a consulta
            cursor.execute(sql_update, params)
            self.connection.commit()
            
            print(f"{cursor.rowcount} linha(s) atualizada(s) em {table}.")
            
        except ValueError as ve:
            print(f"Erro: {ve}")
        except mysql.connector.Error as e:
            print(f"Erro ao atualizar dados em {table}: {e}")
            self.connection.rollback()  # Reverter a transação em caso de erro
        finally:
            cursor.close()


    def delete(self, table, where_clause, where_params):
        cursor = self.connection.cursor()
        try:
            sql_delete = f"DELETE FROM {table} WHERE {where_clause}"
            cursor.execute(sql_delete, list(where_params.values()))
            self.connection.commit()
        except mysql.connector.Error as e:
            print(f"Erro ao deletar dados de {table}: {e}")
        finally:
            cursor.close()

    def get_by_id(self, table, id):
        cursor = self.connection.cursor(dictionary=True)
        try:
            cursor.execute(f"SELECT * FROM {table} WHERE id = %s", (id,))
            return cursor.fetchone()
        except mysql.connector.Error as e:
            print(f"Erro ao obter dados de {table} pelo ID: {e}")
            return None
        finally:
            cursor.close()

    def get_all(self, table):
        cursor = self.connection.cursor(dictionary=True)
        try:
            cursor.execute(f"SELECT * FROM {table}")
            return cursor.fetchall()
        except mysql.connector.Error as e:
            print(f"Erro ao obter todos os dados de {table}: {e}")
            return []
        finally:
            cursor.close()
