from sqlalchemy import Column, Integer, String, Float, ForeignKey
from database import Base
from pydantic import BaseModel

class POCreate(BaseModel):
    reference: str
    vendor_id: int
    amount: float

class Vendor(Base):
    __tablename__ = "vendors"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    contact = Column(String)
    rating = Column(Float)

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    sku = Column(String)
    price = Column(Float)
    stock = Column(Integer)

class PurchaseOrder(Base):
    __tablename__ = "purchase_orders"
    id = Column(Integer, primary_key=True)
    reference = Column(String)
    vendor_id = Column(Integer, ForeignKey("vendors.id"))
    total_amount = Column(Float)
    status = Column(String)