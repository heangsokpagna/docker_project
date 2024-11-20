from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

# Connect to MySQL
def get_db_connection():
    return mysql.connector.connect(
        host="mysql",
        user="root",
        password="root",
        database="testdb"
    )

@app.route('/health')
def health():
    return jsonify({"status": "healthy"}), 200

@app.route('/data')
def data():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM test_table")
        rows = cursor.fetchall()
        return jsonify(rows)
    except Exception as e:
        return str(e), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4743)