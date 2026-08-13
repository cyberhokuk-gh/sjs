import streamlit as st
import sqlite3
import feedparser

st.title("내 뉴스 목록")

# 데이터베이스 연결 (없으면 생성)
conn = sqlite3.connect("news.db")
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS articles (title TEXT, link TEXT UNIQUE, published TEXT)")

# 데이터가 없으면 새로 가져오기 (클라우드에서도 자동으로 채워짐)
cur.execute("SELECT COUNT(*) FROM articles")
if cur.fetchone()[0] == 0:
    keyword = "인공지능"
    url = f"https://news.google.com/rss/search?q={keyword}&hl=ko&gl=KR&ceid=KR:ko"
    feed = feedparser.parse(url)
    for entry in feed.entries:
        cur.execute("INSERT OR IGNORE INTO articles (title, link, published) VALUES (?, ?, ?)",
                    (entry.title, entry.link, entry.get("published", "")))
    conn.commit()

# 화면에 목록 보여주기
cur.execute("SELECT title, link FROM articles LIMIT 20")
for title, link in cur.fetchall():
    st.write(f"- [{title}]({link})")
conn.close()
