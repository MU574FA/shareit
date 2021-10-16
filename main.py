import os
from sys import argv
from pathlib import Path
from waitress import serve
from flask import Flask, request, render_template, send_file, redirect


basedir   = Path(__file__).parent
filespath = os.path.join(basedir, "files")
host      = "0.0.0.0"
port      = 8000

app = Flask(__name__)

@app.route("/", methods=['GET'])
def home():
    context = {}
    context['files'] = os.listdir(filespath)
    return render_template("index.html", context=context)


@app.route("/", methods=['POST'])
def share():
    file = request.files.get("file")
    try:
        path = os.path.join(filespath, file.filename)
        file.save(path)
    except Exception as e:
        return str(e)
    return redirect("/")


@app.route("/download/<file>/", methods=['GET'])
def download(file):
    path = os.path.join(filespath, file)
    return send_file(path)


# @app.route("/delete/<file>/", methods=['GET'])
# def delete(file):
#     path = os.path.join(filespath, file)
#     os.remove(path)
#     return redirect("/")




if __name__ == "__main__":
    if argv[-1] == "debug": 
        app.run(debug=True, host=host, port=port)
    else:
        print("Serving...")
        serve(app, host=host, port=port)
    