from flask import Flask, render_template, jsonify, redirect
import yaml
import os
import optparse

developer = os.getenv("DEVELOPER", "User")
environment = os.getenv("ENVIRONMENT", "development")

app = Flask(__name__)

info = yaml.load(open('info.yml', 'r'))
infoAc = yaml.load(open('infoA.yml', 'r'))
infoExp = yaml.load(open('infoEXP.yml', 'r'))

@app.route('/info')
def hello_world():
    return jsonify(info)


@app.route('/')
def index():
    #return render_template('index.html')
    return render_template("index.html", info=info['info'], developer=developer, infoAc=infoAc['infoA'], infoExp=infoExp['infoExp'])


@app.route('/about', methods=['GET', 'POST'])
def about():
    
    return redirect("http://localhost:5000/#about")
    #return render_template("about.html", info=info['info'])


@app.route('/academic', methods=['GET'])
def aca():

    return redirect("http://localhost:5000/#academic")


@app.route('/work', methods=['GET'])
def work():

    return redirect("http://localhost:5000/#Work")

if __name__ == '__main__':
  app.run(host="0.0.0.0", debug=True)
