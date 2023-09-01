import os
from flask import Blueprint, jsonify, request

from services.broadcast import generate

bp = Blueprint('templates', __name__, url_prefix='/templates')


@bp.route('', methods=['GET'])
def getTemplatesList():
    TEMPLATESDIR = os.getenv('TEMPLATESDIR')
    res = []
    with os.scandir(TEMPLATESDIR) as entries:
        for entry in entries:
            if entry.is_dir:
                res.append(entry.name)

    return jsonify(res)


@bp.route('/<template>', methods=['POST'])
def generateTemplate(template: str):
    return jsonify(generate(template, request.json['title'], request.json['message']))
