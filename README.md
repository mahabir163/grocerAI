# 🛒 GrocerAI

GrocerAI is an AI-powered grocery shopping web application built with Django.

The system allows customers to upload grocery bills, automatically extract product information using OCR and AI, check product availability and stock, and place orders. It also provides an admin control panel for managing customer orders, inventory, and order status.

---

## 🚀 Features

### 👤 Customer Features

- User registration and login
- Grocery product browsing
- Product search and categories
- Upload grocery bills
- OCR-based bill text extraction
- AI-based product extraction
- Automatic product and quantity detection
- Product availability checking
- Stock quantity validation
- Order confirmation
- Address and delivery information
- Cash on Delivery
- Order tracking
- Customer feedback

### 🤖 AI Features

- Extract grocery products from uploaded bills
- Identify product names
- Identify quantities
- Match extracted products with products available in the database
- Automatically determine product availability

### 📦 Inventory Management

- View current product stock
- Automatically reduce stock after successful order placement
- Display available and unavailable products
- Admin inventory monitoring

### 👨‍💼 Admin / Control Panel

- View customer orders
- View customer information
- View ordered products
- View order total
- View current product stock
- Update order status
- Manage products and inventory

Order statuses include:

- Pending
- Accepted
- Packed
- Shipped
- Delivered
- Cancelled

---

## 🏗️ Project Architecture

```text
GrocerAI/
│
├── apps/
│   ├── accounts/
│   ├── cart/
│   ├── chatbot/
│   ├── notification/
│   ├── orders/
│   ├── payment/
│   ├── products/
│   └── recommendation/
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── views.py
│   └── wsgi.py
│
├── static/
├── templates/
├── media/
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md

### 🔄 How GrocerAI Works
Customer
   │
   ▼
Upload Grocery Bill
   │
   ▼
OCR Processing
   │
   ▼
Extract Bill Text
   │
   ▼
AI Product Extraction
   │
   ▼
Product + Quantity
   │
   ▼
Check Product Database
   │
   ├── Available
   │      │
   │      ▼
   │   Confirm Order
   │      │
   │      ▼
   │   Payment / COD
   │      │
   │      ▼
   │   Place Order
   │
   └── Not Available
          │
          ▼
      Show Status

###🛠️ Technologies Used
- Backend
Python
Django
SQLite
- Frontend
HTML
Tailwind CSS
JavaScript
- AI / Machine Learning
OpenAI API
OCR
AI-based product extraction
Deep Learning
- Database
SQLite
Django ORM
- Development Tools
Git
GitHub
Visual Studio Code
Python Virtual Environment
Colab
