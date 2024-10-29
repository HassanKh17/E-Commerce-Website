from app import db
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy import DateTime, ForeignKey, PickleType
from sqlalchemy.orm import relationship
from datetime import datetime
from flask_login import UserMixin


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
    cart = Column(PickleType, default={})
    orders = relationship('Order', back_populates='user')
    reviews = relationship('Review', back_populates='user')

    def get_id(self):
        return super().get_id()


class Product(db.Model):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    description = Column(String, nullable=False)
    image_filename = Column(String)
    category = db.Column(db.String, nullable=False)
    order_items = relationship(
        'OrderItem', back_populates='product', cascade='all, delete-orphan')
    stock = relationship('Stock', back_populates='product')
    reviews = relationship('Review', back_populates='product')


class Stock(db.Model):
    __tablename__ = 'stock'
    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey('products.id'))
    quantity = Column(Integer, nullable=False)
    product = relationship('Product', back_populates='stock')


class Order(db.Model):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', back_populates='orders')
    order_date = Column(DateTime, default=datetime.now())
    items = relationship('OrderItem', back_populates='order')

    # reviews = relationship('Review', back_populates='order')


class OrderItem(db.Model):
    __tablename__ = 'order_items'
    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey('orders.id'))
    product_id = Column(Integer, ForeignKey('products.id'))
    quantity = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)
    order = relationship('Order', back_populates='items')
    product = relationship('Product', back_populates='order_items')
    reviews = relationship('Review', back_populates='order_item')


class Review(db.Model):
    __tablename__ = 'reviews'
    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey('products.id'))
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', back_populates='reviews')
    rating = Column(Integer, nullable=False)
    product = relationship('Product', back_populates='reviews')
    order_item_id = Column(Integer, ForeignKey(
        'order_items.id', name='fk_review_order_item'), nullable=False)
    order_item = relationship('OrderItem', back_populates='reviews')
    content = Column(String, nullable=False)
