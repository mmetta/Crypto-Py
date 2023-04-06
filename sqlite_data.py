import ast
import json
import os
import sqlite3

appData = os.getenv('APPDATA') + '\\CryptoPy'
database = os.path.join(appData, 'cryptodata.db')


def create_db():
    conn = sqlite3.connect(database)
    c = conn.cursor()

    c.execute('''CREATE TABLE par_list
                 (par TEXT NOT NULL);''')

    c.execute('''CREATE TABLE all_list
                     (par TEXT NOT NULL);''')

    c.execute('''CREATE TABLE BRL_list
                         (par TEXT NOT NULL,
                          valor REAL,
                          quant REAL,
                          total value REAL);''')

    c.execute('''CREATE TABLE BUSD_list
                             (par TEXT NOT NULL,
                              valor REAL,
                              quant REAL,
                              total value REAL);''')

    c.execute('''CREATE TABLE USDT_list
                                 (par TEXT NOT NULL,
                                  valor REAL,
                                  quant REAL,
                                  total value REAL);''')

    c.execute('''CREATE TABLE settings 
                                     (fiat TEXT NOT NULL);''')

    c.execute('INSERT INTO settings (fiat) VALUES (?)', ('BUSD',))

    conn.commit()
    conn.close()


def select_settings():
    conn = sqlite3.connect(database)
    c = conn.cursor()
    c.execute("SELECT * FROM settings")
    rows = c.fetchall()
    columns = [column[0] for column in c.description]
    data = []
    for row in rows:
        data.append(dict(zip(columns, row)))
    json_data = json.dumps(data)
    obj = json.loads(json_data)
    if obj:
        return obj[0]
    else:
        return []


def update_settings(n_fiat):
    value = n_fiat['fiat']
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    cursor.execute(f"UPDATE settings SET fiat = '{value}'")
    conn.commit()
    conn.close()


def select_all(tbl):
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    cursor.execute("SELECT par FROM {}".format(tbl))
    rows = cursor.fetchall()
    data = []
    for row in rows:
        data.append(row[0])
    if data:
        return data
    else:
        return []


def insert_par_list(nome):
    conn = sqlite3.connect(database)
    c = conn.cursor()
    c.execute('INSERT INTO par_list (par) VALUES (?)', (nome,))
    conn.commit()
    conn.close()


def delete_par_list(id_par):
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM par_list WHERE par = '{}'".format(id_par))
    conn.commit()
    conn.close()


def update_all_list(lista):
    conn = sqlite3.connect(database)
    c = conn.cursor()
    c.execute('DELETE FROM all_list')
    for nome in lista:
        c.execute('INSERT INTO all_list (par) VALUES (?)', (nome,))
    conn.commit()
    conn.close()


def insert_wallet(val, fiat):
    tbl = f'{fiat}_list'
    conn = sqlite3.connect(database)
    c = conn.cursor()
    c.execute("INSERT INTO {} (par, valor, quant, total) VALUES (?, ?, ?, ?)".format(tbl),
              (val[0], val[1], val[2], val[3]))
    conn.commit()
    conn.close()


def select_wallet(fiat):
    tbl = f'{fiat}_list'
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM {}".format(tbl))
    rows = cursor.fetchall()
    columns = [column[0] for column in cursor.description]
    data = []
    for row in rows:
        data.append(dict(zip(columns, row)))
    json_data = json.dumps(data)
    obj = json.loads(json_data)
    if obj:
        return obj
    else:
        return []


def update_my_wallet(li_par, fiat):
    tbl = f'{fiat}_list'
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM {}'.format(tbl))
    for col in li_par:
        cursor.execute("INSERT INTO {} (par, valor, quant, total) VALUES (?, ?, ?, ?)".format(tbl),
                       (col[0], col[1], col[2], col[3]))
    conn.commit()
    conn.close()


def delete_wallet(id_par, fiat):
    tbl = f'{fiat}_list'
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM {} WHERE par = '{}'".format(tbl, id_par))
    conn.commit()
    conn.close()


def converter(campo):
    return ast.literal_eval(campo)
