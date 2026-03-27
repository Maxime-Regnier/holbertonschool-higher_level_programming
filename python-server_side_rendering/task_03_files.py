#!/usr/bin/env python3
"""Flask application to display product data from JSON or CSV files."""
import json
import csv
from flask import Flask, render_template, request
app = Flask(__name__)
def read__json():
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
@app.route("/products")
def products():
        """Render products from JSON or CSV based on query parameters."""
        source = request.args.get("source")
        product_id = request.args.get("id")
        if source == "json":
            data = read_json()
        elif source == "csv":
            data = read_csv()
        else:
            return render_template(
            "product_display.html",
            error="Wrong source",
            products=None
    )
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
    app.run(debug=True)
