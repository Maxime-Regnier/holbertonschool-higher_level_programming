#!/usr/bin/env python3
"""Flask application to display product data from JSON, CSV, or SQLite."""
 
import json
import csv
import sqlite3
from flask import Flask, render_template, request
 
app = Flask(__name__)
 
 
def create_database():
    """Create and populate the SQLite products.db database."""
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL
        )
    ''')
    # Only insert if table is empty to avoid duplicate entries
    cursor.execute('SELECT COUNT(*) FROM Products')
    if cursor.fetchone()[0] == 0:
        cursor.execute('''
            INSERT INTO Products (id, name, category, price)
            VALUES
            (1, 'Laptop', 'Electronics', 799.99),
            (2, 'Coffee Mug', 'Home Goods', 15.99)
        ''')
    conn.commit()
    conn.close()
 
 
def read_json():
    """Read and return product list from products.json."""
    with open("products.json", "r") as f:
        return json.load(f)
 
 
def read_csv():
    """Read and return product list from products.csv."""
    products = []
    with open("products.csv", "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            products.append({
                "id": int(row["id"]),
                "name": row["name"],
                "category": row["category"],
                "price": float(row["price"])
            })
    return products
 
 
def read_sql():
    """Read and return product list from the SQLite database."""
    conn = sqlite3.connect('products.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute('SELECT id, name, category, price FROM Products')
    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]
 
 
@app.route("/products")
def products():
    """Render products from JSON, CSV, or SQLite based on query parameters."""
    source = request.args.get("source")
    product_id = request.args.get("id")
 
    # Validate source parameter
    if source == "json":
        data = read_json()
    elif source == "csv":
        data = read_csv()
    elif source == "sql":
        data = read_sql()
    else:
        return render_template(
            "product_display.html",
            error="Wrong source",
            products=None
        )
 
    # Filter by id if provided
    if product_id is not None:
        filtered = [p for p in data if p["id"] == int(product_id)]
        if not filtered:
            return render_template(
                "product_display.html",
                error="Product not found",
                products=None
            )
        data = filtered
 
    return render_template("product_display.html", products=data, error=None)
 
 
if __name__ == "__main__":
    create_database()
    app.run(debug=True)
 