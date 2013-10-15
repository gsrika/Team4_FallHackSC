from urllib2 import urlopen
import MySQLdb

def insert_data(pid,gname,gid,pmessage,username,userid,ctime,utime):
	querystring="Insert into suggest_dump  values ('%s','%s','%s','%s','%s','%s','%s','%s','""','""','""')" %(pid,gname,gid,pmessage,username,userid,ctime,utime)
	#print querystring
	querytemp=querystring.replace("suggest_dump","suggest_temp")
	try:
		db=MySQLdb.connect(host="localhost",user="root",passwd="srikanth",db="test")
	   	cur=db.cursor()
		a="printval"
		cur.execute(querystring)
		cur.execute(querytemp)
        	cur.close()
       		db.commit()
        	db.close()
	except MySQLdb.Error,e:	  
		#print "eception occured"
		#print e
		try:
			cur.execute(querytemp)
			cur.close()
			db.commit()
			db.close()
		except MySQLdb.Error,e:
			pass
	

def extract_data(dic,gid):
	for d in dic["data"]:
		#print d
        	pid=d['id']
        	username=d['from']['name']
        	userid=d['from']['id']
        	gname= d['to']['data'][-1]['name']
		if(d.has_key('message')):
	        	pmessage= d['message']
		else:
			pmessage="" 
		#print pmessage
        	ctime=d['created_time']
		utime=d['updated_time']
		pmessage=pmessage.replace("(","")
		pmessage=pmessage.replace(")","")
		pmessage=pmessage.replace("'","")
       		username=username.replace("'","")   
        	insert_data(pid,gname,gid,pmessage,username,userid,ctime,utime)
	
		             


def get_data(gid,token,next,level,visited):
	if(level==1):
		url="https://graph.facebook.com/"+gid+"/feed?limit=500&access_token="+token
	elif(level==2):
		url=next
	else :
		url=next+"&access_token="+token
	print(url)
	html=urlopen(url)
	s=html.read()
	s=s.replace("\n","\\n")
	s=s.replace("false","False")
	s=s.replace("true","True")
	s=s.replace("null","")
	dic=eval(s)
	#print type(dic)
	extract_data(dic,gid)
	if(visited==False):
		if(dic.has_key('paging')):
			next=dic["paging"]['next']
		else:
			next=""
	else:
		next=""
	return next

#html=urlopen("https://graph.facebook.com/333039026750643/feed?limit=40&access_token=CAACEdEose0cBAPoBlQ1x3Raou6GyYY98buLd8h6q6nCyEjnVB7ajHAUHZCUIQeb2gU2zEd0IwQ9PpEWk02wMpaSWGwO0rK8ZAU96PNllCuhBs5yIAdnBe2RYjHMlIMHjgX8OPbESfg3cgU6JTtMIilO9oQqYSrhZCK1nPWOmLVBDqFOcgoFdc8U46DrGguFeSY8F3iR0wZDZD")
##print(html.read())
import pdb

gid="341591699228709"#Viterbi School of Engineering
gid="fall2013usc"
gid="333961479991731"#Computer Science
gid="324969354265911"#FREE FOOD u0040 USC  
gid="409595849094960"#USC Ticket Trades 
gid="333920903329122"# USC Graduate Students
gid="491533930864885" #usc fall 2013
gid="560425023973997"#fall2013usc
gid="150766218418138"#uscfall2013bangalore
gid="116047931844982"#uscfall2012
gid="333038996750646"#jobsandinternship
gid="333918209996058"#uscbusinessadministration
gid="22586725313"#uscfall2013official
gid="333875460000333"#uscclassof2013
gid="334056999982179"#classof2016
gid="333039016750644"#Housing
gid="2211303362"#uscacm
gid="333039026750643"#Free & For Sale 
gid="357239704394798"# usc linux group 
gid="334098683311344"#music industry
gid="334001126654433"#electrical engineering
gid="334063376648208"#psycology
gid="389570297764182"#internation students
gid="334504473270765"#student entreprenues
gid="2200556148"#ais
gid="333927766661769"#class2014
gid="333038976750648" #campustips
token="CAACEdEose0cBAKrygtgKd1L9Y9rQR2UXLzmC4ygjptKahkDNZCAtceZAHUT6heMdZCw5BsmhyjkHtNQZCfRakHC44mYaU2WeqeosnqtOZCrVeLCPOsE7BNZAtdivwUDchZAyCZASmBI5DeOGKZCAfGBZCdFEQZAjDZAGepZARyqEVNEAdsj38pJDvbmmQV4TFnEKpoWp8f320kTsLEQZDZD"
next="acces_token"
gidlist=['333039026750643','341591699228709','333961479991731','324969354265911','409595849094960','333920903329122','491533930864885','560425023973997','150766218418138','333038996750646','333918209996058','333918209996058','22586725313','333875460000333','334056999982179',
'334056999982179','334056999982179','333039016750644','2211303362']
newlist=['357239704394798','334098683311344','334001126654433','334001126654433','334063376648208','389570297764182','334504473270765',
'2200556148','333927766661769','333038976750648']
"""
visited=True
for gid in gidlist:
	print gid 
	level=1
	next="access_token"
	#pdb.set_trace()
	while next!="":
		next=next.replace("\/","/")
		print next,"inside while"
		if(level==1):
			next=get_data(gid,token,next,level,visited)
			level=2
		else :
			if(level==2):
				#print gid
				#print token
				#print next
				#print level
                        	#pdb.set_trace()
				next=next.replace("limit=1000","limit=500")
				next=get_data(gid,token,next,level,visited)
				level=3
			else:
				next=get_data(gid,token,next,level,visited)
"""				
visited=False
for gid in newlist:
	print gid 
	level=1
	next="access_token"
	#pdb.set_trace()
	while next!="":
		next=next.replace("\/","/")
		print next,"inside while"
		if(level==1):
			next=get_data(gid,token,next,level,visited)
			level=2
		else :
			if(level==2):
				#print gid
				#print token
				#print next
				#print level
                        	#pdb.set_trace()
				next=next.replace("limit=1000","limit=500")
				next=get_data(gid,token,next,level,visited)
				level=3
			else:
				next=get_data(gid,token,next,level,visited)
				

"""
#get_data("333039026750643","CAACEdEose0cBAN7TKxn3wWABq6lED8a9d4PgweXbqbhTa92d6ksZCUbDlZCEJQDv5NdYcJZBZBl8MuzX83lVzPZBIJYwMfEL2dNMhi9mc9ZA2L95AmG7G9JJZBQzrZB0VMfkOFCYdqsHZB4I4TbiDsIPGlFEzhZBXJLbC5oJfgMZBT8muU2ynTZB2yMFRF7wK9sJSQsPWqIrZB1fpjgZDZD")

#get_data("341591699228709","CAACEdEose0cBAAJ84t9abgecBo4jVU9MKzlTdQPVykiobMZC7ZBJnJeDuCmZBPVL608StvWaQKSZAnRrmN3N6McMA3Kt97wHB5TuZCYIpEodZCL9IRYXwOHmZBZBsujAN2j3l17rny9x5eZC96XuBbtj00bdcvjlDsCvxZBLXyxv8kTqrTLHqCkv4PpE7ELZBAxBLZA48k7dUekHyAZDZD")

#get_data("415168521871026","CAACEdEose0cBAAJ84t9abgecBo4jVU9MKzlTdQPVykiobMZC7ZBJnJeDuCmZBPVL608StvWaQKSZAnRrmN3N6McMA3Kt97wHB5TuZCYIpEodZCL9IRYXwOHmZBZBsujAN2j3l17rny9x5eZC96XuBbtj00bdcvjlDsCvxZBLXyxv8kTqrTLHqCkv4PpE7ELZBAxBLZA48k7dUekHyAZDZD")

#get_data("357990630922149","CAACEdEose0cBAAJ84t9abgecBo4jVU9MKzlTdQPVykiobMZC7ZBJnJeDuCmZBPVL608StvWaQKSZAnRrmN3N6McMA3Kt97wHB5TuZCYIpEodZCL9IRYXwOHmZBZBsujAN2j3l17rny9x5eZC96XuBbtj00bdcvjlDsCvxZBLXyxv8kTqrTLHqCkv4PpE7ELZBAxBLZA48k7dUekHyAZDZD")

"""
