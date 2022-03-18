'''
This Project is Made by Team-Ignite for Smart India Hackathon (SIH).
Topic : Digital Access Code generation and use for address tracking - AK1207 - 425 (Software).
'''


# Imports for WebApp
from flask import *

# Importing geopy library (For Coordinates)
from geopy.geocoders import Nominatim


# Global Variables
GENERATED = False




app = Flask(__name__,template_folder='template',static_folder='static')


# Function which takes Address and Gives Coordinates

def findcoordinates(address):

    loc = Nominatim(user_agent="GetLoc")
    getLoc = loc.geocode(address)
    # print(getLoc.address)
    # print("Latitude = ", getLoc.latitude, "\n")
    # print("Longitude = ", getLoc.longitude)

    return getLoc.address,getLoc.latitude,getLoc.longitude









@app.route("/")
def LandingPage():
    return render_template('LandingPage.html')


@app.route("/main")
def Main():
    return render_template('MainPage.html', generated = GENERATED)


@app.route("/about")
def AboutPage():
    return render_template('About.html')


@app.route("/generate", methods=['GET', 'POST'])
def GenerateCode():
    global GENERATED

    if request.method == "POST":
        GENERATED = True
        flat_building = str(request.form['flat_building'])
        street = str(request.form['street'])
        city = str(request.form['city'])
        state = str(request.form['state'])
        country = str(request.form['country'])
        pincode = str(request.form['pincode'])

        # print(flat_building)
        # print(street)
        # print(city)
        # print(state)
        # print(country)
        # print(pincode)

        # This Address dosent contain flat and Building
        address = str(street + ',' + city + ',' + country + ',' + pincode)
        print(address)

        a,b,c = findcoordinates(address)
        print(a,b,c)

        return render_template('GenerateCode.html', generated = GENERATED, global_address = a, latitude_generated = b, longitude_generated = c)

        


    GENERATED = False
    return render_template('GenerateCode.html', generated = GENERATED)


@app.route("/verify")
def Verify():
    return render_template('VerifyCode.html')







if __name__ == "__main__":
    app.run(debug=True)