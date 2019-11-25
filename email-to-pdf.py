import gmail
from Settings import *
from datetime import datetime
import time
from bs4 import BeautifulSoup
from extract_uber import *
import pdfkit
import os

#Initialize this at the beginning of the lifecycle.
getSettings = GetSettings()
g = gmail.login(settings['username'], settings['password'])

#Give this session a name
sessionName = str(time.time()) #the name is the timestamp as string - change later

#Download all emails and create a metafile
emails = g.mailbox('advantEdge Expense').mail(after=datetime(2018, 03, 31))
print str(len(emails)) + " emails found"
i = 0;

directory = "emails/{}/html/".format(sessionName)
if not os.path.exists(directory):
    os.makedirs(directory)
    os.makedirs("emails/{}/pdf/".format(sessionName))

metaFile = open("emails/{}/html/files.txt".format(sessionName),"a") #store metadata
for email in emails[:]:
    email.fetch()
    file = open("emails/"+sessionName+"/html/"+str(i)+".html","w")
    file.write(email.html)
    file.close()
    meta = "{}, {}, emails/{}/html/{}.html, {}\n".format(email.fr, email.subject, sessionName, str(i), email.sent_at)
    print meta
    metaFile.write(meta)
    #print "Wrote " + str(i) +".html"
    #Convert email to pdf
    #pdfkit.from_file("emails/"+sessionName+"/html/"+str(i)+".html", "emails/"+sessionName+"/pdf/"+str(i)+".pdf")
    ### JUST DO IT
    #Write Excel Data
    #If the email is from Uber, extract rideInfo
    '''
    if "uber" in email.fr:
        rideInfo = GetDetails(BeautifulSoup(email.html))
        #Write csv with pdf links & rideInfo where applicable
    '''
    i+=1
metaFile.close()
