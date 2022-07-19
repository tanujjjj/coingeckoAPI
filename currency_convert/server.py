from cmath import log
from urllib import response
import requests
from pycoingecko import CoinGeckoAPI
from flask import Flask, request, jsonify
import logging
import sys
import json


app = Flask(__name__)
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG,
                    format=f'%(asctime)s  %(message)s')
logger = logging.getLogger(__name__)


@app.route("/exchange", methods=["GET"])
def exchange_into_dollars():

    coin = request.args.get("coin", "")
    amount = request.args.get("amount")

    if(coin is None or amount is None):
        return({"error": "Missing Parameters"})

    logger.info("coin input value is: %s (type: %s)" % (coin, type(coin)))
    logger.info("amount input value is: %s (type: %s)" %
                (amount, type(amount)))

    amount = float(amount)
    coin = coin.lower()
    if(coin == 'btc'):
        coin = "bitcoin"
    elif(coin == 'eth'):
        coin = "ethereum"
    elif(coin == 'xrp'):
        coin = "ripple"
    else:
        return ({"error": "Invalid coin."})
    if(amount <= 0):
        return ({"error": "Invalid Amount."})
    elif(amount >= 10000):
        return ({"error": "Invalid Amount."})

    resp = requests.get(
        "https://api.coingecko.com/api/v3/simple/price?ids="+coin+"&vs_currencies=usd")
    resp = resp.text
    data = json.loads(resp)

    usd = float(data[coin]['usd'])

    # Calculate this!
    usd_amount = usd*amount

    return jsonify(usd_amount=usd_amount)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6001)
