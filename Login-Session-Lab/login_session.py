from flask import Flask, render_template, request, url_for, redirect
from flask import session as login_session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super-secret-key'


@app.route('/', methods=['GET', 'POST']) # What methods are needed?
def home():
	if request.method == 'GET':
		return render_template('home.html')
	else:
		try:
		    qu = request.form['quote']
		    aut = request.form['author']
		    ag = request.form['age'] 
		    ag = int(ag)       
		    login_session['quote'] = qu
		    login_session['author'] = aut
		    login_session['age'] = ag
		    return render_template('thanks.html')
		except:
			return render_template('error.html')

#[{'quote':dsdsf, 'author': fdfd, 'age': fsfsf},{},{}]
	
#.append({'quote': ,'author': ,'age'})

@app.route('/error')
def error():

	return render_template('error.html')


@app.route('/display')
def display():

	return render_template('display.html', n=login_session['quote'], a=login_session['author'], agw=login_session['age']) # What variables are needed?


@app.route('/thanks')
def thanks():

	return render_template('thanks.html')


if __name__ == '__main__':
	app.run(debug=True)