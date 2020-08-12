import requests
from bs4 import BeautifulSoup

def connect_addr():
	try:
		baidu_request = requests.get("http://www.baidu.com",timeout=(1,1))
		if (baidu_request.status_code == 200):
		    baidu_request.encoding = baidu_request.apparent_encoding
		    baidu_request_bsObj = BeautifulSoup(baidu_request.text, 'html.parser')
		    baidu_input = baidu_request_bsObj.find(value="百度一下")
		    if baidu_input == None:
		        return False
		    return True
		return False
	except:
		return False

if __name__ == "__main__":
	BOOL = connect_addr()
	print(BOOL)