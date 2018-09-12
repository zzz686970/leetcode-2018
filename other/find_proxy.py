import re
import os
import sys
import request
from urllib import request, parse
import random
from bs4 import BeautifulSoup

content = request.urlopen("http://www.proxynova.com/proxy-server-list/country-cn/").read()
soup = BeautifulSoup(content, 'lxml')

print(soup)