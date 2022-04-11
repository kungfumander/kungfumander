from app import app
from db_config import mysql
from flask import flash, render_template, request, redirect, url_for
from werkzeug import generate_password_hash

'''
This block of code is for registering a user with the website and saving their information
into the database. The function save_user_info() can be called to allow a user to register
with the site and use the service. After user input of username, email, password, and role,
a connection to the SQL database is created and the information is inserted into the database.
This can be called later, which will be useful for things like creating listing and applying to
listings, as only businesses can post and only students can apply.
'''
		
@app.route('/register', methods=['POST'])
def save_user_info():
	cursor = None
	try:
		idUser = request.form['Username: ']
		email = request.form['Email: ']
		password = request.form['Password: ']
		role = request.form['Role: ']

		if idUser and email and password and role and request.method == 'POST':
		
			_hashed_password = generate_password_hash(password)
   
			sql = "INSERT INTO user(idUser, email, password_hash, role) VALUES(%s, %s, %s, %s)"
			data = (idUser, email, _hashed_password, role)
			conn = mysql.connect(host = "localhost", user = "**username**", password = "**password**")
			cursor = conn.cursor()
			cursor.execute(sql, data)
			conn.commit()
			
			flash('You registered successfully!')
   
# If there is an error registering, an exception will be run and
# an error will be shown to the user. It will also redirect back to
# the homepage.

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