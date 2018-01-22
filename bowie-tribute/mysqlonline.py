import uuid
import pymysql.cursors


def connect():
	connection = pymysql.connect(host='d6q8diwwdmy5c9k9.cbetxkdyhwsb.us-east-1.rds.amazonaws.com',
								 user='va4rl5lzx7kz4zao',
								 password='qrqz1ex6via44ks2',
								 db='lo6tvwoyy3tbsr6n',
								 charset='utf8mb4',
								 cursorclass=pymysql.cursors.DictCursor)
	try:
	    with connection.cursor() as cursor:
	        # Create a new record
	        sql = "SELECT * FROM `vals`"
	        cursor.execute(sql,)
	        result = cursor.fetchone()
	        val = int(result["current_number"])

	        #Update Query
	        val  += 1
	        update = "UPDATE `vals` SET `current_number`=%s"
	        cursor.execute(update, (val,))
	        connection.commit()



    # connection is not autocommit by default. So you must commit to save
    # your changes.
    #connection.commit()
	finally:
	    connection.close()







if __name__ == '__main__':
	connect()


	

