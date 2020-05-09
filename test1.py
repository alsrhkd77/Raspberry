from flask import Flask, request, render_template, abort, redirect
import sqlite3

app = Flask(__name__)
db = sqlite3.connect('test.db')
db.row_factory = sqlite3.Row
cur = db.cursor()


@app.route('/')
def show_all():  # 확인
    cur.execute("select * from student")
    result = cur.fetchall()
    if not result:
        return abort(404, "Page not found")
    return render_template("index.html", items=result)


@app.route('/update_s', methods=['POST'])
def add_phone():  # 수정
    student_id = int(request.form.get('s_id'))
    student_name = str(request.form.get('s_name'))
    cur.execute("UPDATE student SET NAME = %s WHERE ID = %d", (student_name, student_id))
    db.commit()
    return redirect('/')


if __name__ == '__main__':
    app.run(host='localhost', port=8080)
