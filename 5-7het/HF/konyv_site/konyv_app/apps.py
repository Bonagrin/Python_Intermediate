from django.apps import AppConfig
import mysql.connector
from mysql.connector import Error


class KonyvAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'konyv_app'
    _migrations_run = False  # flag, hogy megakadályozza az ismételt futást

    def ready(self):
        # szerver indulásakor ellenőrzi az adatbázist és létrehozza
        if not KonyvAppConfig._migrations_run:
            self.create_database_if_not_exists()
            KonyvAppConfig._migrations_run = True

    def create_database_if_not_exists(self):
        # létrehozza a 'konyv' MySQL adatbázist, ha nem létezik
        db_config = {
            'host': '127.0.0.1',
            'user': 'mate',
            'password': 'Kismacska.hu',
        }
        db_name = 'konyv'
        
        try:
            # csatlakozás MySQL-hez adatbázis nélkül
            connection = mysql.connector.connect(**db_config)
            cursor = connection.cursor()
            
            # adatbázis létrehozása ha nem létezik
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name} CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;")            
            cursor.close()
            connection.close()
            
        except Error as e:
            print(f"MySQL hiba: {e}")
            print("Ellenőrizd a MySQL kapcsolat adatait (host, user, password)!")
