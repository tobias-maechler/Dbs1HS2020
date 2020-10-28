# Test Lists:
class Tl:
    surNames = ['Bryn', 'Justin', 'Daniel', 'Erik', 'Dan', 'Stephen', 'David', 'Fedor', 'Jason', 'Steve', 'Phil', 'Daniel', 'Mikita', 'Cary', 'Antonio', 'Isaac', 'Jake', 'John', 'Christoph', 'Timothy', 'Phil Hellmuth', 'Scott', 'Sam', 'Sam', 'Brian', 'Rainer', 'Adrian', 'Jason', 'Paul', 'Thomas', 'Igor', 'Dominik', 'Jonathan', 'Aaron Shu Nu', 'Nick', 'Michael', 'Martin', 'William Alex', 'Joseph', 'Ole', 'Daniel', 'Byron', 'Sean', 'Ryan', 'Bertrand', 'Dario', 'Joseph', 'Joseph', 'Richard', 'Steffen', 'Sam', 'Mike', 'Justin Cuong Van', 'Nick', 'Hossein', 'Elton', 'Benjamin', 'Sorel', 'Joe', 'Scotty', 'Jamie', 'Wai Leong', 'Koray', 'Michael', 'Carlos', 'Patrik', 'Anthony', 'Vanessa', 'Allen', 'Sergio', 'Mustapha', 'Philipp', 'Gregory', 'Ben', 'Connor', 'Tobias', 'David', 'Peter', 'Manig', 'Men', 'Wai Kin', 'Kahle', 'Dan', 'David', 'Erick', 'Andrew', 'Thomas John', 'Matthias', 'Gus', 'John', 'Davidi', 'Anthony', 'John', 'Chris', 'Rick', 'Elio', 'Mike', 'Chris', 'Charlie', 'Benjamin']

    familyNames = ['Kenney', 'Bonomo', 'Negreanu', 'Seidel', 'Smith', 'Chidwick', 'Peters', 'Holz', 'Koon', 'ODwyer', 'Ivey', 'Colman', 'Bodyakovsky', 'Katz', 'Esfandiari', 'Haxton', 'Schindler', 'Juanda', 'Vogelsang', 'Adams', 'Jr', 'Seiver', 'Greenwood', 'Trickett', 'Rast', 'Kempe', 'Mateos', 'Mercier', 'Phua', 'Marchese', 'Kurganov', 'Nitsche', 'Duhamel', 'Zang', 'Petrangelo', 'Mizrachi', 'Jacobson', 'Foxen', 'McKeehen', 'Schemion', 'Dvoress', 'Kaverman', 'Winter', 'Riess', 'Grospellier', 'Sammartino', 'Cheong', 'Cada', 'Yong', 'Sontheimer', 'Soverel', 'McDonald', 'Tran', 'Schulman', 'Ensan', 'Tsang', 'Pollak', 'Mizzi', 'Hachem', 'Nguyen', 'Gold', 'Chan', 'Aldemir', 'Watson', 'Mortensen', 'Antonius', 'Gregg', 'Selbst', 'Cunningham', 'Aido', 'Kanit', 'Gruissem', 'Merson', 'Lamb', 'Drinan', 'Reinkemeier', 'Rheem', 'Eastgate', 'Loeser', 'Nguyen', 'Yong', 'Burns', 'Shak', 'Pham', 'Lindgren', 'Lichtenberger', 'Cloutier', 'Eibinger', 'Hansen', 'Cynn', 'Kitai', 'Zinno', 'Racener', 'Klodnicki', 'Salomon', 'Fox', 'Matusow', 'Ferguson', 'Carrel', 'Tollerene']

    prizes = ['56403506', '49128107', '42053307', '37748126', '36742718', '34387646', '33737541', '32556379', '31101729', '30472704', '30311759', '28925059', '28497269', '28470501', '27810801', '27670940', '25269983', '25241271', '25064465', '24330803', '24115184', '23828658', '22307604', '21772841', '21506086', '21427269', '21384435', '19753022', '19330989', '19016194', '18706719', '18649882', '18012110', '17633233', '17498982', '17151328', '17040135', '16817406', '16652259', '16331584', '15607625', '15423295', '15078573', '14993143', '14664515', '14573847', '14553543', '14255396', '14233857', '13727892', '13712877', '13314190', '13169979', '13117530', '13060467', '12968353', '12934492', '12700539', '12644787', '12626067', '12592641', '12488677', '12298005', '12117331', '12106336', '12013265', '11979691', '11906247', '11811098', '11794333', '11566695', '11505780', '11428359', '11374294', '11256946', '11195904', '11150569', '11131450', '11126206', '11068171', '10837736', '10730710', '10633297', '10573561', '10564832', '10464811', '10443473', '10376474', '10278252', '10188621', '10150187', '10143227', '10110236', '10103725', '9906283', '9812147', '9750072', '9584545', '9571776', '9515346']

# Spacers
class Space:
    tab = "\t"
    dTab = "\t\t"
    ret = "\n"

# Write File:

def wl(line):
    return line + "\n"

insertScript = File_object = open(r"/Users/Kevin1/Kevin/Study/Sem1/Dbs/Testat2/Python/Export/inserts python.sql", "w")

insertScript.writelines([
    wl("COPY spieler (id, vorname, nachname, gewinn, chipzahl, aktiv) FROM stdin WITH (ENCODING 'UTF8');")
])


for i in range(len(Tl.surNames)):
    insertScript.writelines(Space.tab +
        "{n}".format(n = i) + Space.tab +
        "'{name}'".format(name = Tl.surNames[i]) + Space.tab +
        "'{name}'".format(name = Tl.familyNames[i]) + Space.tab +
        "{prize}".format(prize = Tl.prizes[i]) + Space.tab +
        "100000" + Space.tab +
        "true" +
        Space.ret)






insertScript.close()
