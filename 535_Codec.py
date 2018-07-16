import string
import random
letters = string.ascii_letters + string.digits
full_url = {}
tiny_url = {}

class Codec:
	def encode(self, longUrl):
		"""Encodes a URL to a shortened URL.
		
		:type longUrl: str
		:rtype: str
		"""

		def six_addr():
			short_url = ""
			for i in range(6):
				char = letters[random.randint(0, 1000)%62]
				short_url += char
			return short_url

		if longUrl in full_url:
			return "http://tinyurl.com/" + full_url
		else:
			short = six_addr()
			full_url[longUrl] = short 
			tiny_url[short] = longUrl
			return "http://tinyurl.com/" + short
		

	def decode(self, shortUrl):
		"""Decodes a shortened URL to its original URL.
		
		:type shortUrl: str
		:rtype: str
		"""
		shortUrl = shortUrl.split("/")[-1]
		if shortUrl in tiny_url:
			return tiny_url[shortUrl]
		else:
			return None
		

# Your Codec object will be instantiated and called as such:
url = "https://blog.csdn.net/memoryjdch/article/details/78261239"
codec = Codec()
print(codec.decode(codec.encode(url)))
