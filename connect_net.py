#-*- coding:utf-8 -*-
import os
import sys
import time
import requests
from bs4 import BeautifulSoup

username = sys.argv[1]
passwd = sys.argv[2]
ip = sys.argv[3]

class Login:
    def __init__(self):
        self.every = 10     #set delay time

    #get time now
    def getCurrentTime(self):
        return time.strftime('[%Y-%m-%d %H:%M:%S]',time.localtime(time.time()))

    #jungle whether can connect the internet
    def canConnect(self):
        try:
            baidu_request = requests.get("http://www.baidu.com")
            if (baidu_request.status_code == 200):
                baidu_request.encoding = baidu_request.apparent_encoding
                baidu_request_bsObj = BeautifulSoup(baidu_request.text, 'html.parser')
                baidu_input = baidu_request_bsObj.find(value="百度一下")
                if baidu_input == None:
                    return False
                else:
                    return True
            else:
                return False
        except:
            return False


    def login(self):
        print (self.getCurrentTime(), u"connecting...")
        url="https://w.seu.edu.cn:801/eportal/?c=Portal&a=login&callback=dr1003&login_method=1&user_account=%2C0%2C"+username+"&user_password="+passwd+"&wlan_user_ip="+ip+"&wlan_user_ipv6=&wlan_user_mac=000000000000&wlan_ac_ip=&wlan_ac_name=jlh_me60&jsVersion=3.3.2&v=7707 HTTP/1.1"   #9745
        #Header

# GET https://w.seu.edu.cn:801/eportal/?c=Portal&a=login&callback=dr1003&login_method=1&user_account=%2C0%2Cxxxxxxxxxx&user_password=xxxxxx&wlan_user_ip=121.248.50.254&wlan_user_ipv6=&wlan_user_mac=000000000000&wlan_ac_ip=&wlan_ac_name=jlh_me60&jsVersion=3.3.2&v=3344 HTTP/1.1
# Accept: application/javascript, */*;q=0.8
# Referer: https://w.seu.edu.cn/a79.htm?UserIP=121.248.50.254&wlanacname=jlh_me60
# Accept-Language: zh-Hans-CN,zh-Hans;q=0.5
# User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; LCTE; rv:11.0) like Gecko
# Accept-Encoding: gzip, deflate
# Host: w.seu.edu.cn:801
# Connection: Keep-Alive
# Cookie: PHPSESSID=vuul47ocshfrh7n1p1j16svq45


        headers={
        "Accept":"application/javascript, */*;q=0.8",
        "Referer":"https://w.seu.edu.cn/a79.htm?UserIP="+ip+"&wlanacname=jlh_me60",
        "Accept-Language":"zh-Hans-CN,zh-Hans;q=0.5",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; LCTE; rv:11.0) like Gecko",
        "Accept-Encoding":"gzip, deflate",
        "Host":"w.seu.edu.cn:801",
        "Connection":"Keep-Alive",
        "Cookie":"PHPSESSID=urqm3p7o7pt8mqv359csj8md64"
        }
        #post information
        #payload={        }
        try:
            r=requests.post(url,headers=headers)
            time.sleep(5)
            can_connect = self.canConnect()
            if can_connect:
                print(self.getCurrentTime(),u'connected!')
            else:
                print(self.getCurrentTime(),u'try to connect failure!')
        except:
            print("post failure")

    #man function
    def main(self):
        print(self.getCurrentTime(), u"Hi，welcome to the system of auto login...")
        while True:
            can_connect = self.canConnect()
            if not can_connect:
                print(self.getCurrentTime(),u"internet breaked...")
                self.login()
            else:
                print(self.getCurrentTime(), u"all normal...")
            time.sleep(self.every)

if __name__ == "__main__":
    os.system("clear")
    login = Login()
    login.main()

