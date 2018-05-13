#!/usr/bin/env python

def report_status(reportstring):
	try :
		from selenium import webdriver
		from selenium.webdriver.common.keys import Keys
		from selenium.webdriver.support.ui import Select
		import datetime
		import time
		import os
		import re
		import random
		import string
	except ImportError:
		print ("failed to load the reporting module")
		exit()
	
	filename="/tmp/relay42_results/reportfile.txt"
	f=open(filename, 'a')
	f.write(reportstring)
	f.write("\n")
	f.close()
