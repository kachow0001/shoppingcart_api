import datetime
from decimal import Decimal
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Account(db.Model):
    __tablename__ = 'accounts'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    
    account_id = db.Column(db.Integer, db.ForeignKey('accounts.id', ondelete='CASCADE'), nullable=False)
    #one to many realtionship 
    users = db.relationship("User",backref = "account",lazy=True, cascade="all,delete")
    admins = db.relationship("Admin",backref = "account",lazy=True, cascade= "all,delete")


        
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    user_name = db.Column(db.String(128),nullable=False)
    date_of_birth = db.Column(db.DateTime)    
    email = db.Column(db.String(128),unique=True,nullable=False)
    password = db.Column(db.String(128), nullable=False)
    address = db.Column(db.String(128))
    
    # Foreign key to Account
    account_id = db.Column(db.Integer, db.ForeignKey('accounts.id'), nullable=False)
    
    
    def __init__(self,user_name:str,password:str,email:str,address:str):
        self.user_name = user_name
        self.password = password
        self.email = email
        self.address = address
    
    def serialize(self):
        return{
            'id':self.id,
            'user_name': self.user_name ,
            'date_of_birth': self.date_of_birth ,
            'email' : self.email,
            'address': self.address
        }


class Admin(db.Model):
    __tablename__ = 'admins'    
    id =db.Column(db.Integer,primary_key=True,autoincrement=True)
    user_name = db.Column(db.String(128),nullable=False)
    password = db.Column(db.String(128), nullable=False)
    
    
    # Foreign key to Account
    account_id = db.Column(db.Integer, db.ForeignKey('accounts.id', ondelete='CASCADE'), nullable=False)

    def __init__(self, user_name: str, password: str):
        self.user_name = user_name
        self.password = password

    def serialize(self):
        return {
            'id': self.id,
            'user_name': self.user_name
        }
          
class Order(db.Model):
    __tablename__ = 'orders'
    
    id =db.Column(db.Integer,primary_key=True,autoincrement=True)
    quantity = db.Column(db.Integer,nullable=False)
    discount = db.Column(db.Numeric(10, 2))
    status  = db.Column(db.String(128),nullable=False)
    price   = db.Column(db.Float(),nullable=False)
    created_at = db.Column(
        db.DateTime,
        default=datetime.datetime.utcnow,
        nullable=False)
    
    #foregin key to user
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'),nullable=False)
    

    def __init__(self, quantity:int, discount:float, status:str, price:float):
        self.quantity = quantity
        self.discount = discount
        self.status = status
        self.price = price

    def serialize(self):
        return {
            'id': self.id,
            'quantity': self.quantity,
            'discount': float(self.discount),
            'status': self.status,
            'price': self.price,
            'created_at': self.created_at,
            'user_id': self.user_id
        }
 
       
# Many-to-many (order-categor
order_category = db.Table('order_category',
    db.Column('order_id', db.Integer, db.ForeignKey('orders.id'), primary_key=True),
    db.Column('category_id', db.Integer, db.ForeignKey('categories.id'), primary_key=True)
)

class Category(db.Model):
    __tablename__ = 'categories'
    
    id =db.Column(db.Integer,primary_key=True,autoincrement=True)
    product_name = db.Column(db.String(128),nullable=False)
    description  = db.Column(db.String(128))
    price   = db.Column(db.Float(),nullable=False)
    #picture = db.Column(db.LargeBinary)
    
   # Many-to-many relationship with Order
    orders = db.relationship('Order', secondary=order_category, backref=db.backref('categories', lazy=True))

    # Foreign key to User
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
                              
