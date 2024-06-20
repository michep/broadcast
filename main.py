import json
import platform
from flask import Flask, Response
from dotenv import load_dotenv

from api.templates import bp as temapltes_bp
from api.hc import bp as hc_bp


plat = platform.system()

if plat =='Linux':
    load_dotenv('.env.linux')
elif plat == 'Windows':
    load_dotenv('.env.windows')
else:
    load_dotenv()

app = Flask(__name__)
# app.config['DEBUG'] = True

@app.errorhandler(Exception)
def handle_error(e: Exception):
    return Response(response=json.dumps(e.args), status=500, mimetype='application/json')

app.register_blueprint(temapltes_bp)
app.register_blueprint(hc_bp)


if __name__ == '__main__':
    app.run('0.0.0.0', port='8083')
