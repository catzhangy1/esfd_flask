'''
Created on Nov 7, 2015

@author: catzhangy2
'''
import psycopg2


def connect_db():
    db = psycopg2.connect(
        database='jetblue',
        user='catzhangy1',
#         user='postgres',
#         password='1234',
        port='5432',
        host='localhost',
    )
    return db


# Don't call this. The database ia already set-up at this point.
def reset_tables(db):
    if db:
        try:
            db.cursor().execute(
                open("schema2.sql", "r").read(),
            )
            db.commit()
            print "Successfully reset tables."
        except:
            print "ate shat fucked died"


# Add entries into database. Must be well-formed.
def insert_into_db(db, entries=[], table="jetblue_data"):
    if db and entries:
        try:
            db.cursor().execute(
                "INSERT INTO %s VALUES %s" % (table, str(entries)[1:-1]),
            )
            db.commit()
            print "Successfully inserted entries into %s." % table
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
def field_query(db, fields=[], table="jetblue_data"):
    if not fields:
        return query(
            db,
            "SELECT * FROM %s ORDER BY RANDOM() LIMIT 1" % table,
        )
    else:
        #### FIX POTENTIAL SQL INJECTION ####
        return query(
            db,
            ''.join(
                "SELECT * FROM %s WHERE " % table,
                ' AND '.join(
                    ["%s = %s" % (f[0], f[1]) for f in fields.items()],
                ),
            ),
        )


def notify_contacts(db, fields):
    persons = field_query()
    # TODO: For each person, send email/text with info on fields


def insert_initial_jetblue_data(db):
    import resume_parser
    insert_into_db(db, resume_parser.parseResume())
