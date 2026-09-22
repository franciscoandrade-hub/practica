from flask import Flask
app = Flask(__name__)

@app.route('/api/status')
def status():
    return {"status": "ok", "entorno": "contenedor-docker", "version": "1.1.0"}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
