from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__)

gyumolcsok = {'alma': 3, 'banán': 2, 'narancs': 5}

# Statikus fájl kiszolgálása (ez kell!)
@app.route('/gyumolcsok.html')
def gyumolcsok_html():
    return send_from_directory('static', 'gyumolcsok.html')

@app.route('/gyumolcs', methods=['GET'])
def get_gyumolcsok():
    return jsonify(gyumolcsok)

@app.route('/gyumolcs', methods=['POST'])
def add_gyumolcs():
    data = request.get_json()
    fajta = data.get('fajta')
    darab = int(data.get('darab', 0))
    
    if fajta not in gyumolcsok:
        gyumolcsok[fajta] = 0
    gyumolcsok[fajta] += darab
    
    if gyumolcsok[fajta] <= 0:          # <= 0, hogy negatív se maradjon
        del gyumolcsok[fajta]
    
    return jsonify(gyumolcsok)

if __name__ == '__main__':
    app.run(host='localhost', port=8080, debug=True)