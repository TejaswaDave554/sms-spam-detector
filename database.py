import sqlite3
import os

def init_db():
    """Initialize the feedback database"""
    db_path = 'data/feedback.db'
    os.makedirs('data', exist_ok=True)
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS feedback (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            message TEXT NOT NULL,
            predicted_label INTEGER NOT NULL,
            user_label INTEGER,
            confidence REAL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    conn.commit()
    conn.close()

def save_feedback(message, predicted_label, user_label, confidence):
    """Save user feedback to database"""
    conn = sqlite3.connect('data/feedback.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        INSERT INTO feedback (message, predicted_label, user_label, confidence)
        VALUES (?, ?, ?, ?)
    ''', (message, predicted_label, user_label, confidence))
    
    conn.commit()
    conn.close()

def get_feedback_data():
    """Get all feedback data for retraining"""
    conn = sqlite3.connect('data/feedback.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT message, user_label FROM feedback WHERE user_label IS NOT NULL')
    data = cursor.fetchall()
    
    conn.close()
    return data

if __name__ == '__main__':
    init_db()
    print("Database initialized successfully!")
