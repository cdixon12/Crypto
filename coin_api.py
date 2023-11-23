#!/usr/bin/env python3
# CoinCap API
# Chase Dixon Project 5/3/23

from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from db_manager import db_session
from flask_bootstrap import Bootstrap
#from flaskext.markdown import Markdown
from coin_classes import Coin, Exchange

app = Flask(__name__)
Bootstrap(app)
#Markdown(app)

def filter_list(l, animal, n):  # filter function for trends winners and losers
    reverse = False
    if animal == 'bull':
        reverse = True
    sort_l = sorted(l, key=lambda x: x.percent_change, reverse=reverse )

    return sort_l[:n]

# get data for coins and exchanges from database
coins = Coin.query.all()
exchanges_old = Exchange.query.all()
exchanges = sorted(exchanges_old, key=lambda x: x.rank)

@app.route('/')
def landing_page(): # Home page

    return render_template('landing.html') 

@app.route('/coins', methods=['GET','POST'])
def coins_page():   # Displays all coins in table

    # reverse coins if rank button pushed
    reverse_coins = False
    if request.method == "POST":
        reverse_coins = True

    # compute total marketcap in Trillions
    total_mc = 0
    for c in coins:
        total_mc += int(c.market_cap) 
    total_mc = total_mc / 1000000000000

    if reverse_coins:
        coins.reverse()

    return render_template('coins.html', coins=coins, total_mc=total_mc) 

@app.route('/exchanges', methods=['GET','POST'])
def exchanges_page():   # Displays all the exchanges in table
    
    # reverse exchanges if rank button pushed
    reverse_exchanges = False
    if request.method == "POST":
        reverse_exchanges = True

    # compute total volume in Billions
    total_vol = 0
    for ex in exchanges:
        if ex.vol == None:
            pass
        else:
            total_vol += int(ex.vol) 
    total_vol = total_vol / 1000000000

    if reverse_exchanges:
        exchanges.reverse()
     
    return render_template('exchanges.html', exchanges=exchanges, total_vol=total_vol) 

@app.route('/trends', methods=['GET', 'POST'])
def trends_page():  # Displays top n winners and losers in tables

    n = 10  # default value
    if request.method == "POST":
        try:
            n = int(request.form['n'])
        except:
            pass

    winners = filter_list(coins, 'bull', n)
    losers = filter_list(coins, 'bear', n)

    return render_template('trends.html', winners=winners, losers=losers, n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9065)
