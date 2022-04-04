
from app import app
from db_config import mysql
from flask import flash, render_template, request, redirect, url_for
from werkzeug import generate_password_hash, check_password_hash
		
@app.route('/register', methods=['POST'])
def save_user_info():
	cursor = None
	try:
		name = request.form['Name: ']
		dob = request.form['Date of Birth: ']
		school = request.form['School: ']
		grade = request.form['School Year: ']
		email = request.form['Email (this will be your username": ']
		password = request.form['Password']

		if name and dob and school and grade and email and password and request.method == 'POST':
		
			_hashed_password = generate_password_hash(password)
			
			sql = "INSERT INTO user(name, password, email) VALUES(%s, %s, %s)"
			data = (name, _hashed_password, email)
			conn = mysql.connect()
			cursor = conn.cursor()
			cursor.execute(sql, data)
			conn.commit()
			
			flash('You registered successfully!')
			
			return redirect(url_for('.home'))
		else:			
			return 'Error while saving user information'
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()
		
@app.route('/')
def home():
	return render_template('registration.html')
		
if __name__ == "__main__":
    app.run()