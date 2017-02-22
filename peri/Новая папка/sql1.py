import sqlite3
conn = sqlite3.connect("weapons_shop.db")
curs = conn.cursor()
curs.execute("DROP TABLE weapons")
curs.execute("""CREATE TABLE weapons
(name VARCHAR(50) PRIMARY KEY,
type VARCHAR(10),
numbers INT,
cost INT,
caliber REAL
)
""")

curs.execute("INSERT INTO weapons VALUES('AWP','Rifles',10,4500,7.62)")
curs.execute("INSERT INTO weapons VALUES('AK-47','Assault',30,2700,5.45)")

name,types, numbers, cost,caliber = 'P90','SMG',50,2500,5.7

curs.execute("INSERT INTO weapons VALUES(?,?,?,?,?)",
    (name,types, numbers, cost,caliber))

ins = "INSERT INTO weapons VALUES(?,?,?,?,?)"



name,types, numbers, cost,caliber = 'Desert Eagle','Pistols',50,2500,5.7
curs.execute(ins,(name,types, numbers, cost,caliber))

conn.commit()

curs.close()
conn.close()
