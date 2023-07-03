from flask import Flask, g, jsonify
from database import query_db, query_sql_db, initialize_database_ddl, initialize_database_dml
import config
import os

app = Flask(__name__)

# Routes
@app.route('/')
def hello_world():
    return 'hello_world from the API!'

@app.route(config.BASE_API_PATH + '/test')
def test():
    result = query_db("select * from test")
    return jsonify(result)

@app.route(config.BASE_API_PATH + '/test_sql_select')
def test_sql_db_select():
    result = query_sql_db("select * from names")
    return jsonify(result)

@app.route(config.BASE_API_PATH + '/test_sql_stored_procedure')
def test_sql_db_stored_procedure():
    sql = "{call [test].[dbo].testStoredProcedure(?)}"
    values = (5)
    result = query_sql_db(sql, values)
    return jsonify(result)

# Base Configuration
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    sql_db = getattr(g, '_sql_database', None)
    if db is not None:
        db.close()
    if sql_db is not None:
        sql_db.close()

# NO CORS
@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  return response

if __name__ == '__main__':

    # Prevent the reloader from running these scripts twice
    if os.environ.get("WERKZEUG_RUN_MAIN") == "true":
        with app.app_context():
            initialize_database_ddl()
            initialize_database_dml()

    app.run(debug=config.DEBUG_MODE, port=config.BASE_API_PORT)