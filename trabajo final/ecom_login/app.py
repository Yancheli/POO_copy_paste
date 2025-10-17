from flask import Flask, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'clave-secreta-123'  # se puede cambiar

# Por ahora, conexión interna por diccionario 
usuarios = {}

@app.route('/')
def home():
    if 'usuario' in session:
        return f"Bienvenido, {session['usuario']}! <a href='/logout'>Cerrar sesión</a>"
    return redirect(url_for('login'))

# ---------- INGRESO ----------
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        correo = request.form['correo']
        contraseña = request.form['contraseña']

        if correo in usuarios and check_password_hash(usuarios[correo]['password'], contraseña):
            session['usuario'] = correo
            flash('Inicio de sesión exitoso!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Correo o contraseña incorrectos', 'danger')

    return render_template('login.html')

# ---------- REGISTRO ----------
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        correo = request.form['correo']
        contraseña = request.form['contraseña']

        if correo in usuarios:
            flash('El correo ya está registrado', 'warning')
        else:
            usuarios[correo] = {'password': generate_password_hash(contraseña)}
            flash('Registro exitoso, ahora puedes iniciar sesión', 'success')
            return redirect(url_for('login'))

    return render_template('register.html')

# ---------- CAMBIO DE CONTRASEÑA ----------
@app.route('/cambio_pass', methods=['GET', 'POST'])
def change_password():
    if request.method == 'POST':
        correo = request.form['correo']
        nueva = request.form['nueva']

        if correo in usuarios:
            usuarios[correo]['password'] = generate_password_hash(nueva)
            flash('Contraseña actualizada correctamente', 'success')
            return redirect(url_for('login'))
        else:
            flash('Usuario no encontrado', 'danger')

    return render_template('cambio_pass.html')

# ---------- DESCONEXIÓN ----------
@app.route('/logout')
def logout():
    session.pop('usuario', None)
    flash('Has cerrado sesión', 'info')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
