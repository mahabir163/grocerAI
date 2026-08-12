# 🛒 GrocerAI

**GrocerAI** is an AI-powered grocery shopping web application built with **Django**.

The application allows customers to upload grocery bills, automatically extract product information using **OCR and AI**, check product availability and stock, and place orders through a simple shopping workflow.

It also provides an **admin control panel** for managing customer orders, inventory, and order status.

---

## 🚀 Features

### 👤 Customer Features

- User registration and login
- Browse grocery products
- Product search and categories
- Upload grocery bills
- OCR-based bill text extraction
- AI-based product extraction
- Automatic product name and quantity detection
- Product availability checking
- Stock quantity validation
- Order confirmation
- Address and delivery information
- Cash on Delivery
- Order tracking
- Customer feedback

---

## 🤖 AI Features

GrocerAI uses AI to simplify grocery ordering from uploaded bills.

### AI Workflow

1. Customer uploads a grocery bill.
2. OCR extracts text from the bill.
3. AI processes the extracted text.
4. Product names and quantities are identified.
5. Extracted products are matched with products in the database.
6. Product availability is checked.
7. Available products are added to the order.

---

## 📦 Inventory Management

The system provides basic inventory management functionality.

- View current product stock
- Check product availability
- Validate requested quantity against available stock
- Automatically reduce stock after successful order placement
- Display unavailable products
- Admin inventory monitoring

---

## 👨‍💼 Admin Control Panel

The admin/control panel allows administrators to manage customer orders and inventory.

### Admin Features

- View customer orders
- View customer information
- View delivery address
- View ordered products
- View product quantities
- View order total
- View current product stock
- Update order status
- Manage products and inventory

### 📋 Order Status

Orders can have the following statuses:

- 🟡 Pending
- 🔵 Accepted
- 🟣 Packed
- 🟦 Shipped
- 🟢 Delivered
- 🔴 Cancelled

---

## 🔄 How GrocerAI Works

```text
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
                  ┌────┴────┐
                  │         │
             Available   Not Available
                  │         │
                  ▼         ▼
          Confirm Order   Show Status
                  │
                  ▼
            Cash on Delivery
                  │
                  ▼
              Place Order
                  │
                  ▼
            Reduce Stock
                  │
                  ▼
             Order Tracking (Show in Admin Dashboard)
