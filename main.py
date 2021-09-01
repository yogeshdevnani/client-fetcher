from bs4 import BeautifulSoup
import requests
import os

def companyFetcher(compName): #from Zauba Corp
    print (f'Company Name : {compName}')
    compName = compName.split()
    compName = '-'.join(compName)
    url = "https://www.zaubacorp.com/companysearchresults/" + compName

    #fetching the HTML code
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text,'lxml')

    searchResults = soup.find(class_ = 'region region-content')
    #print (searchResults)

    #if the search result has a link
    linksFetch = searchResults.find_all('a')
    links = []
    for link in linksFetch:
        links.append (link['href'])
        infoFetcher(link['href'])
        print ("-"*25)

    print (f'Number of Records Found : {len(links)}')



def infoFetcher(companyURL):
    html_resp = requests.get(companyURL).text
    infoSoup = BeautifulSoup(html_resp,'lxml')

    companyNameTag = infoSoup.find('div', class_ = 'container edg edg-cont')
    print (companyNameTag.h1.text)

    nameTag = infoSoup.find_all('div', class_ = 'col-lg-12 col-md-12 col-sm-12 col-xs-12')

    avoidNames = ['Login', 'View other directorships']
    for name in nameTag:
        try:
            if name.h4.text.strip() == 'Director Details':
                nameData = name.find_all('a')
                for personName in nameData:
                    if (personName.text not in avoidNames):
                        print (personName.text)
                        #continue
        except:
            continue




    dataTag = infoSoup.find('div', class_ = 'col-12')
    emailData = dataTag.p.text
    email = emailData.split()[-1]
    print (email)







companyName = input("Enter company's name:\t")
# companyName = 'Ken Origin Limited'
companyFetcher(companyName)
# infoFetcher('https://www.zaubacorp.com/company/KEN-ORIGIN-LIMITED/U45200JH2006PLC012638')