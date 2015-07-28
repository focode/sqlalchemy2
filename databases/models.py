from sqlalchemy import Column, Integer, String, TIMESTAMP
from database import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    email = Column(String(120), unique=True)

    def __init__(self, name=None, email=None):
        self.name = name
        self.email = email

    def __repr__(self):
        return '<User %r>' % (self.name)


class Profile(Base):
    __tablename__ = 'profile'
    idprofile = Column(Integer,primary_key=True)
    milk_type = Column(String(450))
    quantity = Column(Integer)
    brand = Column(String(450))
    start_date = Column(TIMESTAMP)
    delivery_days = Column(String(450))
    name = Column(String(450))
    address = Column(String(450))
    pincode = Column(String(450))
    contact_no = Column(String(450))

    def __init__(self,milk_type=None,quantity=None,brand=None,start_date=None,delivery_days=None,name=None,address=None,pincode=None,contact_no=None):
        self.milk_type = milk_type
        self.quantity = quantity
        self.brand = brand
        self.start_date = start_date
        self.delivery_days = delivery_days
        self.name = name
        self.address = address
        self.pincode = pincode
        self.contact_no = contact_no
    def __repr__(self):
        return '<name %r>' % (self.name)


