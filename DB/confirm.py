import sqlite3
import json

database = "../map.db"
table_name = "floor1"


# assumes table created
try :
    cnt = sqlite3.connect(database)
    cur = cnt.cursor()     
    cur = cur.execute("select * from floor1;")
    vals = cur.fetchall()
    print(vals)

except sqlite3.error as error:
    print("sqlite error : ",error)

finally:
    if cnt:
        cnt.commit()
        cnt.close()
