#focusmode=true

import time
from datetime import datetime as dt

host_path = "C:\Windows\System32\drivers\etc\hosts" #host file location
redirect = "127.0.0.1" #redirect to localhost

site_list = ['facebook.com','www.facebook.com','twitter.com','www.twitter.com','reddit.com','www.reddit.com','news.ycombinator.com','www.news.ycombinator.com','craigslist.org']

while True:
    #if current time is between 9am and 6pm
    if dt(dt.now().year,dt.now().month,dt.now().day,9) < dt.now() <dt(dt.now().year,dt.now().month,dt.now().day,18):
        #open host in read and write mode
        with open(host_path,"r+") as file:
            content = file.read()
            for website in site_list:
                #if site is already in hostfile
                if website in content:
                    pass
                else:
                    file.write(redirect+' '+website+'\n')
        print('focusmode=on')
        break
    else:
        with open(host_path, 'r+') as file:
            content = file.readlines()
            file.seek(0)

            for line in content:
                if not any(website in line for website in site_list):
                    file.write(line)
            file.truncate()
        print('focusmode=off')
        break
    