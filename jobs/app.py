from flask import Flask, render_template 

app = Flask(__name)

@app.route('/')
@app.route('/jobs')
def jobs():
	return render_template('index.html')

if __name__ == '__main__':
	pass
