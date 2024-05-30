from flask import Flask, request, jsonify, render_template, send_from_directory
from flask_login import current_user, LoginManager, login_user, logout_user, login_required, UserMixin
from Projeto_PL import DAO
import hashlib
import os

app = Flask(__name__)
app.secret_key = 'digite aqui sua chave secreta ou adicione um token seguro'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


class User(UserMixin):
    cpf_pessoa = 0
    nome_pessoa = ''
    email_pessoa = ''

    def to_json(self):
        return {
            "cpf_pessoa": self.cpf_pessoa,
            "nome_pessoa": self.nome_pessoa,
            "email_pessoa": self.email_pessoa
        }

    def get_id(self):
        return str(self.cpf_pessoa)


@login_manager.user_loader
def load_user(user_id):
    dao = DAO('tb_pessoa')
    lista = dao.readBy('cpf_pessoa', '==', user_id)
    if len(lista) == 1:
        usr = User()
        usr.cpf_pessoa = str(lista[0].cpf_pessoa)
        usr.nome_pessoa = lista[0].nome_pessoa
        usr.email_pessoa = lista[0].email_pessoa
        return usr
    else:
        return None


# Rota para servir arquivos CSS
@app.route('/static/css/registrar_login.css')
def serve_css():
    return send_from_directory('static/css', 'registrar_login.css')


@app.route('/static/imagens/<path:filename>')
def serve_imagens(filename):
    return send_from_directory('static/imagens', filename)


@app.route('/')
def serve_html():
    return render_template('login.html')


@app.route('/login', methods=['GET'])
def login():
    username = request.args.get('usuario')
    password = request.args.get('senha')
    print(username, password)
    dao = DAO('tb_pessoa')
    lista = dao.readBy('nome_pessoa', '==', username)
    compilacao = hashlib.sha1(password.encode("utf-8")).hexdigest()
    if len(lista) == 1 and lista[0].pwd_pessoa == compilacao:
        usr = User()
        usr.cpf_pessoa = str(lista[0].cpf_pessoa)
        usr.nome_pessoa = lista[0].nome_pessoa
        usr.email_pessoa = lista[0].email_pessoa
        login_user(usr, remember=True)

        if current_user.is_authenticated:
            return jsonify({
                'cpf_pessoa': usr.cpf_pessoa,
                'nome_pessoa': usr.nome_pessoa,
                'email_pessoa': usr.email_pessoa
            })
        else:
            return jsonify({"status": 401, "reason": "Usuario ou senha errados"})


@app.route('/logout', methods=['GET'])
def logout():
    logout_user()
    return jsonify(**{'result': 200, 'data': {'message': 'logout feito com sucesso'}})


@app.route('/consultar', methods=['GET'])
def consultar():
    print(current_user.is_authenticated)
    if current_user.is_authenticated:
        resp = {"result": 200, "data": current_user.to_json()}
    else:
        resp = {"result": 401, "data": {"message": "usuario inexistente"}}
    return jsonify(**resp)



@app.route('/pesquisar', methods=['GET'])
@login_required
def pesquisar():
    idt = request.args.get('cpf')
    dao = DAO('tb_pessoa')
    pessoa = dao.readById(idt)
    if pessoa is None:
        return jsonify({'error': 'data not found'})
    else:
        return jsonify({
            'cpf_pessoa': pessoa.cpf_pessoa,
            'nome_pessoa': pessoa.nome_pessoa,
            'email_pessoa': pessoa.email_pessoa
        })

@app.route('/inserir', methods=['PUT'])
@login_required
def inserir():
    daoPes = DAO("tb_pessoa")
    objPes = daoPes.tb_pessoa()
    objPes.cpf_pessoa = request.args.get('cpf_pessoa')
    objPes.nme_pessoa = request.args.get('nme_pessoa')
    daoPes.create(objPes)

    return jsonify({'cpf_pessoa': objPes.cpf_pessoa})


@app.route('/apagar', methods=['DELETE'])
@login_required
def apagar():
    idt = request.args.get('cpf')
    daoPes = DAO('tb_pessoa')

    if daoPes.readById(idt) is not None:
        daoPes.delete(daoPes.readById(idt))
    return jsonify({'cpf_pessoa': idt})


# incio da pagina index
@app.route('/index.html')
def index_html():
    return render_template('index.html')

# Rota para servir arquivos CSS
@app.route('/static/css/<path:filename>')
def index_css(filename):
    css_path = os.path.join('static/css', filename)
    return send_from_directory(os.path.dirname(css_path), os.path.basename(css_path))

# Rota para servir imagens
@app.route('/static/imagens/<path:filename>')
def index_imagens(filename):
    imagens_path = os.path.join('static/imagens', filename)
    return send_from_directory(os.path.dirname(imagens_path), os.path.basename(imagens_path))

#Inicio da pagina profile
@app.route('/profie.html')
def profie_html():
    return render_template('profie.html')

# Rota para servir arquivos CSS
@app.route('/static/css/<path:filename>')
def profie_css(filename):
    css_path = os.path.join('static/css', filename)
    return send_from_directory(os.path.dirname(css_path), os.path.basename(css_path))

# Rota para servir imagens
@app.route('/static/imagens/<path:filename>')
def profie_imagens(filename):
    imagens_path = os.path.join('static/imagens', filename)
    return send_from_directory(os.path.dirname(imagens_path), os.path.basename(imagens_path))



# incio da pagina registrar-se
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



# #incio da pagina resgistrar ocorrencia

@app.route('/registrar_ocorrencia.html')
def ocorrencia_html():
    return render_template('registrar_ocorrencia.html')

# Rota para servir arquivos CSS
@app.route('/static/css/<path:filename>')
def ocorrencia_css(filename):
    css_path = os.path.join('static/css', filename)
    return send_from_directory(os.path.dirname(css_path), os.path.basename(css_path))

# Rota para servir imagens
@app.route('/static/imagens/<path:filename>')
def ocorrencia_imagens(filename):
    imagens_path = os.path.join('static/imagens', filename)
    return send_from_directory(os.path.dirname(imagens_path), os.path.basename(imagens_path))


# incio da pagina listar ocorrencia

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
