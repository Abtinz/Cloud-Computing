import time
from flask import Flask, abort, request, jsonify

app = Flask(__name__)


@app.route('/movies/search', methods=['GET'])
def search_query():

    try:

        query = request.args.get('query')

        if query is None:
            return abort(400,{'message': 'bad request caused by incorrect and incomplete request queries'})
        
    except Exception as error:
        return abort(400,{'message': 'bad request caused by incorrect and incomplete request queries'})


if __name__ == '__main__':
    

    #initializing the cache system and elastic database, then we will run flask app on 0.0.0.0:5000(no need to debug mode)

    
    app.run(debug=False, host='0.0.0.0', port=5000)