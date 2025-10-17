from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

# ---------------------- CONFIGURACIÓN INICIAL ----------------------
app = Flask(__name__)
app.secret_key = 'clave-secreta-123'

# Configuración de Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager.login_message = "Por favor, inicia sesión para acceder a esta página."
login_manager.login_message_category = "warning"

# diccionario temporal
usuarios = {}

# Clase usuario para Flask-Login
class Usuario(UserMixin):
    def __init__(self, id):
        self.id = id

@login_manager.user_loader
def load_user(user_id):
    if user_id in usuarios:
        return Usuario(user_id)
    return None

# --------------------------------------------

@app.route('/')
@login_required
def home():
    return f"""
    <h2>Bienvenido, {current_user.id}!</h2>
    <a href='/logout'>Cerrar sesión</a> |
    <a href='/ajustes'>Ajustes</a> |
    <a href='/cambio_pass'>Cambiar contraseña</a>
    """

# ---------- INICIO DE SESIÓN ----------
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        correo = request.form['correo']
        contraseña = request.form['contraseña']

        if correo in usuarios and check_password_hash(usuarios[correo]['password'], contraseña):
            usuario = Usuario(correo)
            login_user(usuario)
            flash('Has iniciado sesión correctamente.', 'success')
            return redirect(url_for('home'))
        else:
            flash('El correo o la contraseña son incorrectos.', 'danger')

    return render_template('login.html')

# ---------- REGISTRO ----------
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        correo = request.form['correo']
        contraseña = request.form['contraseña']

        if correo in usuarios:
            flash('Este correo ya está registrado.', 'warning')
        else:
            usuarios[correo] = {'password': generate_password_hash(contraseña)}
            flash('Registro exitoso. Ahora puedes iniciar sesión.', 'success')
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
            flash('La contraseña se actualizó correctamente.', 'success')
            return redirect(url_for('login'))
        else:
            flash('No se encontró ningún usuario con ese correo.', 'danger')

    return render_template('cambio_pass.html')

# ---------- AJUSTES DE USUARIO (CAMBIO DE CORREO SOLAMENTE) ----------
@app.route('/ajustes', methods=['GET', 'POST'])
@login_required
def ajustes_usuario():
    if request.method == 'POST':
        nuevo_correo = request.form['nuevo_correo']

        # Verificar que no esté en uso
        if nuevo_correo in usuarios:
            flash('Ese correo ya está en uso.', 'warning')
        else:
            # Copiar los datos del usuario actual al nuevo correo
            usuarios[nuevo_correo] = usuarios.pop(current_user.id)
            
            # Actualizar sesión
            logout_user()
            usuario = Usuario(nuevo_correo)
            login_user(usuario)
            
            flash('Tu correo se actualizó correctamente.', 'success')
            return redirect(url_for('home'))

    return render_template('ajustes.html', correo_actual=current_user.id)

# ---------- CERRAR SESIÓN ----------
@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Has cerrado sesión correctamente.', 'info')
    return redirect(url_for('login'))

# ---------------------- EJECUCIÓN o LANZAMIENTO ----------------------
if __name__ == '__main__':
    app.run(debug=True)
