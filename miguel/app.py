from flask import Flask, render_template
 
app = Flask(__name__)
 
@app.route('/')
def hola_mundo():
    return "Mi nombre es Miguel y tengo 18 años"
 
if __name__ == '__main__':
    app.run(debug = True)
    @app.route('/nueva')
    def Nomber_edad():
        return "Mi nombre es Miguel y tengo 18 años"
