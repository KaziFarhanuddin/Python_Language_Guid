''' This is to illustrate request module in python for simple request '''
import requests

url = 'https://pythonprogramming.net'
payload = {'q': 'python3'}
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17'}

RESPONES = requests.get(url, params=payload, headers=headers)


print(RESPONES.content)	# In byte object

print()

print(RESPONES.text)	#In str object

print()

print(RESPONES.url)		#Get the url

# To download sometning 
res= requests.get('https://proxy.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.PeUFUDphAWQBWxUCSncALAHaHa%26pid%3D15.1&f=1')
with open('a.png', 'wb') as file:
	for chunk in res.iter_content(chunk_size=1024):
		file.write(chunk)