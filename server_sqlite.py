from flask import Flask, render_template, request, url_for, redirect
import sqlite3 as sql

app = Flask(__name__)

checklist = ['Good', 'Bad', "I don't know"]
department = ['Finance', 'IT', 'HR', 'Production', 'Marketing']
feedback_title = ['First feedback', 'Second feedback']

@app.route('/')
def index():
	return render_template("index.html", checklist=checklist, department=department, feedback_title=feedback_title)

@app.route('/addrecord', methods=['POST'])
def addrecord():
	ft = str(request.form['feedback_title'])
	date = str(request.form['date'])
	name = str(request.form['name'])
	department = str(request.form['department'])
	question1 = str(request.form['question1'])
	question2 = str(request.form['question2'])
	question3 = str(request.form['question3'])
	comment = str(request.form['comment'])

	with sql.connect("database.db") as con:
		cur = con.cursor()
		cur.execute("""INSERT into feedback(feedback_title,feedback_date,name, department,question1,question2,question3,comment) VALUES
				(?,?,?,?,?,?,?,?)""",[ft,date,name,department,question1,question2,question3,comment])
		con.commit()
		msg = "Запись сохранена, спасибо за наблюдение!"

	return render_template("thanks.html", msg=msg)
	con.close()	
	

if __name__ == "__main__":
	app.run(host = '0.0.0.0')
