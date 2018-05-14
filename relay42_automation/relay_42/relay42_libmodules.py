###########################################################################################
# relay42 test automation demonstration
#
#
# (C) 2018 by Sneha Mirajkar (sneha.mirajkar@gmail.com)
#
# Can be copied for any purposes, Please get prior approval.
#
#
#
# The relya42_libmodules.py the library function reporting function is
# used to log messages(info about teststeps and the results of the testcases in the
# /tmp/relay42_results/reportyfile.txt. This function is callable from all other functions
#
###########################################################################################

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
