''' This script shows basic interraction with web using urllib'''
import urllib
import urllib.parse
import urllib.request

url = 'https://pythonprogramming.net'
value = {'q': 'python3'}
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17'}

# Hear we are encoding the values to be searched
data = urllib.parse.urlencode(value)
data=data.encode('utf-8')

# Making request object 
request = urllib.request.Request(url, data,headers=headers)

# Make a request and store the response
response = urllib.request.urlopen(request)

# Reading data
data = response.read()

#Decoading data
decoded_data = data.decode('utf-8')

print(decoded_data)


# To download sometning 
urllib.request.urlretrieve("https://proxy.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.PeUFUDphAWQBWxUCSncALAHaHa%26pid%3D15.1&f=1", "a.png")