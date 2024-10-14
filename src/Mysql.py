import mysql.connector
from mysql.connector import errorcode

# Configurações de conexão
username = 'your_user'         # Usuário do banco de dados
password = 'your_password'     # Substitua pela sua senha
host = 'localhost'             # O host onde o MySQL está rodando
database = 'your_database'     # Nome do banco de dados

def get_connection():
    try:
        connection = mysql.connector.connect(
            user=username,
            password=password,
            host=host,
            database=database
        )
        return connection
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Erro: Nome de usuário ou senha inválidos")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Erro: Banco de dados não existe")
        else:
            print(f"Erro ao conectar ao banco de dados: {err}")
        return None

def setup_database():
    connection = get_connection()
    if connection is None:
        return

    cursor = connection.cursor()
    tables = {
        'SAFRA': """
            CREATE TABLE IF NOT EXISTS safra (
                id INT AUTO_INCREMENT PRIMARY KEY,
                ano INT NOT NULL
            ) ENGINE=InnoDB
        """,
        'CULTURA': """
            CREATE TABLE IF NOT EXISTS cultura (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nome VARCHAR(255) NOT NULL,
                tipo_cultura VARCHAR(255) NOT NULL,
                estadio_fenologico VARCHAR(255) NOT NULL,
                safra_id INT NOT NULL,
                FOREIGN KEY (safra_id) REFERENCES safra(id)
            ) ENGINE=InnoDB
        """,
        'TALHAO': """
            CREATE TABLE IF NOT EXISTS talhao (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nome VARCHAR(255) NOT NULL,
                forma VARCHAR(50) NOT NULL,
                comprimento FLOAT,
                largura FLOAT,
                base FLOAT,
                altura FLOAT,
                base_maior FLOAT,
                base_menor FLOAT,
                data DATE NOT NULL,
                cultura_id INT NOT NULL,
                FOREIGN KEY (cultura_id) REFERENCES cultura(id)
            ) ENGINE=InnoDB
        """,
        'RUAS': """
            CREATE TABLE IF NOT EXISTS ruas (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nome VARCHAR(255) NOT NULL,
                comprimento FLOAT NOT NULL,
                largura FLOAT NOT NULL,
                talhao_id INT NOT NULL,
                FOREIGN KEY (talhao_id) REFERENCES talhao(id)
            ) ENGINE=InnoDB
        """,
        'PRODUTOS': """
            CREATE TABLE IF NOT EXISTS produtos (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nome VARCHAR(255) NOT NULL
            ) ENGINE=InnoDB
        """,
        'PRAGA': """
            CREATE TABLE IF NOT EXISTS praga (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nome VARCHAR(255) NOT NULL,
                condicoes_climaticas VARCHAR(255) NOT NULL
            ) ENGINE=InnoDB
        """,
        'METODO_CONTROLE': """
            CREATE TABLE IF NOT EXISTS metodo_controle (
                id INT AUTO_INCREMENT PRIMARY KEY,
                metodo VARCHAR(255) NOT NULL,
                periodo_ideal VARCHAR(255),
                produto_recomendado INT,
                FOREIGN KEY (produto_recomendado) REFERENCES produtos(id)
            ) ENGINE=InnoDB
        """,
        'DEFENSIVO': """
            CREATE TABLE IF NOT EXISTS defensivo (
                id INT AUTO_INCREMENT PRIMARY KEY,
                data DATE NOT NULL,
                praga_id INT NOT NULL,
                metodo_controle_id INT NOT NULL,
                FOREIGN KEY (praga_id) REFERENCES praga(id),
                FOREIGN KEY (metodo_controle_id) REFERENCES metodo_controle(id)
            ) ENGINE=InnoDB
        """,
        'PRAGATALHAO': """
            CREATE TABLE IF NOT EXISTS praga_talhao (
                id INT AUTO_INCREMENT PRIMARY KEY,
                talhao_id INT NOT NULL,
                praga_id INT NOT NULL,
                defensivo_id INT,
                FOREIGN KEY (talhao_id) REFERENCES talhao(id),
                FOREIGN KEY (praga_id) REFERENCES praga(id),
                FOREIGN KEY (defensivo_id) REFERENCES defensivo(id)
            ) ENGINE=InnoDB;
        """
    }

    for table_name, create_statement in tables.items():
        try:
            # Verificar se a tabela existe
            cursor.execute(f"SHOW TABLES LIKE '{table_name}'")
            result = cursor.fetchone()
            if result:
                print(f"Tabela '{table_name}' já existe.")
            else:
                # Criar a tabela
                cursor.execute(create_statement)
                print(f"Tabela '{table_name}' criada com sucesso.")
        except mysql.connector.Error as err:
            print(f"Erro ao verificar ou criar a tabela '{table_name}': {err}")

    # Mostrar todas as tabelas no banco de dados
    cursor.execute("SHOW TABLES")
    tables = cursor.fetchall()
    print("Tabelas no esquema:")
    for table in tables:
        print(table[0])

    cursor.close()
    connection.close()
