import gmail
from Settings import *
from datetime import datetime

#Initialize this at the beginning of the lifecycle.
getSettings = GetSettings()
g = gmail.login(settings['username'], settings['password'])

#emails = g.inbox().mail(after=datetime(2016, 12, 31), sender="Uber Receipts")
emails = g.mailbox('advantEdge Expense').mail(after=datetime(2018, 03, 31))
print str(len(emails)) + " emails found"
i = 0;
metaFile = open("emails/html/files.txt","a") #store metadata
for email in emails[:]:
    email.fetch()
    #file = open("emails/html/"+ str(i) +".html","w")
    #file.write(email.html)
    #file.close()
    meta = "{}, {}, emails/html/{}.html, {}".format(email.fr, email.subject, str(i), email.sent_at)
    print meta
    metaFile.write(meta)
    #print "Wrote " + str(i) +".html"
    i+=1
metaFile.close()
