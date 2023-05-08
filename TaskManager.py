## Task Tracker
## Created by dbugr (https://dbugr.vercel.app/)

import sqlite3

class TaskManager:
    def __init__(self, db_filename="tasks.db"):
        self.tasks = []
        self.conn = sqlite3.connect(db_filename)
        self.cursor = self.conn.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS tasks (task TEXT)")

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)

    def list_tasks(self):
        return self.tasks

    def save_tasks_to_db(self):
        self.cursor.execute("DELETE FROM tasks")
        for task in self.tasks:
            self.cursor.execute("INSERT INTO tasks (task) VALUES (?)", (task,))
        self.conn.commit()

    def load_tasks_from_db(self):
        self.tasks = []
        self.cursor.execute("SELECT task FROM tasks")
        tasks = self.cursor.fetchall()
        for task in tasks:
            self.tasks.append(task[0])