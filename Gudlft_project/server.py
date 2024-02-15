import json
from flask import Flask,render_template,request,redirect,flash,url_for


def loadClubs():
    """
    Load the clubs from the 'clubs.json' file and return the list of clubs.
    If the file is not found or cannot be decoded as JSON, an empty list is returned.
    """
    try:
        with open('clubs.json') as clubs:
            listOfClubs = json.load(clubs)['clubs']
            return listOfClubs
    except (FileNotFoundError, json.JSONDecodeError) as e: 
        print(e)
        return []

def loadCompetitions():
    """
    Load competitions from the 'competitions.json' file and return a list of competitions.
    If the file is not found or cannot be decoded as JSON, an empty list is returned.
    """
    try:
        with open('competitions.json') as comps:
            listOfCompetitions = json.load(comps)['competitions']
            return listOfCompetitions
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(e)
        return []

def saveData(filename, data):
    """
    Save data to a JSON file.

    Parameters:
    filename (str): The name of the file to save to.
    data (list): The data to save.
    """
    with open(filename, 'w') as file:
        json.dump({'clubs': data} if filename == 'clubs.json' else {'competitions': data}, file)

def find_item_by_attribute(items, attribute, value):
    """
    Find an item (club or competition) in a list of dictionaries by a given attribute (name or email).

    Parameters:
    items (list): The list of items (clubs and competitions dictionaries).
    attribute (str): The attribute to search by (club's of competition's name or club's email).
    value (str): The value of the attribute to find.

    Returns:
    dict: The first item that matches the attribute value, or None if no item is found.
    """
    return next((item for item in items if item[attribute] == value), None)


app = Flask(__name__)
app.secret_key = 'something_special'


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/showSummary',methods=['POST'])
def showSummary():

    clubs = loadClubs()
    competitions = loadCompetitions()
    
    club = find_item_by_attribute(clubs, 'email', request.form['email'])
    #club = [club for club in clubs if club['email'] == request.form['email']][0]
    
    return render_template('welcome.html',club=club,competitions=competitions)


@app.route('/book/<competition>/<club>')
def book(competition,club):

    clubs = loadClubs()
    competitions = loadCompetitions()

    foundClub = find_item_by_attribute(clubs, 'name', club)
    #foundClub = [c for c in clubs if c['name'] == club][0]

    foundCompetition = find_item_by_attribute(competitions, 'name', competition)
    #foundCompetition = [c for c in competitions if c['name'] == competition][0]
    
    if foundClub and foundCompetition:
        return render_template('booking.html',club=foundClub,competition=foundCompetition)
    else:
        flash("Something went wrong-please try again")
        return render_template('welcome.html', club=club, competitions=competitions)


@app.route('/purchasePlaces',methods=['POST'])
def purchasePlaces():

    clubs = loadClubs()
    competitions = loadCompetitions()
    print("Loaded clubs:", clubs)  # Debug print statement
    print("Loaded competitions:", competitions)  # Debug print statement
    
    # Error handling if the clubs or competitions data are not in conformity.
    try:
        competition = find_item_by_attribute(competitions, 'name', request.form['competition'])
        #competition = [c for c in competitions if c['name'] == request.form['competition']][0]
        
        club = find_item_by_attribute(clubs, 'name', request.form['club'])
        #club = [c for c in clubs if c['name'] == request.form['club']][0]
    
    except KeyError:
        print("KeyError:", e)  # Debug print statement       
        flash("Invalid form data. Please try again.")
        return redirect(url_for('index'))
    
    print("Competition:", competition)  # Debug print statement
    print("Club:", club)  # Debug print statement
    
    # If the club or the competition is not found in the database.
    if not competition or not club:
        flash("Club or Competition not found")
        return render_template('welcome.html', club=club, competitions=competitions)

    # Error handling if the number of places required is not a number.
    try:
        placesRequired = int(request.form['places'])
    
    except ValueError:
        flash("Invalid value for number of places required. Please try again.")
        return redirect(url_for('book', competition=competition['name'], club=club['name']))

    # Error handling if the number of club's points is not enough for the number of places required.
    if placesRequired > 12:
        flash("You cannot book more than 12 places per competition. Please try again.")
        return redirect(url_for('book', competition=competition['name'], club=club['name']))

    # Error handling if the number of club's points is not enough for the number of places required.
    if placesRequired > int(club['points']):
        flash("Not enough points Available to the club. Please try again.")
        return redirect(url_for('book', competition=competition['name'], club=club['name']))

    # Error handling if the number of competition's available places is not enough for the number of places required.
    if placesRequired > int(competition['numberOfPlaces']):
        flash("Not enough places available in the competition. Please try again.")
        return redirect(url_for('book', competition=competition['name'], club=club['name']))
    
    # Deducting places from the competition
    competition['numberOfPlaces'] = int(competition['numberOfPlaces']) - placesRequired
    # Save the updated competitions back to the JSON files
    saveData('competitions.json', competitions)

    # Deducting points from the club
    club['points'] = int(club['points']) - placesRequired
    # Save the updated clubs back to the JSON files
    saveData('clubs.json', clubs)



    print("Data SAVED")  # Debug print statement    
    flash('Great-booking complete!')
    return render_template('welcome.html', club=club, competitions=competitions)


# TODO: Add route for points display


@app.route('/logout')
def logout():
    return redirect(url_for('index'))
