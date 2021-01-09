from bson import SON
from sqlalchemy import create_engine, Column, String, Integer, Date
from pymongo import MongoClient
from sqlalchemy.ext.declarative import declarative_base
import datetime
# Mongo connection
from sqlalchemy.orm import sessionmaker

client = MongoClient('mongodb://localhost:27017')
# All run correctly
# 1
# db = client.bookimed.orders
# 2
# db = client["bookimed"]["orders"]
# print(db.find_one())
# 3
db = client["bookimed"]

# mySQL connection
# conn = mdb.connect('hostname', 'username', 'p@s$w0rd', 'database')

engine = create_engine(
    "mysql://root:3463910@localhost:3306/bookimedsql", echo=True)

conn = engine.connect()
# engine.execute("CREATE DATABASE bookimedsql") #create db
# engine.execute("USE bookimedsql")
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

print("connected!\n connection : {}".format(conn))

req_data = db.orders.find_one({}, {"_id": 0, "feedbackId": 1, "flow": 1, "patient": {"name": 1}, "salaryAt": 1,
                                   "saleManager": {"firstName": 1}})

# Dot notation
# req_data = db.orders.find_one({}, {"_id": 0, "feedbackId": 1, "flow": 1, "patient.name": 1, "salaryAt": 1,
#                                    "saleManager.firstName": 1})

# Testing
print(req_data)
for r in req_data.values():
    print(r)


class Orders(Base):
    __tablename__ = 'orders'
    feedbackId = Column("id", Integer, primary_key=True)
    flow = Column(String(100))
    patient_name = Column(String(100))
    salaryAt = Column(Date)
    saleManager_fname = Column(String(100))

    def __repr__(self):
        return "<Orders(feedbackId='%s', flow='%s', patient_name='%s,salaryAt='%s,saleManager_fname='%s)>" % (
            self.feedbackId, self.flow, self.patient_name, self.salaryAt, self.saleManager_fname)


#
#
Base.metadata.create_all(engine)

#
# order = Orders(feedbackId=req_data.feedbackId, flow=req_data.flow, patient_name=req_data.patient_name,
#                salaryAt=req_data.salaryAt, saleManager_fname=req_data.saleManager_fname)
order = Orders(feedbackId=req_data["feedbackId"], flow=req_data["flow"], patient_name=req_data["patient"]["name"],
               salaryAt=req_data["salaryAt"], saleManager_fname=req_data["saleManager"]["firstName"])

orders = session.query(Orders)

# for order in orders:
#     print(order.feebackId)

# session.execute("USE 'bookimedsql'")
# session.execute("SELECT * FROM `orders`")
