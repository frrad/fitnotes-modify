from os import path
import sqlite3

dbname = path.expanduser(
    '~/Downloads/FitNotes_Backup_2015_06_19_18_36_19.fitnotes')

conn = sqlite3.connect(dbname)

c = conn.cursor()


# c.execute('SELECT * FROM SQLITE_MASTER')
# table = c.fetchall()
# for line in table:
#     print line, "\n"


c.execute('SELECT * FROM BodyWeight')
table = c.fetchall()
for line in table:
    print line, "\n"

c.execute(
    "INSERT INTO BodyWeight VALUES(79, '2015-02-02 07:02:23', 97.20496049205761, 18.3, '') ")


c.execute('SELECT * FROM BodyWeight')
table = c.fetchall()
for line in table:
    print line, "\n"
