import sys
import io
import os
from flask import Flask, redirect, url_for, render_template, request, send_file

app = Flask(__name__)

PEOPLE_FOLDER = os.path.join('static', 'images')

TATTOO_PHOTOS = os.path.join('static', 'tattoo_showcase')

app.config['Profile_Photos'] = PEOPLE_FOLDER
app.config['tattoo'] = TATTOO_PHOTOS

@app.route("/")
def home():
	return render_template("index.html")

@app.route("/index")
def return_home():
	return render_template("index.html")

@app.route("/location")
def location():
	return render_template("location.html")

@app.route("/artists")
def artists():
	return render_template("artists.html")

@app.route("/store")
def store():
	return render_template("store.html")

@app.route("/usr_acc")
def account():
	return render_template("usr_acc.html")

@app.route("/usr_log")
def loggin():
	return render_template("loggin.html")

@app.route("/accCreation")
def accCreation():
	return render_template("accCreation.html")

@app.route("/brittany")
def Brittany_bio():
	Profile  = os.path.join(app.config['Profile_Photos'], 'brittany.jpg')
	SLIDER_1 = os.path.join(app.config['tattoo'], 'brit1.jpg')
	SLIDER_2 = os.path.join(app.config['tattoo'], 'brit2.jpg')
	SLIDER_3 = os.path.join(app.config['tattoo'], 'brit3.jpg')
	SLIDER_4 = os.path.join(app.config['tattoo'], 'brit4.jpg')

	NAME = "Brittany Hinkel"
	BOOKER = "brittany/book"
	URL = "https://calendar.google.com/calendar/embed?src=forthewubwubs%40gmail.com&ctz=America%2FLos_Angeles"
	IG_URL = "NONE"

	with open('templates/bios/brittany.txt', 'r') as f:
		return render_template('art_bios.html', BOOKER = BOOKER, text=f.read(), user_image = Profile, NAME = NAME, URL = URL , IG_URL = IG_URL, SLIDER_1 = SLIDER_1, SLIDER_2 = SLIDER_2, SLIDER_3 = SLIDER_3, SLIDER_4 = SLIDER_4)

@app.route("/brandy")
def Brandy_bio():
	Profile  = os.path.join(app.config['Profile_Photos'], 'brandy.jpg')
	SLIDER_1 = os.path.join(app.config['tattoo'], 'bran1.jpg')
	SLIDER_2 = os.path.join(app.config['tattoo'], 'bran2.jpg')
	SLIDER_3 = os.path.join(app.config['tattoo'], 'bran3.jpg')
	SLIDER_4 = os.path.join(app.config['tattoo'], 'bran4.jpg')

	NAME = "Brandy Hinkel"
	BOOKER = "brandy/book"
	URL = "https://calendar.google.com/calendar/embed?src=forthewubwubs%40gmail.com&ctz=America%2FLos_Angeles"
	IG_URL = "https://www.instagram.com/voovootattoo/"

	with open('templates/bios/brandy.txt', 'r') as f:
		return render_template('art_bios.html', BOOKER = BOOKER, text=f.read(), user_image = Profile, NAME = NAME, URL = URL , IG_URL = IG_URL, SLIDER_1 = SLIDER_1, SLIDER_2 = SLIDER_2, SLIDER_3 = SLIDER_3, SLIDER_4 = SLIDER_4)

@app.route("/faith")
def Faith_bio():
	Profile  = os.path.join(app.config['Profile_Photos'], 'faith.jpg')
	SLIDER_1 = os.path.join(app.config['tattoo'], 'fait1.jpg')
	SLIDER_2 = os.path.join(app.config['tattoo'], 'fait2.jpg')
	SLIDER_3 = os.path.join(app.config['tattoo'], 'fait3.jpg')
	SLIDER_4 = os.path.join(app.config['tattoo'], 'fait4.jpg')

	NAME = "Faith G-Brown"
	BOOKER = "faith/book"
	URL = "https://calendar.google.com/calendar/embed?src=forthewubwubs%40gmail.com&ctz=America%2FLos_Angeles"
	IG_URL = "https://www.instagram.com/faithgbrown/"

	with open('templates/bios/faith.txt', 'r') as f:
		return render_template('art_bios.html', BOOKER = BOOKER, text=f.read(), user_image = Profile, NAME = NAME, URL = URL , IG_URL = IG_URL, SLIDER_1 = SLIDER_1, SLIDER_2 = SLIDER_2, SLIDER_3 = SLIDER_3, SLIDER_4 = SLIDER_4)

@app.route("/chelsea")
def Chelsea_bio():
	Profile  = os.path.join(app.config['Profile_Photos'], 'chelsea.jpg')
	SLIDER_1 = os.path.join(app.config['tattoo'], 'chel1.jpg')
	SLIDER_2 = os.path.join(app.config['tattoo'], 'chel2.jpg')
	SLIDER_3 = os.path.join(app.config['tattoo'], 'chel3.jpg')
	SLIDER_4 = os.path.join(app.config['tattoo'], 'chel4.jpg')

	NAME = "Chelsea Bouge"
	BOOKER = "chelsea/book"
	URL = "https://calendar.google.com/calendar/embed?src=forthewubwubs%40gmail.com&ctz=America%2FLos_Angeles"
	IG_URL = "https://www.instagram.com/damn_chelsea/"

	with open('templates/bios/chelsea.txt', 'r') as f:
		return render_template('art_bios.html', BOOKER = BOOKER, text=f.read(), user_image = Profile, NAME = NAME, URL = URL , IG_URL = IG_URL, SLIDER_1 = SLIDER_1, SLIDER_2 = SLIDER_2, SLIDER_3 = SLIDER_3, SLIDER_4 = SLIDER_4)

@app.route("/deshawn")
def Deshawn_bio():
	Profile  = os.path.join(app.config['Profile_Photos'], 'deshawn.jpg')
	SLIDER_1 = os.path.join(app.config['tattoo'], 'desh1.jpg')
	SLIDER_2 = os.path.join(app.config['tattoo'], 'desh2.jpg')
	SLIDER_3 = os.path.join(app.config['tattoo'], 'desh3.jpg')
	SLIDER_4 = os.path.join(app.config['tattoo'], 'desh4.jpg')

	NAME = "Deshawn Harris"
	BOOKER = "deshawn/book"
	URL = "https://calendar.google.com/calendar/embed?src=forthewubwubs%40gmail.com&ctz=America%2FLos_Angeles"
	IG_URL = "https://www.instagram.com/religiontattoo/"

	with open('templates/bios/deshawn.txt', 'r') as f:
		return render_template('art_bios.html', BOOKER = BOOKER, text=f.read(), user_image = Profile, NAME = NAME, URL = URL , IG_URL = IG_URL, SLIDER_1 = SLIDER_1, SLIDER_2 = SLIDER_2, SLIDER_3 = SLIDER_3, SLIDER_4 = SLIDER_4)

@app.route("/tonya")
def Tonya_bio():
	Profile  = os.path.join(app.config['Profile_Photos'], 'tonya.jpg')
	SLIDER_1 = os.path.join(app.config['tattoo'], 'tony1.jpg')
	SLIDER_2 = os.path.join(app.config['tattoo'], 'tony2.jpg')
	SLIDER_3 = os.path.join(app.config['tattoo'], 'tony3.jpg')
	SLIDER_4 = os.path.join(app.config['tattoo'], 'tony4.jpg')

	NAME = "Tonya Fred"
	BOOKER = "tonya/book"
	URL = "https://calendar.google.com/calendar/embed?src=forthewubwubs%40gmail.com&ctz=America%2FLos_Angeles"
	IG_URL = "https://www.instagram.com/just_here_nor_there/"

	with open('templates/bios/tonya.txt', 'r') as f:
		return render_template('art_bios.html', BOOKER = BOOKER, text=f.read(), user_image = Profile, NAME = NAME, URL = URL , IG_URL = IG_URL, SLIDER_1 = SLIDER_1, SLIDER_2 = SLIDER_2, SLIDER_3 = SLIDER_3, SLIDER_4 = SLIDER_4)

@app.route("/brittany/book")
def brit_book():
	URL = "https://calendar.google.com/calendar/embed?src=v4abul3afsp63isgbvdhkud4u4%40group.calendar.google.com&ctz=America%2FLos_Angeles"
	return render_template('booker.html', URL = URL)

@app.route("/brandy/book")
def bran_book():
	return render_template('booker.html')

@app.route("/faith/book")
def fait_book():
	return render_template('booker.html')

@app.route("/chelsea/book")
def chel_book():
	return render_template('booker.html')

@app.route("/deshawn/book")
def desh_book():
	return render_template('booker.html')

@app.route("/tonya/book")
def tony_book():
	return render_template('booker.html')
















if __name__ == "__main__":
	app.run(debug=True)