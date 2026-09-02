from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/clientes', methods=['GET', 'POST'])
def clientes():
    if request.method == 'POST':

        nome = request.form['nome']
        email = request.form['email']
        telefone = request.form['telefone']

        conn = sqlite3.connect('restaurante.db')
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO clientes
            (nome, email, telefone) VALUES (?, ?, ?)''', (nome, email, telefone))

        conn.commit()
        conn.close()

        return render_template('cadastro_cliente.html', 
                               mensagem=f"Cliente {nome} cadastrado com sucesso!")
    
    return render_template('cadastro_cliente.html', mensagem=None)

if __name__ == '__main__':
    app.run(debug=True)