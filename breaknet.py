#-*- coding:utf-8 -*-
import os
import sys
import time
import requests
from bs4 import BeautifulSoup
import json

username = sys.argv[1]
ip = sys.argv[2]
macaddr = sys.argv[3]

class Logout:
    def getCurrentTime(self):
        return time.strftime('[%Y-%m-%d %H:%M:%S]',time.localtime(time.time()))

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


    def logout(self):
        print (self.getCurrentTime(), u"begin logout...")



        
        #url = "https://w.seu.edu.cn:801/eportal/?c=Portal&a=unbind_mac&callback=dr1003&user_account="+username+"&wlan_user_mac=F0761CF32C62&wlan_user_ip="+ip+"&jsVersion=3.3.2&v=3825 HTTP/1.1"

# GET https://w.seu.edu.cn:801/eportal/?c=Portal&a=unbind_mac&callback=dr1003&user_account=220194697&wlan_user_mac=F0761CF32C62&wlan_user_ip=121.248.51.32&jsVersion=3.3.2&v=7723 HTTP/1.1
# Accept: application/javascript, */*;q=0.8
# Referer: https://w.seu.edu.cn/
# Accept-Language: zh-Hans-CN,zh-Hans;q=0.5
# User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; LCTE; rv:11.0) like Gecko
# Accept-Encoding: gzip, deflate
# Host: w.seu.edu.cn:801
# Connection: Keep-Alive
# Cookie: PHPSESSID=urqm3p7o7pt8mqv359csj8md64

# GET https://w.seu.edu.cn:801/eportal/?c=Portal&a=unbind_mac&callback=dr1003&user_account=220194697&wlan_user_mac=F0761CF32C62&wlan_user_ip=121.248.51.32&jsVersion=3.3.2&v=3725 HTTP/1.1
# Accept: application/javascript, */*;q=0.8
# Referer: https://w.seu.edu.cn/
# Accept-Language: zh-Hans-CN,zh-Hans;q=0.5
# User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; LCTE; rv:11.0) like Gecko
# Accept-Encoding: gzip, deflate
# Host: w.seu.edu.cn:801
# Connection: Keep-Alive
# Cookie: PHPSESSID=urqm3p7o7pt8mqv359csj8md64

# GET https://w.seu.edu.cn:801/eportal/?c=Portal&a=unbind_mac&callback=dr1003&user_account=220194697&wlan_user_mac=B46D8332A7A8&wlan_user_ip=121.248.50.254&jsVersion=3.3.2&v=6923 HTTP/1.1
# Accept: application/javascript, */*;q=0.8
# Referer: https://w.seu.edu.cn/
# Accept-Language: zh-Hans-CN,zh-Hans;q=0.5
# User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; LCTE; rv:11.0) like Gecko
# Accept-Encoding: gzip, deflate
# Host: w.seu.edu.cn:801
# Connection: Keep-Alive
# Cookie: PHPSESSID=vuul47ocshfrh7n1p1j16svq45




#360
        # url = "https://w.seu.edu.cn:801/eportal/?c=Portal&a=unbind_mac&callback=dr1003&user_account="+username+"&wlan_user_mac=B46D8332A7A8&wlan_user_ip="+ip+"&jsVersion=3.3.2&v=6728 HTTP/1.1"
        # headers = {
        # "Host":"w.seu.edu.cn:801",
        # "Connection":"Keep-Alive",
        # "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; LCTE; rv:11.0) like Gecko",
        # "Accept":"application/javascript, */*;q=0.8",
        # "Referer":"https://w.seu.edu.cn/",
        # "Accept-Encoding":"gzip, deflate",
        # "Accept-Language":"zh-Hans-CN,zh-Hans;q=0.5",
        # "Cookie":"PHPSESSID=vuul47ocshfrh7n1p1j16svq45"
        # }
#firefox
# GET https://w.seu.edu.cn:801/eportal/?c=Portal&a=unbind_mac&callback=dr1003&user_account=220194697&wlan_user_mac=F0761CF32C62&wlan_user_ip=121.248.52.3&jsVersion=3.3.2&v=10302 HTTP/1.1
# Host: w.seu.edu.cn:801
# User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:73.0) Gecko/20100101 Firefox/73.0
# Accept: */*
# Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
# Accept-Encoding: gzip, deflate, br
# Connection: keep-alive
# Referer: https://w.seu.edu.cn/
# Cookie: gr_user_id=746ed3d1-431d-4c27-84f7-24997bd4d419; PHPSESSID=qp77egojhh0mpei0jsf4p1muk5




#1: F0D4E2E9F434
        url =  "https://w.seu.edu.cn:801/eportal/?c=Portal&a=unbind_mac&callback=dr1003&user_account="+username+"&wlan_user_mac="+macaddr+"&wlan_user_ip="+ip+"&jsVersion=3.3.2&v=10302 HTTP/1.1"
        headers = {
        "Host":"w.seu.edu.cn:801",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:73.0) Gecko/20100101 Firefox/73.0",
        "Accept":"*/*",
        "Accept-Language":"zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Accept-Encoding":"gzip, deflate, br",
        "Connection":"keep-alive",
        "Referer":"https://w.seu.edu.cn/",
        "Cookie":"gr_user_id=746ed3d1-431d-4c27-84f7-24997bd4d419; PHPSESSID=qp77egojhh0mpei0jsf4p1muk5"
        }
        try:
            r=requests.post(url,headers=headers)
            print(self.getCurrentTime(),r.text)
            time.sleep(10)
            can_connect = self.canConnect()
            if can_connect:
                print(self.getCurrentTime(),u'try to break failure!')
            else:
                print(self.getCurrentTime(),u'break succeed')
        except:
            print("break net post failure")
    def main(self):
        print(self.getCurrentTime(), u"Hi，welcome to the system of auto logout...")
        while self.canConnect():
            self.logout()
            time.sleep(5)
        print("execute finish")

if __name__ == "__main__":
    logout = Logout()
    logout.main()
