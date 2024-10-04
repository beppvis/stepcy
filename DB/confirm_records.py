import sqlite3
import platform
from pathlib import Path
import json

database = "../map.db"
table_name = "floor1"

p = Path(__file__).parents[1]
database = str(p) + "/map.db"



# assumes table created
try :
    cnt = sqlite3.connect(database)
    cur = cnt.cursor()     
    cur = cur.execute("select * from floor1;")
    vals = cur.fetchall()
    for record in vals:
        print(record)

except sqlite3.Error as error:
    print("sqlite error : ",error)

finally:
    if cnt:
        cnt.commit()
        cnt.close()
