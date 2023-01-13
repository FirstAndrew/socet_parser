from sqlalchemy import Column, Table, Integer, String, MetaData , any_, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import mapper

engine = create_engine('sqlite:///DB/orm.sqlite', echo=True) # connect to server

Base = declarative_base()

class Good_details_db(Base):
    __tablename__ = 'goods_details'
    id = Column(Integer, primary_key = True)
    name = Column(String)
    price = Column(String)
    photo = Column(String)
    link = Column(String)
    description = Column(String)
    wether = Column(String)
    size = Column(String)
    color = Column(String)

    def __init__(self, id,name,price,photo,link,description,wether,size,color) :
        self.id = id
        self.name = name
        self.price = price
        self.photo = photo
        self.link = link
        self.description = description
        self.wether = wether
        self.size = size
        self.color = color
        

class Good_db(Base):
    __tablename__ = 'goods'
    id = Column(Integer, primary_key = True)
    name = Column(String)
    price = Column(String)
    photo = Column(String)
    link = Column(String)

    def __init__(self,Id,Name,Price,Photo,Link):
        self.id = Id
        self.name = Name
        self.price = Price
        self.photo = Photo
        self.link = Link


if __name__ == "__main__":
    metaData = MetaData()

    # gods_table = Table('goods', metaData,
    #     Column('id', Integer, primary_key=True),
    #     Column('name', String),
    #     Column('price', String),
    #     Column('photo', String),
    #     Column('link', String)
    # )
    metaData.create_all(engine)



