import gmail
from Settings import *
from datetime import datetime
import time

#Initialize this at the beginning of the lifecycle.
getSettings = GetSettings()
g = gmail.login(settings['username'], settings['password'])

#Give this session a name
sessionName = str(time.time()) #the name is the timestamp as string - change later

#Download all emails and create a metafile
emails = g.mailbox('advantEdge Expense').mail(after=datetime(2018, 03, 31))
print str(len(emails)) + " emails found"
i = 0;
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
    #If the email is from Uber, extract rideInfo
    #Convert emails to pdf
    #Write csv with pdf links
    i+=1
metaFile.close()

#create a tarball of the Download
#upload to s3 or something
#delete sessionName folder recursively 
