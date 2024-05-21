import sqlite3

def create_db():
    conn = sqlite3.connect('zdf_articles.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS articles (
            id INTEGER PRIMARY KEY,
            link TEXT,
            news_category TEXT,
            author TEXT,
            publish_time TEXT,
            title TEXT,
            scribe TEXT,
            text TEXT
        )
    ''')
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_db()
