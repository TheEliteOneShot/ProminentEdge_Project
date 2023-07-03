from flask import Flask, g, jsonify, request
from database import initialize_database_ddl, initialize_database_dml
import services
import config
import os
import json

app = Flask(__name__)

# Routes
@app.route('/')
def hello_world():
    return 'hello_world from the API!'

@app.route(config.BASE_API_PATH + '/test')
def test():
    #result = query_db("select * from test")
    return jsonify(True)

@app.route(config.BASE_API_PATH + '/upload_cad_files', methods = ['POST'])
def upload_cad_file():
    
    fileData = []

    for file in request.files.getlist('file'):
        result = json.loads(file.read())
        result['filename'] = file.filename
        fileData.append(result)
    
    result = services.upload_cad_file(fileData)

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