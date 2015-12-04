# -*- coding: utf-8 -*- 
#
#Raptor
#
####VERSION########
_version = "0"
####COMPILACION####
_build = "5"
##################
#
#
#   Proporciona una interfaz para el manejo de la API de 
#   last.fm (http://www.last.fm/es/api) y Youtube in MP3 
#   (http://youtubeinmp3.com/api/) para facil acceso a 
#   la informacion.
#   permite ver informacion acerca de temas, albumes y 
#   artistas, ademas permite hacer busquedas sobre temas,
#   albumes y artistas.
#   Permite descargar un archivo MP3 tomando como base el 
#   MBID (music brainz id) y establece los 
#   metadatos propios del titulo.
#

import sys, os, urllib, urllib2, json, eyed3, os.path, uuid, random, smtplib, shutil, time, platform

dataapptemp = {"artist":"","track":""}

##########################
#@PARAM MBID = sys.argv[2]
##########################

class download(object):
	info={"name":"", "duration":"", "artist":"", "album":"", "image":"", "gener":"", "position":""}
	imagedata = 0
	_mbid = str()

	def __init__(self, mbid):
		_mbid = mbid

	def getLink(self, id):
		url = "http://youtubeinmp3.com/fetch/?api=advanced&format=JSON&video=http://www.youtube.com/watch?v=" + id
		req = urllib2.Request(url)
		opener = urllib2.build_opener()
		f = opener.open(req)
		json_data = json.load(f)
		return json_data['link']

	def getId(self, searchTerms):
		url = r"https://www.googleapis.com/youtube/v3/search?part=snippet&q=" + searchTerms + "&type=video&key=AIzaSyAfXxWUUZ1nxII62vg-XR0Shuv_ikuVT2A"
		url = url.replace(" ", "+")
		req = urllib2.Request(url)
		opener = urllib2.build_opener()
		f = opener.open(req)
		json_data = json.load(f)
		print json_data['items'][0]['id']['videoId']
		return json_data['items'][0]['id']['videoId']

	def getInfo(self, mbid):
		req = urllib2.Request("http://ws.audioscrobbler.com/2.0/?method=track.getInfo&api_key=0fbca00bcc89957dd5075f8c9661fe71&mbid=" + mbid + "&format=json")
		opener = urllib2.build_opener()
		f = opener.open(req)
		json_data = json.load(f)
		self.info["name"] = json_data['track']['name']
		self.info["duration"] = json_data['track']['duration']
		self.info["artist"] = json_data['track']['artist']['name']
		self.info["album"] = json_data['track']['album']['title']
		self.info["image"] = json_data['track']['album']['image'][3]["#text"]
		self.info["gener"] = json_data['track']['toptags']['tag'][0]["name"]
		self.info["position"] = json_data['track']['album']['@attr']['position']
		dataapptemp["artist"] = self.info["artist"]
		dataapptemp["track"] = self.info["name"]
		#for d in info:
		#	print(info[d])


	def getFile(self, url):
		if not os.path.exists("apptemp"):
			os.mkdir("apptemp")
		file_name = self.info["name"]+".mp3"
		if os.path.exists("appmusic/"+file_name):
		    print json.dumps({"status":"success","name":file_name})
		    return True;
		u = urllib2.urlopen(url)
		f = open("apptemp/"+file_name, 'wb')
		meta = u.info()
		file_size = int(meta.getheaders("Content-Length")[0])
		print "Downloading: %s Bytes: %s" % (file_name, file_size)

		file_size_dl = 0
		block_sz = 8192
		while True:
		    buffer = u.read(block_sz)
		    if not buffer:
		        break

		    file_size_dl += len(buffer)
		    f.write(buffer)
		    status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
		    status = status + chr(8)*(len(status)+1)
		    #print status,

		f.close()
		print json.dumps({"status":"success","name":file_name})
		return False;
		#except:
		    #print "Unexpected error near line 96: ", sys.exc_info()[1]

	def setInfo(self, name):
		audiofile = eyed3.load("apptemp/"+self.info["name"]+".mp3")
		audiofile.tag.artist = self.info["artist"]
		audiofile.tag.album = self.info["album"]
		audiofile.tag.album_artist = self.info["artist"]
		audiofile.tag.title = self.info["name"]
		audiofile.tag.track_num = int(self.info["position"])
		imagedata = open("apptemp/"+name+".jpg","rb").read()
		audiofile.tag.images.set(3,imagedata,"image/jpeg",u"By Raptor")
		audiofile.tag.save()
		if not os.path.exists("appmusic"):
			os.mkdir("appmusic")
		shutil.move("apptemp/"+self.info["name"]+".mp3", "appmusic/"+self.info["name"]+".mp3")

	def getImage(self, name):
		print self._mbid
		urllib.urlretrieve(self.info['image'], "apptemp/"+name+".jpg")
		
##########################
#@PARAM _type = resource type, is between: track, album, artit, tag.
#@PARAM _function = action to be run, is between: search, getinfo, getsimilar
#@PARAM _param = search terms or mbid (music brainz id), only one of the two
##########################

def controller(_method, _param):
	_type = _method.split(".")[0]
	_function = _method.split(".")[1]
	_url = "http://ws.audioscrobbler.com/2.0/?method=" +_method + "&api_key=0fbca00bcc89957dd5075f8c9661fe71&format=json"
	_endUrl = str()
	_fill = False
	if _function == "search":
		_endUrl = "&"+_type+"="+_param
	else:
		_endUrl = "&mbid="+_param
	if _function == "getinfo":
		if not os.path.exists("data"):
			os.mkdir("data")
		if os.path.exists("data/"+_param):
			archi=open("data/"+_param,'r')
			linea=archi.readline()
			while linea!="":
				print linea
				linea=archi.readline()
			archi.close()
			return
		else:
			archi=open("data/"+_param,'w')
			archi.close()
			_fill = True
	f = urllib2.urlopen(_url + _endUrl)
	_outer = f.read()
	if _fill == True:
		tmpFile=open("data/"+_param,'a')
		tmpFile.write(_outer)
		tmpFile.close()
	print _outer
	f.close()

##########################
#no arguments
##########################

def cmd_help():
	print json.dumps({
		"name":"raptor",
		"build": _version+"."+_build,
		"company":"SpeakerBlack",
		"usage":"raptor 'command' ['param1,param2,paramN']",
		"commands":{"help":"information about raptor",
		"controller":{"description":"read information specified", 
		"usage":"controller 'type' 'function' 'param1[,param2]'"},
		"download":{"description":"download mp3 file indicated MBID", 
		"usage":"download 'mbid'"},
		"getlinkfile":{"description":"get the link for download te file.mp3", 
		"usage":"getlinkfile 'search terms'"}, "reportex":{"description":"registers an external exception in the record", 
		"usage":"reportex 'exception'"}, "getlastview":{"description":"show lasted records", 
		"usage":"getlastview"}},
		"building SO":platform.system()+" "+platform.architecture()[0]+" "+platform.version()})

##########################
#@PARAM terms = search terms
##########################

def cmd_getLinkfile(terms):
	_url = "https://www.googleapis.com/youtube/v3/search?part=snippet&q=" + terms.strip().replace(" ", "+") + "&type=video&key=AIzaSyAfXxWUUZ1nxII62vg-XR0Shuv_ikuVT2A"
	f = urllib2.urlopen(_url)
	data = json.loads(f.read())
	_url = "http://youtubeinmp3.com/fetch/?format=JSON&video=http://www.youtube.com/watch?v=" + data['items'][0]['id']['videoId']
	f = urllib2.urlopen(_url)
	data = json.loads(f.read())
	return data['link']
	#print data['link']

##########################
#@PARAM MBID = sys.argv[2]
##########################

def cmd_download():
	dw = download(sys.argv[2])
	dw.getInfo(sys.argv[2])
	if (dw.getFile(cmd_getLinkfile(dataapptemp["track"] + " " + dataapptemp["artist"]))):
	    return
	dw.getImage(sys.argv[2])
	dw.setInfo(sys.argv[2])
	os.remove("apptemp/"+sys.argv[2]+".jpg")	

#############################
#@PARAM strEx = Exception runtime
#############################

def writeLogException(strEx):
    if not os.path.exists("data"):
        os.mkdir("data")
    log=open('data/log.txt','a')
    log.write(time.ctime()+' - '+strEx+'\n')
    log.close()

def getLastView():
    ficheros = os.listdir("data/")
    n = len(ficheros) 
    print json.dumps(ficheros[n-40:n])


#############################
#@PARAM COMMAND = sys.argv[1]
#############################

def main():
    try:
        if len(sys.argv) >= 2:
            if sys.argv[1] == "help":
                cmd_help()
            elif sys.argv[1] == "download":
                cmd_download()
            elif sys.argv[1] == "controller":
                controller(sys.argv[2], sys.argv[3])
            elif sys.argv[1] == "getlinkfile":
                cmd_getLinkfile(sys.argv[2])
            elif sys.argv[1] == "getlastview":
                getLastView()
            elif sys.argv[1] == "reportex":
                writeLogException("external exception >> "+sys.argv[2])
            else:
                cmd_help()
        else:
            cmd_help()
    except Exception, e:
        writeLogException(str(sys.exc_info()))
        print json.dumps({"status":"error","exception":json.dumps(str(sys.exc_info()))})
	
###################
#Start the programm
###################

if __name__ == "__main__":
	main()
