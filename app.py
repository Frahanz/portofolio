from flask import Flask,render_template,request,jsonify

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