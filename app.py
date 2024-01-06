from flask import Flask, jsonify
from ntscraper import Nitter
import time

app = Flask(__name__)
scraper = Nitter()

@app.route('/get_tweets/<username>/<int:number>', methods=['GET'])
def get_tweets(username,number):
    start_time = time.time()
    tweets = scraper.get_tweets(username, mode='user', number=number)
    end_time = time.time()
    execution_time = end_time - start_time

    response = {
        'tweets': tweets,
        'numberOfTweets': number,
        'execution_time': execution_time
    }

    return jsonify(response)

@app.route('/',methods=['GET'])
def routeChecking():
     response={
            'status':'OK',
            'server status':'Running',
     }
     return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
