import mariadb
import sys

def connection(nome):
    try:
        conn = mariadb.connect(
            user="root",
            password="senhaforte",
            host="192.168.15.8",
            port=3306,
            database="ru_zero"

        )
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)

    # Get Cursor
    cur = conn.cursor()

    try:
        cur.execute(f"SELECT numero_matricula FROM pessoa WHERE nome='{nome}'")
        for data in cur:
            print(data)
    except:
        return print('Cadastro não encontrado')