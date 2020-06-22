import sqlite3

db_name = 'C:/Users/Exist/Desktop/cat_humor_school/cat_humor_school.sqlite3'

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def select_all(*args, **kwargs):
    conn = sqlite3.connect(db_name)
    conn.row_factory = dict_factory
    cur = conn.cursor()    
    rows = cur.execute(*args, **kwargs).fetchall()
    return rows

def select_one(*args, **kwargs):
    conn = sqlite3.connect(db_name)
    conn.row_factory = dict_factory
    cur = conn.cursor()
    row = cur.execute(*args, **kwargs).fetchone() 
    return row

def excute_commit(*args, **kwargs):
    try:
        with sqlite3.connect(db_name) as conn:
            cur = conn.cursor()
            cur.execute(*args, **kwargs)
            conn.commit()
            return cur.lastrowid
    except Exception as e:
        conn.rollback()
        raise Exception('rollbacked db')
