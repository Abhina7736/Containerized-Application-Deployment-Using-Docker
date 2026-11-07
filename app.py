
from flask import Flask, render_template, jsonify, request
import os
import psycopg

app = Flask(__name__)

def db():
    return psycopg.connect(
        host=os.getenv("DB_HOST"),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/health")
def health():
    return jsonify({"status": "healthy"})

@app.route("/db-check")
def db_check():
    try:
        with db() as conn:
            conn.execute("SELECT 1")
        return jsonify({"database": "connected"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/visitors", methods=["GET", "POST"])
def visitors():
    try:
        with db() as conn:
            if request.method == "POST":
                data = request.get_json() or {}
                name = data.get("name", "").strip()
                purpose = data.get("purpose", "").strip()
                if not name or not purpose:
                    return jsonify({"error": "Enter name and purpose"}), 400
                cur = conn.execute(
                    "INSERT INTO visitors (name,purpose) VALUES (%s,%s) RETURNING id",
                    (name, purpose))
                return jsonify({"message": "Visitor registered", "id": cur.fetchone()[0]})

            search = request.args.get("search", "")
            rows = conn.execute(
                """SELECT id,name,purpose,check_in,check_out FROM visitors
                WHERE name ILIKE %s ORDER BY id DESC""",
                (f"%{search}%",)).fetchall()
            return jsonify([dict(id=r[0], name=r[1], purpose=r[2],
                check_in=str(r[3]) if r[3] else None,
                check_out=str(r[4]) if r[4] else None) for r in rows])
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/visitors/<int:id>/check-in", methods=["POST"])
def check_in(id):
    return update_status(id, "check_in")

@app.route("/visitors/<int:id>/check-out", methods=["POST"])
def check_out(id):
    return update_status(id, "check_out")

def update_status(id, action):
    try:
        with db() as conn:
            condition = "check_in IS NULL" if action == "check_in" else "check_in IS NOT NULL AND check_out IS NULL"
            row = conn.execute(
                f"UPDATE visitors SET {action}=CURRENT_TIMESTAMP WHERE id=%s AND {condition} RETURNING id",
                (id,)).fetchone()
            if not row:
                return jsonify({"error": "Invalid visitor or action"}), 400
        return jsonify({"message": action.replace("_", "-") + " successful"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/stats")
def stats():
    try:
        with db() as conn:
            total = conn.execute("SELECT COUNT(*) FROM visitors").fetchone()[0]
            today = conn.execute(
                "SELECT COUNT(*) FROM visitors WHERE check_in::date=CURRENT_DATE"
            ).fetchone()[0]
        return jsonify({"total_visitors": total, "today_visitors": today})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
