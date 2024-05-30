from flask import Flask, render_template, send_from_directory, request
from DAO import DAO
import os

app = Flask(__name__)

@app.route('/registrar_ocorrencia', methods=['GET', 'POST'])
def ocorrencia_html():
    tipo = DAO("tb_tipo")
    lstTipo = tipo.readAll()
    return render_template('registrar_ocorrencia.html', lstTipo=lstTipo)

@app.route('/salvar_ocorrencia', methods=['GET', 'POST'])
def salvar_html():

    if request.method == 'POST':
        # Obter dados do formulário
        descricao = request.form.get('descricao')
        data_ocorrencia = request.form.get('data_ocorrencia')
        fk_departamento = request.form.get('fk_departamento')
        fk_pessoa = request.form.get('fk_pessoa')
        fk_tipo = request.form.get('fk_tipo')

        # Adicione logs para verificar os dados
        print("Descrição:", descricao)
        print("Data de Ocorrência:", data_ocorrencia)
        print("Departamento:", fk_departamento)
        print("Pessoa:", fk_pessoa)
        print("Tipo:", fk_tipo)

        # Criar um dicionário com os dados
        novos_dados = {
            'descricao': descricao,
            'data_ocorrencia': data_ocorrencia,
            'fk_departamento': fk_departamento,
            'fk_pessoa': fk_pessoa,
            'fk_tipo': fk_tipo
        }

        # Exemplo de uso do DAO para criar uma nova ocorrência
        nova_ocorrencia = OcorrenciaDAO.criar_ocorrencia(novos_dados)

        # Adicione logs para verificar se a ocorrência foi criada
        print("Ocorrência criada:", nova_ocorrencia)

        # Redirecionar para outra página ou fazer qualquer outra ação desejada

    return render_template('registrar_ocorrencia.html')

# Rota para servir arquivos CSS
@app.route('/static/css/<path:filename>')
def ocorrencia_css(filename):
    css_path = os.path.join('static/css', filename)
    return send_from_directory(os.path.dirname(css_path), os.path.basename(css_path))

# Rota para servir imagens
@app.route('/static/imagens/<path:filename>')
def serve_imagens(filename):
    imagens_path = os.path.join('static/imagens', filename)
    return send_from_directory(os.path.dirname(imagens_path), os.path.basename(imagens_path))

if __name__ == '__main__':
    app.run(debug=True)
