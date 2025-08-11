
# Flask + MongoDB Atlas + JSON API

This project is a simple Flask application that demonstrates:

1. **JSON API Endpoint** — `/api` reads data from a backend file (`data.json`) and returns it as JSON.
2. **Frontend Form Submission** — A web form inserts user data into **MongoDB Atlas**.
3. **Success & Error Handling** — On success, redirect to a success page. On error, show message without redirect.

---

## 📂 Project Structure

```

flask-mongo-app/
├── app.py               # Main Flask application
├── data.json            # JSON data for /api route
├── requirements.txt     # Python dependencies
├── .env.example         # Example environment variables (copy to .env)
├── templates/
│   ├── form.html        # Form page
│   └── success.html     # Success page
└── .gitignore

````

---

## ⚙️ Setup Instructions

### 1️ Clone the repo
```bash
git clone https://github.com/lokeshj2403/DevOps.git
cd Assignment-3
````

### 2️ Create virtual environment & install dependencies

```bash
python3 -m venv venv
source venv/bin/activate  # On macOS/Linux
# OR .\venv\Scripts\activate  # On Windows PowerShell

pip install -r requirements.txt
```

* Fill in your MongoDB Atlas URI and database details:

```
MONGO_URI="mongodb+srv://<username>:<password>@cluster0.mongodb.net/?retryWrites=true&w=majority"
DB_NAME="my_database"
COLLECTION_NAME="submissions"
```


---

### 3 Run the Application

```bash
python app.py
```

Visit:

* Form page → [http://127.0.0.1:5000/](http://127.0.0.1:5000/)
* JSON API → [http://127.0.0.1:5000/api](http://127.0.0.1:5000/api)

---

## 📝 Features

* **/api route** — Reads and returns JSON from `data.json`
* **Form submission** — Saves `{ name, email }` into MongoDB Atlas
* **Error handling** — Displays error message on form page without redirect
* **Success redirect** — Goes to `/success` page showing `"Data submitted successfully"`

---

Suggested:

1. `/api` endpoint in browser
2. Form page before submission
3. Success page after submission
4. MongoDB Atlas collection showing inserted data
5. Error case (invalid DB URI)

---

## 🛠️ Technologies Used

* [Flask](https://flask.palletsprojects.com/) — Python web framework
* [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) — Cloud NoSQL database
* [PyMongo](https://pymongo.readthedocs.io/) — Python driver for MongoDB
* [dotenv](https://pypi.org/project/python-dotenv/) — Load environment variables from `.env`

---
