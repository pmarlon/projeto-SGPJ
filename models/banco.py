from sqlite3 import *


class Banco:

    def __init__(self):

        self.conn = None
        self.cursor = None
        self.connected = False

    def connect(self):
        self.conn = connect('banco.db')
        self.cursor = self.conn.cursor()
        self.connected = True

    def disconnect(self):
        self.conn.close()
        self.connected = False

    def execute(self, sql, parms=None):
        if self.connected:
            if parms:
                self.cursor.execute(sql, parms)
                return True
            else:
                self.cursor.execute(sql)
        return False

    def fetchall(self):
        return self.cursor.fetchall()

    def persist(self):
        if self.connected:
            self.conn.commit()
            return True
        return False


def init_db():
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
        PRIMARY KEY('id' AUTOINCREMENT))
    """)

    banco.execute("""CREATE TABLE IF NOT EXISTS advogados(
        id INTEGER,
        nome	TEXT NOT NULL,
        endereco	TEXT NOT NULL,
        cidade_uf	TEXT NOT NULL,
        cep	NUMERIC,
        fone_com	NUMERIC,
        fax	NUMERIC,
        email	TEXT NOT NULL,
        oab	INTEGER NOT NULL UNIQUE,
        cpf	INTEGER NOT NULL UNIQUE,
        PRIMARY KEY('id' AUTOINCREMENT))
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
        responsavel	TEXT NOT NULL,
        emenda	TEXT NOT NULL,
        saida	TEXT,
        destino	TEXT NOT NULL,
        PRIMARY KEY('id' AUTOINCREMENT)                   
    )
    """)

    banco.persist()
    banco.disconnect()


def view(tabela):

    try:
        banco = Banco()
        banco.connect()
        banco.execute(f'SELECT * FROM {tabela}')
        rows = banco.fetchall()
        banco.disconnect()
        return rows
    except OperationalError:
        print(f'Ocorreu um erro. Tente novamente')


def search(tabela, *args, **kwargs):
    banco = Banco()
    banco.connect()
    for chave, valor in kwargs.items():
        banco.execute(f"SELECT * FROM {tabela} where {chave} like '%{valor}%'")
        rows = banco.fetchall()
        print(rows)
    banco.disconnect()
    return rows


def insert(tabela, *args):

    try:
        banco = Banco()
        banco.connect()
        banco.execute(f'INSERT INTO {tabela} VALUES {args}')
        banco.persist()
        banco.disconnect()

    except OperationalError:
        print(f'Ocorreu um erro! Tente novamente')


def update(rid, tabela, **kwargs):

    try:
        banco = Banco()
        banco.connect()
        for chave, valor in kwargs.items():
            banco.execute(f'UPDATE {tabela} SET {chave}="{valor}" WHERE id={rid}')
            banco.persist()
        banco.disconnect()
    except OperationalError:
        print('dados inválidos')


def delete(rid, tabela):
    try:
        banco = Banco()
        banco.connect()
        banco.execute(f'DELETE FROM {tabela} WHERE id = {rid}')
        banco.persist()
        banco.disconnect()
    except OperationalError:
        print('Ocorreu um erro. Tente novamente')

init_db()

if __name__ == '__main__':

    #print(view('advogados'))


    #update(1, 'advogados', fone_com='2633-9956')
    #print(view('advogados'))
    #delete(5, 'teste')

    print(search('advogados', endereco='rua', fax='9'))
