from pathlib import Path

# API
DEBUG_MODE = True
BASE_API_PATH = '/api'
BASE_API_PORT = 5001

# DATABASE
SQLITE_DATABASE_PATH = f'{Path.cwd()}/backend/database/the_database.db'

DATABASE_DDL_PATH = f'{Path.cwd()}/backend/database/ddl.sql'
DATABASE_DML_PATH = f'{Path.cwd()}/backend/database/dml.sql'