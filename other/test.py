import zipfile
import re
import sys


def get_file():
    if sys.version[0] == '3':
        import urllib.request
        urllib.request.urlretrieve('http://www.pythonchallenge.com/pc/def/channel.zip','./channel.zip')
    else:
        import urllib
        urllib.urlretrieve('http://www.pythonchallenge.com/pc/def/channel.zip','./channel.zip')

  
get_file()
zip_file=zipfile.ZipFile('./channel.zip')

file_list=[]
next_str='90052'
file_content=zip_file.read('%s.txt' % next_str).decode('utf-8')
while next_str:
    file_list.append("%s.txt" % next_str)
    next_str=re.compile('Next nothing is ([0-9]+)').match(file_content)
    if next_str:
        next_str=next_str.groups()[0]
        file_content=zip_file.read('%s.txt' % next_str).decode('utf-8')
        # print( file_content)
    else:
        break
    
# print: Collect the comments.
print ("".join([zip_file.getinfo(i).comment.decode('utf-8') for i in file_list]))
