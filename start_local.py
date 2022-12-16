from server.app import app

app.run(debug=True, threaded=True, port=3030, host='127.0.0.1')
