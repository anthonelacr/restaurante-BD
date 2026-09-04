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

        id_cliente = request.form['id_cliente']
        nome_prato = request.form['nome_prato']
        valor_unitario = request.form['valor_unitario']
        qtd_pratos = request.form['qtd_pratos']
        valor_total = request.form['valor_total']

        conn = sqlite3.connect('restaurante.db')
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO pedido
            (id_cliente, nome_prato, valor_unitario, qtd_pratos, valor_total) VALUES (?, ?, ?, ?, ?)''', 
            (id_cliente, nome_prato, valor_unitario, qtd_pratos, valor_total))

        conn.commit()
        conn.close()

        return render_template('cadastro_restaurante.html',
                               mensagem=f"Pedido cadastrado com sucesso!")
    return render_template('cadastro_restaurante.html', mensagem=None)

@app.route('/pedido', methods=['GET', 'POST'])
def pedido():
    if request.method == 'GET':

        query = '''
                SELECT co.id_contato, co.nome, co.email, ca.data_cadastro,
                       t.telefone_res, t.telefone_co, t.telefone_cel,
                       GROUP_CONCAT(cat.tipo_cadastro, ', ') as tipos
                FROM contato co
                LEFT JOIN telefones t ON co.id_telefone = t.id_telefone
                LEFT JOIN cadastro ca ON co.id_contato = ca.id_contato
                LEFT JOIN categoria cat ON co.id_contato = cat.id_contato
                GROUP BY co.id_contato
                ORDER BY co.nome
            '''

        conn = sqlite3.connect('restaurante.db')
        cursor = conn.cursor()
            
            
            cursor.execute(query)
            pedidos = cursor.fetchall()
            conn.close()
    
    return render_template('listar.html', pedidos=pedidos)

if __name__ == '__main__':
    app.run(debug=True)



if __name__ == '__main__':
    app.run(debug=True)