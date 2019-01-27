import bs4 as bs
from multiprocessing import Pool
import random
import string
import requests


def handel_local_links(url, link):
	if link.startswith('/'):
		return ''.join([url, link])
	else:
		return link

def random_url():
	starting = ''.join(random.SystemRandom().choice(string.ascii_lowercase) for _ in range(3))
	url = ''.join(['http://', starting, '.com'])
	return url

def get_link(url):
	try:
		req = requests.get(url)
		soup = bs.BeautifulSoup(req.text, 'lxml')
		body = soup.body
		links = [link.get('href') for link in body.find_all('a')]
		links = [handel_local_links(url, link) for link in links]
		links = [str(link.encode('ascii')) for link in links]
		return links

	except TypeError as e:
		print(e)
		print("Got a no links on page")
		return []
	except IndexError as e:
		print(e)
		print("Dident find any useful links")
		return []
	except AttributeError as e:
		print(e)
		print("Likely got None for link")
		return []
	except Exception as e:
		print(e)
		return []

def main():
	how_mani = 50 
	p=Pool(processes=how_mani)
	parse_us = [random_url() for _ in range(how_mani) ]
		
	data = p.map(get_link, [link for link in parse_us])
	data = [url for url_list in data for url in url_list]
	p.close()

	with open('urls.txt', 'w') as f:
		f.write(str(data))

if __name__ == '__main__':
	main()

