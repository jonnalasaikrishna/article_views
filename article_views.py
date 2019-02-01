#!/usr/bin/env python
import psycopg2


def connect(dbname="news"):
    """Connect to the PostgreSQL database and returns a database connection."""
    try:
        conn = psycopg2.connect("dbname={}".format(dbname))
        cur = conn.cursor()
        return conn, cur
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


def query_article():
    """Prints most popular three articles of all time"""
    conn, cur = connect()
    query1 = ("select * from article limit 3")
    cur.execute(query1)
    res = cur.fetchall()
    conn.close()
    print ("\nThe most popular three articles of all time:\n")
    for i in range(0, len(res), 1):
        print (res[i][0] + " --> " + str(res[i][1]) + " views")


def query_author():
    conn, cur = connect()
    query2 = ("select * from author order by views desc")
    cur.execute(query2)
    res2 = cur.fetchall()
    conn.close()
    print ("\nThe most popular article authors of all time:\n")
    for i in range(0, len(res2), 1):
        print (res2[i][0] + " --> " + str(res2[i][1]) + " views")


def query_errors():
    """Print days on which more than 1% of requests lead to errors"""
    conn, cur = connect()
    query3 = ("select * from errors where error >1")
    cur.execute(query3)
    res3 = cur.fetchall()
    conn.close()
    print("\nDays with more than 1% of requests lead to errors:\n")
    for i in range(0, len(res3), 1):
        print(str(res3[i][0]) + " --> " + str(round(res3[i][1], 2))+" %errors")


if __name__ == '__main__':
    # uncomment the below code to make views
    query_article()
    query_author()
    query_errors()
    print("Success!")
