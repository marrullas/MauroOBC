import sqlite3
con = sqlite3.connect('ejemplo1.db')
cur = con.cursor()

def crear_db():

    cur.execute('CREATE TABLE Alumnos(id INTEGER, nombre TEXT, apellido TEXT  )')

    data = [
        (1,'Fulano', 'Detal'),
        (1,'Perencejo', 'Detal'),
        (1,'Muchilanga', 'Detal'),
        (1,'Magola', 'Detal'),
        (1,'Pepe', 'Detal'),
        (1,'Paco', 'Detal'),
        (1,'Pipe', 'Detal'),
        (1,'Pepa', 'Detal'),

    ]
    cur.executemany("INSERT INTO Alumnos VALUES(?, ?, ?)", data)
    con.commit()
    con.close()

def consultar(nombre):
    #nombre = 'Paco'
    sql = f"SELECT * FROM Alumnos WHERE nombre='{nombre}'"
    print(sql)
    row = cur.execute(sql)
    #row = cur.execute(f'SELECT * FROM Alumnos')
    print(row.fetchall())
    con.close()

#crear_db()

consultar('Pepe')

