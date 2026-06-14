import sqlite3
conn = sqlite3.connect('todo.db')
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS tasks(id INTEGER PRIMARY KEY AUTOINCREMENT,title TEXT)")
while True:
    print("1:タスク追加,2:タスク一覧,3:終了")
    choice = input("選択してください")
    if choice == "3":
        break
    elif choice == "1":
        title = input("新しいタスクを入力してください")
        cursor.execute("INSERT INTO tasks(title) VALUES (?)",(title,))
        print("タスクを追加しました！")

    elif choice == "2":
        cursor.execute("SELECT * FROM tasks")
        tasks = cursor.fetchall()
        for task in tasks:
            print(task[1])