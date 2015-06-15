#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'oki'

import MySQLdb
import MySQLdb.cursors

class Database:

    # constructor with connection to the host
    def __init__(self, host):
        self.connect(host)
        self.MY_TOILET_ID = 3
        self.MY_POS_ID = 1

    # destructor
    def __del__(self):
        self.cursor.close()
        self.db.close()

    # connect to MySQL
    def connect(self, host):
        self.db = MySQLdb.connect(
            host=host,
            db='ototsukasa',
            user='ototsukasa',
            passwd='ototsukasa',
            charset='utf8',
            cursorclass=MySQLdb.cursors.DictCursor
        )
        self.cursor = self.db.cursor()

    # execute
    def execute(self, text):
        self.cursor.execute(text)

    # commit
    def commit(self):
        self.db.commit()

    # execute and commit
    def execute_and_commit(self, text):
        self.execute(text)
        self.commit()

    # execute and fetch all
    def fetch(self, text):
        self.execute(text)
        return self.cursor.fetchall()

    # register new music information
    def register_music(self, word, url):
        self.execute_and_commit(u'insert into musics values(null, {0}, "{1}", "{2}", now())'.format(self.MY_TOILET_ID, word, url))

    # fetch music information
    def fetch_music_randomly(self):
        return self.fetch(u'SELECT url ,name AS address FROM musics AS m LEFT JOIN toilets AS t ON m.toilet_id = t.id LEFT JOIN location AS l ON t.pos_id = l.pos_id order by rand() limit 1')[0]

    # post new review
    #def post_review(self, star, text):
        # self.execute_and_commit(u'insert into reviews values(null, {0}, {1}, "{2}", now())'.format(30, star, text))

    # fetch the newest reservation
    def fetch_reservation(self):
        return self.fetch(u'select * from reservations where toilet_id = {0} order by `updatetime` desc limit 1'.format(self.MY_TOILET_ID))[0]

    # fetch the newest status
    def fetch_status(self):
        return self.fetch(u'select * from status where toilet_id = {0} order by `updatetime` desc limit 1'.format(self.MY_TOILET_ID))[0]

    # fetch the newest reservation
    def update_status(self, is_occupied):
        empty = "Occupied" if is_occupied else "Empty"
        self.execute_and_commit(u'insert into status values(null, {0}, "{1}", now())'.format(self.MY_TOILET_ID, empty))

    def register_review(self,comment):
        self.execute_and_commit(u'INSERT INTO reviews(pos_id,comment) VALUES({0},"{1}")'.format(self.MY_POS_ID,comment))


def main():
    db = Database('157.82.7.193')
    db.update_status(True)


if __name__ == '__main__':
    main()
