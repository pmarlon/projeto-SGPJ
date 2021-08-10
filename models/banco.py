from sqlite3 import *


class Banco:
    """ Classe de criação do Banco de dados """
    def __init__(self):

        self.conn = None
        self.cursor = None
        self.connected = False

    def connect(self):
        """ Realiza a conexão com o banco de dados"""
        self.conn = connect('banco.db')
        self.cursor = self.conn.cursor()
        self.connected = True

    def disconnect(self):
        """ Se desconecta do banco """
        self.conn.close()
        self.connected = False

    def execute(self, sql, parms=None):
        """ Executa as consultas ao banco de dados """

        if self.connected:
            if parms:
                self.cursor.execute(sql, parms)
                return True
            else:
                self.cursor.execute(sql)
        return False

    def fetchall(self):
        """ Busca todas as linhas de um resultado de consulta e retorna uma lista com os resultados """
        return self.cursor.fetchall()

    def persist(self):
        """ Confirma a execução atual, gravando no banco de dados """
        if self.connected:
            self.conn.commit()
            return True
        return False


def init_db():
    """ Função que cria as tabelas do banco de dados caso não existam """
    banco = Banco()
    banco.connect()
    banco.execute("""CREATE TABLE IF NOT EXISTS processos (
        id INTEGER,
        caso INTEGER UNIQUE,
        autor TEXT NOT NULL,
        reu	TEXT NOT NULL,
        adv_externo	TEXT NOT NULL,
        adv_adverso	TEXT NOT NULL,
        processo	TEXT NOT NULL,
        inicio	TEXT NOT NULL,
        vr_causa	REAL NOT NULL,
        tipo_acao	TEXT NOT NULL,
        vara_tribunal	TEXT NOT NULL,
        uf_municipio	TEXT NOT NULL,
        situacao	TEXT,
        pos_feito	TEXT,
        observacao	TEXT,
        valor_atual	REAL,
        pedido	TEXT,
        fim	TEXT,
        perda	TEXT,
        end_parte_adv TEXT,
        PRIMARY KEY("id" AUTOINCREMENT))
    """)

    banco.execute("""CREATE TABLE IF NOT EXISTS advogados(
        id INTEGER,
        nome	TEXT NOT NULL,
        endereco	TEXT NOT NULL,
        cidade_uf	TEXT NOT NULL,
        cep	NUMERIC,
        fax	NUMERIC,
        fone_com	NUMERIC,
        email	TEXT NOT NULL,
        oab	TEXT NOT NULL UNIQUE,
        cpf	INTEGER NOT NULL UNIQUE,
        PRIMARY KEY("id" AUTOINCREMENT))
        """)
    banco.execute("""CREATE TABLE IF NOT EXISTS consultas(
        id INTEGER,
        consulta	INTEGER NOT NULL UNIQUE,
        ref	TEXT NOT NULL,
        prioridade	TEXT NOT NULL,
        esperado	TEXT,
        entrada	TEXT NOT NULL,
        origem	TEXT NOT NULL,
        assunto	TEXT NOT NULL,
        interessado	TEXT NOT NULL,
        adv_cojur TEXT NOT NULL,
        emenda	TEXT NOT NULL,
        saida	TEXT,
        destino	TEXT NOT NULL,
        PRIMARY KEY("id" AUTOINCREMENT)                   
    )
    """)

    banco.execute("""CREATE TABLE IF NOT EXISTS ocorrencias (
        id INTEGER,
        caso INTEGER NOT NULL,
        data TEXT NOT NULL,
        descricao TEXT,
        valor TEXT NOT NULL,
        vr_atual TEXT NOT NULL, 
        FOREIGN KEY(caso) REFERENCES processos (caso) ON DELETE CASCADE,
        PRIMARY KEY("id" AUTOINCREMENT)
)
""")

    banco.persist()
    banco.disconnect()


def view(tabela):
    """ Função que recebe por parâmetro o nome da tabela
     a ser consultada e retorna todas as linhas encontradas """
    banco = Banco()
    banco.connect()
    banco.execute(f'SELECT * FROM {tabela}')
    rows = banco.fetchall()
    banco.disconnect()
    return rows


def search(tabela, *, parms='*', clause=None):
    """ Função que recebe como parâmetro obrigatório o nome da tabela a ser consultada,
         como parâmetro padrão recebe os filtros da pesquisa e retorna todas as linhas encontradas """
    banco = Banco()
    banco.connect()
    banco.execute(f"SELECT {parms} FROM {tabela} {clause}")
    rows = banco.fetchall()
    banco.disconnect()
    return rows


def insert(tabela, *args):
    """ Função que recebe como parâmetro obrigatório o nome da tabela a ser consultada,
        e os dados para inserção como *args e os insere na tabela escolhida """

    banco = Banco()
    banco.connect()
    banco.execute(f"INSERT INTO {tabela} VALUES (NULL{', ?' * len(args)})", args)
    banco.persist()
    banco.disconnect()


def update(rid, tabela, **kwargs):
    """ Função que recebe como parâmetro obrigatório o nome da tabela e o id da linha que deseja editar,
        além dos valores de nome da coluna e dados a serem atualizados """

    banco = Banco()
    banco.connect()
    for coluna, valor in kwargs.items():
        banco.execute(f'UPDATE {tabela} SET {coluna}="{valor}" WHERE id={rid}')
        banco.persist()
    banco.disconnect()


def delete(rid, tabela):
    """ Função que recebe como parâmetro obrigatório o nome da tabela e o id da linha que deseja deletar """

    banco = Banco()
    banco.connect()
    banco.execute("PRAGMA foreign_keys = ON")
    banco.execute(f'DELETE FROM {tabela} WHERE id = {rid}')
    banco.persist()
    banco.disconnect()


init_db()
