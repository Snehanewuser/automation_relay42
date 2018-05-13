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
engagement = "Tomato_" + ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(3)])
report_status(engagement)
engagement_link = create_engagement(engagement)
report_status(engagement_link)
return_audience_link=create_audience(engagement)
send_req_n_validate_audi_entry(return_audience_link, engagement)
print "All testcases are executed, please check/tmp/relay42_results folder"
exit()



