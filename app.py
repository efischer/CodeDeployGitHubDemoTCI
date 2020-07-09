from flask import Flask
app = Flask(__name__)

@app.route('/')
def principal():
	return "hola"
	
@app.route('/suma/<int:s1>/<int:s2>',methods=['GET'])
def suma(s1,s2):
    return str(s1+s2)
	
@app.route('/resta/<int:s1>/<int:s2>',methods=['GET'])
def resta(s1,s2):
    return str(s1-s2)

if __name__ == '__main__':
    app.run()