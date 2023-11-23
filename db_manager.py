#!/usr/bin/env python3

# Chase Dixon Final Project 5/3/23

import requests
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker, declarative_base
#from coin_classes import Coin

#create an engine for your DB using sqlite and storing it in a file named coins.sqlite
engine = create_engine("sqlite:///coins.sqlite")


db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

def init_db(): # 15 LOC
    '''Create the database and fill it with the Coins and Exchanges

    Args:
        None

    Returns:
        None
    '''

    # import your classes that represent tables in the DB and then create_all of the tables
    from coin_classes import Coin, Exchange
    Base.metadata.create_all(bind=engine)

    # Create list of Coin objects 
    response = requests.request("GET", "https://api.coincap.io/v2/assets/")
    coins = response.json()['data']
    coin_list = []   
    for coin in coins: 
        c = list(coin.values())
        coin_list.append(Coin(c[1], c[2], c[3], c[4], c[5], c[6], c[7], c[8], c[9], c[10], c[11]))

    # Create list of Exchange objects
    response = requests.request("GET", "https://api.coincap.io/v2/exchanges/")
    exchanges = response.json()['data']
    exchange_list = []   
    for exchange in exchanges: 
        ex = list(exchange.values())
        exchange_list.append(Exchange(ex[1], ex[2], ex[3], ex[4], ex[5], ex[7]))
 
    for obj in coin_list:       # add each Coin object to the db
        db_session.add(obj)

    for obj in exchange_list:   # add each Exchange object to the db
        db_session.add(obj)

    # save the database
    db_session.commit()



