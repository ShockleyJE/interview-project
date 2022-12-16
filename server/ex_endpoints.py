from flask import request, Response, jsonify
from server.app import app
from server.ex_query import get_all_tables, get_coldata_for_table, get_keydata_for_table

# Blueprint examples: https://realpython.com/flask-blueprint/#what-a-flask-blueprint-looks-like

"""
GET endpoint for tables and schemas
Optional default sk query parameter
"""
#@app.route('/tables', methods = ['GET'], defaults={'sk': None})
@app.route('/tables', methods = ['GET'])
def api_get_tables():
    res = get_all_tables()
    return jsonify(res)

@app.route('/columns', methods = ['GET'])
def api_get_columns():
    args = request.args
    table = args.get('table')
    coldata = get_coldata_for_table(table)
    return jsonify(coldata)

@app.route('/foreignkeys', methods = ['GET'])
def api_get_foreignkeys():
    args = request.args
    table = args.get('table')
    coldata = get_keydata_for_table(table)
    return jsonify(coldata)

"""
PUT endpoint with a request body
"""
@app.route('/genre', methods = ['PUT'])
def api_addMusicArtist():
    data = request.json
    print(data)
    try:
        return Response("{ 'message' : 'success' }", status=201, mimetype='application/json')
    except Exception as e:
        return Response("{ 'message' : 'not all parameters available' }", status=400, mimetype='application/json')