from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
# Enable CORS so your React frontend running on port 3000 can call the API
CORS(app)

# In-memory database of products
PRODUCTS = [
    {"id": 1, "name": "Classic Sneakers", "price": 85.00},
    {"id": 2, "name": "Cotton T-Shirt", "price": 25.50},
    {"id": 3, "name": "Denim Jacket", "price": 110.00},
    {"id": 4, "name": "Leather Backpack", "price": 145.00}
]

@app.route('/api/products', methods=['GET'])
def get_products():
    return jsonify(PRODUCTS)

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)