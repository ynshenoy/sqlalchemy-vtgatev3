from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import MetaData, Table, Column, BigInteger, String
from sqlalchemy.orm import sessionmaker
import sqlalchemy_vtgatev3 as vt3 # will register vtgatev3 dialect

#engine = create_engine("mysql://vituser:vituser@127.0.0.1/vittest2")
print("Creating engine..")
engine = create_engine("vtgatev3://localhost:15001/vt_test_keyspace")
print("Created engine.. type {}".format(type(engine)))

Base = declarative_base()
class Message(Base):
    __tablename__ = 'test_table'

    id = Column(BigInteger, primary_key=True)
    msg = Column(String(250))

Session = sessionmaker(bind=engine, autocommit=True)
#Session = sessionmaker(bind=engine)
session = Session()


msg1 = Message(msg="Hello! This is a test message for vtgate via session.")
#import pudb; pu.db
session.begin()
session.add(msg1)
session.commit()

result = session.query(Message)
for row in result:
    print (row.id, row.msg)
