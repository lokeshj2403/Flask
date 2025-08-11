import os
import uuid
from flask import Flask, render_template, request, redirect, url_for, jsonify
from pymongo import MongoClient
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = os.getenv("DB_NAME", "test_database")
COLLECTION_NAME = os.getenv("COLLECTION_NAME", "submissions")
TODO_COLLECTION_NAME = os.getenv("TODO_COLLECTION_NAME", "todo_items")

app = Flask(__name__)

client = None
collection = None
todo_collection = None

def init_db():
    """Initialize MongoDB connection and collections."""
    global client, collection, todo_collection
    if client is None:
        if not MONGO_URI:
            raise ValueError("MONGO_URI not set in environment variables.")
        client = MongoClient(MONGO_URI)
        db = client[DB_NAME]
        collection = db[COLLECTION_NAME]
        todo_collection = db[TODO_COLLECTION_NAME]

# ---------- Part A: /api route returning JSON from MongoDB ----------
@app.route("/api", methods=["GET"])
def api_data():
    """Return all submission data as JSON."""
    try:
        init_db()
        data = list(collection.find({}, {"_id": 0}))  # exclude _id from response
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ---------- Part B: Frontend form to insert data into MongoDB ----------
@app.route("/", methods=["GET"])
def form():
    """Render the HTML form for name and email."""
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    """Handle form submission for name and email."""
    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip()

    if not name or not email:
        return render_template("index.html", error="Name and email are required.")

    try:
        init_db()
        doc = {"name": name, "email": email}
        collection.insert_one(doc)
        return redirect(url_for("success"))
    except Exception as e:
        return render_template("index.html", error=f"Failed to submit: {str(e)}")

@app.route("/success", methods=["GET"])
def success():
    """Render the success page after form submission."""
    return render_template("success.html", message="Data submitted successfully")

# ---------- Part C: /submittodoitem backend API ----------
@app.route("/submittodoitem", methods=["POST"])
def submit_todo_item():
    """
    Accept itemName and itemDescription via POST
    and store them in the MongoDB todo_items collection.
    """
    try:
        init_db()
        item_name = request.form.get("itemName", "").strip()
        item_desc = request.form.get("itemDescription", "").strip()

        if not item_name or not item_desc:
            return jsonify({"error": "Item Name and Description are required"}), 400

        todo_item = {
            "id": str(uuid.uuid4()),  # unique ID
            "itemName": item_name,
            "itemDescription": item_desc
        }
        todo_collection.insert_one(todo_item)

        return jsonify({
            "message": "To-Do item added successfully",
            "item": todo_item
        }), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
