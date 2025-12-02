import mysql.connector

séma_kapcsolat = mysql.connector.connect(
    host = 'localhost',
    user = 'mate',
    password = 'Kismacska.hu',
    database = 'gyümölcsök'
)

try:
    kurzor = séma_kapcsolat.cursor()
    kurzor.execute('''
    CREATE TABLE gyümölcs(
        id int auto_increment primary key,
        név VARCHAR(255),
        darab int)
    ''')
    
    gyümölcsöt_beszúr = 'insert into gyümölcs(név, darab) values (%s, %s)'
    kurzor.execute(gyümölcsöt_beszúr, ('alma', 3))
    kurzor.execute(gyümölcsöt_beszúr, ('banán', 2))
    kurzor.execute(gyümölcsöt_beszúr, ('narancs', 5))
    
    kurzor.execute('select * from gyümölcs')
    gyümölcsök = kurzor.fetchall() #letölti a lekérdezés össz sorát
    
    for gyümölcs in gyümölcsök:
        print(gyümölcs) 
    
except Exception as e:
    print(e)
    séma_kapcsolat.rollback() #leredeti állapot visszaállás
    
else:
    séma_kapcsolat.commit()

séma_kapcsolat.close()    

    