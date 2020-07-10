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
@app.route('/coseno/<int:s1>',methods=['GET'])
def coseno(s1):
    var_coseno = str(math.cos(s1))
    return print("Se imprime el coseno de un valor en radianes:\n")
    return var_coseno

#Alfonso Opazo
#Metodo que devuelve el valor de Pi
@app.route('/pi/<int:s1>',methods=['GET'])
def pi():
    var_pi = str(math.pi)
    return print("Se imprime el valor de Pi:\n")
    return  var_pi


#Claudio Diaz
#logaritmo base 10
@app.route('/logaritmo/<int:s1>',methods=['GET'])
def logaritmo(s1):
    print('Logaritmo en base 10:')
    return str(math.log10(s1))

<<<<<<< HEAD
##felipe ramirez
##raiz cubica
@app.route('/raizcubica/<int:s1>',methods=['GET'])
def raizcubica(s1):
    return str(s1**(1/3))    
=======
#Ignacio Fajardo
@app.route('/logaritmo2/<int:s1>',methods=['GET'])
def logaritmo2(s1):
    print('Logaritmo en base 2:')
    return str(math.log2(s1))

>>>>>>> 23c3b1a843039df7df1e0bf94577e7858c619252
if __name__ == '__main__':
    app.run()
