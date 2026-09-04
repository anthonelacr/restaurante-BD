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


@app.route('/pedido', methods=['GET', 'POST'])
def pedido():
    if request.method == 'POST':

        nome_prato = request.form['nome_prato']
        id_cliente = request.form['id_cliente']
        valor_unitario = request.form['valor_unitario']
        qtd_pratos = request.form['qtd_pratos']
        valor_total = request.form['valor_total']

        conn = sqlite3.connect('restaurante.db')
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO pedido
            (nome_prato, id_cliente, valor_unitario, qtd_pratos, valor_total) VALUES (?, ?, ?, ?, ?)''', 
            (nome_prato, id_cliente, valor_unitario, qtd_pratos, valor_total))

        conn.commit()
        conn.close()

        return render_template('cadastro_restaurante.html',
                               mensagem=f"Pedido cadastrado com sucesso!")
    return render_template('cadastro_restaurante.html', mensagem=None)




if __name__ == '__main__':
    app.run(debug=True)