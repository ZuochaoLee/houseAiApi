# -*- coding: UTF-8 -*-
import urllib2
import sys
import config
import random
if __name__ == '__main__':
	in_put=sys.argv[1]
	while True:
		i=random.randint(0, len(config.slave))
		ip=config.slave[i]
		url="http://"+ip+":8788/fc/"+in_put
		try: 
			res=urllib2.urlopen(url,timeout = 8).read().decode('utf-8')
			print res
		except urllib2.URLError, e:
			del  config.slave[i] 

