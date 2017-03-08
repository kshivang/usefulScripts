#!/usr/bin/env python
import requests
import time
import re
import sys
import getpass
import signal
from bs4 import BeautifulSoup

def liveSession( html ):
    a = 0
    run = True
    while run:
        a = a + 1
        # for i in range(100):
        time.sleep(60)
            # sys.stdout.write("\r%d times refreshed! Next Refresh in %3d seconds" % (a, 100-i))
            # sys.stdout.flush()
        print("\r%d times refreshed!" % (a))
        soup = BeautifulSoup(html, "html.parser")
        script = soup.script.string
        arrayString = re.findall('"([^"]*)"', script)
        url = arrayString[0]
        try:
            r = requests.get(url)
            if r.status_code == 200:
                html = r.text
        except requests.exceptions.ConnectionError:
            print("Network error")
            return

def login():
    requestLogout = requests.get('https://gateway.iitk.ac.in:1003/logout?0501030a00253727')

    time.sleep(1)

    soup = BeautifulSoup(requests.get('http://google.com').text , "html.parser")

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
    return True

# Override ^C call to log out and exit  
signal.signal(signal.SIGINT, signal_handler)

def signal_handler(signal, frame):
    requests.get('https://gateway.iitk.ac.in:1003/logout?0501030a00253727')
    print '\nYou are logged out!'
    sys.exit(0)

# If on fortinet server run script
if re.match('(200)|(303)', str(requestLogout.status_code)) is not None :
    while login() :
        print "Connection interruted, retrying!"
else :
    print "Not on fortinet network"

exit()

