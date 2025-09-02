import sqlite3
from datetime import datetime

DB_NAME = "queries.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS queries
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  query TEXT,
                  answer TEXT,
                  justification TEXT,
                  pdf_name TEXT,
                  timestamp TEXT)''')
    conn.commit()
    conn.close()

def save_query(query, answer, justification, pdf_name):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("INSERT INTO queries (query, answer, justification, pdf_name, timestamp) VALUES (?, ?, ?, ?, ?)",
              (query, answer, justification, pdf_name, datetime.now().isoformat()))
    conn.commit()
    conn.close()

def get_history():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT query, answer, justification, pdf_name, timestamp FROM queries ORDER BY id DESC LIMIT 5")
    rows = c.fetchall()
    conn.close()
    return rows
