from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

@app.route('/Registrar.html')
def Registrar_html():
    return render_template('Registrar.html')

# Rota para servir arquivos CSS
@app.route('/static/css/<path:filename>')
def Registrar_css(filename):
    css_path = os.path.join('static/css', filename)
    return send_from_directory(os.path.dirname(css_path), os.path.basename(css_path))

# Rota para servir imagens
@app.route('/static/imagens/<path:filename>')
def Registrar_imagens(filename):
    imagens_path = os.path.join('static/imagens', filename)
    return send_from_directory(os.path.dirname(imagens_path), os.path.basename(imagens_path))


""""# Função para conectar ao banco de dados
def conectar_bd():
    return sqlite3.connect('mydb.db')  # Substitua 'seu_banco.db' pelo nome do seu banco de dados

# Rota para exibir o formulário de cadastro de pessoa
@app.route('/cadastro_pessoa')
def cadastro_pessoa():
    return render_template('registrar_login.html')  # Renderiza o formulário HTML para cadastro de pessoa

# Rota para inserir dados da pessoa no banco
@app.route('/inserir_pessoa', methods=['POST'])
def inserir_pessoa():
    if request.method == 'POST':  # Verifica se a requisição é do tipo POST (envio de dados do formulário)
        # Captura os dados enviados pelo formulário
        cpf = request.form['cpf_pessoa']
        nome = request.form['nome_pessoa']
        email = request.form['email_pessoa']
        data_nascimento = request.form['data_pessoa']
        endereco = request.form['endereco_pessoa']
        senha = request.form['senha_pessoa']
        sexo = request.form['sexo_pessoa']

        # Conectar ao banco de dados
        conexao = conectar_bd()
        cursor = conexao.cursor()

        # Inserir os dados na tabela tb_pessoa
        cursor.execute("INSERT INTO tb_pessoa (cpf_pessoa, nome_pessoa, email_pessoa, data_pessoa, endereco_pessoa, senha_pessoa, sexo_pessoa) VALUES (?, ?, ?, ?, ?, ?, ?)",
                       (cpf, nome, email, data_nascimento, endereco, senha, sexo))

        # Confirmar as mudanças e fechar a conexão
        conexao.commit()
        conexao.close()

        return "Dados inseridos com sucesso!"  # Mensagem de confirmação após a inserção"""

if __name__ == '__main__':
    app.run(debug=True)  # Inicia a aplicação Flask em modo de depuração
