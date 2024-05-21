import requests
import json
import csv
from io import StringIO

# URL de la feuille de calcul Google Sheets au format CSV
SHEET_URL = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vSwN6Ar0wkARcuGgHmsft-hPk2RNtd5QfWQrs8aEQh8Ui00u4Wyao2MFJcw8hLEkB2E8w2iJJtB1WIC/pub?output=csv'

def fetch_new_data():
    response = requests.get(SHEET_URL)
    if response.status_code == 200:
        data = []
        csv_content = StringIO(response.text)
        csv_reader = csv.DictReader(csv_content)
        for row in csv_reader:
            data.append({
                "latitude": float(row['Latitude']),
                "longitude": float(row['Longitude']),
                "espece": row['Espèce'],
                "date": row['Date'],
                "observateur": row['Observateur']
            })
        return data
    else:
        raise Exception("Failed to fetch data from Google Sheets")

# Récupère les nouvelles données
new_data = fetch_new_data()

# Sauvegarde les données mises à jour
with open('data.js', 'w') as file:
    file.write('var data = ' + json.dumps(new_data, indent=2) + ';')
