import requests
from bs4 import BeautifulSoup

def make_request(url):
	r = requests.get(url, verify=False)
	#html = r.text
	#soup = BeautifulSoup(html, 'html.parser')
	return r

def wordpress_login_exists(url:str):
	''' looks for wp-login.php page for a given url 
	>>> bool
	'''

	# TODO sanitze url (starts with http ends with /)
	if url[0:4] == "http" and url[-1] == "/":
		try:
			r_url=url+'wp-login.php'
			r = make_request(url+"wp-login.php")
			if r:
				# print(f"request for {r.url} got status {r.status_code} [{r.url == r_url}]")
				if r and r.ok  and (r.status_code == 200):
					return r.url == r_url
		except Exception as e:
			print(e)

		return False