import oracledb

# Configurações de conexão
username = 'system'  # Usuário do banco de dados
password = 'your_password'  # Substitua pela sua senha
dsn = 'localhost:1521/XEPDB1'  # DSN para conexão

def get_connection():
    try:
        connection = oracledb.connect(
            user=username,
            password=password,
            dsn=dsn
        )
        return connection
    except oracledb.Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None
    
def setup_database():
    connection = get_connection()
    if connection is None:
        return

    cursor = connection.cursor()

    cursor.execute("SELECT table_name FROM user_tables WHERE table_name = 'SAFRA'")
    safra_exists = cursor.fetchone()

    if safra_exists:
        print("Tabela 'SAFRA' já existe. Pulando criação de tabelas.")
        return

    # Define the updated table structures to match the new fields in your classes
    tables = {
        'SAFRA': """
            CREATE TABLE safra (
                id NUMBER GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
                ano NUMBER NOT NULL
            )
        """,
        'CULTURA': """
            CREATE TABLE cultura (
                id NUMBER GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
                nome VARCHAR2(255) NOT NULL,
                tipo_cultura VARCHAR2(255) NOT NULL,
                estadio_fenologico VARCHAR2(255) NOT NULL,
                safra_id NUMBER NOT NULL,
                FOREIGN KEY (safra_id) REFERENCES safra(id)
            )
        """,
        'TALHAO': """
            CREATE TABLE talhao (
                id NUMBER GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
                nome VARCHAR2(255) NOT NULL,
                forma VARCHAR2(50) NOT NULL,
                comprimento FLOAT,
                largura FLOAT,
                base FLOAT,
                altura FLOAT,
                base_maior FLOAT,
                base_menor FLOAT,
                data DATE NOT NULL,
                cultura_id NUMBER NOT NULL,
                FOREIGN KEY (cultura_id) REFERENCES cultura(id)
            )
        """,
        'RUAS': """
            CREATE TABLE ruas (
                id NUMBER GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
                nome VARCHAR2(255) NOT NULL,
                comprimento FLOAT NOT NULL,
                largura FLOAT NOT NULL,
                talhao_id NUMBER NOT NULL,
                FOREIGN KEY (talhao_id) REFERENCES talhao(id)
            )
        """,
        'PRODUTOS': """
            CREATE TABLE produtos (
                id NUMBER GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
                nome VARCHAR2(255) NOT NULL,
                dose_recomendada VARCHAR2(255)  -- New field for recommended dose
            )
        """,
        'PRAGA': """
            CREATE TABLE praga (
                id NUMBER GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
                nome VARCHAR2(255) NOT NULL,
                estagio VARCHAR2(255) NOT NULL,  -- New field for stage
                nivel_infestacao VARCHAR2(255) NOT NULL,  -- New field for infestation level
                condicoes_climaticas VARCHAR2(255) NOT NULL
            )
        """,
        'METODO_CONTROLE': """
            CREATE TABLE metodo_controle (
                id NUMBER GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
                metodo VARCHAR2(255) NOT NULL,
                periodo_ideal VARCHAR2(255),  -- Ideal period for control
                dose_recomendada VARCHAR2(255),  -- New field for recommended dose
                metodo_alternativo VARCHAR2(255),  -- New field for alternative method
                produto_recomendado NUMBER,  -- Foreign key to recommended product
                FOREIGN KEY (produto_recomendado) REFERENCES produtos(id)
            )
        """,
        'DEFENSIVO': """
            CREATE TABLE defensivo (
                id NUMBER GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
                data DATE NOT NULL,
                praga_id NUMBER NOT NULL,
                metodo_controle_id NUMBER NOT NULL,
                FOREIGN KEY (praga_id) REFERENCES praga(id),
                FOREIGN KEY (metodo_controle_id) REFERENCES metodo_controle(id)
            )
        """,
        'PRAGATALHAO': """
            CREATE TABLE praga_talhao (
                id NUMBER GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
                talhao_id NUMBER NOT NULL,
                praga_id NUMBER NOT NULL,
                defensivo_id NUMBER,
                FOREIGN KEY (talhao_id) REFERENCES talhao(id),
                FOREIGN KEY (praga_id) REFERENCES praga(id),
                FOREIGN KEY (defensivo_id) REFERENCES defensivo(id)
            )
        """
    }

    # Create all tables
    for table_name, create_statement in tables.items():
        try:
            cursor.execute(f"SELECT table_name FROM user_tables WHERE table_name = '{table_name.upper()}'")
            result = cursor.fetchone()
            if result:
                print(f"Tabela '{table_name}' já existe.")
            else:
                cursor.execute(create_statement)
                print(f"Tabela '{table_name}' criada com sucesso.")
        except oracledb.DatabaseError as e:
            print(f"Erro ao verificar ou criar a tabela '{table_name}': {e}")

    # Print the tables currently in the schema
    cursor.execute("SELECT table_name FROM user_tables")
    tables = cursor.fetchall()
    print("Tabelas no esquema:")
    for table in tables:
        print(table[0])

    cursor.close()
    connection.close()

def insert_data():
    connection = get_connection()
    if connection is None:
        return
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT COUNT(*) FROM safra")
        safra_count = cursor.fetchone()[0]

        if safra_count > 0:
            print("Data already exists in 'safra'. Skipping data insertion.")
            return

        # Step 1: Insert into safra (single entry for 2024)
        cursor.execute("""
            INSERT INTO safra (ano) 
            VALUES (2024)
        """)
        cursor.execute("SELECT id FROM safra WHERE ano = 2024")
        safra_id = cursor.fetchone()[0]

        # Step 2: Insert Cultura (Cana-de-açúcar)
        cursor.execute("""
            INSERT INTO cultura (nome, tipo_cultura, estadio_fenologico, safra_id)
            VALUES (:1, :2, :3, :4)
        """, ('Cana-de-açúcar', 'Agrícola', 'Pós-floração', safra_id))
        cursor.execute("SELECT id FROM cultura WHERE nome = 'Cana-de-açúcar' AND safra_id = :1", (safra_id,))
        cultura_id = cursor.fetchone()[0]

        # Lista de pragas e seus detalhes
        pragas_detalhes = [
            ('Percevejo-castanho', 'Adulto', 'Moderado', 'Clima seco', 'Controle cultural: rotação de culturas', 'Imidacloprid', '150 mL/ha', 'Cobertura do solo', 'Durante a fase de crescimento'),
            ('Pulgão-da-cana', 'Ovo', 'Leve', 'Clima úmido', 'Controle cultural: rotação de culturas', 'Imidacloprid', '200 g/ha', 'Manejo integrado de pragas', 'Durante o plantio ou início'),
            ('Formiga-cortadeira', 'Ovo', 'Severo', 'Clima seco', 'Controle cultural: rotação de culturas', 'Imidacloprid', '150 g/ha', 'Cobertura do solo', 'Durante a fase de crescimento'),
            ('Percevejo-castanho', 'Adulto', 'Moderado', 'Alta umidade, clima quente', 'Cobertura do solo', 'Lufenuron', '120 mL/ha', 'Cobertura do solo', 'Períodos de alta umidade')
        ]

        for praga in pragas_detalhes:
            # Step 3: Insert into praga
            cursor.execute("""
                INSERT INTO praga (nome, estagio, nivel_infestacao, condicoes_climaticas) 
                VALUES (:1, :2, :3, :4)
            """, (praga[0], praga[1], praga[2], praga[3]))
            cursor.execute("SELECT id FROM praga WHERE nome = :1", (praga[0],))
            praga_id = cursor.fetchone()[0]

            # Step 4: Insert into produtos
            cursor.execute("""
                INSERT INTO produtos (nome, dose_recomendada) 
                VALUES (:1, :2)
            """, (praga[5], praga[6]))
            cursor.execute("SELECT id FROM produtos WHERE nome = :1", (praga[5],))
            produto_id = cursor.fetchone()[0]

            # Step 5: Insert into metodo_controle
            cursor.execute("""
                INSERT INTO metodo_controle (metodo, periodo_ideal, dose_recomendada, metodo_alternativo, produto_recomendado)
                VALUES (:1, :2, :3, :4, :5)
            """, (praga[4], praga[8], praga[6], praga[7], produto_id))
            cursor.execute("SELECT id FROM metodo_controle WHERE metodo = :1", (praga[4],))
            metodo_controle_id = cursor.fetchone()[0]

            # Step 6: Insert into defensivo
            cursor.execute("""
                INSERT INTO defensivo (data, praga_id, metodo_controle_id) 
                VALUES (SYSDATE, :1, :2)
            """, (praga_id, metodo_controle_id))

        # Step 7: Insert into talhao (single entry for Talhão 1)
        cursor.execute("""
            INSERT INTO talhao (nome, forma, comprimento, largura, base, altura, base_maior, base_menor, data, cultura_id)
            VALUES (:1, :2, :3, :4, :5, :6, :7, :8, SYSDATE, :9)
        """, ('Talhão 1', 'retangulo', 100, 50, None, None, None, None, cultura_id))
        cursor.execute("SELECT id FROM talhao WHERE nome = 'Talhão 1' AND cultura_id = :1", (cultura_id,))
        talhao_id = cursor.fetchone()[0]

        # Step 8: Insert into praga_talhao (for each praga)
        for praga in pragas_detalhes:
            cursor.execute("SELECT id FROM praga WHERE nome = :1", (praga[0],))
            praga_id = cursor.fetchone()[0]

            cursor.execute("""
                INSERT INTO praga_talhao (talhao_id, praga_id, defensivo_id)
                VALUES (:1, :2, NULL)
            """, (talhao_id, praga_id))

        # Step 9: Insert into ruas (single entry)
        cursor.execute("""
            INSERT INTO ruas (nome, comprimento, largura, talhao_id)
            VALUES (:1, :2, :3, :4)
        """, ('Rua 1', 50, 5, talhao_id))

        # Commit all changes
        connection.commit()
        print("Data inserted successfully.")

    except oracledb.Error as e:
        print(f"Error occurred: {e}")
        connection.rollback()  # Rollback in case of any error
    finally:
        cursor.close()

def init():
    setup_database()
    insert_data()

