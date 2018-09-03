#!/usr/bin/env python

import psycopg2


class NewsQueryProcessor:

    def __init__(self):
        self.conn = psycopg2.connect("dbname=news")

    def get_query_results(self, query):
        cur = self.conn.cursor()
        cur.execute(query)
        rows = cur.fetchall()
        cur.close()
        return rows
