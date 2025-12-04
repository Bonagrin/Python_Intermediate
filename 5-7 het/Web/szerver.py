import http.server
import urllib.parse

# - Ez a fájl megmutatja, hogyan kezelhetünk GET és POST kéréseket a SimpleHTTPRequestHandler
# - A kérés útvonalát és query-paramétereit a urllib.parse segítségével elemezzük

class WebSzerver(http.server.SimpleHTTPRequestHandler):
    """    A `SimpleHTTPRequestHandler`-t örököljük, és felülírjuk a `do_GET` és `do_POST`
    metódusokat, hogy egy közös `valasz` metódust használjunk a válasz összeállításához.
    """

    def do_GET(self):
        # GET kérés esetén hívjuk meg a segédfüggvényt, megadva hogy GET érkezett
        self.valasz('GET')

    def do_POST(self):
        # POST kérés esetén ugyanez, de 'POST' típussal — a POST testét külön kezeljük
        self.valasz('POST')

    def valasz(self, lekerdezes):
        """Összeállítja és elküldi a HTML választ.

        Paraméterek:
        - lekerdezes: szöveg, ami jelzi a HTTP metódust ('GET' vagy 'POST')

        Fő lépések:
        1. A self.path-ot elemezzük (urlparse) — ez tartalmazhat query stringet is.
        2. A query stringet parse_qs segítségével dictionary-vé alakítjuk.
        3. Visszaküldünk egy egyszerű HTML választ, ahol megjelenítjük:
           - a HTTP módszert, az útvonalat és a paramétereket
        4. POST esetén elolvassuk a kérés törzsét (body) a Content-Length alapján
        """

        # Parse-oljuk az URL-t és a query paramétereket (pl. ?nev=Anna&kor=30)
        elemzett_url = urllib.parse.urlparse(self.path)
        parameterek = urllib.parse.parse_qs(elemzett_url.query)

        # Küldjük vissza az OK státuszt és a HTML tartalom típus fejlécet
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()

        # Kezdő HTML tartalom írása a response bufferre
        self.wfile.write(bytes('<html><body>', 'UTF-8'))
        self.wfile.write(bytes('<p>Lekérdezés: ' + lekerdezes + '</p>', 'UTF-8'))
        
        # Kiírjuk az útvonal részét (a query string nélkül)
        self.wfile.write(bytes('<p>Útvonal: <code>' + elemzett_url.path + '</code></p>', 'UTF-8'))
        self.wfile.write(bytes('<p>Paraméterek:</p>', 'UTF-8'))

        # A parameterek dict formátumban érkeznek, ahol a kulcs -> lista (több azonos kulcs)
        for kulcs in parameterek:
            # Itt csak az első értéket írjuk ki (parameterek[kulcs][0])
            self.wfile.write(bytes('<li>' + kulcs + ': ' + parameterek[kulcs][0] + '</li>', 'UTF-8'))

        # Zárjuk a paraméterlista HTML szakaszát
        self.wfile.write(bytes('</ul></p>', 'UTF-8'))

        # Ha POST kérés érkezett, olvassuk be a request body-t és írjuk ki
        if (lekerdezes == 'POST'):
            # A Content-Length fejléc megmondja, hány bájtot kell olvasni a rfile-ból
            adat = self.rfile.read(int(self.headers['Content-Length'])).decode('UTF-8')
            self.wfile.write(bytes('<p>Adat: ' + adat + '</p>', 'UTF-8'))

        # Befejezzük a HTML dokumentumot
        self.wfile.write(bytes('</body></html>', 'UTF-8'))

if __name__ == '__main__':
    # Szerver indítása: figyeljük a localhost:8080 címet
    # A serve_forever blokkál, ezért a futtatás terminálban tartja a processzt
    http.server.HTTPServer(('localhost', 8080), WebSzerver).serve_forever()
