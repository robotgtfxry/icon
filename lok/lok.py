from flask import Flask, render_template_string
import folium

app = Flask(__name__)

@app.route('/')
def home():
    # Tworzenie mapy z centrum w określonych współrzędnych
    mapa = folium.Map(location=[51.5074, -0.1278], zoom_start=10)  # Przykładowo: Londyn

    # Lista lokalizacji do dodania (latitude, longitude, description)
    lokalizacje = [
        (51.5074, -0.1278, "Londyn", ""),
        (48.8566, 2.3522, "Paryż", ""),
        (40.7128, -74.0060, "Nowy Jork", ""),
        (35.6895, 139.6917, "Tokio", ""),
        (50.03219191209948, 22.008929832479907, "Rzeszów", ""),
        (0,0, "punkt 0", ""),
        (50.04266731766691, 22.05123542813991, "twoja hata", "missel attack")
    ]
    servery = [
        (31.32131, 31.3233, "data center")
    ]

    for lat, lon, opis in servery:
        folium.Marker(
            location=[lat, lon],
            popup=opis,
            icon=folium.Icon(prefix='fa', icon='server', color='grrey')
        ).add_to(mapa)

    # Dodawanie markerów do mapy
    for lat, lon, opis, wiad in lokalizacje:
        folium.Marker(
            location=[lat, lon],
            popup=opis,
            tooltip=wiad,
            icon=folium.Icon(prefix='fa', icon='shield', color='black', )
        ).add_to(mapa)

    # Generowanie HTML dla mapy
    mapa_html = mapa._repr_html_()
    
    # Używanie szablonu HTML do wyświetlenia mapy
    return render_template_string('''
        <!DOCTYPE html>
        <html>
        <head>
            <title>Mapa lokalizacji</title>
        </head>
        <body>
            <h1>Mapa lokalizacji</h1>
            <div>{{ mapa_html|safe }}</div>
        </body>
        </html>
    ''', mapa_html=mapa_html)

if __name__ == '__main__':
    app.run(debug=True)
