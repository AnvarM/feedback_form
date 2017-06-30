from flask import Flask, render_template, request, url_for
from time import ctime
import sqlite3 as sql

app = Flask(__name__)

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/addrecord', methods=['GET','POST'])
def addrecord():
	if request.method == 'POST':
		msg = ""
		try:
			ts = ctime()
			date = request.args.get('date')
			oneviewid = request.args.get('oneviewid')
			shift = request.args.get('shift')
			department = request.args.get('department')
			area = request.args.get('area')
			employee_exam = request.args.get('employee_exam')
			activity = request.args.get('activity')
			attention_work = request.args.get('attention_work')
			attention_road = request.args.get('attention_road')
			appropriate_tools = request.args.get('appropriate_tools')
			tools_is_ok = request.args.get('tools_is_ok')
			ppe = request.args.get('ppe')
			ppe_special = request.args.get('ppe_special')
			capture = request.args.get('capture')
			comment = request.args.get('comment')
			print (date)
			with sql.connect("database.db") as con:
				cur = con.cursor()
				cur.execute('INSERT into observations(timest,date_of_observation,oneviewid, shift, department, area, employee_exam,\
					activity, attention_work, attention_road, appropriate_tools, tools_is_ok, ppe, capture, comment VALUES\
					(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)', (ts,date,oneviewid,shift,department,area,employee_exam,\
					activity,attention_work,attention_road,appropriate_tools,tools_is_ok,ppe,ppe_special,capture,comment))
				con.commit()
				msg = "Record saved succesfully"
		except:
			con.rolback()
			msg="Error in insert operation"
		finally:
			#return render_template("thanks.html", msg=msg)
			return render_template("data.html", date=date, oneviewid=oneviewid, shift=shift) 
			con.close()			

	#return render_template("data.html", date=date, oneviewid=oneviewid, shift=shift) 
	#(date,oneviewid,shift,department,area,employee_exam,
	#activity,attention_work,attention_road,appropriate_tools,tools_is_ok,ppe,ppe_special,capture,comment)
	

if __name__ == "__main__":
	app.run(host = '0.0.0.0', debug=True)
