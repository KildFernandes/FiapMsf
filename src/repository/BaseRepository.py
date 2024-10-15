import oracledb

class BaseRepository:
    def __init__(self, connection):
        self.connection = connection

    def insert(self, table, data):
        cursor = self.connection.cursor()
        try:
            columns = ', '.join(data.keys())
            values = ', '.join([f":{i+1}" for i in range(len(data))])  # Oracle uses :1, :2 for placeholders
            sql_insert = f"INSERT INTO {table} ({columns}) VALUES ({values})"

            # Bind the values (including the correctly formatted date)
            cursor.execute(sql_insert, list(data.values()))
            self.connection.commit()
            return cursor.lastrowid  # Returns the ID of the last inserted record
        except oracledb.Error as e:
            print(f"Erro ao inserir dados em {table}: {e}")
        finally:
            cursor.close()

    def update(self, table, data, where_clause, where_params):
        cursor = self.connection.cursor()
        try:
            if len(data.keys()) != len(data.values()):
                raise ValueError("Número de colunas não corresponde ao número de valores.")

            set_clause = ', '.join([f"{key} = :{i+1}" for i, key in enumerate(data.keys())])
            sql_update = f"UPDATE {table} SET {set_clause} WHERE {where_clause}"
            
            params = list(data.values()) + list(where_params.values())
            
            cursor.execute(sql_update, params)
            self.connection.commit()
            
            print(f"{cursor.rowcount} linha(s) atualizada(s) em {table}.")
            
        except ValueError as ve:
            print(f"Erro: {ve}")
        except oracledb.Error as e:
            print(f"Erro ao atualizar dados em {table}: {e}")
            self.connection.rollback()  # Revert the transaction in case of error
        finally:
            cursor.close()

    def delete(self, table, where_clause, where_params):
        cursor = self.connection.cursor()
        try:
            sql_delete = f"DELETE FROM {table} WHERE {where_clause}"
            cursor.execute(sql_delete, list(where_params.values()))
            self.connection.commit()
        except oracledb.Error as e:
            print(f"Erro ao deletar dados de {table}: {e}")
        finally:
            cursor.close()

    def get_by_id(self, table, id):
        cursor = self.connection.cursor()
        try:
            cursor.execute(f"SELECT * FROM {table} WHERE id = :1", (id,))
            return cursor.fetchone()
        except oracledb.Error as e:
            print(f"Erro ao obter dados de {table} pelo ID: {e}")
            return None
        finally:
            cursor.close()

    def get_all(self, table):
        cursor = self.connection.cursor()
        try:
            cursor.execute(f"SELECT * FROM {table}")
            return cursor.fetchall()
        except oracledb.Error as e:
            print(f"Erro ao obter todos os dados de {table}: {e}")
            return []
        finally:
            cursor.close()
