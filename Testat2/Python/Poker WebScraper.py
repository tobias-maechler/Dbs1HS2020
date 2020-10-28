import bs4
import urllib
import random
from urllib.request import Request

### Tasks
# First 1000 player from the ATM are Pros
# 1001 - 10'000 are Beginners
# New Field 'Preisgeld'
# In DB create 150 Tournaments
# In DB create 100 Qualifyings

# Init Lists

surNames = []
familyNames = []
prizes = []

# First Pass

req = Request('https://pokerdb.thehendonmob.com/ranking/all-time-money-list/', headers={'User-Agent': 'Mozilla/5.0'})

source = urllib.request.urlopen(req).read()

html = bs4.BeautifulSoup(source, 'html.parser')

for n in html.find_all(class_ = 'name'):
    cleanName = n.text.strip()
    cleanName = cleanName.replace("\'", "")
    fullName = cleanName.rsplit(' ', 1)
    surNames.append(fullName[0])
    familyNames.append(fullName[1])

for p in html.find_all(class_ = 'prize'):
    pClean = p.text.strip()
    pNew = pClean[2:].replace(',', '')
    if pNew != '' and pNew.isdigit():
        prizes.append(pNew)

print("Finished pass 1")

# Pass 2 - 100
"""
for i in range(2, 101):
    req = Request(f'https://pokerdb.thehendonmob.com/ranking/all-time-money-list/{i}', headers={'User-Agent': 'Mozilla/5.0'})
    source = urllib.request.urlopen(req).read()
    html = bs4.BeautifulSoup(source, 'html.parser')

    for n in html.find_all(class_ = 'name'):
        cleanName = n.text.strip()
        fullName = cleanName.rsplit(' ', 1)
        # Check for 2 Names:
        if len(fullName) == 2:
            surNames.append(fullName[0])
            familyNames.append(fullName[1])
        elif len(fullName) == 1:
            surNames.append(fullName[0])
            familyNames.append("")
    for p in html.find_all(class_ = 'prize'):
        pClean = p.text.strip()
        pNew = pClean[2:].replace(',', '')
        if pNew != '' and pNew.isdigit():
            prizes.append(pNew)

    print("Finished pass {p}".format(p = i))
"""
# Print Output

print(surNames)
print(familyNames)
print(prizes)
