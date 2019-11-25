# encoding=utf8
import gmail
from Settings import *
from datetime import datetime
import csv
import os

#Initialize this at the beginning of the lifecycle.
getSettings = GetSettings()
g = gmail.login(settings['username'], settings['password'])

excel = []

#emails = g.inbox().mail(after=datetime(2016, 12, 31), sender="Uber Receipts")
emails = g.mailbox('advantEdge Expense').mail(after=datetime(2019, 10, 31), before=datetime(2019, 11, 26))
print str(len(emails)) + " emails found"
i = 0
for email in emails[:]:
	email.fetch()
	datetime = date = str(email.sent_at)
	date = str(email.sent_at).split(' ')[0]
	filepath = "emails/November 2019/"
	if not os.path.exists(filepath):
		os.makedirs(filepath)
	filename = filepath + date + ' ({}).html'.format(str(i))
	fileLink = date + ' ({}).html'.format(str(i))
	file = open(filename ,"w")
	file.write(str(email.html))
	file.close()
	data = {'datetime': datetime, 'from': email.fr, 'subject':  email.subject, 'date': date, 'filename': '=HYPERLINK("{}")'.format(fileLink)}
	excel.append(data)
	#print "Wrote " + str(i) +".html"
	i+=1

sortedlist = sorted(excel, key=lambda k: k['datetime'])

with open(filepath + 'Expenses.csv', 'wb') as f:
	w = csv.DictWriter(f, sortedlist[0].keys())
	w.writeheader()
	w.writerows(sortedlist)
