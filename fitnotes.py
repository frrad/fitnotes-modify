from os import path
import sqlite3
import csv
import glob


def date_format(input_date):
    (m, d, y) = input_date.split('/')
    while len(m) < 2:
        m = '0' + m
    while len(d) < 2:
        d = '0' + d

    return '%s-%s-%s 12:00:00' % (y, m, d)


# CREATE TABLE BodyWeight
# (
#     _id INTEGER PRIMARY KEY AUTOINCREMENT,
#     date TEXT NOT NULL,
#     body_weight_metric REAL NOT NULL,
#     body_fat REAL NOT NULL,
#     comments TEXT
# )
def new_data(path):
    with open(path, 'r') as file:
        reader = csv.DictReader(file)
        for line in reader:
            pounds = float(line['Weight'])
            date = date_format(line['Date'])
            kilos = pounds * \
                0.45359290943563975
            yield 'INSERT INTO BodyWeight (date, body_weight_metric, body_fat, comments) VALUES ("%s" , %.14f, 0.0, "")' % (date, kilos)


csv_files = glob.glob(path.expanduser('~/Downloads/collate*.csv'))
dbname = path.expanduser(
    '~/Downloads/FitNotes_Backup_2015_06_19_18_36_19.fitnotes')
path = csv_files[0]


conn = sqlite3.connect(dbname)
c = conn.cursor()

for command in new_data(path):
    c.execute(command)

conn.commit()
conn.close()
