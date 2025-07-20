import sqlite3
from datetime import  datetime, timezone
import tzlocal

DATABASE = "worksync.db"


def initialize_db():
    """Initialize the database and create necessary tables."""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        task_detail TEXT NOT NULL,
        current_status TEXT,
        help_taken TEXT,
        completion_time INTEGER,
        reason TEXT,
        deployment_status TEXT,
        comments TEXT,
        created_at DATETIME
    )
    """)
    conn.commit()
    conn.close()


def add_task_to_db(task_detail, current_status, help_taken, completion_time, reason, deployment_status, comments, created_at):
    """Insert task details into the database."""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO tasks (task_detail, current_status, help_taken, completion_time, reason, deployment_status, comments, created_at)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (task_detail, current_status, help_taken, completion_time or None, reason, deployment_status, comments, created_at))
    conn.commit()
    conn.close()


def fetch_tasks_for_today():
    """Fetch tasks created on the current date."""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    current_utc_date = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%fZ")
    utc_dt = datetime.strptime(current_utc_date, "%Y-%m-%dT%H:%M:%S.%fZ")
    utc_dt = utc_dt.replace(tzinfo=timezone.utc)
    local_tz = tzlocal.get_localzone()
    created_at = utc_dt.astimezone(local_tz).strftime("%Y-%m-%d")
    cursor.execute("""
    SELECT id, task_detail, current_status, help_taken, completion_time, reason, deployment_status, comments
    FROM tasks
    WHERE DATE(created_at) = ?
    """, (created_at,))
    tasks = cursor.fetchall()
    conn.close()
    return tasks


def update_task_in_db(task_id, task_detail, current_status, help_taken, completion_time, reason, deployment_status, comments):
    """Update an existing task in the database."""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("""
    UPDATE tasks
    SET task_detail = ?, current_status = ?, help_taken = ?, completion_time = ?, reason = ?, deployment_status = ?, comments = ?
    WHERE id = ?
    """, (task_detail, current_status, help_taken, completion_time or None, reason, deployment_status, comments, task_id))
    conn.commit()
    conn.close()



def save_email_to_db(sender,password, receiver, cc, subject):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS email_info (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sender TEXT,
            password TEXT,
            receiver TEXT,
            cc TEXT,
            subject TEXT
        )
    ''')
    cursor.execute('DELETE FROM email_info')  # Optional: keep only latest entry
    cursor.execute('''
        INSERT INTO email_info (sender, password, receiver, cc, subject)
        VALUES (?, ?, ?, ?, ?)
    ''', (sender, password, receiver, cc, subject))
    conn.commit()
    conn.close()

def is_email_configured():
    conn = sqlite3.connect('worksync.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS email_info (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sender TEXT,
            password TEXT,
            receiver TEXT,
            cc TEXT,
            subject TEXT
        )
    ''')
    cursor.execute('SELECT COUNT(*) FROM email_info')
    count = cursor.fetchone()[0]
    conn.close()
    return count > 0

def fetch_email_configured():
    conn = sqlite3.connect('worksync.db')
    cursor = conn.cursor()
    cursor.execute('SELECT sender, password, receiver, cc, subject FROM email_info')
    email_details = cursor.fetchall()
    conn.close()
    return email_details