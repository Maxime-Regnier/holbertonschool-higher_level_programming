#!/usr/bin/env python3
"""Flask application with a dynamic /items route using Jinja loops and conditions."""
import json
from flask import Flask, render_template
app = Flask(__name__)
@app.route("/items")
def items():
        """Read items from items.json and render them with items.html."""
with open("items.json", "r") as f:
    data = json.load(f)
    item_list = data.get("items", [])
    return render_template("items.html", items=items_list)
if __name__ == "__main__":
    app.run(debug=True)