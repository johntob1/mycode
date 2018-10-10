#!/usr/bin/env python3

import re

loginfail = 0
loginpass = 0
failedIPList = []

keystone_file = open('/home/student/mycode/attemptlogin/keystone.common.wsgi', 'r')
keystone_file_lines = keystone_file.readlines()
for i in keystone_file_lines:
    if "- - - - -] Authorization failed." in i:
        loginfail = loginfail + 1
        failedIPList.append(re.findall(r'[0-9]+(?:\.[0-9]+){3}', i)) 
    elif "- - - - -] Loaded 2 encryption keys" in i:
        loginpass = loginpass + 1

print('The number of failed log in attempts is '+ str(loginfail))
print('failed IPs ', failedIPList)
print('The number of succesful logins is '+ str(loginpass))
