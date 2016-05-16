import MySQLdb, json, shutil
##import json, shutil

_connection = {"SERVER":"raptor-speakerblack.c9users.io","DATABASE":"raptor","USER":"speakerblack","PASSWORD":""}

_db_ = MySQLdb.connect(_connection['SERVER'],_connection['USER'],_connection['PASSWORD'],_connection['DATABASE'])
def _getDataBase():
	cursor = _db_.cursor()
	return cursor

def _close():
	_db_.commit()
	_db_.close()

def query(sql):
	_data = _getDataBase()
	_data.execute(sql)
	return _data.fetchall()
	_close()

def execute(sql):
	_data = _getDataBase()
	_data.execute(sql)
	_close()

def printJson(__object, status):
	print json.dumps({"status":status,"data":__object})

def moveUploadedFile(src,dest):
	shutil.move(src, dest)