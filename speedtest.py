#!/usr/bin/python
import csv
import datetime
import os
import time

from twython import Twython

# twitter constants
CONSUMER_KEY = '2NdKpaNZNRJSsaIgzvGJ0MrRA'
CONSUMER_SECRET = 'CbJs1cMwDNSiiPWnGdEWMt9xB7bONRwE7kz5eMZzfFSKxsK1Ge'
ACCESS_KEY = '19665109-e9xQmFkKiifQVyHvf9PHofpZZgMANbKSQ5vSdLpOg'
ACCESS_SECRET = 'sft9DieLsRCwXD8oounOMUJy3gLNiPkFPZxfwg9ecriab'


def test():
    # run speedtest-cli
    print '  running speedtest'
    speedtest_results = os.popen("speedtest-cli --simple").read()
    print '  speedtest complete'
    # split the 3 line result (ping,down,up)
    test_results_lines = speedtest_results.split('\n')

    current_time = time.time()
    date = datetime.datetime.fromtimestamp(current_time).strftime('%Y-%m-%d %H:%M:%S')

    # if speedtest could not connect set the speeds to 0
    if "Cannot" in speedtest_results:
        ping = 100
        download = 0
        upload = 0

    # extract the values for ping down and up values
    else:
        ping = test_results_lines[0][6:11]
        download = test_results_lines[1][10:14]
        upload = test_results_lines[2][8:12]

    print '  speedtest results=', date, ' ping=', ping, ' download=', download, ' upload=', upload

    # append the data to file
    print '  writing to file'
    output_file = open('/var/www/assets/speedtest-data.csv', 'a')
    writer = csv.writer(output_file)
    writer.writerow((current_time * 1000, ping, download, upload))
    output_file.close()
    print '  write complete'

    # connect to twitter
    # api = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET)

    # tweet
    # api.update_status(status='Test status')

    # try to tweet if speedtest couldnt even connect. Probably wont work if the internet is down
    # if "Cannot" in a:
    #        try:
    #                tweet="Hey @Comcast @ComcastCares? #comcastoutage #comcast"
    #                twit.statuses.update(status=tweet)
    #        except:
    #                pass

    # tweet if down speed is less than whatever I set
    # elif eval(d)<50:
    #        print "trying to tweet"
    #        try:
    #                # i know there must be a better way than to do (str(int(eval())))
    #                tweet="Hey @Comcast why  " + str(int(eval(d))) + "down\\" + str(int(eval(u)))
    #                twit.statuses.update(status=tweet)
    #        except Exception,e:
    #                print str(e)
    #                pass
    return

print 'starting test cycle...'
test()
print 'test cycle completed'
