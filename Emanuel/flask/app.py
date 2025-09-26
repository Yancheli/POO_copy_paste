from flask import Flask, render_template


app = Flask(__name__, template_folder='src/templates')
  




@app.route('/')
def hola_mundo():
    datos = {"nombre": "Emanuel",
             "edad": 18}
    return render_template('auth/login.html',data = datos)


if __name__ == '__main__':
    app.run(host = '0.0.0.0', port=5000,debug= True)