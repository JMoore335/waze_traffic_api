#!/usr/bin/env python

import os, sys
from datetime import datetime
import requests
from collections import namedtuple
import csv
from time import sleep
import re
import time

#5th decimal == 1.1 m
#6th decimal == 0.11 m
#7th decimal == 11.0 mm


#Append 'a', Overwrite 'wb'
fd = open('ga_state.csv', 'a')
write = csv.writer(fd)

ft = open('gsp_county.csv', 'a')
write2 = csv.writer(ft)

ga_state = []
gsp_county = []
k = 0
j = 0
p = 0
while k < 10:
    #GEORGIA (STATE)
    r = requests.get('http://localhost:8080/waze/traffic-notifications?latBottom=30.335586&latTop=35.030596&lonLeft=-85.297852&lonRight=-81.518555')

    #GREENVILLE + SPARTANBURG (COUNTY)
    r2 = requests.get('http://localhost:8080/waze/traffic-notifications?latBottom=34.667401&latTop=35.216753&lonLeft=-82.600708&lonRight=-81.672363')



    #HERE, VARIABLE (i) REPRESENTS INDIVIDUAL ITERATIONS OF POLICE PER REPORT. SO IF THE REPORT HAS 12 NOTIFICATIONS, THEN (i) WOULD NEED TO BE AT LEAST 12.
    i = 0
    while i < 500:
        try:
            if r.json()['alerts'][i]['type'] == 'POLICE':
                ga_state.append([r.json()['alerts'][i]['type'], r.json()['alerts'][i]['latitude'], r.json()['alerts'][i]['longitude'], r.json()['alerts'][i]['numOfThumbsUp'], r.json()['alerts'][i]['subType']]) if ([r.json()['alerts'][i]['latitude'], r.json()['alerts'][i]['longitude'], r.json()['alerts'][i]['numOfThumbsUp'], r.json()['alerts'][i]['subType']]) not in ga_state else None

            if r2.json()['alerts'][i]['type'] == 'POLICE':
                gsp_county.append([r2.json()['alerts'][i]['type'], r2.json()['alerts'][i]['latitude'], r2.json()['alerts'][i]['longitude'], r2.json()['alerts'][i]['numOfThumbsUp'], r2.json()['alerts'][i]['subType']]) if ([r2.json()['alerts'][i]['latitude'], r2.json()['alerts'][i]['longitude'], r2.json()['alerts'][i]['numOfThumbsUp'], r2.json()['alerts'][i]['subType']]) not in gsp_county else None

                #print r.json()['alerts'][i]['latitude']
                #print r.json()['alerts'][i]['longitude']
                #print r.json()['alerts'][i]['subType']
                #print r.json()['alerts'][i]['numOfThumbsUp']

            i = i + 1
        except KeyboardInterrupt:
            print "KEYBOARD INTERRUPTED"
            sys.exit()
        except:
            break


    i = 0
    while i < 500:
        try:
            if gsp_county[i][0] == 'POLICE':
                write.writerow([gsp_county[i][0], gsp_county[i][1], gsp_county[i][0], gsp_county[i][0], gsp_county[i][0], gsp_county[i][0], gsp_county[i][0],])



            if r2.json()['alerts'][i]['type'] == 'POLICE':
                gsp_county.append([r2.json()['alerts'][i]['latitude'], r2.json()['alerts'][i]['longitude'], r2.json()['alerts'][i]['numOfThumbsUp'], r2.json()['alerts'][i]['subType']]) if ([r2.json()['alerts'][i]['latitude'], r2.json()['alerts'][i]['longitude'], r2.json()['alerts'][i]['numOfThumbsUp'], r2.json()['alerts'][i]['subType']]) not in gsp_county else None

                #print r.json()['alerts'][i]['latitude']
                #print r.json()['alerts'][i]['longitude']
                #print r.json()['alerts'][i]['subType']
                #print r.json()['alerts'][i]['numOfThumbsUp']

            i = i + 1
        except KeyboardInterrupt:
            print "KEYBOARD INTERRUPTED"
            sys.exit()
        except:
            break




    print "SLEEP 1800 SECONDS (30 MIN)."
    time.sleep(1800)
    k = k + 1

#FETCH LOOP END
#NOW REMOVE DUPLICATES


#a = 0
#while a < 300:
#    try:
        #print r.json()['alerts'][a]['latitude'], r.json()['alerts'][a]['longitude']
#        print r.json()['alerts'][a]['latitude'] + ',' + r.json()['alerts'][a]['longitude']

#        a = a + 1
#    except KeyboardInterrupt:
#        print "KEYBOARD INTERRUPTED"
#        sys.exit()
#    except:
#        print "LIST FINISHED"
#        sys.exit()


#fd = open('bf_trades_3.csv', 'wb')
#write = csv.writer(fd)

#print r.status_code
#print r.headers['content-type']


