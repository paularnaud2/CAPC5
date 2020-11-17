import flask
import connexion

# app = flask.Flask('My server', template_folder='template')
app = connexion.App(__name__, specification_dir='./')
app.add_api('swagger.yml')

@app.route('/')
def home():
	
	return flask.render_template('home.html')

@app.route('/test')
def test():
	
	return 'test'

# app.run(host='0.0.0.0', port=5000, debug=True)
app.run(host='192.168.1.106')