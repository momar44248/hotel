import csv
from flask import Flask, render_template

app = Flask(__name__)

def get_rooms_from_csv(filename='rooms.csv'):
    rooms = []
    with open(filename, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        # Supposer que la première ligne est l'en-tête (headers)
        headers = next(reader) 
        for row in reader:
            # Crée un dictionnaire pour chaque ligne pour un accès plus facile
            room_dict = dict(zip(headers, row))
            rooms.append(room_dict)
    return rooms

@app.route('/')
def home():
    # Récupère la liste des chambres sous forme de dictionnaires
    all_rooms = get_rooms_from_csv()
    # Passe les données au template HTML
    return render_template('hotel_base.html', rooms=all_rooms)
