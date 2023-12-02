from flask import Flask,render_template,request

app=Flask(__name__)

@app.route('/')
def index():
    courses = ["Python","C","C#","JAVA"]
    is_logged_in = True
    return render_template("index.html", courses=courses, is_logged_in=is_logged_in)

@app.route('/<name>')
def a(name):
    return f'<h1>THIS IS AWESOME {name}<h1>' 

@app.route('/user/<name>')
def user(name):
    fruits = ["apple","banana","orange"]
    return render_template("user.html", user_name=name, fruits=fruits)


@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/register')
def demo():
    return render_template("register.html")

@app.route("/confim", methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        n = request.form.get('name')
        a = request.form.get('age')
        c = request.form.get('city')
        return  render_template('confirm.html',name=n,age=a,city=c)




if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0',port=80)