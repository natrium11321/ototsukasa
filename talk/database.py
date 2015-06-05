#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'oki'

import MySQLdb
import MySQLdb.cursors

class Database:

    # constructor with connection to the host
    def __init__(self, host):
        self.connect(host)

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
        self.execute_and_commit(u'insert into musics values(null, {0}, "{1}", "{2}", now())'.format(30, word, url))

    # fetch music information
    def fetch_music_randomly(self):
        return self.fetch(u'select * from musics order by rand() limit 1')[0]

    # post new review
    #def post_review(self, star, text):
        # self.execute_and_commit(u'insert into reviews values(null, {0}, {1}, "{2}", now())'.format(30, star, text))

    # post new review
    def fetch_lock_state(self):
        return self.fetch(u'select * from reservations order by `time` limit 1')[0]


def main():
    db = Database('157.82.6.126')
    music = db.fetch_music_randomly()

    print music['url']


if __name__ == '__main__':
    main()
