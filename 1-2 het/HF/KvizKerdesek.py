import json
import datetime
import os
import random
import re
import unicodedata
from enum import Enum, auto

class ValaszHiba(Exception):
    def __init__(self, uzenet: str):
        self.uzenet = uzenet
        super().__init__(uzenet)

class KerdesTipus(Enum):
    SZOVEGES = auto()
    EGESZ_SZAM = auto()
    DATUM = auto()
    LEBEGOS = auto()
    HALMAZOS = auto()
    TOBBVALASZOS = auto()
    IGAZHAMIS = auto()


class Kviz:
    def __init__(self, json_utvonal: str):
        self.json_utvonal = json_utvonal
        self.kerdesek = []
        self.pontszam = 0
        self.max_pont = 0

    def betolt(self):
        with open(self.json_utvonal, encoding="utf-8") as f:
            adatok = json.load(f)

        def _normalize_enum_key(s: str) -> str:
            nk = unicodedata.normalize('NFD', s)
            no_marks = ''.join(c for c in nk if not unicodedata.category(c).startswith('M'))
            key = re.sub(r'[^0-9A-Za-z]+', '_', no_marks).strip('_').upper()
            return key

        for elem in adatok:
            tipus_raw = elem.get("tipus", "")
            key = _normalize_enum_key(tipus_raw)
            try:
                tipus_enum = KerdesTipus[key]
            except KeyError:
                tipus_enum = KerdesTipus[tipus_raw]

            self.kerdesek.append({
                "kerdes": elem["kerdes"],
                "valasz": elem["valasz"],
                "tipus": tipus_enum,
                "minta": elem["minta"]
            })

        self.max_pont = len(self.kerdesek) * 5

    def eredmeny_mentese(self):
        konyvtar = os.path.dirname(self.json_utvonal)
        cel = os.path.join(konyvtar, "Kviz_Eredmenyek.json")

        eredmeny = {
            "nev": input("\nAdd meg a neved: "),
            "datum": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "pontszazalek": round(100 * self.pontszam / self.max_pont, 2),
            "pontszam": self.pontszam
        }

        try:
            with open(cel, "r", encoding="utf-8") as f:
                lista = json.load(f)
        except FileNotFoundError:
            lista = []

        lista.append(eredmeny)

        with open(cel, "w", encoding="utf-8") as f:
            json.dump(lista, f, ensure_ascii=False, indent=4)

        print(f"Eredmények mentve ide: {cel}")

    def kerdes_feltesz(self, kerdes: str, helyes: str, tipus: KerdesTipus, minta: str):

        if tipus == KerdesTipus.SZOVEGES:
            valasz = input(kerdes + "\n")
            if minta and re.search(minta, valasz):
                self.pontszam += 5
                return True, "Helyes!"
            raise ValaszHiba(f"Helytelen! A helyes válasz: {helyes}")

        elif tipus == KerdesTipus.EGESZ_SZAM:
            try:
                val = int(input(kerdes + "\n"))
            except ValueError:
                raise ValaszHiba("Érvénytelen szám!")
            
            helyes_szam = int(helyes)
            if val == helyes_szam:
                self.pontszam += 5
                return True, "Helyes!"

            elt = abs(100 * (val - helyes_szam) // helyes_szam)
            pont = max(0, 5 - elt // 10)
            self.pontszam += pont
            return False, f"Eltérés: {elt}%, részpontszám: {pont}"

        elif tipus == KerdesTipus.DATUM:
            try:
                val = datetime.datetime.fromisoformat(input(kerdes + "\n"))
                good = datetime.datetime.fromisoformat(helyes)
            except ValueError:
                raise ValaszHiba("Hibás formátum! Használd: ÉÉÉÉ-HH-NN")

            if val == good:
                self.pontszam += 5
                return True, "Helyes!"
            raise ValaszHiba(f"Helytelen! A helyes válasz: {helyes}")

        elif tipus == KerdesTipus.LEBEGOS:
            try:
                val = float(input(kerdes + "\n"))
            except ValueError:
                raise ValaszHiba("Érvénytelen szám!")

            helyes_szam = float(helyes)
            if abs(val - helyes_szam) <= 0.0001:
                self.pontszam += 5
                return True, "Helyes!"

            return False, f"Eltérés: {val - helyes_szam:.5f}"

        elif tipus == KerdesTipus.HALMAZOS:
            megadott = {e.strip().lower() for e in input(kerdes + "\n").split(",")}
            jo = {e.strip().lower() for e in helyes.split(",")}

            if megadott == jo:
                self.pontszam += 5
                return True, "Helyes!"

            hianyzo = jo - megadott
            felesleges = megadott - jo

            pont = 5
            if len(hianyzo) == 1:
                pont = 3
            elif len(hianyzo) >= 2:
                pont = 1

            self.pontszam += pont
            uzenet = f"Hiányzó: {', '.join(hianyzo)}; Felesleges: {', '.join(felesleges)}; Részpontszám: {pont}"
            return False, uzenet

        elif tipus == KerdesTipus.TOBBVALASZOS:
            opciok = helyes.split(", ")
            helyes_opcio = opciok[0]

            random.shuffle(opciok)
            betuk = "ABCD"

            print(kerdes)
            parok = {betuk[i]: opciok[i] for i in range(len(opciok))}
            for b, v in parok.items():
                print(f"  {b}. {v}")

            valasz = input("> ").upper().strip()

            if valasz in parok and parok[valasz] == helyes_opcio:
                self.pontszam += 5
                return True, "Helyes!"
            return False, f"Helytelen! A helyes válasz: {helyes_opcio}"

        elif tipus == KerdesTipus.IGAZHAMIS:
            print(kerdes)
            print("  A. IGAZ")
            print("  B. HAMIS")
            valasz = input("> ").strip().upper()

            if (valasz == "A" and helyes.upper() == "IGAZ") or \
               (valasz == "B" and helyes.upper() == "HAMIS"):
                self.pontszam += 5
                return True, "Helyes!"
            return False, f"Helytelen! A helyes válasz: {helyes.upper()}"

    def futtat(self):
        self.betolt()

        for elem in self.kerdesek:
            while True:
                try:
                    helyes, uzenet = self.kerdes_feltesz(
                        elem["kerdes"],
                        elem["valasz"],
                        elem["tipus"],
                        elem["minta"]
                    )
                    print(uzenet)
                    break
                except ValaszHiba as h:
                    print(h.uzenet)
                    break

        print(f"\nPontszám: {self.pontszam}/{self.max_pont}")
        print(f"Százalék: {self.pontszam / self.max_pont * 100:.2f}%\n")
        self.eredmeny_mentese()

if __name__ == "__main__":
    fajl = input("Add meg a kvíz JSON fájl útvonalát: ")
    k = Kviz(fajl)
    k.futtat()
