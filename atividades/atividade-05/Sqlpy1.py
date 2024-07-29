import sqlite3

# Conectar ao banco de dados
conn = sqlite3.connect("tasks.db")
cursor = conn.cursor()

# Criar a tabela 'tasks' se ela não existir
cursor.execute('''
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        description TEXT NOT NULL,
        completed INTEGER NOT NULL CHECK (completed IN (0, 1))
    )
''')
conn.commit()

# Operações CRUD

def create_task(description):
    # Verificar se a tarefa já existe
    cursor.execute("SELECT id FROM tasks WHERE description = ?", (description,))
    existing_task = cursor.fetchone()
    
    if existing_task:
        print(f"Tarefa com a descrição '{description}' já existe.")
    else:
        cursor.execute("INSERT INTO tasks (description, completed) VALUES (?, 0)", (description,))
        conn.commit()
        print(f"Tarefa '{description}' adicionada com sucesso.")

def list_tasks():
    cursor.execute("SELECT id, description, completed FROM tasks")
    tasks = cursor.fetchall()
    if not tasks:
        print("Nenhuma tarefa encontrada.")
    else:
        for task in tasks:
            print(f"ID: {task[0]}, Description: {task[1]}, Completed: {'Yes' if task[2] else 'No'}")

def mark_completed(task_id):
    cursor.execute("UPDATE tasks SET completed = 1 WHERE id = ?", (task_id,))
    conn.commit()

def delete_task(task_id):
    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    print(f"Tarefa com ID {task_id} excluída com sucesso.")

# Testar as funções
create_task("Aprender Python")
create_task("Ler um capitulo da auto-biografia do Jonas(Harry Potter)")

print("Tarefas antes de serem completadas:")
list_tasks()

mark_completed(1)  # Marcar a tarefa com ID 1 como concluída
mark_completed(4)
mark_completed(3)

delete_task(5)
delete_task(6)

print("\nTarefas apos serem completadas:")
list_tasks()

# Fechar a conexão
conn.close()
