import os
from flask import Flask, render_template, request, redirect, url_for, jsonify
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = os.getenv("DB_NAME", "test_database")
COLLECTION_NAME = os.getenv("COLLECTION_NAME", "submissions")

app = Flask(__name__)

client = None
collection = None

def init_db():
    global client, collection
    if client is None:
        if not MONGO_URI:
            raise ValueError("MONGO_URI not set.")
        client = MongoClient(MONGO_URI)
        db = client[DB_NAME]
        collection = db[COLLECTION_NAME]

# ---------- Part A: /api route returning JSON from MongoDB ----------
@app.route("/api", methods=["GET"])
def api_data():
    try:
        init_db()
        data = list(collection.find({}, {"_id": 0}))  # exclude _id for JSON
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ---------- Part B: Frontend form to insert data into MongoDB ----------
@app.route("/", methods=["GET"])
def form():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
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
    return render_template("success.html", message="Data submitted successfully")

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
