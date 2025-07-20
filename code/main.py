from db_handler import initialize_db
from gui import create_gui
import threading
import time

def periodic_task_check(interval=3600):
    while True:
        initialize_db()
        create_gui()
        time.sleep(interval)

def main():
    thread = threading.Thread(target=periodic_task_check, args=(3600,), daemon=True)
    thread.start()
    while True:
        time.sleep(1)

if __name__ == "__main__":
    main()
