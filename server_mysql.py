from flask import Flask, render_template, request, url_for, redirect
from time import ctime
from flaskext.mysql import MySQL

mysql = MySQL()
app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'user_name'
app.config['MYSQL_DATABASE_PASSWORD'] = 'password'
app.config['MYSQL_DATABASE_DB'] = 'db_name'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)
conn = mysql.connect()

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
	print (ft,date,name,department,question1,question2,question3,comment)
	cursor = conn.cursor()

	cursor.execute("""INSERT into feedback(feedback_title,feedback_date,name, department,question1,question2,question3,comment) VALUES
			(%s,%s,%s,%s,%s,%s,%s,%s)""", [ft,date,name,department,question1,question2,question3,comment])
	conn.commit()
	msg = "Thank you for feedback!"

	return render_template("thanks.html", msg=msg)
	conn.close()	

if __name__ == "__main__":
	app.run(host = '0.0.0.0')
