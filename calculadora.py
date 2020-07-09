from flask import Flask
app = Flask(__name__)

@app.route('/suma/<int:s1>/<int:s2>',methods=['GET'])
def suma(s1,s2):
    return str(s1+s2)
    
@app.route('/divir/<int:s1>/<int:s2>',methods=['GET'])
def dividir(s1,s2):
    return str(s1/s2)

@app.route('/restar/<int:s1>/<int:s2>',methods=['GET'])
def restar(s1,s2):
    return str(s1-s2)

if __name__ == '__main__':
    app.run()