'''
Created on Nov 7, 2015

@author: catzhangy2
'''
import psycopg2


def connect_db():
    db = psycopg2.connect(
        database='jetblue',
        user='postgres',
        password='1234',
        port='5432',
        host='localhost',
    )
    return db


# Don't call this. The database ia already set-up at this point.
def create_table(db):
    if db:
        try:
            db.cursor().execute(
                "".join(
                    "CREATE TABLE jetblue_data (",
                    "origin text,",
                    "destination text,",
                    "hotel_property text,",
                    "hotel_nights_stay decimal,",
                    "hotel_check_in_date date,",
                    "hotel_check_out_date date,",
                    "expedia_price money,",
                    "jetblue_price money,",
                    "percent_savings decimal,",
                    "month_of_travel decimal,",
                    "advance_weeks int",
                    ");",
                ),
            )
            db.commit()
            print "Success: Table jetblue_data Created."
        except:
            print "ate shat fucked died"


# Add entries into database
def insert_into_db(db, entries=[]):
    if db and entries:
        try:
            db.cursor().execute(
                "INSERT INTO jetblue_data VALUES %s" % str(entries)[1:-1],
            )
            db.commit()
            print "Successfully inserted entries into db."
        except:
            print "ate shat fucked died"


# Arbitrary query from database
def query(db, query):
    if db and query:
        try:
            cur = db.cursor()
            cur.execute(query)
            return cur.fetchall()
        except:
            print "ate shat fucked died"
            return []


# Takes a mapping of fields, converts to a query, and executes
def search_query(db, fields):
    if not fields:
        return query(
            db,
            "SELECT * FROM jetblue_data ORDER BY RANDOM() LIMIT 1",
        )
    else:
        return query(
            db,
            ''.join(
                "SELECT * FROM jetblue_data WHERE ",
                ' AND '.join(
                    ["%s = %s" % (f[0], f[1]) for f in fields.items()],
                ),
            ),
        )


# TODO: Addy
def insert_initial_jetblue_data(db):
    import resume_parser
    insert_into_db(db, resume_parser.parseResume())
