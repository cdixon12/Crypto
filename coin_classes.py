#!/usr/bin/env python3

# Chase Dixon Project 5/3/23
import os
from db_manager import Base
from sqlalchemy import Column, Integer, String, Boolean
import requests

class Coin(Base):
    __tablename__ = 'coins'
    
    coin_id = Column(Integer, primary_key=True)
    rank = Column(Integer)
    symbol = Column(String)
    name = Column(String)
    supply = Column(Integer)
    max_supply = Column(Integer)
    market_cap = Column(Integer)
    vol = Column(Integer)
    price = Column(Integer)
    percent_change = Column(Integer)
    vwap = Column(Integer)
    site = Column(String)

    def __init__(self, rank, symbol, name, supply,
                    max_supply, market_cap, vol, price, 
                    percent_change, vwap, site):
        self.rank = rank
        self.symbol = symbol
        self.name = name
        self.supply = supply
        self.max_supply = max_supply
        self.market_cap = market_cap
        self.vol = vol
        self.price = price
        self.percent_change = percent_change
        self.vwap = vwap 
        self.site = site



class Exchange(Base):
    __tablename__ = 'exchanges'
    ex_id = Column(Integer, primary_key=True)
    name = Column(String)
    rank = Column(Integer)
    percent_vol = Column(Integer)
    vol = Column(Integer)
    pairs = Column(Integer)
    site = Column(String)

    def __init__(self, name, rank, 
                percent_vol, vol, pairs, site):
        self.name = name
        self.rank = rank
        self.percent_vol = percent_vol
        self.vol = vol
        self.pairs = pairs
        self.site = site


