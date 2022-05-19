from flask import Flask, render_template, make_response, request, jsonify
from settings import *

from blueprint import bp

app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)

app.register_blueprint(bp, url_prefix="/")

if __name__ == '__main__':
    app.run(debug=True)
