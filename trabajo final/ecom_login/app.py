from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash
from config import Config
from models import db, Usuario

# ---------------------- CONFIGURACIÓN INICIAL ----------------------
app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
with app.app_context():
    db.create_all()

# ---------------------- CONFIGURACIÓN DE LOGIN ----------------------
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager.login_message = "Por favor, inicia sesión para acceder a esta página."
login_manager.login_message_category = "warning"

@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.get(int(user_id))

# ---------------------- RUTAS ----------------------

@app.route('/')
@login_required
def home():
    if current_user.rol == 'admin':
        return render_template('admin/dashboard.html', nombre=current_user.correo)
    return render_template('user/catalogo.html', nombre=current_user.correo)

# ---------- LOGIN ----------
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        correo = request.form['correo']
        contraseña = request.form['contraseña']

        usuario = Usuario.query.filter_by(correo=correo).first()
        if usuario and usuario.check_password(contraseña):
            login_user(usuario)
            flash('Has iniciado sesión correctamente.', 'success')
            return redirect(url_for('home'))
        else:
            flash('Correo o contraseña incorrectos.', 'danger')

    return render_template('login.html')

# ---------- REGISTRO ----------
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        nombre = request.form['nombre']
        correo = request.form['correo']
        contraseña = request.form['contraseña']

        existente = Usuario.query.filter_by(correo=correo).first()
        if existente:
            flash('Este correo ya está registrado.', 'warning')
        else:
            nuevo = Usuario(nombre=nombre, correo=correo, rol='cliente')
            nuevo.set_password(contraseña)
            db.session.add(nuevo)
            db.session.commit()
            flash('Registro exitoso. Ahora puedes iniciar sesión.', 'success')
            return redirect(url_for('login'))

    return render_template('register.html')

# ---------- CAMBIO DE CONTRASEÑA ----------
@app.route('/change_password', methods=['GET', 'POST'])
@login_required
def change_password():
    if request.method == 'POST':
        nueva = request.form['nueva']
        current_user.set_password(nueva)
        db.session.commit()
        flash('Contraseña actualizada correctamente.', 'success')
        return redirect(url_for('home'))

    return render_template('cambio_pass.html')

# ---------- AJUSTES DE USUARIO ----------
@app.route('/ajustes', methods=['GET', 'POST'])
@login_required
def ajustes_usuario():
    if request.method == 'POST':
        nuevo_correo = request.form['nuevo_correo']
        existente = Usuario.query.filter_by(correo=nuevo_correo).first()
        if existente:
            flash('Ese correo ya está en uso.', 'warning')
        else:
            current_user.correo = nuevo_correo
            db.session.commit()
            flash('Correo actualizado correctamente.', 'success')
            return redirect(url_for('home'))

    return render_template('ajustes.html', correo_actual=current_user.correo)

# ---------- LOGOUT ----------
@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Sesión cerrada correctamente.', 'info')
    return redirect(url_for('login'))

# ---------------------- EJECUCIÓN ----------------------
if __name__ == '__main__':
    app.run(debug=True)
