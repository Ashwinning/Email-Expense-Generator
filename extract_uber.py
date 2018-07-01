from bs4 import BeautifulSoup
import pdfkit

#Accepts a soup and returns the total fare
def GetDetails(soup):
    details = {}
    details['totalPrice'] = soup.find_all("td", class_="totalPrice")[0].get_text()
    dateAndRideType = soup.find_all("td", class_="rideInfo gray")[0].get_text()
    keyVal = dateAndRideType.split('|')
    details['date'] = keyVal[0].strip()
    details['rideType'] = keyVal[1].strip()
    startTime = soup.find_all("td", class_="firstAddress")[0].contents[0].get_text()
    details['startTime']=startTime.split("|")[0].strip()
    endTime = soup.find_all("td", class_="address")[1].contents[0].get_text()
    details['endTime']=endTime.split("|")[0].strip()
    details['startAddress'] = soup.find_all("td", class_="firstAddress")[0].contents[1].get_text().strip()
    details['endAddress'] = soup.find_all("td", class_="address")[0].contents[1].get_text().strip()
    details['distance'] = soup.find_all("td", class_="tripInfo")[0].get_text().strip()
    details['time'] = soup.find_all("td", class_="tripInfo")[1].get_text().strip()
    return details

'''
with open('emails/html/files.txt', 'r') as file:
    for line in file:
        data = line.split(',')
        with open(data[2], 'r') as html:
            pdfkit.from_file(f, '{}.pdf'.format(data[]))
'''
