###########################################################################################
# relay42 test automation demonstration
# (C) 2018 by Sneha Mirajkar (sneha.mirajkar@gmail.com)
# Can be copied for any purposes, Please get prior approval.
#
# The relya42_main.py generates the runtime username, password, engagement-id to be passed
# to the functions called from  the relay42_usermodules.py as mentioned below             
# create engagement create audience and send_request_and_validate_audience-entry          
#
###########################################################################################



#!/usr/bin/env python

from relay42_usermodules import *
from relay42_libmodules import *
import random
import string
import uuid
import re
import time

newscript ="*******************************************************************************"
report_status(newscript)
engagement = "Tomato_" + ''.join([random.choice(string.ascii_letters +
string.digits) for n in xrange(3)])
username="relay42test1@gmail.com"
password="relay42test"
report_status(engagement)
engagement_link = create_engagement(username, password, engagement)
report_status(engagement_link)
return_audience_link=create_audience(username, password, engagement)
send_req_n_validate_audi_entry(username, password,
return_audience_link, engagement)
print "All testcases are executed, please check/tmp/relay42_results folder"
exit()
