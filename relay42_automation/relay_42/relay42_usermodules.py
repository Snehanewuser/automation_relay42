#!/usr/bin/env python

def create_engagement(engagement):
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
		from relay42_libmodules import *
	except ImportError:
		print ("failed to load selenium module for create_engagement")
		exit()

	try :
		driver = webdriver.Firefox()
		driver.get("https://admin.relay42.com")
		time.sleep(2)
		driver.find_element_by_name("username").send_keys("relay42test1@gmail.com")
		driver.find_element_by_name("password").send_keys("relay42test")
		driver.find_element_by_xpath('//button[@type="submit"]').click()
		time.sleep(5)
		driver.get("https://admin.relay42.com/site-1233/profiles/engagements/add")
		time.sleep(5)
		driver.find_element_by_xpath('//div[@class="controls input-container"]//input[@id="data-interaction-mainFieldValue"]').click()
		driver.find_element_by_xpath('//div[@class="controls input-container"]//input[@id="data-interaction-mainFieldValue"]').send_keys(engagement)
		time.sleep(5)
		descrption = engagement + "Am I a fruit or a phone"
		driver.find_element_by_xpath('//div[@class="controls input-container"]//textarea[@id="data-interaction-description"]').click()
		driver.find_element_by_xpath('//div[@class="controls input-container"]//textarea[@id="data-interaction-description"]').send_keys(descrption)
		driver.find_element_by_xpath('//button[@type="submit"]').click()
		time.sleep(5)
		reference_engage_link= driver.current_url
		time.sleep(5)
		driver.quit()
		report_status(reference_engage_link)
		time.sleep(5)
		reportstring ="successfully created engagement "+engagement
		report_status(reportstring)
		teststatus = "testcase_createEngagement:PASS"
		report_status(teststatus)
		return reference_engage_link

	except :
		reportstring ="something went wrong with engagement creation"
		report_status(reportstring)
		teststatus = "testcase_createEngagement:FAIL"
		report_status(teststatus)
		driver.quit()
		exit()

def create_audience(engagement):

	try :
		from selenium import webdriver
		from selenium.webdriver.common.keys import Keys
		from selenium.webdriver.support.ui import Select
		from selenium.webdriver.common.action_chains import ActionChains
		import datetime
		import time
		import os
		import re
		import random
		import string
		from relay42_libmodules import *
	
	except ImportError:
			print ("failed to load selenium module for create_")
			exit()
	try :
		driver = webdriver.Firefox()
		driver.get("https://admin.relay42.com")
		time.sleep(2)
		driver.find_element_by_name("username").send_keys("relay42test1@gmail.com")
		driver.find_element_by_name("password").send_keys("relay42test")
		driver.find_element_by_xpath('//button[@type="submit"]').click()
		time.sleep(5)
		driver.get("https://admin.relay42.com/site-1233/profiles/segments/add")
		audience_name = "new_audience_for "+engagement
		audience_descptn = "audience description for "+engagement
		time.sleep(5)
		driver.find_element_by_xpath('//div[@class="controls input-container"]//input[@id="segment-name"]').click()
		driver.find_element_by_xpath('//div[@class="controls input-container"]//input[@id="segment-name"]').send_keys(audience_name)
		time.sleep(5)
		driver.find_element_by_link_text('Engagement').click()
		driver.find_element_by_link_text('Engagement').click()
		time.sleep(5)
		getid=driver.find_element_by_link_text(engagement).get_attribute("id")
		time.sleep(5)
		dragable=driver.find_element_by_xpath('//a[@id="' + getid + '"]').get_attribute("id")
		time.sleep(10)
		driver.find_element_by_xpath('//div[@class="controls input-container"]//textarea[@id="segment-description"]').click()
		driver.find_element_by_xpath('//div[@class="controls input-container"]//textarea[@id="segment-description"]').click()
		dropable=driver.find_element_by_xpath('//div[@id="dropTargetAnd"]').get_attribute("id")
		#print dropable
		time.sleep(5)
		## load drag and drop helper
		with open("drag_and_drop_helper.js") as f:
			drag_and_drop_js = f.read()
		# perform drag&drop
		driver.execute_script(drag_and_drop_js + "$('#" + dragable + "').simulateDragDrop({ dropTarget: '#" + dropable + "'});")
		time.sleep(15)
		driver.find_element_by_link_text('Next').click()
		time.sleep(10)
		driver.find_element_by_link_text('Next').click()
		time.sleep(10)
		driver.find_element_by_link_text('Confirm').click()
		time.sleep(10)
		get_audience=driver.current_url
		time.sleep(5)
		driver.quit()
		report_status(get_audience)
		succes_statement = "successfully created the audience "+audience_name+" for "+ engagement
		report_status(succes_statement)
		teststatus= "testcase_createaudience:PASS"
		report_status(teststatus)
		return get_audience
	
	except :
		reportstring ="something went wrong with Audience creation for "+ engagement
		report_status(reportstring)
		teststatus = "testcase_createaudience:FAIL"
		report_status(teststatus)
		driver.quit()
		exit()

def send_req_n_validate_audi_entry(audiencelink, engagement):

	try :
		from selenium import webdriver
		from selenium.webdriver.common.keys import Keys
		from selenium.webdriver.support.ui import Select
		from selenium.webdriver.common.action_chains import ActionChains
		import datetime
		import time
		import os
		import re
		import random
		import uuid
		import string
		import requests
		from relay42_libmodules import *
	
	except ImportError:
		print ("failed to load selenium module for create_")
		exit()
	try: 
		driver = webdriver.Firefox()
		driver.get("https://admin.relay42.com")
		time.sleep(2)
		driver.find_element_by_name("username").send_keys("relay42test1@gmail.com")
		driver.find_element_by_name("password").send_keys("relay42test")
		driver.find_element_by_xpath('//button[@type="submit"]').click()
		time.sleep(5)
		driver.get(audiencelink)
		time.sleep(10)
		
		apistring= driver.find_element_by_xpath('//div[@class="col-md-3"]/p[2]').get_attribute("innerText")
		reportstring= apistring +" is the api_identifier for " +audiencelink+"and engagement "+engagement
		report_status(reportstring)
		time.sleep(10)
		
		epoch_time = int(time.time())
	
		randonuuid = uuid.uuid4()
		
		send_request="https://t.svtrd.com/t-1233?i="+str(randonuuid)+"&e=true&et="+engagement+"&cb="+str(epoch_time)
		report_status(send_request)
		
		resp = requests.get(send_request).content
		user_enter_audience = "https://api.relay42.com/v1/site-1233/profiles/42/segments"+"?partnerId="+str(randonuuid)
		
		resp_1 = requests.get(user_enter_audience, auth=('relay42test1@gmail.com', 'relay42test'), verify=False).content
		if (re.search(apistring, resp_1)):
			report_string = "the user has entered the audience list"
			report_status(report_string)
			teststatus = "testcase_send_req_n_validate_audi_entry:PASS"
			report_status(teststatus)
			driver.quit()
		else :
			report_string = "the user has NOT entered the audience list"
			report_status(report_string)
			teststatus = "testcase_send_req_n_validate_audi_entry:FAIL"
			report_status(teststatus)
			driver.quit()
	except :
		report_string = "Unable to validate to the send_req_n_validate_audi_entry module"
		report_status(report_string)
		teststatus = "testcase_send_req_n_validate_audi_entry:FAIL"
		report_status(teststatus)
		driver.quit()
		
