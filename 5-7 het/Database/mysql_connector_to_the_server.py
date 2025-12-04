import mysql.connector

szerver_kapcsolat = mysql.connector.connect(
    host = 'localhost',
    user = 'mate',
    password = 'Kismacska.hu'   
)

kurzor = szerver_kapcsolat.cursor()
kurzor.execute('DROP DATABASE IF EXISTS gyümölcsök')
kurzor.execute('CREATE DATABASE gyümölcsök')
szerver_kapcsolat.close()