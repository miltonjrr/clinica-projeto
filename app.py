from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__)
app.secret_key = 'chave_secreta_aqui'


# Conexão com banco de dados SQLite

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def home():
    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Lógica de login aqui
        email = request.form['email']
        password = request.form['password']

        # Lógica para verificar as credenciais (a ser implementada)
        if email == 'exemplo@dominio.com' and password == 'senha123':
            flash('Login realizado com sucesso!')
            return redirect(url_for('home')) # Redireciona para a pag inicial
        else:
            flash('Credenciais inválidas. Tente novamente.')

    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        cpf = request.form['cpf']
        telefone = request.form['telefone']

        #Validando dados (básico)
        if not nome or not email or not cpf or not telefone:
            flash('Todos os campos são obrigatórios')
            return redirect(url_for('home'))

        #Inserir dados no banco de dados
        conn = get_db_connection()
        conn.execute('INSERT INTO usuarios (nome, email, cpf, telefone) VALUES (?, ?, ?, ?)', 
                    (nome, email, cpf, telefone))
        conn.commit()
        conn.close()

        flash('Cadastro realizado com sucesso!')
        return redirect(url_for('login'))
    
    return render_template('register.html')

    

if __name__ == '__main__':
    app.run(debug=True)
