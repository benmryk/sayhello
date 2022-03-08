from flask import Flask,render_template,redirect,request,flash,url_for

app = Flask(__name__)
app.secret_key = "qwertyuiopp"

@app.route('/')
def home():
    return redirect(url_for('index'))

@app.route('/hello',methods = ['POST','GET'])
def index():
    if request.method == "POST":
        msg = request.form['name_input']
        flash('Hi '+ str(request.form['name_input'])+', great to see you!')
        return render_template('index.html',msg = msg)
    else:
        flash("Whats your name?")
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug = True)