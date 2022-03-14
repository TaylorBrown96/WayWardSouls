import sys
import io
import os
from flask import Flask, redirect, url_for, render_template, request, send_file
from markupsafe import Markup

app = Flask(__name__)
basepath = os.path.abspath("/home/TaylorBrown1996/mysite/templates")

PEOPLE_FOLDER = os.path.join('static', 'images')

TATTOO_PHOTOS = os.path.join('static', 'tattoo_showcase')


app.config['Profile_Photos'] = PEOPLE_FOLDER
app.config['tattoo'] = TATTOO_PHOTOS


Form_op_Bran =Markup("""<option>Choose...</option>
						<option selected>Brandy Hinkel AKA"VooVoo" (Tattoo Artist)</option>
						<option>Brittany Hinkel (Tattoo Artist)</option>
						<option>Faith G-Brown (Tattoo Artist)</option>
						<option>Chelsea Bogue (Tattoo Artist)</option>
						<option>DeShawn Harris (Tattoo Apprentice)</option>
						<option>Tonya Fred (Piercer)</option>""")

Form_op_Brit =Markup("""<option>Choose...</option>
						<option>Brandy Hinkel AKA"VooVoo" (Tattoo Artist)</option>
						<option selected>Brittany Hinkel (Tattoo Artist)</option>
						<option>Faith G-Brown (Tattoo Artist)</option>
						<option>Chelsea Bogue (Tattoo Artist)</option>
						<option>DeShawn Harris (Tattoo Apprentice)</option>
						<option>Tonya Fred (Piercer)</option>""")

Form_op_Fait =Markup("""<option>Choose...</option>
						<option>Brandy Hinkel AKA"VooVoo" (Tattoo Artist)</option>
						<option>Brittany Hinkel (Tattoo Artist)</option>
						<option selected>Faith G-Brown (Tattoo Artist)</option>
						<option>Chelsea Bogue (Tattoo Artist)</option>
						<option>DeShawn Harris (Tattoo Apprentice)</option>
						<option>Tonya Fred (Piercer)</option>""")

Form_op_Chel =Markup("""<option>Choose...</option>
						<option>Brandy Hinkel AKA"VooVoo" (Tattoo Artist)</option>
						<option>Brittany Hinkel (Tattoo Artist)</option>
						<option>Faith G-Brown (Tattoo Artist)</option>
						<option selected>Chelsea Bogue (Tattoo Artist)</option>
						<option>DeShawn Harris (Tattoo Apprentice)</option>
						<option>Tonya Fred (Piercer)</option>""")

Form_op_Desh =Markup("""<option>Choose...</option>
						<option>Brandy Hinkel AKA"VooVoo" (Tattoo Artist)</option>
						<option>Brittany Hinkel (Tattoo Artist)</option>
						<option>Faith G-Brown (Tattoo Artist)</option>
						<option>Chelsea Bogue (Tattoo Artist)</option>
						<option selected>DeShawn Harris (Tattoo Apprentice)</option>
						<option>Tonya Fred (Piercer)</option>""")

Form_op_Tony =Markup("""<option>Choose...</option>
						<option>Brandy Hinkel AKA"VooVoo" (Tattoo Artist)</option>
						<option>Brittany Hinkel (Tattoo Artist)</option>
						<option>Faith G-Brown (Tattoo Artist)</option>
						<option>Chelsea Bogue (Tattoo Artist)</option>
						<option>DeShawn Harris (Tattoo Apprentice)</option>
						<option selected>Tonya Fred (Piercer)</option>""")

@app.route("/")
def home():
	return render_template("index.html")

@app.route("/home")
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

@app.route("/success")
def success():
    return render_template("success.html")

@app.route("/brittany")
def Brittany_bio():
	Profile  = os.path.join(app.config['Profile_Photos'], 'brittany.jpg')
	SLIDER_1 = os.path.join(app.config['tattoo'], 'Brittany1.jpg')
	SLIDER_2 = os.path.join(app.config['tattoo'], 'Brittany2.jpg')
	SLIDER_3 = "NONE" #os.path.join(app.config['tattoo'], 'Brittany3.jpg')
	SLIDER_4 = "NONE" #os.path.join(app.config['tattoo'], 'Brittany4.jpg')
	SLIDER_5 = "NONE" #os.path.join(app.config['tattoo'], 'Brittany5.jpg')
	SLIDER_6 = "NONE" #os.path.join(app.config['tattoo'], 'Brittany6.jpg')
	SLIDER_7 = "NONE" #os.path.join(app.config['tattoo'], 'Brittany7.jpg')
	SLIDER_8 = "NONE" #os.path.join(app.config['tattoo'], 'Brittany8.jpg')
	SLIDER_9 = "NONE" #os.path.join(app.config['tattoo'], 'Brittany9.jpg')
	SLIDER_10 = "NONE" #os.path.join(app.config['tattoo'], 'Brittany10.jpg')


	NAME = "Brittany Hinkel"
	BOOKER = "brittany/book"
	IG_URL = "NONE"

	with open(basepath + '/bios/brittany.txt', 'r') as f:
		BIO = f.read()

	return render_template('art_bios.html',
		BOOKER = BOOKER,
		text = BIO,
		user_image = Profile,
		NAME = NAME,
		IG_URL = IG_URL,

		SLIDER_1 = SLIDER_1,
		SLIDER_2 = SLIDER_2,
		SLIDER_3 = SLIDER_3,
		SLIDER_4 = SLIDER_4,
		SLIDER_5 = SLIDER_5,
		SLIDER_6 = SLIDER_6,
		SLIDER_7 = SLIDER_7,
		SLIDER_8 = SLIDER_8,
		SLIDER_9 = SLIDER_9,
		SLIDER_10 = SLIDER_10)

@app.route("/brandy")
def Brandy_bio():
	Profile  = os.path.join(app.config['Profile_Photos'], 'brandy.jpg')
	SLIDER_1 = os.path.join(app.config['tattoo'], 'Brandy1.jpg')
	SLIDER_2 = os.path.join(app.config['tattoo'], 'Brandy2.jpg')
	SLIDER_3 = "NONE" #os.path.join(app.config['tattoo'], 'Brandy3.jpg')
	SLIDER_4 = "NONE" #os.path.join(app.config['tattoo'], 'Brandy4.jpg')
	SLIDER_5 = "NONE" #os.path.join(app.config['tattoo'], 'Brandy5.jpg')
	SLIDER_6 = "NONE" #os.path.join(app.config['tattoo'], 'Brandy6.jpg')
	SLIDER_7 = "NONE" #os.path.join(app.config['tattoo'], 'Brandy7.jpg')
	SLIDER_8 = "NONE" #os.path.join(app.config['tattoo'], 'Brandy8.jpg')
	SLIDER_9 = "NONE" #os.path.join(app.config['tattoo'], 'Brandy9.jpg')
	SLIDER_10 = "NONE" #os.path.join(app.config['tattoo'], 'Brandy10.jpg')

	NAME = "Brandy Hinkel"
	BOOKER = "brandy/book"
	IG_URL = "https://www.instagram.com/voovootattoo/"

	with open(basepath + '/bios/brandy.txt', 'r') as f:
		BIO = f.read()

	return render_template('art_bios.html',
		BOOKER = BOOKER,
		text = BIO,
		user_image = Profile,
		NAME = NAME,
		IG_URL = IG_URL,

		SLIDER_1 = SLIDER_1,
		SLIDER_2 = SLIDER_2,
		SLIDER_3 = SLIDER_3,
		SLIDER_4 = SLIDER_4,
		SLIDER_5 = SLIDER_5,
		SLIDER_6 = SLIDER_6,
		SLIDER_7 = SLIDER_7,
		SLIDER_8 = SLIDER_8,
		SLIDER_9 = SLIDER_9,
		SLIDER_10 = SLIDER_10)

@app.route("/faith")
def Faith_bio():
	Profile  = os.path.join(app.config['Profile_Photos'], 'faith.jpg')
	SLIDER_1 = os.path.join(app.config['tattoo'], 'Faith1.jpg')
	SLIDER_2 = os.path.join(app.config['tattoo'], 'Faith2.jpg')
	SLIDER_3 = "NONE" #os.path.join(app.config['tattoo'], 'Faith3.jpg')
	SLIDER_4 = "NONE" #os.path.join(app.config['tattoo'], 'Faith4.jpg')
	SLIDER_5 = "NONE" #os.path.join(app.config['tattoo'], 'Faith5.jpg')
	SLIDER_6 = "NONE" #os.path.join(app.config['tattoo'], 'Faith6.jpg')
	SLIDER_7 = "NONE" #os.path.join(app.config['tattoo'], 'Faith7.jpg')
	SLIDER_8 = "NONE" #os.path.join(app.config['tattoo'], 'Faith8.jpg')
	SLIDER_9 = "NONE" #os.path.join(app.config['tattoo'], 'Faith9.jpg')
	SLIDER_10 = "NONE" #os.path.join(app.config['tattoo'], 'Faith10.jpg')

	NAME = "Faith G-Brown"
	BOOKER = "faith/book"
	IG_URL = "https://www.instagram.com/faithgbrown/"

	with open(basepath + '/bios/faith.txt', 'r') as f:
		BIO = f.read()

	return render_template('art_bios.html',
		BOOKER = BOOKER,
		text = BIO,
		user_image = Profile,
		NAME = NAME,
		IG_URL = IG_URL,

		SLIDER_1 = SLIDER_1,
		SLIDER_2 = SLIDER_2,
		SLIDER_3 = SLIDER_3,
		SLIDER_4 = SLIDER_4,
		SLIDER_5 = SLIDER_5,
		SLIDER_6 = SLIDER_6,
		SLIDER_7 = SLIDER_7,
		SLIDER_8 = SLIDER_8,
		SLIDER_9 = SLIDER_9,
		SLIDER_10 = SLIDER_10)

@app.route("/chelsea")
def Chelsea_bio():
	Profile  = os.path.join(app.config['Profile_Photos'], 'chelsea.jpg')

	SLIDER_1 = os.path.join(app.config['tattoo'], 'Chelsea1.jpg')
	SLIDER_2 = os.path.join(app.config['tattoo'], 'Chelsea2.jpg')
	SLIDER_3 = "NONE" #os.path.join(app.config['tattoo'], 'Chelsea3.jpg')
	SLIDER_4 = "NONE" #os.path.join(app.config['tattoo'], 'Chelsea4.jpg')
	SLIDER_5 = "NONE" #os.path.join(app.config['tattoo'], 'Chelsea5.jpg')
	SLIDER_6 = "NONE" #os.path.join(app.config['tattoo'], 'Chelsea6.jpg')
	SLIDER_7 = "NONE" #os.path.join(app.config['tattoo'], 'Chelsea7.jpg')
	SLIDER_8 = "NONE" #os.path.join(app.config['tattoo'], 'Chelsea8.jpg')
	SLIDER_9 = "NONE" #os.path.join(app.config['tattoo'], 'Chelsea9.jpg')
	SLIDER_10 = "NONE" #os.path.join(app.config['tattoo'], 'Chelsea10.jpg')

	NAME = "Chelsea Bouge"
	BOOKER = "chelsea/book"
	IG_URL = "https://www.instagram.com/damn_chelsea/"

	with open(basepath + '/bios/chelsea.txt', 'r') as f:
		BIO = f.read()

	return render_template('art_bios.html',
		BOOKER = BOOKER,
		text = BIO,
		user_image = Profile,
		NAME = NAME,
		IG_URL = IG_URL,

		SLIDER_1 = SLIDER_1,
		SLIDER_2 = SLIDER_2,
		SLIDER_3 = SLIDER_3,
		SLIDER_4 = SLIDER_4,
		SLIDER_5 = SLIDER_5,
		SLIDER_6 = SLIDER_6,
		SLIDER_7 = SLIDER_7,
		SLIDER_8 = SLIDER_8,
		SLIDER_9 = SLIDER_9,
		SLIDER_10 = SLIDER_10)

@app.route("/deshawn")
def Deshawn_bio():
	Profile  = os.path.join(app.config['Profile_Photos'], 'deshawn.jpg')
	SLIDER_1 = os.path.join(app.config['tattoo'], 'DeShawn1.jpg')
	SLIDER_2 = os.path.join(app.config['tattoo'], 'DeShawn2.jpg')
	SLIDER_3 = "NONE" #os.path.join(app.config['tattoo'], 'DeShawn3.jpg')
	SLIDER_4 = "NONE" #os.path.join(app.config['tattoo'], 'DeShawn4.jpg')
	SLIDER_5 = "NONE" #os.path.join(app.config['tattoo'], 'DeShawn5.jpg')
	SLIDER_6 = "NONE" #os.path.join(app.config['tattoo'], 'DeShawn6.jpg')
	SLIDER_7 = "NONE" #os.path.join(app.config['tattoo'], 'DeShawn7.jpg')
	SLIDER_8 = "NONE" #os.path.join(app.config['tattoo'], 'DeShawn8.jpg')
	SLIDER_9 = "NONE" #os.path.join(app.config['tattoo'], 'DeShawn9.jpg')
	SLIDER_10 = "NONE" #os.path.join(app.config['tattoo'], 'DeShawn10.jpg')

	NAME = "Deshawn Harris"
	BOOKER = "deshawn/book"
	IG_URL = "https://www.instagram.com/religiontattoo/"

	with open(basepath + '/bios/deshawn.txt', 'r') as f:
		BIO = f.read()

	return render_template('art_bios.html',
		BOOKER = BOOKER,
		text = BIO,
		user_image = Profile,
		NAME = NAME,
		IG_URL = IG_URL,

		SLIDER_1 = SLIDER_1,
		SLIDER_2 = SLIDER_2,
		SLIDER_3 = SLIDER_3,
		SLIDER_4 = SLIDER_4,
		SLIDER_5 = SLIDER_5,
		SLIDER_6 = SLIDER_6,
		SLIDER_7 = SLIDER_7,
		SLIDER_8 = SLIDER_8,
		SLIDER_9 = SLIDER_9,
		SLIDER_10 = SLIDER_10)

@app.route("/tonya")
def Tonya_bio():
	Profile  = os.path.join(app.config['Profile_Photos'], 'tonya.jpg')
	SLIDER = "NONE"

	NAME = "Tonya Fred"
	BOOKER = "tonya/book"
	IG_URL = "https://www.instagram.com/just_here_nor_there/"

	with open(basepath + '/bios/tonya.txt', 'r') as f:
		BIO = f.read()

	return render_template('art_bios.html',
		BOOKER = BOOKER,
		text = BIO,
		user_image = Profile,
		NAME = NAME,
		IG_URL = IG_URL,

		SLIDER_1 = SLIDER)


"""
	For Booking appointments
"""
@app.route("/brittany/book")
def brittany_book():
	return render_template('booker.html', Form = Form_op_Brit)

@app.route("/brandy/book")
def brandy_book():
	return render_template('booker.html', Form = Form_op_Bran)

@app.route("/faith/book")
def faith_book():
	return render_template('booker.html', Form = Form_op_Fait)

@app.route("/chelsea/book")
def chelsea_book():
	return render_template('booker.html', Form = Form_op_Chel)

@app.route("/deshawn/book")
def deshawn_book():
	return render_template('booker.html', Form = Form_op_Desh)

@app.route("/tonya/book")
def tonya_book():
	return render_template('booker.html', Form = Form_op_Tony)

if __name__ == "__main__":
	app.run(debug=True)