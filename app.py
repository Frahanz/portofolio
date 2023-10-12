import os
from os.path import join, dirname
from dotenv import load_dotenv
from flask import Flask,render_template,request,jsonify

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

app=Flask(__name__)
@app.route('/',methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/about',methods=['GET'])
def about():
    return render_template('about.html')

@app.route('/info',methods=['GET'])
def info():
    portofolio = request.args.get('portofolio')
    print(portofolio)
    return jsonify({
        'msg' : 'GET Info'
    })

if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)