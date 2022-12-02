import mariadb
import sys

def wrning_connection(n_matricula):
    dados = 0

    try:
        conn = mariadb.connect(
            user="root",
            password="senhaforte",
            host="localhost",
            port=3306,
            database="ru_zero"

        )
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)

    # Get Cursor
    cur = conn.cursor()

    try:
        cur.execute(f"SELECT penalidades FROM pessoa WHERE numero_matricula='{n_matricula}'")
        for data in cur:
            penalidade = data
        nova_penalidade = (int(penalidade[0]) + 1)
        cur.execute(f"UPDATE ru_zero.pessoa SET penalidades={nova_penalidade} WHERE numero_matricula = '{n_matricula}'")
        cur.execute(f"SELECT email, penalidades FROM pessoa WHERE numero_matricula='{n_matricula}'")
        for data in cur:
            dados = data

    except:
        return print('Cadastro não encontrado')

    return dados

def register_user(numero_matricula, email):
    try:
        conn = mariadb.connect(
            user="root",
            password="senhaforte",
            host="localhost",
            port=3306,
            database="ru_zero"

        )
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)

    # Get Cursor
    cur = conn.cursor()

    try:
        cur.execute(f"INSERT INTO pessoa(nome, numero_matricula, penalidades, email) VALUES('teste','{numero_matricula}',0,'{email}');")
        conn.commit()
    except:
        return print('Cadastro não encontrado')

    return
