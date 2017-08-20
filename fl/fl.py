#!/usr/bin/env python
import requests
import time
import re
import sys
import getpass
import signal
from bs4 import BeautifulSoup

a = 0

def liveSession( html ):
    a = 0
    run = True
    while run:
        a = a + 1
        for i in range(1000):
            time.sleep(1)
            # sys.stdout.write("\r%d times refreshed! Next Refresh in %3d seconds" % (a, 1000-i))
            # sys.stdout.flush()
        soup = BeautifulSoup(html, "html.parser")
        script = soup.script.string
        arrayString = re.findall('"([^"]*)"', script)
        url = arrayString[0]
        html = requests.get(url).text

    return



def login():
    soup = BeautifulSoup(requests.get('http://9gag.com').text , "html.parser")

    Magic = soup.find("input", {'name': "magic"}).attrs['value']
    Tredir = soup.find("input", {'name': "4Tredir"}).attrs['value']

    # UserName = raw_input('IITK user name:')
    # Password = getpass.getpass('Password:')

    payload = {'4Tredir': Tredir, 'magic': Magic, 'username': 'kshivang', 'password': 'Kuchnaya'}

    f = requests.post('https://gateway.iitk.ac.in:1003', data = payload);

    soup = BeautifulSoup(f.text , "html.parser")
    if soup.h2.string is not None:
        str = soup.h2.string
        print str
        substr = 'again'
        if substr in str:
            return True

    print "Fortinet Logged in!"
    liveSession(f.text)
    return False

def signal_handler(signal, frame):
    requests.get('https://gateway.iitk.ac.in:1003/logout?0501030a00253727')
    print '\nYou are logged out!'
    sys.exit(0)



signal.signal(signal.SIGINT, signal_handler)
requestLogout = requests.get('https://gateway.iitk.ac.in:1003/logout?0501030a00253727')
time.sleep(1)

if re.match('(200)|(303)', str(requestLogout.status_code)) is not None :

    while login():
        print "Try Again!"

else:
    print "Internet connection Problem!"


