from flask import *

app = Flask(__name__,template_folder='template',static_folder='static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')


@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'GET':
        print("This is a GET request")

    elif request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        print(username,password)
        return redirect('/')

    return render_template('form.html')
    


@app.route('/<string:name>')
def namewaalafunction(name):
    print(name)
    return render_template('name.html',name = name, aditya="taaha")

if __name__ == "__main__":
    app.secret_key = "somesecretkey" 
    app.run(debug=True)

