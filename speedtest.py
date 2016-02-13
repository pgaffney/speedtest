#!/usr/bin/python
import os
import sys
import csv
import datetime
import time
from twython import Twython

def test():

        #run speedtest-cli
        print '  running speedtest'
        speedtestResults = os.popen("speedtest-cli --simple").read()
        print '  speedtest complete'
        #split the 3 line result (ping,down,up)
        testResultsLines = speedtestResults.split('\n')

        currentTime = time.time()
        date = datetime.datetime.fromtimestamp(currentTime).strftime('%Y-%m-%d %H:%M:%S')
        
        #if speedtest could not connect set the speeds to 0
        if "Cannot" in speedtestResults:
                ping = 100
                download = 0
                upload = 0

        #extract the values for ping down and up values
        else:
                ping = testResultsLines[0][6:11]
                download = testResultsLines[1][10:14]
                upload = testResultsLines[2][8:12]

        print '  speedtest results=', date, ' ping=', ping, ' download=', download, ' upload=', upload

        #append the data to file
        print '  writing to file'
        outputFile = open('/var/www/assets/speedtest-data.csv', 'a')
        writer = csv.writer(outputFile)
        writer.writerow((currentTime*1000,ping,download,upload))
        outputFile.close()
        print '  write complete'

        #connect to twitter
        CONSUMER_KEY = '2NdKpaNZNRJSsaIgzvGJ0MrRA'
        CONSUMER_SECRET = 'CbJs1cMwDNSiiPWnGdEWMt9xB7bONRwE7kz5eMZzfFSKxsK1Ge'
        ACCESS_KEY = '19665109-e9xQmFkKiifQVyHvf9PHofpZZgMANbKSQ5vSdLpOg'
        ACCESS_SECRET = 'sft9DieLsRCwXD8oounOMUJy3gLNiPkFPZxfwg9ecriab'
        api = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)

        #tweet
        #api.update_status(status='Test status')

        #try to tweet if speedtest couldnt even connect. Probably wont work if the internet is down
        #if "Cannot" in a:
        #        try:
        #                tweet="Hey @Comcast @ComcastCares why is my internet down? I pay for 150down\\10up in Washington DC? #comcastoutage #comcast"
        #                twit.statuses.update(status=tweet)
        #        except:
        #                pass

        # tweet if down speed is less than whatever I set
        #elif eval(d)<50:
        #        print "trying to tweet"
        #        try:
        #                # i know there must be a better way than to do (str(int(eval())))
        #                tweet="Hey @Comcast why is my internet speed " + str(int(eval(d))) + "down\\" + str(int(eval(u))) + "up when I pay for 150down\\10up in Washington DC? @ComcastCares @xfinity #comcast #speedtest"
        #                twit.statuses.update(status=tweet)
        #        except Exception,e:
        #                print str(e)
        #                pass
        return
        
if __name__ == '__main__':
        print 'starting test cycle...'
        test()
        print 'test cycle completed'
