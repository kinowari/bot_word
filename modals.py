
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///application.sqlite', echo=True)

Session = sessionmaker(bind=engine)
Session.configure(bind=engine)
Base = declarative_base()


Session.configure(bind=engine)
session = Session()

class User(Base):
    __tablename__='User'
    id = Column(Integer, primary_key=True)
    tg_id=Column(String(228), index=True)

    def __repr__(self):  # как выводить объекты этого класса.
        return '<User %r>' % (self.nickname)

class Quest(Base):
    __tablename__ = 'Quest'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    strTime = Column(String(12))
    operation = Column(String(12))
    string = Column(String(1000))

Base.metadata.create_all(engine)

