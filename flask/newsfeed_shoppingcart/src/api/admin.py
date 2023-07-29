from flask import Blueprint, jsonify, abort, request
from ..models import User, db, db, Account, Admin,Order,order_category,Category
import hashlib
import secrets

"""
def
scramble(password: str):
    Hash and salt the given password
    #salt = secrets.token_hex(16)
    return hashlib.sha512((password + salt).encode('utf-8')).hexdigest()
"""

bp = Blueprint('admin', __name__, url_prefix='/admins')


@bp.route('', methods=['GET'])  # decorator takes path and list of HTTP verbs
def index():
    admins = Admin.query.all()  # ORM performs SELECT query
    ad_result = []
    for ad in admins:
        print(ad)
        ad_result.append(ad.serialize())
    return jsonify(ad_result)  # return JSON response


# Task2
@bp.route('/<int:id>', methods=['GET'])
def show(id: int):
    ad = Admin.query.get_or_404(id)
    return jsonify(ad.serialize())

"""
# Task4 - POST

@bp.route('', methods=['POST'])
def create():

    # bracket notation to access username and passwword
    username = request.json['username']
    password = request.json['password']
    print("printing", username, password)
    # req body must contain username and password
    if len(username) < 3 or len(password) < 8:
        return abort(400)
    print("helloo")
    # hashed_password = scramble(password)

    # construct User
    usr = User(
        username=username,
        password=password
        # password=hashed_password
    )
    print("userrr" + str(usr))
    db.session.add(usr)  # prepare CREATE statement
    print("user saved")
    db.session.commit()  # execute CREATE statement
    print('jhfkjgluigi')
    return jsonify(usr.serialize())


@bp.route('/<int:id>', methods=['DELETE'])
def delete(id: int):
    usr = User.query.get_or_404(id)
    try:
        db.session.delete(usr)  # prepare DELETE statement
        db.session.commit()  # execute DELETE statement
        return jsonify(True)
    except:
        # something went wrong :(
        return jsonify(False)


@bp.route('/<int:id>', methods=['PATCH', 'PUT'])
def update(id: int):
    
    update() function body, 
    add this code to query for the user record that matches the id
    
    usr = User.query.get_or_404(id)

    if 'username' not in request.json and 'password' not in request.json:
        return abort(400)

    if 'username' in request.json:
        username = request.json['username']
        if len(username) < 3:
            return abort(400)
        usr.username = username

    if 'password' in request.json:
        password = request.json['password']
        if len(password) < 8:
            return abort(400)
        usr.password = scramble(password)

    try:
        db.session.commit()
        return jsonify(usr.serialize())
    except:
        return jsonify(False)


@bp.route('/<int:id>/liked_tweets', methods=['GET'])
def liked_tweets(id: int):
    usr = User.query.get_or_404(id)
    result = []
    for t in usr.liked_tweets:
        result.append(t.serialize())
    return jsonify(result)


    
""" 
