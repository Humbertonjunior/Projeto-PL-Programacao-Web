from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

@app.route('/listar-ocorrencia.html')
def lista_ocorrencia_html():
    return render_template('listar-ocorrencia.html')

# Rota para servir arquivos CSS
@app.route('/static/css/<path:filename>')
def lista_ocorrencia_css(filename):
    css_path = os.path.join('static/css', filename)
    return send_from_directory(os.path.dirname(css_path), os.path.basename(css_path))

# Rota para servir imagens
@app.route('/static/imagens/<path:filename>')
def lista_ocorrencia_imagens(filename):
    imagens_path = os.path.join('static/imagens', filename)
    return send_from_directory(os.path.dirname(imagens_path), os.path.basename(imagens_path))


if __name__ == "__main__":
    app.run(port=8080, debug=True)
