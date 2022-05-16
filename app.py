from flask import Flask, render_template, make_response, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return 'Aplicação rodando'

if __name__ == '__main__':
    app.run(debug=True)
