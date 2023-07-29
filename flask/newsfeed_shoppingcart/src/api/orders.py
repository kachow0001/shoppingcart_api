from flask import Blueprint, jsonify, abort, request
from ..models import User, db, Account, Admin,Order,order_category,Category

bp = Blueprint('orders', __name__, url_prefix='/orders')


@bp.route('/',methods=['GET'])

def order_details():
    orders = Order.query.all()
    od_result = []
    for od in orders:
        print(od)
        od_result.append(od.serialize())
    return jsonify(od_result)   


@bp.route('', methods=['POST'])
def create():
    # req body must contain user_id and content
    if 'user_id' not in request.json or 'order details' not in request.json:
        return abort(400)
    # user with id of user_id must exist
    Order.query.get_or_404(request.json['user_id'])
    # construct orderdetails
    o = Order(
        user_id=request.json['user_id'],
        =request.json['quantity'],
    )
    db.session.add(o) # prepare CREATE statement
    db.session.commit() # execute CREATE statement
    return jsonify(o.serialize())


@bp.route('/<int:id>', methods=['DELETE'])
def delete(id: int):
    od = Order.query.get_or_404(id)
    try:
        db.session.delete(od)  # prepare DELETE statement
        db.session.commit()  # execute DELETE statement
        return jsonify(True)
    except:
        # something went wrong :(
        return jsonify(False)




