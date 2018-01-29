import sqlite3
import tweepy
import uuid
import pymysql.cursors
from albums import AlbumData

class Bowie(AlbumData):

	consumer_key = "#"
	cosumer_secret = "#"
	access_token = "#"
	access_token_secret = "#"
	db_conn = ''

	def __init__(self):
		super().__init__()

		connection = pymysql.connect(host='#',
								 user='#',
								 password='#',
								 db='#',
								 charset='utf8mb4',
								 cursorclass=pymysql.cursors.DictCursor)

		self.db_conn = connection

	def bowie_tribute(self):
		try:
		    with self.db_conn.cursor() as cursor:
		        # Create a new record
		        sql = "SELECT * FROM `vals`"
		        cursor.execute(sql,)
		        result = cursor.fetchone()
		        val = int(result["current_number"])
		        if ( val == 24):
		        	val = 0
		        filename = self.albumdata[int(val)]
		finally:
		    print("Done")
		###
		auth = tweepy.OAuthHandler(self.consumer_key, self.cosumer_secret)
		auth.set_access_token(self.access_token,self.access_token_secret)
		api = tweepy.API(auth)
		api.update_profile_image(filename)
		val += 1
		################
		try:
		    with self.db_conn.cursor() as cursor:
		        # Create a new record
		        update = "UPDATE `vals` SET `current_number`=%s"
		        cursor.execute(update, (val,))
		        self.db_conn.commit()
		finally:
		    self.db_conn.close()

    # connection is not autocommit by default. So you must commit to save
    # your changes.
    #connection.commit()

#bow = Bowie()
#bow.bowie_tribute()



'''
 val  += 1
		        update = "UPDATE `vals` SET `current_number`=%s"
		        cursor.execute(update, (val,))
		        self.db_conn.commit()
'''


