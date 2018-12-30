#!/usr/bin/python

import psycopg2 #this is module for postgres DB same as cx_Oracle

def emquery():

	conn = psycopg2.connect(database="emdb", user = "emuser", password = "emuser", host = "ctmtest.mylab.com", port = "5433")
	cur = conn.cursor()
	cur.execute('select job_name,message from alarm')
	rows = cur.fetchall()
	for row in rows:
		print row
	
	conn.commit()
	conn.close()
	
def ctmquery():
	conn = psycopg2.connect(database="ctrlmdb", user = "ctmuser", password = "ctmuser", host = "ctmtest.mylab.com", port = "5432")
	cur = conn.cursor()
	cur.execute('select jobname , nodeid from cmr_ajf')
	rows = cur.fetchall()
	for row in rows:
		print row
	
	conn.commit()
	conn.close()

print('em query results \n ')

emquery()
print('\n ---------------------------------------------------------------------------------------- \n')
print('\n \n ctm db query results \n ')

ctmquery()

#refrence https://www.tutorialspoint.com/postgresql/postgresql_python.htm
