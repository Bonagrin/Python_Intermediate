import http.server
import urllib.parse

'''
http://localhost:8080/gyumolcs
http://localhost:8080/gyumolcs?fajta=alma&darab=4  #hozzáad 4 almát
http://localhost:8080/gyumolcs?fajta=banán&darab=-2  #elvesz 2 banánt (ha 0 lesz, törli is)
'''

class WebSzerver(http.server.SimpleHTTPRequestHandler):
    gyumolcsok = {
        'alma': 3,
        'banán': 2,
        'narancs': 5,
    }

    def do_GET(self):
        elemzett_url = urllib.parse.urlparse(self.path)
        if elemzett_url.path == '/gyumolcs':
            self.hozzaad(elemzett_url.query)
            self.valasz()

    def hozzaad(self, adat):
        parameterek = urllib.parse.parse_qs(adat)
        if 'fajta' in parameterek and 'darab' in parameterek:
            fajta = parameterek['fajta'][0]
            darab = int(parameterek['darab'][0])
            if fajta not in self.gyumolcsok:
                self.gyumolcsok[fajta] = 0
            self.gyumolcsok[fajta] += darab
            if self.gyumolcsok[fajta] == 0:
                self.gyumolcsok.pop(fajta)

    def valasz(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(bytes('<html><body>gyümölcsök:<ul>', 'UTF-8'))
        for gyumolcs in self.gyumolcsok:
            self.wfile.write(bytes('<li>' + gyumolcs + ': ' + str(self.gyumolcsok[gyumolcs]) + '</li>', 'UTF-8'))
        self.wfile.write(bytes('</ul></body></html>', 'UTF-8'))

http.server.HTTPServer(('localhost', 8080), WebSzerver).serve_forever()