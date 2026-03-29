from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import Depends
from sqlalchemy.orm import Session
from fastapi import HTTPException
from database import engine, SessionLocal, Base
from models import Base, Vendor, Product, PurchaseOrder
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()   

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

# Create Vendor
class VendorCreate(BaseModel):
    name: str
    contact: str
    rating: float

@app.post("/vendors")
def create_vendor(v: VendorCreate, db: Session = Depends(get_db)):
    vendor = Vendor(
        name=v.name,
        contact=v.contact,
        rating=v.rating
    )
    db.add(vendor)
    db.commit()
    return {"message": "Vendor created"}

# Get Vendors
@app.get("/vendors")
def get_vendors(db: Session = Depends(get_db)):
    return db.query(Vendor).all()

# Create Product
@app.post("/products")
def create_product(name: str, sku: str, price: float, stock: int):
    db = SessionLocal()
    product = Product(name=name, sku=sku, price=price, stock=stock)
    db.add(product)
    db.commit()
    return {"message": "Product created"}

# Get Products
@app.get("/products")
def get_products():
    db = SessionLocal()
    return db.query(Product).all()

# Create Purchase Order (with 5% tax)
from pydantic import BaseModel

class POCreate(BaseModel):
    reference: str
    vendor_id: int
    amount: float

@app.post("/purchase-order")
def create_po(po: POCreate, db: Session = Depends(get_db)):

    vendor = db.query(Vendor).filter(Vendor.id == po.vendor_id).first()
    if not vendor:
        raise HTTPException(status_code=400, detail="Vendor not found")

    total = po.amount + (po.amount * 0.05)

    new_po = PurchaseOrder(
        reference=po.reference,
        vendor_id=po.vendor_id,
        total_amount=total,
        status="Created"
    )

    db.add(new_po)
    db.commit()

    return {"total_with_tax": total}