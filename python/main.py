from flask import Flask, jsonify, request 
from flask_cors import CORS
import os
import uuid
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime


# ma secret key pour la génération de mon token
SECRET_KEY = "mysecretkey"

'''
 TODO méthode decorator pour check user auth ou non et éventuellement ses droits
'''

# ma méthode qui contient mon dict de users et qui retourne le pwd de mon user si il existe, ici le pwd de base est "stef", 
# la méthode prend en param le username reçu depuis mon front
def getUser(username):
    lst_users = [{'name':'stef','pwd':"sha256$xzjkcf9AZjT2JWlv$bb6dd197cecf17f0ca5bd0f82f78ff84210831e4a6f356abeea4747f2794b222"},
                {'name':'cam','pwd':"sha256$xzjkcf9AZjT2JWlv$bb6dd197cecf17f0ca5bd0f82f78ff84210831e4a6f356abeea4747f2794b222"}]
    for user in lst_users:
        if username == user['name']:
            return user['pwd']
        else:
            return None

app = Flask(__name__)

# j'authorise les requêtes http depuis n'importe quel nom de domaine
CORS(app)



@app.route('/', methods=['GET'])
def index():
    model = {'message':"mon api fonctionne",
        'status': 200}
    return jsonify(model)

# ici j'utilise "generate_password_hash" avec un hashage en sha256 pour mon pwd lors de sa création
# pour mon id_user j'utilise un uuid pour générer un id aléatoire pour éviter les attaques de bots qui pourraient
# boucler sur une requète delete avec une variable iterative, exemple d'id généré "12eb7b9d-0818-465c-a50a-0cf98db5e9f4" 
@app.route('/create', methods=['POST'])
def create():
    data = request.get_json()
    print(data['password'])
    hash_pass = generate_password_hash(data['password'], method='sha256')
    print(hash_pass)
    id_user = str(uuid.uuid4())
    print(id_user)

    model = {'message':"user créé",
            'status': 200}

    return jsonify(model)


# ici je check si mon user existe et si le pwd qu'il a transmis correspond à celui en BDD avec la méthode "check_password_hash"
# ensuite je génére un token avec un id, une date d'expiration et ma secret key, que je renvoie pour être sauvegardé dans
# les prochaines requètes de mon user
@app.route('/authenticate', methods=['POST'])
def authenticate():
    data = request.get_json()
    pwdUser = getUser(data['id'])
    print(request.headers)
    if pwdUser:
        if check_password_hash(pwdUser, data['password']):
            token = jwt.encode({"id":data['id'], "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=5)}, SECRET_KEY)
            model = {'message' : "ok identification", 'token': token.decode('UTF-8'), 'status':200}
            return jsonify(model)

    model = {'message':"pas de user trouvé",
            'status': 404}
    return jsonify(model)

@app.route('/test', methods=['GET'])
def test():
    model = {'message':"une super réponse",
        'status': 200}
    return jsonify(model)

@app.route('/config', methods=['GET'])
def config():
    model = {"configs":[
                {"id":"1",'name': 'config1'},
                {"id":"2",'name': 'config2'}],
            'status': 200}
    return jsonify(model)

# ici je récupère juste le fichier envoyé par mon front pour ensuite le stocker dans le dossier static
@app.route('/file', methods=['POST'])
def file():
    print(request.headers['Authorization'])
    file = request.files['file']
    file.save(os.path.join("static", file.filename))
    model = {'message':"fichier reçu",
        'status': 200}
    return jsonify(model)

################################ MAIN ############################################

if __name__ == "__main__":
    app.run()