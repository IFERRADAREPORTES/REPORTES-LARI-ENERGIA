from flask import Flask, render_template, request, redirect, url_for, session
from datetime import timedelta

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta_aqui'  # Cambia por algo seguro
app.permanent_session_lifetime = timedelta(minutes=15)

USUARIOS = {
    'FPIMENTEL': 'LARI2025',
    'ETAMAYO': 'LARI2025',
    'IFERRADA': 'LARI2025',
    'EJIMENEZ': 'LARI2025'
}

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form.get('username')
        contrasena = request.form.get('password')

        if usuario in USUARIOS and contrasena == USUARIOS[usuario]:
            session.permanent = True
            session['usuario'] = usuario
            return redirect(url_for('indicadores'))
        else:
            return render_template('login.html', error="Credenciales incorrectas")
    return render_template('login.html')

@app.route('/INDICADORESLARI-ENERGIA')
def indicadores():
    if 'usuario' in session:
        return render_template('welcome.html', usuario=session['usuario'])
    else:
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('usuario', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
