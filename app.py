from flask import Flask, render_template
import math

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')
	
@app.route('/suma/<int:s1>/<int:s2>',methods=['GET'])
def suma(s1,s2):
    return str(s1+s2)
	
@app.route('/resta/<int:s1>/<int:s2>',methods=['GET'])
def resta(s1,s2):
    return str(s1-s2)

@app.route('/dividir/<int:s1>/<int:s2>',methods=['GET'])
def divide(s1,s2):
    return str(s1/s2)

@app.route('/multiplicar/<int:s1>/<int:s2>',methods=['GET'])
def multiplica(s1,s2):
    return str(s1*s2)

@app.route('/raiz/<int:s1>',methods=['GET'])
def raiz(s1):
    return str(math.sqrt(s1))

#Alfonso Opazo
#Metodo que devuelve el coseno de un numero
@app.route('/raiz/<int:s1>',methods=['GET'])
def coseno(s1):
    return str(math.cos(s1))

if __name__ == '__main__':
    app.run()
