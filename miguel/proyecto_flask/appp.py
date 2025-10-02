from flask import Flask, render_template


app = Flask(__name__, template_folder='src/templates')
  




@app.route('/')
def hola_mundo():
    datos = {"nombre": "Miguel",
             "edad": 18}
    gustos = ["Programar", "Correr", "Jugar"]
    return render_template('auth/login.html',data = datos,gustos = gustos,titulo = "Pagina de inicio")
   


if __name__ == '__main__':
    app.run(host = '0.0.0.0', port=5000,debug= True)
