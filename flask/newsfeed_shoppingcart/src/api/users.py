from flask import Blueprint, jsonify, abort, request
from ..models import User, db, Account, Admin,Order,order_category,Category
import hashlib
import secrets

"""
def
scramble(password: str):
    Hash and salt the given password
    #salt = secrets.token_hex(16)
    return hashlib.sha512((password + salt).encode('utf-8')).hexdigest()
"""

bp = Blueprint('users', __name__, url_prefix='/users')


@bp.route('', methods=['GET']) # decorator takes path and list of HTTP verbs

def index():
    users = User.query.all()  # ORM performs SELECT query
    usr_result = []
    for usr in users:
        usr_result.append(usr.serialize())
        #print(usr_result)
    return jsonify(usr_result) # return JSON response


@bp.route('/<int:id>', methods=['GET'])
def show(id: int):
    usr = User.query.get_or_404(id)
    return jsonify(usr.serialize()) 


