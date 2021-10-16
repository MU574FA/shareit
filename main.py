import os
import socket
from sys import argv
from pathlib import Path
from waitress import serve
from functions import make_unique
from flask import Flask, request, render_template, send_file, redirect

# ----- App Settings -----
basedir   = Path(__file__).parent
filespath = os.path.join(basedir, "files")
host      = "0.0.0.0"
port      = 8000
host_name = socket.gethostname()
host_addr = socket.gethostbyname(host_name + ".local")

# ----- Creating the app -----
app = Flask(__name__)


# ----- Home page -----
@app.route("/", methods=['GET'])
def home():
    context = {}
    context['files']       = os.listdir(filespath)
    context['remote_addr'] = request.remote_addr
    context['host_addr']   = host_addr
    return render_template("index.html", context=context)


# ----- Shareing files handler -----
@app.route("/", methods=['POST'])
def share():
    try:
        file          = request.files.get("file")
        files         = os.listdir(filespath)
        file.filename = make_unique(file.filename, files)
        path          = os.path.join(filespath, file.filename)
        file.save(path)
    except Exception as e: return str(e)
    return redirect("/")


# ----- Download files handler -----
@app.route("/download/<file>/", methods=['GET'])
def download(file):
    path = os.path.join(filespath, file)
    return send_file(path)

# ----- Delete files handler -----
@app.route("/delete/<file>/", methods=['GET'])
def delete(file):
    if request.remote_addr == host_addr:
        path = os.path.join(filespath, file)
        os.remove(path)
    return redirect("/")


if __name__ == "__main__":
    if argv[-1] == "debug": 
        app.run(debug=True, host=host, port=port)
    else:
        
        print(f"Serving on http://{host_addr}:{port}")
        serve(app, host=host, port=port)
    