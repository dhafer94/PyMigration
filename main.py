from sqlalchemy import create_engine
from pymongo import MongoClient
from mysql import connector


client = MongoClient('mongodb://localhost:27017')
# db = client.bookimed.orders
db = client["bookimed"]["orders"]
#
# engine = create_engine(
#     "mysql+mysqlconnector://root:3463910@localhost:3306", echo=True)
#
# conn = engine.connect()
#
# print("connected!\n connection : {}".format(conn))

print(db.find_one())
