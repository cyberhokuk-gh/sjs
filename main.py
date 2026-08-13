import sqlite3

conn = sqlite3.connect("news.db")
cur = conn.cursor()

cur.execute("SELECT COUNT(*) FROM articles")
print("저장된 기사 수:", cur.fetchone()[0])

cur.execute("SELECT title FROM articles LIMIT 5")
for row in cur.fetchall():
    print("-", row[0])

conn.close()


