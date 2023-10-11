import sqlite3
import sqlite3
from flask import Flask, render_template, request, redirect, url_for

# Create a SQLite database and a 'todos' table
def create_table():
    conn = sqlite3.connect('todos.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS todos (id INTEGER PRIMARY KEY, task TEXT)')
    conn.commit()
    conn.close()


app = Flask(__name__)

app.config['DATABASE'] = 'todos.db'  # Set the database file

# Initialize the database
def get_db():
    return sqlite3.connect(app.config['DATABASE'])


# Create the 'todos' table if it doesn't exist
create_table()

def main():
    app.run(debug=False)
    
@app.route('/')
def index():
    conn = get_db()
    cursor = conn.execute('SELECT * FROM todos')
    todos = cursor.fetchall()
    return render_template('index.html', todos=todos)

@app.route('/add', methods=['POST'])
def add_todo():
    todo = request.form.get('todo')
    if todo:
        conn = get_db()
        conn.execute('INSERT INTO todos (task) VALUES (?)', (todo,))
        conn.commit()
    return redirect(url_for('index'))

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update_todo(id):
    conn = get_db()
    cursor = conn.execute('SELECT * FROM todos WHERE id = ?', (id,))
    todo = cursor.fetchone()

    if request.method == 'POST':
        new_todo = request.form.get('todo')
        if new_todo:
            conn.execute('UPDATE todos SET task = ? WHERE id = ?', (new_todo, id))
            conn.commit()
            return redirect(url_for('index'))

    return render_template('update.html', todo=todo)


@app.route('/delete/<int:id>')
def delete_todo(id):
    conn = get_db()
    conn.execute('DELETE FROM todos WHERE id = ?', (id,))
    conn.commit()
    return redirect(url_for('index'))


if __name__ == '__main__':
    main()
