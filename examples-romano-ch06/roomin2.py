import sqlite3

class DatabaseManager:
    def __init__(self):
        # Maak een connectie met de rooming.db-database
        # Als rooming.db nog niet bestaat, wordt ie aangemaakt
        self.conn = sqlite3.connect("roomin.db")
        self.c = self.conn.cursor()

        # We gaan met een schone lei beginnen
        # Verwijder de tabel voor de interieurs als ze al bestaat
        self.c.execute(''' DROP TABLE IF EXISTS interieurs; ''')
        # Verwijder de tabel voor de foto's als ze al bestaat
        self.c.execute(''' DROP TABLE IF EXISTS fotos; ''')
        self.conn.commit()

        # Maak de tabel voor de interieurs aan
        self.c.execute('''CREATE TABLE IF NOT EXISTS interieurs (
                             id integer PRIMARY KEY,
                             verhaal text NOT NULL
                         );''')
        # Maak de tabel voor de foto's aan
        self.c.execute('''CREATE TABLE IF NOT EXISTS fotos (
                             id integer PRIMARY KEY,
                             id_interieur integer NOT NULL,
                             beschrijving text NOT NULL,
                             FOREIGN KEY (id_interieur) REFERENCES interieurs (id)
                         );''')
        self.conn.commit()
                       
    def voeg_interieur_voorlopig_toe(self, interieur):
        self.c.execute('''INSERT INTO interieurs (id, verhaal) VALUES (?, ?)''',
                       (interieur.id, interieur.verhaal))

    def voeg_foto_voorlopig_toe(self, foto):
        self.c.execute('''INSERT INTO fotos (id, id_interieur, beschrijving)
                             VALUES(?, ?, ?)''',
                       (foto.id, foto.interieur.id, foto.beschrijving))

    def leg_gegevens_vast(self):
        self.conn.commit()
           

class Interieur:
    id = 0
    def __init__(self, verhaal):
        self.__class__.id += 1
        self.id = self.__class__.id
        self.verhaal = verhaal
        self.fotos = list()
    def foto_toevoegen(self, beschrijving):
        foto = Foto(self, beschrijving)
        self.fotos.append(foto)
    def bewaren(self, dbm):
        dbm.voeg_interieur_voorlopig_toe(interieur=self)
        for foto in self.fotos: dbm.voeg_foto_voorlopig_toe(foto)
        dbm.leg_gegevens_vast()
        print("Interieur", self.verhaal, "is bewaard met", len(self.fotos), "foto's")

        
class Foto:
    id = 99
    def __init__(self, interieur, beschrijving):
        self.__class__.id += 1
        self.id = self.__class__.id
        self.interieur = interieur
        self.beschrijving = beschrijving

# Testen - De database bestaat nog niet op voorhand

i1 = Interieur("Lekker knus bij de haard")
i1.foto_toevoegen("Haard")
i1.foto_toevoegen("Zetel")
i1.foto_toevoegen("Schemerlamp")
dbm = DatabaseManager()
i1.bewaren(dbm)

# Output

"""
Interieur Lekker knus bij de haard is bewaard met 3 foto's
"""



        
