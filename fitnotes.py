from os import path
import sqlite3

dbname = path.expanduser(
    '~/Downloads/FitNotes_Backup_2015_06_19_18_36_19.fitnotes')

conn = sqlite3.connect(dbname)

c = conn.cursor()


c.execute('SELECT * FROM SQLITE_MASTER')
print c.fetchall()
