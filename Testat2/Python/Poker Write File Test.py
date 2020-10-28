# Write File:

def wl(line):
    return line + "\n"

insertScript = File_object = open(r"inserts python.sql","w")

# insertScript.writelines(L) for L = [
# "COPY spieler (id, vorname, nachname, gewinn, chipzahl, aktiv) FROM stdin WITH (ENCODING 'UTF8');",
# "1  'Daniel'  'Negreanu'    2000000 100000  true",
# "1  'Daniel'  'Negreanu'    2000000 100000  true"
# ]

insertScript.writelines([
wl("COPY spieler (id, vorname, nachname, gewinn, chipzahl, aktiv) FROM stdin WITH (ENCODING 'UTF8');"),
wl("    1  'Daniel'  'Negreanu'    2000000 100000  true",),
wl("    1  'Daniel'  'Negreanu'    2000000 100000  true")
])






insertScript.close()
