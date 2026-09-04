from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cliente', methods=['GET', 'POST'])
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
        cursor.execute('''INSERT INTO pedidos
            (id_cliente, nome_prato, valor_unitario, qtd_pratos, valor_total) VALUES (?, ?, ?, ?, ?)''', 
            (id_cliente, nome_prato, valor_unitario, qtd_pratos, valor_total))

        conn.commit()
        conn.close()

        return render_template('cadastro_pedido.html',
                               mensagem=f"Pedido cadastrado com sucesso!")
    return render_template('cadastro_pedido.html', mensagem=None)

#------------------------pedido------------------------------

@app.route('/listar-pedidos')
def listar_pedidos():
    conn = sqlite3.connect('restaurante.db')
    cursor = conn.cursor()
    
    query = '''
        SELECT p.id_pedido, p.id_cliente, c.nome, p.nome_prato, p.valor_unitario, p.qtd_pratos, p.valor_total
        FROM pedidos p
        LEFT JOIN clientes c ON c.id_cliente = p.id_cliente
        ORDER BY c.nome
    '''
    
    cursor.execute(query)
    pedidos = cursor.fetchall()
    conn.close()
    
    return render_template('listar_pedidos.html', pedidos = pedidos)


@app.route('/editar-pedido/<int:id_pedido>', methods=['GET', 'POST'])
def editar_pedido(id_pedido):
    if request.method == 'GET':
        conn = sqlite3.connect('restaurante.db')
        cursor = conn.cursor()

        query = '''
            SELECT p.id_pedido, p.id_cliente, c.nome, p.nome_prato, p.valor_unitario, p.qtd_pratos, p.valor_total
            FROM pedidos p
            LEFT JOIN clientes c ON c.id_cliente = p.id_cliente
            WHERE p.id_pedido = ?
        '''
        cursor.execute(query, (id_pedido,))
        pedido = cursor.fetchone()
        conn.commit()
        conn.close()

        return render_template('cadastro_pedido.html', modo='editar', pedido=pedido)

    if request.method == 'POST':
        id_cliente = request.form['id_cliente']
        nome_prato = request.form['nome_prato']
        valor_unitario = request.form['valor_unitario']
        qtd_pratos = request.form['qtd_pratos']
        valor_total = request.form['valor_total']

        conn = sqlite3.connect('restaurante.db')
        cursor = conn.cursor()

        cursor.execute('''
            UPDATE pedidos
            SET id_cliente = ?, nome_prato = ?, valor_unitario = ?, qtd_pratos = ?, valor_total = ?
            WHERE id_pedido = ?
        ''', (id_cliente, nome_prato, valor_unitario, qtd_pratos, valor_total, id_pedido))

        conn.commit()
        conn.close()

        return redirect(url_for('listar_pedidos'))

@app.route('/excluir-pedido/<int:id_pedido>', methods=['POST'])
def excluir_pedido(id_pedido):
    conn = sqlite3.connect('restaurante.db')
    cursor = conn.cursor()

    cursor.execute('DELETE FROM pedidos WHERE id_pedido = ?', (id_pedido,))

    conn.commit()
    conn.close()

    return redirect(url_for('listar_pedidos'))


#-------------------------cliente------------------------------

@app.route('/listar-clientes')
def listar_clientes():
    conn = sqlite3.connect('restaurante.db')
    cursor = conn.cursor()

    query = '''
        SELECT c.id_cliente, c.nome, c.email, c.telefone
        FROM clientes c
        ORDER BY c.nome
    '''

    cursor.execute(query)
    clientes = cursor.fetchall()
    conn.close()

    return render_template('listar_clientes.html', clientes = clientes)

@app.route('/editar-cliente/<int:id_cliente>', methods=['GET', 'POST'])
def editar_cliente(id_cliente):
    conn = sqlite3.connect('restaurante.db')
    cursor = conn.cursor()

    query = '''
        SELECT c.id_cliente, c.nome, c.email, c.telefone
        FROM clientes c
        WHERE c.id_cliente = ?
    '''
    cursor.execute(query, (id_cliente,))
    cliente = cursor.fetchone()
    conn.commit()
    conn.close()
    
    return render_template('cadastro_cliente.html', modo='editar', cliente=cliente)

    if request.method == 'POST':

        nome = request.form['nome']
        email = request.form['email']
        telefone = request.form['telefone']

        conn = sqlite3.connect('restaurante.db')
        cursor = conn.cursor()

        cursor.execute('''
            UPDATE clientes
            SET id_cliente = ?, nome  = ?, email = ?, telefone = ?
            WHERE id_cliente = ?
        ''', (id_cliente, nome, email, telefone))

        conn.commit()
        conn.close()

        return redirect(url_for('listar_clientes'))

@app.route('/excluir-cliente/<int:id_cliente>', methods=['POST'])
def excluir_cliente(id_cliente):
    conn = sqlite3.connect('restaurante.db')
    cursor = conn.cursor()
    
    cursor.execute('DELETE FROM clientes WHERE id_cliente = ?', (id_cliente,))
    
    conn.commit()
    conn.close()
    
    return redirect(url_for('listar_clientes'))


if __name__ == '__main__':
    app.run(debug=True)