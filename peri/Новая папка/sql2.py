import sqlite3
conn = sqlite3.connect("weapons_shop.db")
curs = conn.cursor()

# curs.execute("SELECT name,cost FROM weapons WHERE cost < 4000 ORDER BY cost DESC ")
# rows = curs.fetchall()
# print(rows)
#
# for row in rows:
#     print('Название оружия: {0[0]}, цена оружия: {0[1]}'.format(row))

curs.execute("SELECT * FROM weapons")
rows = curs.fetchall()
print(rows)

curs.execute("UPDATE weapons SET name = 'Новое название', cost = 30000 WHERE name = 'P90' ")
curs.execute("DELETE FROM weapons WHERE name = 'AK-47'")
conn.commit()


curs.execute("SELECT * FROM weapons")
rows = curs.fetchall()
print(rows)



curs.close()
conn.close()
