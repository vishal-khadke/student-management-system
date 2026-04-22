from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('students.db')
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY, name TEXT)')
    conn.commit()
    conn.close()

init_db()

@app.route('/')
def index():
    conn = sqlite3.connect('students.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM students')
    students = cur.fetchall()
    conn.close()
    return render_template('index.html', students=students)

@app.route('/add', methods=['POST'])
def add():
    name = request.form.get('name')
    conn = sqlite3.connect('students.db')
    cur = conn.cursor()
    cur.execute('INSERT INTO students (name) VALUES (?)', (name,))
    conn.commit()
    conn.close()
    return redirect('/')

@app.route('/delete/<int:id>')
def delete(id):
    conn = sqlite3.connect('students.db')
    cur = conn.cursor()
    cur.execute('DELETE FROM students WHERE id=?', (id,))
    conn.commit()
    conn.close()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)