#!/bin/python3

import sys
import os
from urllib.request import Request
from urllib.request import urlopen
from urllib.error import URLError
import json

import requests 

# Complete the function below.

def getMovieTitles(substr):
    substr = substr.lower()
    total_page = 0
    result = {}
    url = 'https://jsonmock.hackerrank.com/api/movies/search/?Title=%s' %(substr)
    content = requests.get(url).content 

    json_content = json.loads(content)
    total_page = json_content['total_pages']

    for i in range(0, total_page+1):
        url = 'https://jsonmock.hackerrank.com/api/movies/search/?Title=%s&page=%s' %(substr, i)
        content = requests.get(url).content 
        json_content = json.loads(content)
        for el in json_content['data']:
            if 'Title' in el and substr in  el['Title'].lower():
                result[el['imdbID']]  = el['Title']
    res = [val for val in result.values() ]
    res.sort()
    return res


    
f = open(os.environ['OUTPUT_PATH'], 'w')
    

try:
    _substr = str(input())
except:
    _substr = None

res = getMovieTitles(_substr)
for res_cur in res:
    f.write( str(res_cur) + "\n" )

f.close()



