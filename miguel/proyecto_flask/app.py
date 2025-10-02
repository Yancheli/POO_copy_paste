from flask import Flask, render_template

app = Flask(__name__)

@app.route("/<nombre>")
def hola(nombre):
    gustos = ['Programar', 'Videojuegos', 'valorant', 'Música']
    datos = {
        'nombre': nombre, 
        'Edad': 19,
        'gustos': gustos,
        'cantidad' : len(gustos)  
    }
    return render_template('auth/login.html', data=datos)
@app.route("/about")
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
