import random
import names
import data

# Data:
class Content:
    surNames = ['Bryn', 'Justin', 'Daniel', 'Erik', 'Dan', 'Stephen', 'David', 'Fedor', 'Jason', 'Steve', 'Phil', 'Daniel', 'Mikita', 'Cary', 'Antonio', 'Isaac', 'Jake', 'John', 'Christoph', 'Timothy', 'Phil Hellmuth', 'Scott', 'Sam', 'Sam', 'Brian', 'Rainer', 'Adrian', 'Jason', 'Paul', 'Thomas', 'Igor', 'Dominik', 'Jonathan', 'Aaron Shu Nu', 'Nick', 'Michael', 'Martin', 'William Alex', 'Joseph', 'Ole', 'Daniel', 'Byron', 'Sean', 'Ryan', 'Bertrand', 'Dario', 'Joseph', 'Joseph', 'Richard', 'Steffen', 'Sam', 'Mike', 'Justin Cuong Van', 'Nick', 'Hossein', 'Elton', 'Benjamin', 'Sorel', 'Joe', 'Scotty', 'Jamie', 'Wai Leong', 'Koray', 'Michael', 'Carlos', 'Patrik', 'Anthony', 'Vanessa', 'Allen', 'Sergio', 'Mustapha', 'Philipp', 'Gregory', 'Ben', 'Connor', 'Tobias', 'David', 'Peter', 'Manig', 'Men', 'Wai Kin', 'Kahle', 'Dan', 'David', 'Erick', 'Andrew', 'Thomas John', 'Matthias', 'Gus', 'John', 'Davidi', 'Anthony', 'John', 'Chris', 'Rick', 'Elio', 'Mike', 'Chris', 'Charlie', 'Benjamin']

    familyNames = ['Kenney', 'Bonomo', 'Negreanu', 'Seidel', 'Smith', 'Chidwick', 'Peters', 'Holz', 'Koon', 'ODwyer', 'Ivey', 'Colman', 'Bodyakovsky', 'Katz', 'Esfandiari', 'Haxton', 'Schindler', 'Juanda', 'Vogelsang', 'Adams', 'Jr', 'Seiver', 'Greenwood', 'Trickett', 'Rast', 'Kempe', 'Mateos', 'Mercier', 'Phua', 'Marchese', 'Kurganov', 'Nitsche', 'Duhamel', 'Zang', 'Petrangelo', 'Mizrachi', 'Jacobson', 'Foxen', 'McKeehen', 'Schemion', 'Dvoress', 'Kaverman', 'Winter', 'Riess', 'Grospellier', 'Sammartino', 'Cheong', 'Cada', 'Yong', 'Sontheimer', 'Soverel', 'McDonald', 'Tran', 'Schulman', 'Ensan', 'Tsang', 'Pollak', 'Mizzi', 'Hachem', 'Nguyen', 'Gold', 'Chan', 'Aldemir', 'Watson', 'Mortensen', 'Antonius', 'Gregg', 'Selbst', 'Cunningham', 'Aido', 'Kanit', 'Gruissem', 'Merson', 'Lamb', 'Drinan', 'Reinkemeier', 'Rheem', 'Eastgate', 'Loeser', 'Nguyen', 'Yong', 'Burns', 'Shak', 'Pham', 'Lindgren', 'Lichtenberger', 'Cloutier', 'Eibinger', 'Hansen', 'Cynn', 'Kitai', 'Zinno', 'Racener', 'Klodnicki', 'Salomon', 'Fox', 'Matusow', 'Ferguson', 'Carrel', 'Tollerene']

    prizes = ['56403506', '49128107', '42053307', '37748126', '36742718', '34387646', '33737541', '32556379', '31101729', '30472704', '30311759', '28925059', '28497269', '28470501', '27810801', '27670940', '25269983', '25241271', '25064465', '24330803', '24115184', '23828658', '22307604', '21772841', '21506086', '21427269', '21384435', '19753022', '19330989', '19016194', '18706719', '18649882', '18012110', '17633233', '17498982', '17151328', '17040135', '16817406', '16652259', '16331584', '15607625', '15423295', '15078573', '14993143', '14664515', '14573847', '14553543', '14255396', '14233857', '13727892', '13712877', '13314190', '13169979', '13117530', '13060467', '12968353', '12934492', '12700539', '12644787', '12626067', '12592641', '12488677', '12298005', '12117331', '12106336', '12013265', '11979691', '11906247', '11811098', '11794333', '11566695', '11505780', '11428359', '11374294', '11256946', '11195904', '11150569', '11131450', '11126206', '11068171', '10837736', '10730710', '10633297', '10573561', '10564832', '10464811', '10443473', '10376474', '10278252', '10188621', '10150187', '10143227', '10110236', '10103725', '9906283', '9812147', '9750072', '9584545', '9571776', '9515346']

    places = ['Philadelphia', 'Buford', 'Tampa', 'Larchwood', 'Ft. Lauderdale', 'Dublin', 'Cannes', 'Wien', 'London', 'Berlin', 'Milano', 'Edinburgh', 'Helsinki', 'Tallinn', 'Bukarest', 'Prag', 'Lloret de Mar', 'Malta', 'Newcastle', 'Wiesbaden', 'Hamburg', 'Manchester', 'Liverpool', 'Malmö', 'Sanremo', 'Tianjin', 'Tapei', 'Aberdeen', 'Divonne les Bains', 'Beijing', 'Everett', 'Pompano Beach', 'Minsk', 'Dakar', 'Göteborg', 'Luton', 'Shenyang', 'Hollywood', 'Columbus', 'Zurich', 'Buenos Aires', 'Melbourne', 'Pressburg', 'Boston', 'Seefeld', 'Montana', 'Jacksonville', 'Niagara Falls', 'Rapperswil', 'Brüssel']

# Formating
class Format:
    tab = "\t"
    dTab = "\t\t"
    sep = "\t"
    ret = "\n"

    def wl(line):
        return line + "\n"

# Helper Functions

floorman = {}

def pickFloorman():
    index = random.randint(1, 76)
    pick = floorman.pop(index, -1)
    if pick == -1:
        return pickFloorman()
    elif pick == 1:
        return index
    else:
        pick -= 1
        floorman[index] = pick
        return index

def randomDate():
    day = random.randint(1, 26)
    month = random.randint(1, 12)
    year = random.randint(2015, 2023)
    return f"{day:02}-{month:02}-{year}"

def randomEndDate(startDate):
    day = int(startDate[0] + startDate[1])
    month = int(startDate[3] + startDate[4])
    year = int(startDate[6] + startDate[7] + startDate[8] + startDate[9])
    if day < 16:
        day += random.randint(1, 10)
    elif month < 11:
        month += random.randint(1, 2)
    else:
        year += 1
        month = 1
    return f"{day:02}-{month:02}-{year}"

def rankCounter(int):
    if int <= 500:
        if int <= 100:
            return 10
        elif int <= 200 and int > 100:
            return 9
        elif int <= 300 and int > 200:
            return 8
        elif int <= 400 and int > 300:
            return 7
        else:
            return 6
    else:
        if int <= 600:
            return 5
        elif int <= 700 and int > 600:
            return 4
        elif int <= 800 and int > 700:
            return 3
        elif int <= 900 and int > 800:
            return 2
        else:
            return 1

############ Write File: ############

insertScript = File_object = open(r"/Users/Kevin1/Kevin/Study/Sem1/Dbs/Testat2/Python/Export/inserts python.sql", "w")

# Write Comments
insertScript.writelines([Format.wl("-- Autoren: Kevin Löffler & Tobias Mächler")])
insertScript.writelines([Format.wl("-- Player data scraped from thehendonmob.com")])
insertScript.writelines([Format.ret])

insertScript.writelines([
    Format.wl("COPY spieler (id, vorname, nachname, gewinn, chipzahl, aktiv) FROM stdin WITH (ENCODING 'UTF8');")
])

### create SPIELER table:

lastItem = len(data.surNames) - 1

for i in range(lastItem):
    insertScript.writelines(
        "{id}".format(id = i + 1) + Format.sep +
        "{name}".format(name = data.surNames[i]) + Format.sep +
        "{name}".format(name = data.familyNames[i]) + Format.sep +
        "{prize}".format(prize = data.prizes[i]) + Format.sep +
        "100000" + Format.sep +
        "true" + Format.ret)

insertScript.writelines(
    "{id}".format(id = lastItem + 1) + Format.sep +
    "{name}".format(name = data.surNames[lastItem]) + Format.sep +
    "{name}".format(name = data.familyNames[lastItem]) + Format.sep +
    "{prize}".format(prize = data.prizes[lastItem]) + Format.sep +
    "100000" + Format.sep +
    "true" +
    "\n\\." + Format.ret)

insertScript.writelines("\n\n")

### create FLOORMAN table

insertScript.writelines([
    Format.wl("COPY floorman (id, vorname, nachname, erfahrung) FROM stdin WITH (ENCODING 'UTF8');")
])

for i in range(74):
    # Build Floorman List:
    id = i + 1
    xp = random.randint(1, 3)
    floorman[id] = xp
    # Create Syntax
    insertScript.writelines(
        "{id}".format(id = id) + Format.sep +
        "{first}".format(first = names.get_first_name()) + Format.sep +
        "{last}".format(last = names.get_last_name()) + Format.sep +
        "{xp}".format(xp = xp) + Format.ret)

insertScript.writelines(
    "{id}".format(id = 75) + Format.sep +
    "{first}".format(first = names.get_first_name()) + Format.sep +
    "{last}".format(last = names.get_last_name()) + Format.sep +
    "{xp}".format(xp = xp) +
    "\n\\." + Format.ret)

insertScript.writelines("\n\n")

### create TOURNAMENT table

insertScript.writelines([
    Format.wl("COPY tournament (id, maxspieler, preisgeld, datum, ort, floorman) FROM stdin WITH (ENCODING 'UTF8');")
])

for i in range(99):
    insertScript.writelines(
        "{id}".format(id = i + 1) + Format.sep +
        "24" + Format.sep +
        "{prize}".format(prize = random.randint(10000, 1000000)) + Format.sep +
        "{date}".format(date = randomDate()) + Format.sep +
        "{place}".format(place = random.choice(Content.places)) + Format.sep +
        "{floorman}".format(floorman = pickFloorman()) + Format.ret)

insertScript.writelines(
    "{id}".format(id = 100) + Format.sep +
    "24" + Format.sep +
    "{prize}".format(prize = random.randint(10000, 1000000)) + Format.sep +
    "{date}".format(date = randomDate()) + Format.sep +
    "{place}".format(place = random.choice((Content.places))) + Format.sep +
    "{floorman}".format(floorman = pickFloorman()) +
    "\n\\." + Format.ret)

insertScript.writelines("\n\n")

### create PROFI table

insertScript.writelines([
    Format.wl("COPY profi (spielerid, rank, tournament) FROM stdin WITH (ENCODING 'UTF8');")
])

for i in range(999):
    insertScript.writelines(
        "{id}".format(id = i + 1) + Format.sep +
        "{rank}".format(rank = rankCounter(i)) + Format.sep +
        "{tour}".format(tour = random.randint(1, 100)) + Format.ret)

insertScript.writelines(
    "{id}".format(id = 1000) + Format.sep +
    "{rank}".format(rank = rankCounter(i)) + Format.sep +
    "{tour}".format(tour = random.randint(1, 100)) +
    "\n\\." + Format.ret)

insertScript.writelines("\n\n")

### create BEGINNER table

insertScript.writelines([
    Format.wl("COPY beginner (spielerid, zugelassen) FROM stdin WITH (ENCODING 'UTF8');")
])

for i in range(8999):
    insertScript.writelines(
        "{id}".format(id = i + 1001) + Format.sep +
        "false" + Format.ret)

insertScript.writelines(
    "{id}".format(id = 10000) + Format.sep +
    "false" +
    "\n\\." + Format.ret)

insertScript.writelines("\n\n")

### create QUALIFYING table

insertScript.writelines([
    Format.wl("COPY qualifying (id, startdatum, endedatum) FROM stdin WITH (ENCODING 'UTF8');")
])


for i in range(99):
    qualifyingStartDate = randomDate()

    insertScript.writelines(
        "{id}".format(id = i + 1) + Format.sep +
        "{start}".format(start = qualifyingStartDate) + Format.sep +
        "{end}".format(end = randomEndDate(qualifyingStartDate)) + Format.ret)

insertScript.writelines(
    "{id}".format(id = 100) + Format.sep +
    "{start}".format(start = qualifyingStartDate) + Format.sep +
    "{end}".format(end = randomEndDate(qualifyingStartDate)) +
    "\n\\." + Format.ret)

insertScript.writelines("\n\n")

### create QUALIFYING SPIELER table

insertScript.writelines([
    Format.wl("COPY qualifyingspieler (id, Spielerid) FROM stdin WITH (ENCODING 'UTF8');")
])

for i in range(8999):
    insertScript.writelines(
        "{qID}".format(qID = random.randint(1, 100)) + Format.sep +
        "{sID}".format(sID = i + 1001) + Format.ret)

insertScript.writelines(
    "{qID}".format(qID = random.randint(1, 100)) + Format.sep +
    "{sID}".format(sID = 10000) +
    "\n\\." + Format.ret)

insertScript.writelines("\n")

insertScript.close()
