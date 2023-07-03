import sqlite3
import config
from flask import g

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(config.SQLITE_DATABASE_PATH)
        db.row_factory = sqlite3.Row
    return db

def initialize_database_ddl():
    with open(config.DATABASE_DDL_PATH) as f:
        db = get_db()
        db.executescript(f.read())
        db.commit()

def initialize_database_dml():
    with open(config.DATABASE_DML_PATH) as f:
        db = get_db()
        db.executescript(f.read())
        db.commit()

def query_db(query, args=()):
    cur = get_db().execute(query, args)
    columns = [col[0] for col in cur.description]
    return [dict(zip(columns, row)) for row in cur.fetchall()]