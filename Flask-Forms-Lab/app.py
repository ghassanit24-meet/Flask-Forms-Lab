from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)


username = "ghassan"
password = "123"
facebook_friends=["Rommie","Ali","Kinda", "Atef", "Julia", "masharka"]


@app.route('/', methods = ['GET', 'POST'])  # '/' for the default page
def login():
	if request.method == 'GET':
			return render_template('login.html')
	else:
			name2 = request.form ['username']
			password2 = request.form ['password']
			if name2 == username and password2 == password:
					return redirect(url_for('home'))
			else:
  				return render_template('login.html')

@app.route('/home')
def home():
	return render_template('home.html', friends = facebook_friends)

@app.route('/friend_exists/<string:name>',methods=['GET','POST'])
def friend_exists(name):
		exist=name
		return render_template('friend_exists.html',name=name,friends=facebook_friends)


if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
    debug=True
	)