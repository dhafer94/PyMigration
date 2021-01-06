from bson import SON
from sqlalchemy import create_engine
from pymongo import MongoClient
from mysql import connector

# mySQL connection
# engine = create_engine(
#     "mysql+mysqlconnector://root:3463910@localhost:3306", echo=True)
#
# conn = engine.connect()
#
# print("connected!\n connection : {}".format(conn))

# Mongo connection
client = MongoClient('mongodb://localhost:27017')
# All run correctly
# 1
# db = client.bookimed.orders
# 2
# db = client["bookimed"]["orders"]
# print(db.find_one())
# 3
db = client["bookimed"]

pipeline = [
]
req_data = db.orders.find_one({}, {"_id": 0, "feedbackId": 1, "flow": 1, "patient": {"name": 1}, "salaryAt": 1,
                          "saleManager": {"firstName": 1}})
print(req_data)