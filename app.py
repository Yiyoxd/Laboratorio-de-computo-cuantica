from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/auth', methods=['POST'])
def auth():
    # Simula login exitoso con cualquier usuario
    return redirect(url_for('menu'))

@app.route('/menu')
def menu():
    return render_template('menu.html')

@app.route('/simulador')
def simulador():
    return render_template('simulador.html')

@app.route('/curso')
def curso():
    return render_template('curso.html')

if __name__ == '__main__':
    app.run(debug=True)
