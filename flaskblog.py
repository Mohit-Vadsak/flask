from flask import Flask,render_template,url_for, flash, redirect
#render_template is used to link python file wt=ith html page so we can use template
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'a9d74616a9ffad0afe5f427ee392fe10'

posts =[
	{
		'author':'Mohit Vadsak',
		'title':'Blog Post 1',
		'content':'First Post Content',
		'date_posted':'April 30, 2018'
	},
	{
		'author':'Milan Vadsak',
		'title':'Blog Post 2',
		'content':'Second Post Content',
		'date_posted':'April 27, 2018'
	}
]

@app.route('/') 
@app.route('/home')
def home():
    return render_template('home.html',posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/register', methods=['GET', 'POST'])
def register():
	form =  RegistrationForm('/register')
	if form.validate_on_submit():
		flash(f'Account created  for {form.username.data}!','success')
		return redirect(url_for('home'))
	return render_template('register.html', title= 'Register', form = form)

@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm('/login')
	return render_template('login.html', title='Login', form = form)


if __name__=='__main__':
	app.run(debug=True)
    