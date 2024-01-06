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

if __name__ == '__main__':
    app.run(debug=True)
# ------------------------
# from ntscraper import Nitter
# import time
# scraper=Nitter()
# start_time = time.time()
# tweets = scraper.get_tweets('userName', mode='user', number=5)
# print(tweets)

# end_time = time.time()

# execution_time = end_time - start_time
# print(f"Execution time: {execution_time} seconds")
