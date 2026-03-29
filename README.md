#  ERP Purchase Order (PO) System

##  About Project

This is a simple project to manage Purchase Orders.
It is made using **Python (FastAPI)** for backend and **HTML, CSS, JavaScript** for frontend.

 In this system you can:

* Add and manage vendors
* Add and manage products
* Create purchase orders (with automatic 5% tax)

---

##  Technologies Used

* Backend: FastAPI (Python)
* Database: PostgreSQL
* Frontend: HTML, CSS, JavaScript
* ORM: SQLAlchemy

---

##  How to Run Backend

1. Clone project

```
git clone <your-repo-link>
cd erp-po-system/backend
```

2. Create virtual environment

```
python -m venv .venv
.venv\Scripts\activate
```

3. Install packages

```
pip install fastapi uvicorn sqlalchemy psycopg2
```

4. Create database

```
CREATE DATABASE erp_db;
```

5. Update database URL in `database.py`

6. Run server

```
uvicorn main:app --reload
```

7. Open API

```
http://127.0.0.1:8000/docs
```

---

##  How to Run Frontend

* Go to frontend folder

```
cd ../frontend
```

* Open `index.html` in browser
  (or use Live Server)

---

##  Database Tables

* Vendors → store vendor details
* Products → store product details
* Purchase Orders → store orders with vendor link

---

##  API Endpoints

* POST /vendors → add vendor

* GET /vendors → get vendors

* POST /products → add product

* GET /products → get products

* POST /purchase-order → create order

---

##  Logic

   Total Amount = Amount + 5% Tax

* Vendor must exist
* Total is calculated automatically

---

##  Errors

* 400 → Vendor not found
* 422 → Wrong input
* 500 → Server error

---

##  Features

* Simple REST API
* Connected database
* Clean code
* Auto tax calculation

---

##  Future Improvements

* Login system (JWT)
* Add multiple products in one order
* Better UI dashboard
* AI product description

---

##  Author

Govind Maurya

---

##  Note

This project is made for learning and assignment purpose to show backend + frontend connection.
