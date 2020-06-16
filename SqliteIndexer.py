import sqlite3
import shutil
import os


def create_new_database():
    shutil.copy('blog.db', 'blog.db.back')
    os.remove('blog.db')
    create_db()


def create_db():
    conn = sqlite3.connect('blog.db')
    c = conn.cursor()
    c.execute('''
    CREATE TABLE IF NOT EXISTS BLOG(
        ID INTEGER PRIMARY KEY  AUTOINCREMENT   NOT NULL,
        TITLE          TEXT    NOT NULL,
        SUBTITLE       TEXT            ,
        DATE           TEXT    NOT NULL,
        CATEGORIES     TEXT            ,
        COVER          TEXT            ,
        TAGS           TEXT            ,
        CONTENT        TEXT
    );
    ''')
    conn.commit()
    conn.close()


def insert_data(metadata, content):
    conn = sqlite3.connect('blog.db')
    c = conn.cursor()
    c.execute("INSERT INTO BLOG (TITLE,SUBTITLE,DATE,CATEGORIES,COVER,TAGS,CONTENT) \
          VALUES (?,?,?,?,?,?,?)", (metadata['title'][0],
                                    metadata['subtitle'][0],
                                    metadata['date'][0],
                                    metadata['categories'][0],
                                    metadata['cover'][0],
                                    metadata['tags'][0],
                                    content))
    conn.commit()
    conn.close()
