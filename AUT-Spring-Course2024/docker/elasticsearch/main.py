import time
from flask import Flask, request, jsonify

app = Flask(__name__)




if __name__ == '__main__':
    time.sleep(50)

    #initializing the cache system and elastic database, then we will run flask app on 0.0.0.0:5000(no need to debug mode)

    time.sleep(50)
    app.run(debug=False, host='0.0.0.0', port=5000)