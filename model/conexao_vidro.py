import psycopg2


class ConexaoVidro:

    """Metodo Construtor"""
    def __init__(self):
        """connetion recebe informacoes para conexao com postgre"""
        self.connection = psycopg2.connect(
            user="postgres",
            password="root",
            host="localhost",
            port="5432",
            database="temperCalcDB"
        )

        """Instancia um objeto cursor"""
        self.cursor = self.connection.cursor()

        """Variavel que vai guardar o nome da tabela"""
        self.table_name = None

        """Variavel que vai guardar o SQL de insercao"""
        self.sql_insert = None
        self.sql_delete = None
        self.sql_query = None
        self.return_query = None

        """Variavel que vai guardar os valores a serem inseridos no banco
            tem que ser uma tupla ( )"""
        self.inserted_values = ()
        self.delete_value = None

        # Verificar o que estes comandos fazem na conexão
        # self.autocommit = extensions.ISOLATION_LEVEL_AUTOCOMMIT
        # self.connection.set_isolation_level(self.autocommit)
                
    def insert_vidro(self):
        try:
            """Instancia um objeto cursor"""
            self.cursor = self.connection.cursor()
            self.table_name = "vidros"
            self.sql_insert = "INSERT INTO " + self.table_name + "(codigo, descricao, espessura, preco) VALUES(%s,%s,%s,%s)"
            self.cursor.execute(self.sql_insert, self.inserted_values)
            
            """Realiza o commit na conexao(insere os dados no banco)"""
            self.connection.commit()
            print("Cadastro realizado com Sucesso!")

        except:
            print("Erro")
            self.connection = None

        finally:

            self.cursor.close()
            self.connection.close()


    def delete_vidro(self, delete_value):

        self.cursor = self.connection.cursor()
        self.delete_value = delete_value
        self.table_name = "vidros"
        self.sql_query = "Delete from " + self.table_name + " where codigo = %s "

        self.cursor.execute(self.sql_query, (self.delete_value,))
        self.connection.commit()
        self.cursor.close()
        self.connection.close()

    def buscar_vidro(self):
        self.cursor = self.connection.cursor()
        self.table_name = "vidros"
        self.sql_query = "Select codigo from " + self.table_name
        self.cursor.execute(self.sql_query)
        
        self.return_query = self.cursor.fetchall()

        return self.return_query
    
    def preenche_combobox_vidro(self):
        self.cursor = self.connection.cursor()
        self.table_name = "vidros"
        self.sql_query = "Select descricao from " + self.table_name
        self.cursor.execute(self.sql_query)
        
        self.return_query = self.cursor.fetchall()

        return self.return_query


