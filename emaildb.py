import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

file_name = input("input file name")
if len(file_name) < 1:
    file_name = 'mbox.txt'

file = open(file_name)
for linia in file:
    if not linia.startswith('From: ') : continue
    pices = linia.split()
    email = pices[1]
    znak = email.find('@')
    domena = email[(znak+1):]
    #print(domena)

    cur.execute('SELECT count FROM Counts WHERE org = ?' ,(domena,))
    row = cur.fetchone()
    if row is None:
        cur.execute('INSERT INTO Counts (org,count) VALUES (?,1)',(domena,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (domena,))
    conn.commit()


cur.close()