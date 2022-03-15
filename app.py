from flask import *

app = Flask(__name__,template_folder='template',static_folder='static')





@app.route("/")
def LandingPage():
    return render_template('LandingPage.html')


@app.route("/main")
def Main():
    return render_template('MainPage.html')


@app.route("/about")
def AboutPage():
    return render_template('About.html')


@app.route("/generate")
def GenerateCode():
    return render_template('GenerateCode.html')


@app.route("/verify")
def Verify():
    return render_template('VerifyCode.html')







if __name__ == "__main__":
    app.run(debug=True)