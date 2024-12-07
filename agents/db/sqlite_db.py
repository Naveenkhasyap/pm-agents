import sqlite3
import os

class SQLiteDB:
  def __init__(self):
    cwd = os.getcwd()
    self.conn = sqlite3.connect(f"{cwd}/example.db")
    cursor = self.conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT UNIQUE NOT NULL
        )
        ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS market (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT NOT NULL
        )
        ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS market_news (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            questionId INTEGER NOT NULL,
            title TEXT NOT NULL,
            newsId TEXT NOT NULL
        )'''
        )
    