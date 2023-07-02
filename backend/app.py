from flask import Flask, g, jsonify
from database import query_db, initialize_database_ddl, initialize_database_dml
import config
import os

app = Flask(__name__)

# Routes
@app.route('/')
def hello_world():
    return 'test'

@app.route(config.BASE_API_PATH + '/test')
def test():
    print('here')
    result = query_db("select * from test")
    return jsonify(result)


# Base Configuration
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

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