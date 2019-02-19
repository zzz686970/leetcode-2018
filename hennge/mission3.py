import requests 
import hashlib 
import hmac 
import base64
import json
from otp import *
from hashlib import sha512
# from hotpie import HOTP, TOTP


"""steps to generate TOTP
Generate a key, K, which is an arbitrary bytestring, and share it securely with the client.
Agree upon an epoch, T0, and an interval, TI, which will be used to calculate the value of the counter C (defaults are the Unix epoch as T0 and 30 seconds as TI)
Agree upon a cryptographic hash method (default is SHA-1)
Agree upon a token length, N (default is 6)
"""

username = 'E0146282@u.nus.edu'

url = 'https://hdechallenge-solve.appspot.com/challenge/003/endpoint'
payload = {'github_url':'https://gist.github.com/zzz686970/bb161e3e63c78fdc66106d3695db13c3',
			'contact_email':username}

shared_secret = username + 'HDECHALLENGE003'

headers = {'Content-Type':'application/json',
			'Host': 'admissionchallenge.example.com',
			'Accept': '*/*',
			'Content-Length': '104'
			}
## new instance
# passwd = TOTP(K = b'E0146282@u.nus.eduHDECHALLENGE003', digits = 10, digestmod=sha512)

# print(passwd)

# print(username, passwd)
# key = b'E0146282@u.nus.eduHDECHALLENGE003'
# passwd = TOTP(key, digits=10, window=30, digestmod=sha512)      # <time-based-value>
# print(passwd)
# content = requests.post(url, data = json.dumps(payload), headers = headers, auth = (username, passwd))
# print(content.text)
# # ## print request headers
# post_Authorization = dict(content.request.headers).get('Authorization')
# post_pass = post_Authorization.split(' ')[-1]
# print(base64.b64decode((post_pass).encode('utf-8')))
# b'E0146282@u.nus.edu:1360773359'
# 1137242573

### test
# b'ninja@example.com:1773133250'
# 0x69afddc2

import time
import datetime
s = "Mon, 17 Mar 2014 15:20:51 GMT"
## 1395069651 ?
# 1395040851


timestamp = 1395069651

#转换成localtime
time_local = time.localtime(timestamp)
#转换成新的时间格式(2016-05-05 20:28:54)
dt = time.strftime("%Y-%m-%d %H:%M:%S",time_local)
print(dt)

timestamp2 = time.mktime(time.strptime(s, '%a, %d %b %Y %H:%M:%S GMT'))
passwd = TOTP(K = b'6E696E6A61406578616D706C652E636F6D4844454348414C4C454E4745303033',  digits = 10, clock = 1395069651, digestmod=sha512).zfill(10)

print(passwd)
# 0259575741   1436253523
## 1116017629  1084217382
## 0x428513dd   
# 1467508979   0215534052
# 2122929532   1450749009
# 1060211184
# Successful TOTP generated: 1773133250, for time of Mon, 17 Mar 2014 15:20:51 GMT
## original 3723c28513dd6d3b6d22af67de6e36fe8c5d56ee0ab9cf2ec6912a654539ded258a1d14963d23506e268e075a869099fb4ded3f526df760258941a8fb91a9e62

## d5 52 e2 04 2cacfe 2a8632e2 4214 559b7d53  46c4dcf3eb021f2133eafc546440aaa57b0806c4874dce52e8b921ee3b1cfd54544cfea493f6adeb4aaad145c9587d
