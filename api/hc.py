from flask import Blueprint, jsonify, request

from services.broadcast import generate

bp = Blueprint('hc', __name__, url_prefix='/hc')


@bp.route('', methods=['GET'])
def getHealthCheck():
    return jsonify('ok')
